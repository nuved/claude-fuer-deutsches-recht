# -*- coding: utf-8 -*-
"""
Sichere Rueckwandlung ASCII-transliterierter Umlaute (ue/ae/oe) in echte
Umlaute (ü/ä/ö), bevor deutscher Text an das neuronale MT-Modell geht.

Warum: NLLB kennt "Buergschaft"/"Pfaendung"/"uebersteigt" nicht und
halluziniert dann. Mit echten Umlauten uebersetzt es korrekt.

Sicherheitsprinzip: KEINE blinde ue->ü-Ersetzung (zerstoert "zuerst",
"bauen", "Frequenz", "Steuer", "neue", "aktuell" ...). Stattdessen zwei
Schichten, beide gegen die real vorkommenden Falsch-Positiven getestet:

  1. Stamm-Teilstrings, die in echten Nicht-Umlaut-Woertern NICHT vorkommen
     (pruef, fuehr, ueber, moeglich, itaet -> ität ...).
  2. Ganzwort-Liste fuer haeufige transliterierte Woerter.

'ss' bleibt unangetastet (modernes Deutsch; NLLB kennt "muss", "dass").
"""

import re

# --- Schicht 1: sichere Stamm-Teilstrings (Kleinschreibung; case wird bewahrt)
# Jeder Eintrag ist so gewaehlt, dass er in gaengigen Nicht-Umlaut-Woertern
# nicht als Teilstring auftritt.
_STEMS = [
    ("itaet", "ität"),    # Qualitaet, Kausalitaet, Aktualitaet, Universitaet
    ("aetae", "ätä"),
    ("pruef", "prüf"),     # pruefen, Pruefung, ueberpruefen
    ("fuehr", "führ"),     # fuehren, fallfuehrenden, Verfuehrung
    ("gruend", "gründ"),   # Begruendung, gruendlich
    (" grund", " grund"),  # (Schutz, kein Umlaut) – bewusst neutral
    ("rueck", "rück"),     # Rueckfrage, zurueck
    ("drueck", "drück"),   # ausdruecklich
    ("stueck", "stück"),   # Grundstueck, Aktenstueck
    ("moeglich", "möglich"),
    ("staend", "ständ"),   # vollstaendig, staendig, Umstaende
    ("kuend", "künd"),     # Kuendigung
    ("gemaess", "gemäß"),
    ("maessig", "mäßig"),
    ("buerg", "bürg"),     # Buerge, Buergschaft, Buerger, Buergin
    ("pfaend", "pfänd"),
    ("aender", "änder"),   # Aenderung, abaendern
    ("ueber", "über"),
    ("gegenueber", "gegenüber"),
    ("waehl", "wähl"),
    ("naechst", "nächst"),
    ("wuensch", "wünsch"),
    ("erfuell", "erfüll"),
    ("duerf", "dürf"),     # beduerftig, duerfen
    ("beduerf", "bedürf"),
    ("loesch", "lösch"),
    ("loes", "lös"),       # Loesung, aufloesen
    ("hoech", "höch"),
    ("hoeh", "höh"),
    ("groess", "größ"),
    ("eroeffn", "eröffn"),
    ("behoerd", "behörd"),
    ("oeffentlich", "öffentlich"),
    ("persoenlich", "persönlich"),
    ("noetig", "nötig"),
    ("gehoer", "gehör"),
    ("traeg", "träg"),     # traegt, Vertraege, Traeger
    ("einschlaeg", "einschläg"),
    ("zuege", "züge"),     # Auszuege, Bezuege
    ("fuenf", "fünf"),
    ("koenn", "könn"),
    ("muess", "müss"),
    ("haeuf", "häuf"),
    ("laeuf", "läuf"),
    ("vollstaend", "vollständ"),
    ("selbststaend", "selbstständ"),
    ("zustaend", "zuständ"),
    ("gegenstaend", "gegenständ"),
    ("umstaend", "umständ"),
    ("verstaend", "verständ"),
    ("bestaetig", "bestätig"),
    ("taetig", "tätig"),
    ("qualitaet", "qualität"),
    ("kaeuf", "käuf"),     # Kaeufer, verkaeuflich
    ("verkaeuf", "verkäuf"),
    ("laeng", "läng"),
    ("gaeng", "gäng"),     # gaengig, Vorgaenge
    ("empfaeng", "empfäng"),
    ("anfaeng", "anfäng"),
    ("haelt", "hält"),
    ("faellig", "fällig"),
    ("zulaess", "zuläss"),
    ("unzulaess", "unzuläss"),
    ("massgeb", "maßgeb"),
    ("verhaeltnis", "verhältnis"),
    ("geschaeft", "geschäft"),
    ("beschaeftig", "beschäftig"),
    ("gewaehr", "gewähr"),
    ("erklaer", "erklär"),
    ("aufklaer", "aufklär"),
    ("beruecksicht", "berücksicht"),
    ("ausschuess", "ausschüss"),
    ("beschluess", "beschlüss"),
    ("schluess", "schlüss"),
    ("verfueg", "verfüg"),
    ("genueg", "genüg"),
    ("beguenstig", "begünstig"),
    ("verguet", "vergüt"),
    ("gebuehr", "gebühr"),
    ("buerger", "bürger"),
    ("nachtraeg", "nachträg"),
    ("vertraeg", "verträg"),
    ("antraeg", "anträg"),
    ("betraeg", "beträg"),
    ("ermaess", "ermäß"),
    ("veraeusser", "veräußer"),
    ("erhoeh", "erhöh"),
    ("aufloes", "auflös"),
    ("abloes", "ablös"),
    ("angehoer", "angehör"),
    ("zugehoer", "zugehör"),
    ("stoerung", "störung"),
    ("verstoess", "verstöß"),
    ("verstoss", "verstoß"),
    ("moeblier", "möblier"),
]

