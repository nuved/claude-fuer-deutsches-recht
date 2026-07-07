#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Erzeugt persische (Farsi) Begleitdateien SKILL.fa.md neben jeder SKILL.md.

Additive Uebersetzungsebene: die deutschen SKILL.md bleiben unveraendert und
massgeblich. Die .fa-Datei ist eine Orientierungshilfe fuer persischsprachige
Nutzerinnen und Nutzer und traegt ein deutlich sichtbares Banner (RTL) mit
Haftungshinweis und Link auf das deutsche Original.

Aufrufbeispiele:

    # Prototyp: nur 8 Dateien, nach stdout-Statistik
    python3 scripts/translate-skills-fa.py --limit 8

    # Nur bestimmte Plugins
    python3 scripts/translate-skills-fa.py --plugins agb-recht-pruefer,mietrecht

    # Voller Lauf (ueberspringt bereits erzeugte Dateien)
    python3 scripts/translate-skills-fa.py

    # Voller Lauf, alles neu
    python3 scripts/translate-skills-fa.py --force

Backends:
    --backend deterministic   (Standard) regel-/woerterbuchbasiert, offline
    --backend nllb            lokales neuronales MT (optional, benoetigt
                              transformers+torch/ctranslate2; deutlich langsamer)
    --backend anthropic       LLM-Uebersetzung via ANTHROPIC_API_KEY (kostenpflichtig)

Nur der Standard-Backend ist ohne Zusatzinstallation lauffaehig. Die anderen
Backends sind als Qualitaets-Upgrade vorbereitet; sie nutzen denselben Walker,
dasselbe Banner und dieselbe Idempotenz.
"""

import argparse
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import translate_skills_fa_lib as tlib  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BANNER = """> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>
"""


def build_fa_document(src_text, rel_path):
    fm, body = tlib.split_frontmatter(src_text)
    translated_body = tlib.translate_body(body)
    parts = []
    if fm is not None:
        parts.append(fm.rstrip("\n"))
        parts.append("")
    parts.append(BANNER)
    parts.append(translated_body.lstrip("\n"))
    doc = "\n".join(parts)
    if not doc.endswith("\n"):
        doc += "\n"
    return doc


def iter_skill_files(plugins_filter=None):
    for root, dirs, files in os.walk(REPO):
        # .git, node_modules, venvs und versteckte Ordner ueberspringen
        dirs[:] = [d for d in dirs if d not in (".git", "node_modules")
                   and not d.startswith(".venv") and not d.startswith(".")]
        if os.sep + "skills" + os.sep not in root + os.sep:
            continue
        if "SKILL.md" not in files:
            continue
        rel = os.path.relpath(os.path.join(root, "SKILL.md"), REPO)
        top = rel.split(os.sep, 1)[0]
        if plugins_filter and top not in plugins_filter:
            continue
        yield os.path.join(root, "SKILL.md"), rel


def translate_deterministic(src_text, rel):
    return build_fa_document(src_text, rel)


def find_model_dir():
    base = os.path.join(REPO, "scripts", ".venv-fa", "models")
    if not os.path.isdir(base):
        return None
    for name in sorted(os.listdir(base)):
        d = os.path.join(base, name)
        if os.path.isfile(os.path.join(d, "model.bin")):
            return d
    return None


def build_fa_document_neural(src_text, translator):
    import translate_fa_neural as tn
    fm, body = tn.split_frontmatter(src_text)
    translated_body = tn.translate_body_neural(body, translator)
    parts = []
    if fm is not None:
        parts.append(fm.rstrip("\n"))
        parts.append("")
    parts.append(BANNER)
    parts.append(translated_body.lstrip("\n"))
    doc = "\n".join(parts)
    if not doc.endswith("\n"):
        doc += "\n"
    return doc


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0, help="max. Anzahl Dateien (0 = alle)")
    ap.add_argument("--plugins", default="", help="kommagetrennte Plugin-Ordner")
    ap.add_argument("--force", action="store_true", help="bestehende .fa neu erzeugen")
    ap.add_argument("--backend", default="deterministic",
                    choices=["deterministic", "nllb", "anthropic"])
    ap.add_argument("--model-dir", default="", help="CT2-Modellordner (Autodetekt)")
    ap.add_argument("--threads", type=int, default=8, help="CT2 inter_threads")
    ap.add_argument("--batch-size", type=int, default=64)
    ap.add_argument("--cache", default="", help="Translation-Memory JSONL")
    ap.add_argument("--dry-run", action="store_true", help="nichts schreiben, nur zaehlen")
    ap.add_argument("--print", dest="do_print", action="store_true",
                    help="erste Zieldatei auf stdout ausgeben (Prototyp-Kontrolle)")
    ap.add_argument("--progress-every", type=int, default=500)
    args = ap.parse_args()

    plugins = set(p for p in args.plugins.split(",") if p) or None

    translator = None
    if args.backend == "anthropic":
        print("[!] Backend 'anthropic' benoetigt ANTHROPIC_API_KEY und ist hier "
              "nicht aktiviert.", file=sys.stderr)
        return 2
    if args.backend == "nllb":
        model_dir = args.model_dir or find_model_dir()
        if not model_dir:
            print("[!] Kein CT2-Modell gefunden (scripts/.venv-fa/models/*/model.bin).",
                  file=sys.stderr)
            return 2
        import translate_fa_neural as tn
        cache = args.cache or os.path.join(REPO, "scripts", ".fa-translation-memory.jsonl")
        print(f"[nllb] Modell: {model_dir}\n[nllb] Cache: {cache}\n"
              f"[nllb] threads={args.threads} batch={args.batch_size}", file=sys.stderr)
        translator = tn.NeuralTranslator(model_dir, cache,
                                         inter_threads=args.threads,
                                         batch_size=args.batch_size)

    total = created = skipped = 0
    t0 = time.time()
    printed = False
    for src, rel in iter_skill_files(plugins):
        total += 1
        dst = os.path.join(os.path.dirname(src), "SKILL.fa.md")
        if os.path.exists(dst) and not args.force:
            skipped += 1
            if args.limit and (created + skipped) >= args.limit:
                pass
            continue
        with open(src, encoding="utf-8") as fh:
            src_text = fh.read()
        if translator is not None:
            doc = build_fa_document_neural(src_text, translator)
        else:
            doc = translate_deterministic(src_text, rel)
        if args.do_print and not printed:
            print("=" * 70)
            print(f"# QUELLE: {rel}")
            print("=" * 70)
            print(doc)
            print("=" * 70)
            printed = True
        if not args.dry_run:
            tmp = dst + ".tmp"
            with open(tmp, "w", encoding="utf-8") as fh:
                fh.write(doc)
            os.replace(tmp, dst)   # atomar: unterbrechungssicher
        created += 1
        if args.progress_every and created % args.progress_every == 0:
            rate = created / max(time.time() - t0, 0.001)
            cached = getattr(translator, "_new", None)
            extra = f", TM+{cached}" if cached is not None else ""
            print(f"  ... {created} erzeugt ({rate:.1f} Dateien/s), "
                  f"{skipped} uebersprungen{extra}", file=sys.stderr)
        if args.limit and created >= args.limit:
            break

    if translator is not None:
        translator.close()
    dt = time.time() - t0
    print(f"\nFertig: {created} erzeugt, {skipped} uebersprungen, "
          f"{total} gesehen in {dt:.1f}s.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
