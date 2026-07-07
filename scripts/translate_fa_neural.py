# -*- coding: utf-8 -*-
"""
Neuronaler DE->FA-Backend (NLLB-200 via CTranslate2, offline, CPU).

Uebersetzt die natuersprachlichen deutschen Textsegmente einer SKILL.md nach
Persisch und bewahrt dabei das Markdown-Geruest sowie alle rechtlich tragenden
Zeichen (Paragraphenzitate, Gesetzeskuerzel, URLs, Platzhalter, Code) WORTGETREU.

Kernidee gegen doppelte Arbeit: ein persistenter Uebersetzungsspeicher
(Translation Memory, JSONL). Wegen der hohen Redundanz des Korpus sind nach den
ersten ~1000 Dateien die allermeisten Segmente bereits im Cache; das Modell
laeuft dann nur noch auf wirklich neuem Text. Dadurch wird der Gesamtlauf
tragbar und ist jederzeit fortsetzbar.
"""

import json
import os
import re

from translate_skills_fa_lib import (
    _PROTECT_RE,
    _MD_PREFIX_RE,
    HEADERS,
    EXACT_LINES,
    translate_header,
    split_frontmatter,
)
from de_umlaut import restore as restore_umlauts

SRC_LANG = "deu_Latn"
TGT_LANG = "pes_Arab"
TOKENIZER_ID = "facebook/nllb-200-distilled-600M"

# Nur Segmente mit mindestens einem Buchstaben werden uebersetzt.
_HAS_LETTER = re.compile(r"[A-Za-zÄÖÜäöüß]")

# Zeichen, die NLLB als OOV zu <unk> macht -> vor der Inferenz normalisieren.
_MT_PUNCT = {
    "–": "-", "—": "-", "‐": "-", "‑": "-", "―": "-",
    "„": '"', "“": '"', "”": '"', "»": '"', "«": '"',
    "‚": "'", "‘": "'", "’": "'", "…": "...", "•": "-",
    " ": " ", " ": " ", " ": " ",
}
_MT_PUNCT_RE = re.compile("|".join(re.escape(k) for k in _MT_PUNCT))
_UNK_RE = re.compile(r"\s*<unk>\s*")


def normalize_for_mt(text):
    return _MT_PUNCT_RE.sub(lambda m: _MT_PUNCT[m.group(0)], text)


def split_protected(text):
    """Zerlegt Text in (is_text, content)-Segmente; geschuetzte Spannen bleiben."""
    parts = []
    last = 0
    for m in _PROTECT_RE.finditer(text):
        if m.start() > last:
            parts.append((True, text[last:m.start()]))
        parts.append((False, m.group(0)))
        last = m.end()
    if last < len(text):
        parts.append((True, text[last:]))
    return parts


class NeuralTranslator:
    def __init__(self, model_dir, cache_path, inter_threads=4, beam_size=1,
                 batch_size=64):
        import ctranslate2
        import transformers

        self.tok = transformers.AutoTokenizer.from_pretrained(
            TOKENIZER_ID, src_lang=SRC_LANG
        )
        self.translator = ctranslate2.Translator(
            model_dir, device="cpu", intra_threads=1, inter_threads=inter_threads
        )
        self.beam_size = beam_size
        self.batch_size = batch_size
        self.cache = {}
        self.cache_path = cache_path
        self._new = 0
        if os.path.exists(cache_path):
            with open(cache_path, encoding="utf-8") as fh:
                for ln in fh:
                    ln = ln.strip()
                    if not ln:
                        continue
                    try:
                        de, fa = json.loads(ln)
                        self.cache[de] = fa
                    except Exception:
                        pass
        self._sink = open(cache_path, "a", encoding="utf-8")

    # -- eigentliche Modell-Inferenz (ungecacht) --------------------------
    def _model_translate(self, texts):
        srcs = [self.tok.convert_ids_to_tokens(self.tok.encode(t)) for t in texts]
        results = self.translator.translate_batch(
            srcs,
            target_prefix=[[TGT_LANG]] * len(srcs),
            beam_size=self.beam_size,
            max_batch_size=self.batch_size,
            no_repeat_ngram_size=3,      # gegen Wiederhol-Degeneration
            repetition_penalty=1.3,
            max_decoding_length=256,
        )
        out = []
        for r in results:
            toks = r.hypotheses[0]
            if toks and toks[0] == TGT_LANG:
                toks = toks[1:]
            dec = self.tok.decode(self.tok.convert_tokens_to_ids(toks))
            dec = _UNK_RE.sub(" ", dec).strip()
            out.append(dec)
        return out

    def translate_many(self, texts):
        """texts: Liste[str] -> dict[str,str]; nutzt und fuellt Cache."""
        need = []
        seen = set()
        for t in texts:
            k = t.strip()
            if not k or k in self.cache or k in seen or not _HAS_LETTER.search(k):
                continue
            seen.add(k)
            need.append(k)
        # nach Laenge sortieren: aehnlich lange Segmente pro Batch -> weniger
        # Padding-Verschwendung -> bessere CPU-Auslastung.
        need.sort(key=len)
        for i in range(0, len(need), self.batch_size):
            chunk = need[i:i + self.batch_size]
            # Umlaute restaurieren + Sonderzeichen normalisieren (gegen OOV/
            # <unk>), Cache aber unter dem Originaltext fuehren.
            trans = self._model_translate(
                [normalize_for_mt(restore_umlauts(t)) for t in chunk])
            for de, fa in zip(chunk, trans):
                self.cache[de] = fa
                self._sink.write(json.dumps([de, fa], ensure_ascii=False) + "\n")
                self._new += 1
            self._sink.flush()
        return {t: self.cache.get(t.strip(), t) for t in texts}

    def close(self):
        try:
            self._sink.close()
        except Exception:
            pass