# --- Schicht 2: Ganzwoerter (Kleinschreibung) ---
_WORDS = {
    "fuer": "für",
    "duerfen": "dürfen",
    "wuerde": "würde",
    "wuerden": "würden",
    "waere": "wäre",
    "waeren": "wären",
    "haette": "hätte",
    "haetten": "hätten",
    "koennte": "könnte",
    "koennten": "könnten",
    "muesste": "müsste",
    "spaeter": "später",
    "gaebe": "gäbe",
    "naeher": "näher",
    "ueblich": "üblich",
    "aehnlich": "ähnlich",
    "gaengige": "gängige",
    "taeglich": "täglich",
    "vorlaeufig": "vorläufig",
    "endgueltig": "endgültig",
    " zwoelf": " zwölf",
    "tonalitaet": "tonalität",
}

# Regex fuer case-erhaltende Teilstring-Ersetzung
def _case_preserve(replacement, matched):
    if matched.isupper() and len(matched) > 1:
        return replacement.upper()
    if matched[:1].isupper():
        return replacement[:1].upper() + replacement[1:]
    return replacement


def _build_stem_re():
    # laengste zuerst
    stems = sorted(_STEMS, key=lambda kv: len(kv[0]), reverse=True)
    parts = []
    lookup = {}
    for de, fa in stems:
        key = de.strip()
        lookup[key.lower()] = fa.strip()
        parts.append(re.escape(key.strip()))
    pattern = re.compile("(" + "|".join(parts) + ")", re.IGNORECASE)
    return pattern, lookup


_STEM_RE, _STEM_LOOKUP = _build_stem_re()
_WORD_RE = re.compile(r"\b(" + "|".join(re.escape(w) for w in sorted(_WORDS, key=len, reverse=True)) + r")\b",
                      re.IGNORECASE)


def restore(text):
    if "ue" not in text and "ae" not in text and "oe" not in text:
        return text

    def word_sub(m):
        w = m.group(0)
        return _case_preserve(_WORDS[w.lower()], w)
    text = _WORD_RE.sub(word_sub, text)

    def stem_sub(m):
        seg = m.group(0)
        return _case_preserve(_STEM_LOOKUP[seg.lower()], seg)
    text = _STEM_RE.sub(stem_sub, text)
    return text


if __name__ == "__main__":
    # Selbsttest: Umlaute korrekt; Falsch-Positive UNVERAENDERT.
    must_change = {
        "Buergschaft": "Bürgschaft",
        "uebersteigt": "übersteigt",
        "Pfaendungsmoeglichkeit": "Pfändungsmöglichkeit",
        "Pruefung": "Prüfung",
        "gemaess": "gemäß",
        "Kuendigung": "Kündigung",
        "vollstaendige": "vollständige",
        "naechsten": "nächsten",
        "Begruendung": "Begründung",
        "persoenlich": "persönlich",
        "Kausalitaet": "Kausalität",
        "regelmaessig": "regelmäßig",
        "gegenueber": "gegenüber",
        "Rueckfrage": "Rückfrage",
        "Verfuegung": "Verfügung",
        "einschlaegige": "einschlägige",
        "Loesung": "Lösung",
        "fuer": "für",
    }
    must_stay = ["zuerst", "bauen", "Bauer", "Frequenz", "Konsequenz",
                 "Eloquenz", "Steuer", "Steuerberater", "neue", "Reue",
                 "aktuell", "eventuell", "quelle", "zueinander", "Abenteuer",
                 "Influencer", "Issue", "Request", "genau", "Vertrauen"]
    ok = True
    for src, exp in must_change.items():
        got = restore(src)
        flag = "OK " if got == exp else "XX "
        if got != exp:
            ok = False
        print(f"  {flag} {src!r} -> {got!r} (exp {exp!r})")
    print("---")
    for w in must_stay:
        got = restore(w)
        flag = "OK " if got == w else "XX "
        if got != w:
            ok = False
        print(f"  {flag} {w!r} -> {got!r}")
    print("\nALL PASS" if ok else "\nFAILURES PRESENT")
