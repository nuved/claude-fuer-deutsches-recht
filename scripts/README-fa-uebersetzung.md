# Persische Übersetzungsebene für Skills (`SKILL.fa.md`)

Dieser Ordner enthält die **additive** Pipeline, die neben jeder `SKILL.md`
eine persische (Farsi) Begleitdatei `SKILL.fa.md` erzeugt. Die deutschen
Skill-Dateien bleiben unverändert und **maßgeblich**; die `.fa`-Datei ist eine
maschinelle **Orientierungshilfe** mit deutlich sichtbarem RTL-Banner
(Haftungshinweis, „deutsche Fassung maßgeblich", Link auf das Original).

Sie setzt die im Commit „Persische Übersetzungsebene (additiv)" begonnene Linie
fort (`README.fa.md`, `QUICKSTART.fa.md`, `CLAUDE.fa.md`, `references/*.fa.md`).

## Dateien

| Datei | Zweck |
| --- | --- |
| `translate-skills-fa.py` | CLI: Walker, Banner, Idempotenz, Backend-Auswahl |
| `translate_skills_fa_lib.py` | Deterministische Engine + Schutzmuster (Zitate, Gesetzeskürzel, Gerichte, URLs, Platzhalter), Ueberschriften- und Bausteinwörterbuch |
| `translate_fa_neural.py` | Neuronaler Backend (NLLB-200 via CTranslate2), Segment-Planung, Translation-Memory |
| `de_umlaut.py` | Sichere Rückwandlung ASCII-transliterierter Umlaute (ue/ae/oe → ü/ä/ö) vor der Inferenz; Selbsttest via `python de_umlaut.py` |
| `.venv-fa/` | Python-3.11-venv mit `ctranslate2`, `transformers`, `sentencepiece` und dem CT2-Modell unter `.venv-fa/models/` (nicht eingecheckt) |
| `.fa-translation-memory.jsonl` | Translation-Memory (Segment → Übersetzung), macht Läufe schnell und fortsetzbar (nicht eingecheckt) |
| `.fa-run.log`, `.fa-run.pid` | Lauf-Protokoll und PID des Hintergrundlaufs |

## Setup (einmalig)

```bash
python3.11 -m venv scripts/.venv-fa
scripts/.venv-fa/bin/python -m pip install --only-binary=:all: \
    ctranslate2 sentencepiece transformers huggingface_hub
# CT2-Modell (≈2.5 GB) nach scripts/.venv-fa/models/ laden:
scripts/.venv-fa/bin/python - <<'PY'
from huggingface_hub import snapshot_download
snapshot_download("entai2965/nllb-200-distilled-600M-ctranslate2",
                  local_dir="scripts/.venv-fa/models/nllb-200-distilled-600M-ctranslate2")
PY
```

## Lauf

```bash
# Voller Lauf (überspringt bereits erzeugte .fa-Dateien -> fortsetzbar)
scripts/.venv-fa/bin/python scripts/translate-skills-fa.py --backend nllb \
    --threads 16 --batch-size 64 --progress-every 200

# Nur ein Plugin, alles neu
scripts/.venv-fa/bin/python scripts/translate-skills-fa.py --backend nllb \
    --plugins mietrecht --force

# Deterministischer Backend (ohne Modell, sofort, aber Prosa nur teilübersetzt)
scripts/.venv-fa/bin/python scripts/translate-skills-fa.py --backend deterministic --limit 5 --print
```

**Fortsetzen nach Abbruch:** einfach denselben Befehl erneut starten. Bereits
vorhandene `SKILL.fa.md` werden übersprungen, das Translation-Memory wird
wiederverwendet. Schreibvorgänge sind atomar (`.tmp` + `os.replace`).

**Monitoring:**
```bash
tail -f scripts/.fa-run.log
find . -name SKILL.fa.md | wc -l          # Fortschritt (Ziel: 26.179)
```

## Qualität und Grenzen (ehrlich)

- **Struktur, Zitate, Platzhalter:** sauber. Paragraphen (`§ 305 BGB`),
  Gesetzeskürzel, Gerichte, Aktenzeichen, URLs und `[Platzhalter]` bleiben
  wörtlich; Tabellen und Codeblöcke bleiben erhalten.
- **Prosa:** echtes Persisch (NLLB-200-distilled-600M, `beam_size=1`,
  `no_repeat_ngram_size=3`). Modellbedingt gibt es gelegentliche
  Fehlübersetzungen von Fachbegriffen; deshalb der Banner „deutsche Fassung
  maßgeblich". Für höhere Qualität `--beam-size` erhöhen (langsamer) oder einen
  API-Backend anbinden.
- **Umlaut-Transliteration:** In ~17 % der Dateien stehen `ue/ae/oe` statt
  `ü/ä/ö`. `de_umlaut.py` stellt sie vor der Inferenz sicher wieder her (sonst
  halluziniert das Modell). Der Selbsttest deckt echte Falsch-Positive ab
  (`zuerst`, `bauen`, `Frequenz`, `Steuer`, `neue` bleiben unverändert).

## Backends

| Backend | Aktiv | Qualität | Kosten |
| --- | --- | --- | --- |
| `deterministic` | ja | Struktur gut, Prosa teils deutsch | 0, sofort |
| `nllb` | ja (venv+Modell) | echtes Persisch, MT-typische Fehler | CPU-Zeit |
| `anthropic` | vorbereitet | am besten | `ANTHROPIC_API_KEY`, kostenpflichtig |