# ---------------------------------------------------------------------------
# Dokument-Planung: Segmente einsammeln, dann rendern
# ---------------------------------------------------------------------------

def _plan_line(line):
    """Gibt (renderer, needed_texts). renderer(trans_map) -> uebersetzte Zeile."""
    if not line.strip():
        return (lambda m: line), []
    # Tabellentrenner
    if "|" in line and re.match(r"^\s*\|?[\s:|-]+\|?\s*$", line):
        return (lambda m: line), []
    # Codezeilen werden ausserhalb behandelt (in translate_body_neural)

    pm = _MD_PREFIX_RE.match(line)
    prefix, content = pm.group(1), pm.group(2)

    # Ueberschrift: exakte Treffer aus Woerterbuch (schnell, korrekt),
    # sonst ueber das Modell (fluessiges Persisch statt Glossar-Mischtext).
    if prefix.strip().startswith("#"):
        c = content.strip()
        if c in HEADERS:
            val = HEADERS[c]
            return (lambda m: prefix + val), []
        segs = split_protected(content)
        needed = [s.strip() for is_t, s in segs if is_t and _HAS_LETTER.search(s)]

        def render_h(m, prefix=prefix, segs=segs):
            buf = []
            for is_t, s in segs:
                if is_t and _HAS_LETTER.search(s):
                    buf.append(_apply(s, m))
                else:
                    buf.append(s)
            return prefix + "".join(buf)
        return render_h, needed

    # Exakte hochfrequente Zeile -> kuratierte Uebersetzung
    stripped = line.strip()
    if stripped in EXACT_LINES:
        lead = line[: len(line) - len(line.lstrip())]
        val = EXACT_LINES[stripped]
        return (lambda m: lead + val), []
    if content.strip() in EXACT_LINES:
        val = EXACT_LINES[content.strip()]
        return (lambda m: prefix + val), []

    # Tabellenzeile mit Inhalt: Zellen als Segmente
    if line.count("|") >= 2:
        cells = line.split("|")
        needed = []
        plan = []  # (kind, payload)
        for cell in cells:
            core = cell.strip()
            if core and _HAS_LETTER.search(core):
                segs = split_protected(core)
                plan.append(("cell", (cell, segs)))
                for is_t, c in segs:
                    if is_t and _HAS_LETTER.search(c):
                        needed.append(c.strip())
            else:
                plan.append(("raw", cell))

        def render(m, plan=plan):
            out = []
            for kind, payload in plan:
                if kind == "raw":
                    out.append(payload)
                else:
                    cell, segs = payload
                    lead = cell[: len(cell) - len(cell.lstrip())] or " "
                    trail = cell[len(cell.rstrip()):] or " "
                    buf = []
                    for is_t, c in segs:
                        if is_t and _HAS_LETTER.search(c):
                            buf.append(_apply(c, m))
                        else:
                            buf.append(c)
                    out.append(lead + "".join(buf).strip() + trail)
            return "|".join(out)
        return render, needed

    # Standardzeile: geschuetzte Spannen ausklammern, Rest uebersetzen
    segs = split_protected(content)
    needed = [c.strip() for is_t, c in segs if is_t and _HAS_LETTER.search(c)]

    def render(m, prefix=prefix, segs=segs):
        buf = []
        for is_t, c in segs:
            if is_t and _HAS_LETTER.search(c):
                buf.append(_apply(c, m))
            else:
                buf.append(c)
        return prefix + "".join(buf)
    return render, needed


def _apply(segment, trans_map):
    """Ersetzt ein Textsegment durch seine Uebersetzung, Rand-Whitespace bleibt."""
    core = segment.strip()
    fa = trans_map.get(core, core)
    lead = segment[: len(segment) - len(segment.lstrip())]
    trail = segment[len(segment.rstrip()):]
    return lead + fa + trail


def translate_body_neural(body, translator):
    lines = body.split("\n")
    renderers = []
    all_needed = []
    in_code = False
    for line in lines:
        if line.strip().startswith("```"):
            in_code = not in_code
            renderers.append((lambda m, l=line: l))
            continue
        if in_code:
            renderers.append((lambda m, l=line: l))
            continue
        render, needed = _plan_line(line)
        renderers.append(render)
        all_needed.extend(needed)
    trans_map = translator.translate_many(all_needed)
    return "\n".join(r(trans_map) for r in renderers)
