#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phase A des schnellen persischen Laufs: uebersetzt ALLE eindeutigen Textsegmente
des Korpus in das Translation-Memory (voll ausgelastete Batches, statt kleiner
Pro-Datei-Batches). Danach rendert `translate-skills-fa.py --backend nllb` die
26.179 Dateien fast nur noch aus dem Cache (Phase B, sehr schnell).

Aufruf:
    scripts/.venv-fa/bin/python scripts/warm-fa-cache.py --threads 16 --batch-size 128
"""

import argparse
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import translate_fa_neural as tn  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def iter_skill_md():
    for root, dirs, files in os.walk(REPO):
        dirs[:] = [d for d in dirs if d not in (".git", "node_modules")
                   and not d.startswith(".venv") and not d.startswith(".")]
        if os.sep + "skills" + os.sep not in root + os.sep:
            continue
        if "SKILL.md" in files:
            yield os.path.join(root, "SKILL.md")


def collect_segments():
    uniq = set()
    for path in iter_skill_md():
        body = tn.split_frontmatter(open(path, encoding="utf-8").read())[1]
        in_code = False
        for line in body.split("\n"):
            s = line.strip()
            if s.startswith("```"):
                in_code = not in_code
                continue
            if in_code:
                continue
            for seg in tn._plan_line(line)[1]:
                uniq.add(seg)
    return uniq


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--threads", type=int, default=16)
    ap.add_argument("--batch-size", type=int, default=128)
    ap.add_argument("--model-dir", default="")
    ap.add_argument("--cache", default="")
    ap.add_argument("--progress-every", type=int, default=5000)
    args = ap.parse_args()

    model_dir = args.model_dir or None
    if not model_dir:
        base = os.path.join(REPO, "scripts", ".venv-fa", "models")
        for n in sorted(os.listdir(base)):
            if os.path.isfile(os.path.join(base, n, "model.bin")):
                model_dir = os.path.join(base, n)
                break
    cache = args.cache or os.path.join(REPO, "scripts", ".fa-translation-memory.jsonl")

    print(f"[warm] Modell: {model_dir}", flush=True)
    print(f"[warm] Cache:  {cache}", flush=True)
    print("[warm] sammle eindeutige Segmente ...", flush=True)
    t0 = time.time()
    segs = collect_segments()
    tr = tn.NeuralTranslator(model_dir, cache, inter_threads=args.threads,
                             batch_size=args.batch_size)
    todo = [s for s in segs if s.strip() and s.strip() not in tr.cache
            and tn._HAS_LETTER.search(s)]
    todo.sort(key=len)
    print(f"[warm] {len(segs)} eindeutig, davon {len(tr.cache)} schon im Cache, "
          f"{len(todo)} offen. (Sammeln {time.time()-t0:.0f}s)", flush=True)

    done = 0
    for i in range(0, len(todo), args.batch_size):
        chunk = todo[i:i + args.batch_size]
        tr.translate_many(chunk)   # dedupt+cacht+schreibt
        done += len(chunk)
        if done % args.progress_every < args.batch_size:
            el = time.time() - t0
            rate = tr._new / max(el, 1)
            rem = (len(todo) - done) / max(rate, 0.1) / 3600
            print(f"[warm] {done}/{len(todo)} offen bearbeitet, "
                  f"TM+{tr._new} ({rate:.1f} Segmente/s), ~{rem:.1f}h Rest",
                  flush=True)
    tr.close()
    print(f"[warm] fertig: TM+{tr._new} neue Segmente in {time.time()-t0:.0f}s. "
          f"Cache jetzt {len(tr.cache)}.", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
