# -*- coding: utf-8 -*-
"""
Deutsch -> Persisch (Farsi) Uebersetzungs-Bibliothek fuer SKILL.md-Dateien.

Diese Bibliothek liefert die deterministische Uebersetzungs-Engine, die von
scripts/translate-skills-fa.py verwendet wird. Sie ist bewusst regel- und
woerterbuchbasiert (kein Netz, keine API, reproduzierbar, auditierbar) und
folgt dem Konventionsbestand der uebrigen Generatoren im Repository.

Designprinzipien:

1. Struktur bleibt erhalten. Markdown-Geruest (Ueberschriften, Listen,
   Tabellen, Codebloecke) wird nie zerstoert.
2. Rechtlich tragende Zeichen bleiben WORTGETREU: Paragraphenzitate (§ ...),
   Gesetzeskuerzel (BGB, StGB, ZPO, DSGVO ...), Gerichtsnamen, Aktenzeichen,
   URLs, Domains, Platzhalter ([Name der Mandantin]).
3. Hochfrequente Bausteine (Arbeitsweg-Bullets, Ausformulierungspflicht-Block,
   Quellenregeln, Standard-Ueberschriften) werden EXAKT und korrekt uebersetzt.
4. Der individuelle Fliesstext ("long tail") wird ueber ein Fachglossar
   angenaehert; nicht sicher uebersetzbare deutsche Begriffe bleiben deutsch
   stehen. Die deutsche Fassung ist und bleibt massgeblich.

Der erzeugte persische Text ist eine ORIENTIERUNGSHILFE, keine amtliche
Uebersetzung. Das steht als Banner in jeder Zieldatei.
"""

import re

# ---------------------------------------------------------------------------
# 1. Schutzmuster: bleiben immer woertlich erhalten
# ---------------------------------------------------------------------------

# Gaengige Gesetzes-/Normkuerzel und Institutionen (Grossbuchstaben-Tokens),
# die als solche stehenbleiben muessen.
LAW_ABBRS = set("""
BGB HGB StGB StPO ZPO VwGO VwVfG SGB SGG FGO AO GG BVerfGG UWG UrhG MarkenG
PatG GebrMG DesignG GeschmMG GmbHG AktG UmwG GenG PartGG InsO StaRUG EGInsO
KSchG TzBfG ArbGG BetrVG BPersVG TVG AGG EFZG BUrlG MuSchG BEEG SGB
DSGVO BDSG TTDSG TMG TKG NIS2 KIVO GDPR AIACT VVG VAG WpHG KWG ZAG GwG
BauGB BauNVO BauO HOAI VOB VgV GWB UVgO SektVO KonzVgV RVG GKG JVEG GNotKG
BRAO BORA StBerG WPO BNotO PAO EStG KStG GewStG UStG ErbStG GrEStG BewG
FGG FamFG VersAusglG LPartG BtOG SGB WEG ErbbauRG StVO StVG StVZO FeV
BImSchG KrWG WHG BNatSchG UVPG UmwRG TierSchG AMG BtMG ApoG HeilprG
SG WStG WDO WBO WSG WPflG KDVG SVG BBesG SUG NATO
GewO ProdHaftG ProdSG GPSG UKlaG PAngV EGBGB ROM AEUV EUV EMRK
CIC CCEO KStG AVAG BEEG UVGV
""".split())

# Gerichte / gaengige juristische Abkuerzungen (bleiben woertlich)
COURTS = set("""
BVerfG BVerwG BGH BAG BSG BFH EuGH EuG EGMR OLG KG OLGZ LG AG VG OVG VGH
LAG LSG FG LArbG AGH BPatG GBA GenStA StA
""".split())

LEGAL_ABBR_TOKENS = [
    "i.V.m.", "i.S.d.", "i.S.v.", "i.S.e.", "i.d.R.", "i.E.", "i.Ü.",
    "u.a.", "u.U.", "z.B.", "d.h.", "ggf.", "vgl.", "gem.", "grds.",
    "Rn.", "Rz.", "Rdnr.", "ff.", "Abs.", "Nr.", "Halbs.", "Alt.",
    "Buchst.", "lit.", "Var.", "S.", "Hs.", "m.w.N.", "st.Rspr.",
]

_ABBR_ALT = "|".join(re.escape(a) for a in
                     sorted(LEGAL_ABBR_TOKENS, key=len, reverse=True))
_LAWCODE_ALT = "|".join(re.escape(a) for a in
                        sorted(LAW_ABBRS | COURTS, key=len, reverse=True))

# Regex-Schutzmuster (werden vor der Uebersetzung maskiert). Reihenfolge zaehlt.
_PROTECT_PATTERNS = [
    r"```.*?```",                              # Codeblock inline (fallback)
    r"`[^`]+`",                                 # Inline-Code
    r"\[[^\]]*\]\([^)]*\)",                     # Markdown-Link
    r"https?://[^\s)]+",                        # URL
    r"\b[\w.-]+\.(?:de|com|org|eu|net|int|gov)\b",  # Domain
    r"§+\s?\d+[a-z]?(?:\s?(?:Abs\.|S\.|Nr\.|Halbs\.|Alt\.|Buchst\.)\s?\d+[a-z]?)*",  # § 305 Abs. 1 ...
    r"\bArt\.\s?\d+[a-z]?(?:\s?(?:Abs\.|S\.|Nr\.|lit\.)\s?\d+[a-z]?)*",  # Art. 6 Abs. 1
    # Aktenzeichen (auch ohne 'Az.'-Praefix), z.B. VII ZB 25/21, 1 BvR 1/20, 8 C 12/19
    r"\b(?:[IVXLC]{1,5}|\d{1,3})\s?[A-Z][a-zA-Z]{0,4}\.?\s?\d{1,5}/\d{2,4}\b",
    r"\bAz\.?\s?[\w./ -]+",                      # Aktenzeichen mit Praefix
    r"(?:" + _ABBR_ALT + r")",                  # ff., i.V.m., Rn. ...
    r"\b(?:" + _LAWCODE_ALT + r")\b",           # BGB, StGB, WStG, WDO, BGH ...
    r"\[[^\]]+\]",                               # Platzhalter [Name ...]
    r"\b\d{1,2}[./]\d{4}\b",                     # 06/2026
    r"\bv\d+\.\d+\.\d+\b",                       # v429.3.0
]
_PROTECT_RE = re.compile("|".join(_PROTECT_PATTERNS), re.DOTALL)

_SENT = ""  # privater Bereich als Maskenanker


def _protect(text, store):
    """Ersetzt schutzwuerdige Segmente durch Maskenanker."""
    def repl(m):
        store.append(m.group(0))
        return f"{_SENT}{len(store) - 1}{_SENT}"
    return _PROTECT_RE.sub(repl, text)


def _restore(text, store):
    def repl(m):
        return store[int(m.group(1))]
    return re.sub(rf"{_SENT}(\d+){_SENT}", repl, text)


# ---------------------------------------------------------------------------
# 2. Exakte Ueberschriften (haeufigste zuerst; deckt Grossteil ab)
# ---------------------------------------------------------------------------

HEADERS = {
    "Arbeitsweg": "مسیر کار",
    "Prüfprogramm": "برنامهٔ بررسی",
    "Normenanker": "لنگرهای قانونی",
    "Arbeitsworkflow": "روند کار",
    "Ausgabe": "خروجی",
    "Prüfraster": "شبکهٔ بررسی",
    "Prüfroutine": "روال بررسی",
    "Fallweichen": "انشعاب‌های پرونده",
    "Auftrag": "دستور کار",
    "Aufgabe": "وظیفه",
    "Quellen": "منابع",
    "Prüf- und Arbeitslogik": "منطق بررسی و کار",
    "Output": "خروجی",
    "Leitentscheidungen": "آرای راهنما",
    "Einstieg": "نقطهٔ ورود",
    "Workflow": "روند کار",
    "Arbeitsauftrag": "دستور کار",
    "Norm- und Quellenanker": "لنگرهای قانونی و منابع",
    "Typische Fehler": "خطاهای رایج",
    "Normen & Rechtsprechung": "قوانین و رویهٔ قضایی",
    "Kuratierte Normen-Bibliothek": "کتابخانهٔ گزیدهٔ قوانین",
    "Normen und Rechtsprechung": "قوانین و رویهٔ قضایی",
    "Rechtsrahmen": "چارچوب حقوقی",
    "Output-Module": "ماژول‌های خروجی",
    "Arbeitsbereich": "حوزهٔ کار",
    "Qualitätsgate": "دروازهٔ کیفیت",
    "Was dieser Arbeitsgang nicht macht": "آنچه این گام کاری انجام نمی‌دهد",
    "Typische Fallen": "دام‌های رایج",
    "Quellenregel": "قاعدهٔ منابع",
    "Typische Fallstricke": "دام‌های رایج",
    "Rechtlicher Rahmen": "چارچوب حقوقی",
    "Red-Team-Fragen": "پرسش‌های تیم مقابل (Red-Team)",
    "Kaltstart-Fragen": "پرسش‌های شروع سرد",
    "Anschluss-Skills": "اسکیل‌های پیوسته",
    "Kaltstart": "شروع سرد",
    "Aktuelle Rechtsprechung": "رویهٔ قضایی روز",
    "Mandantenfall": "پروندهٔ موکل",
    "Erste Schritte": "نخستین گام‌ها",
    "Arbeitsmodus": "حالت کار",
    "Plugin-Kontext": "زمینهٔ افزونه",
    "Fachlicher Anker": "لنگر تخصصی",
    "Rechtsgrundlagen": "مبانی قانونی",
    "Fallweichen dieser Speziallage": "انشعاب‌های این وضعیت ویژه",
    "Kaltstartfragen": "پرسش‌های شروع سرد",
    "Direktstart: lesen, entscheiden, liefern": "شروع مستقیم: بخوان، تصمیم بگیر، تحویل بده",
    "Ausgabeformat": "قالب خروجی",
    "Wofür dieser Arbeitsgang da ist": "این گام کاری برای چیست",
    "Quellen- und Sicherheitsregel": "قاعدهٔ منابع و ایمنی",
    "Kaltstart in 6 Fragen": "شروع سرد در ۶ پرسش",
    "Zentrale Normen": "قوانین محوری",
    "Worum es geht": "موضوع چیست",
    "Fachlicher Zuschnitt": "برش تخصصی",
    "Einsatzlage": "وضعیت کاربرد",
    "Eingaben": "ورودی‌ها",
    "Ergebnisformat": "قالب نتیجه",
    "Arbeitsprodukt": "محصول کار",
    "Startfragen": "پرسش‌های آغازین",
    "Quellen- und Aktualitätsregel": "قاعدهٔ منابع و به‌روزبودن",
    "Fachlicher Kontext": "زمینهٔ تخصصی",
    "Fachlicher Kern": "هستهٔ تخصصی",
    "Einschlägige Normen und Quellen": "قوانین و منابع مرتبط",
    "Sachverhaltsaufnahme — Startfragen": "ثبت واقعیات پرونده — پرسش‌های آغازین",
    "Praxistipps": "نکات عملی",
    "Mustertexte": "متن‌های نمونه",
    "Trade-off-Matrix": "ماتریس موازنه",
    "Wann dieses Modul hilft": "این ماژول کِی کمک می‌کند",
    "Wann dieses Modul hilft / Kaltstart-Fragen": "این ماژول کِی کمک می‌کند / پرسش‌های شروع سرد",
    "Worum geht es konkret": "موضوع به‌طور مشخص چیست",
    "Schritt für Schritt": "گام‌به‌گام",
    "Prüf- und Arbeitsschritte": "گام‌های بررسی و کار",
    "Prozess": "فرایند",
    "Ziel": "هدف",
    "Zweck": "هدف",
    "Vorgehen": "روش اقدام",
    "Hinweise": "یادداشت‌ها",
    "Beispiel": "نمونه",
    "Beispiele": "نمونه‌ها",
    "Checkliste": "سیاههٔ بررسی",
    "Risiken": "خطرها",
    "Zusammenfassung": "خلاصه",
    "Quellenanker": "لنگر منابع",
    "Quellen und Aktualität": "منابع و به‌روزبودن",
    "Sicherheitsregeln": "قواعد ایمنی",
    "Grenzen": "مرزها",
    "Grenzen des Skills": "مرزهای این اسکیل",
    "Kontext": "زمینه",
    "Rolle": "نقش",
    "Anwendungsfall": "مورد کاربرد",
    "Anwendungsfälle": "موارد کاربرد",
    "Definitionen": "تعاریف",
    "Fachkern": "هستهٔ تخصصی",
}

# Muster fuer Ueberschriften mit variablem Anteil: (regex, template)
# {x} = uebersetzter/roher Rest
HEADER_PATTERNS = [
    (re.compile(r"^Fachkern:\s*(.+)$"), "هستهٔ تخصصی: {x}"),
    (re.compile(r"^Fachlicher Kern\s*[—-]\s*(.+)$"), "هستهٔ تخصصی — {x}"),
    (re.compile(r"^Fachlicher Kern:\s*(.+)$"), "هستهٔ تخصصی: {x}"),
    (re.compile(r"^Quellen\s+Stand\s+(.+)$"), "منابع، وضعیت {x}"),
    (re.compile(r"^Quellen\s*\(Stand\s*(.+)\)$"), "منابع (وضعیت {x})"),
    (re.compile(r"^Schritt\s+(\d+)\s*[—-]\s*(.+)$"), "گام {0} — {x}"),
    (re.compile(r"^Stufe\s+(\d+)\s*[—-]\s*(.+)$"), "مرحله {0} — {x}"),
]


# ---------------------------------------------------------------------------
# 3. Exakte Volltextzeilen (hochfrequente Bausteine) -> korrekt uebersetzt
# ---------------------------------------------------------------------------

EXACT_LINES = {
    # Arbeitsweg-Bullets (Zehntausende Vorkommen)
    "Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?":
        "روشن‌کردن نقش، هدف و محصول کاری خواسته‌شده: چه کسی اقدام می‌کند، چه تصمیمی در پیش است، چه مهلتی در جریان است و چه خروجی‌ای لازم است؟",
    "Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).":
        "تعیین مرجع صالح و انتخاب درست مخاطب: موکل، طرف مقابل، ادارهٔ صالح یا دادگاه، کارشناسان و در صورت لزوم نهاد اتحادیهٔ اروپا/بین‌المللی (به جزئیات اسکیل نگاه کنید).",
    "Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.":
        "نخست علامت‌گذاری مهلت‌ها و خطرهای فوری: تنها از مهلت‌های همان حوزهٔ حقوقی مشخص و همان پرونده استفاده کنید؛ اعتراض (Widerspruch)، دعوا (Klage)، ایراد (Einspruch)، طرق شکایت (Rechtsmittel)، مرور زمان (Verjährung)، سقوط حق (Verwirkung) و مهلت‌های ایراد، اعلام، ثبت و انقضا را به‌دقت جدا کنید و هرگز از حوزهٔ تخصصی دیگری برندارید.",
    "Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.":
        "گردآوری اسناد و ادلّه و بررسی خلأها: پرونده‌های اداری، اسناد قراردادی، لوایح، تصمیم‌های اداری (Bescheide)، صورت‌جلسه‌ها، نظرهای کارشناسی و ادلّهٔ بیرونیِ همان حوزه — مدارک نبود را از راه دسترسی به پرونده یا پرسش از موکل فراهم کنید، و برای تغییرهای روزِ قوانین و رویهٔ اداری بررسی زنده انجام دهید.",
    "Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.":
        "راستی‌آزماییِ قوانینِ پایه: قوانینِ مرتبط در زمینهٔ افزونه را به‌صورت زنده در gesetze-im-internet.de، dejure.org، eur-lex.europa.eu و درگاه‌های رسمی فدرال/ایالتی بررسی کنید — نشانی مآخذ را در gesetze-im-internet.de، dejure.org، openJur و پایگاه‌های BVerfG/BGH/EuGH به‌صورت زنده وارسی کنید؛ هیچ استنادِ برخاسته از دانش مدل نیاورید.",
    # Quellen-/Rechtsprechungsregeln
    "Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.":
        "رویهٔ قضایی را تنها هنگامی بیفزایید که دادگاه، تاریخ، شمارهٔ پرونده و یک منبعِ آزادانه قابل‌بررسی موجود باشد؛ از استنادهای کورِ BeckRS/juris استفاده نکنید.",
    "Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:":
        "پیش از هر نتیجه‌گیریِ حقوقی، این لنگرها را با متنِ روزِ قانون بسنجید؛ حقوقِ خاص و حقوقِ ایالتی را تنها زمانی بیفزایید که دستورِ کارِ مشخص را پشتیبانی کند:",
    "Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag trägt:":
        "پیش از هر نتیجه‌گیریِ حقوقی، این لنگرها را با متنِ روزِ قانون بسنجید؛ حقوقِ خاص و حقوقِ ایالتی را تنها زمانی بیفزایید که دستورِ کارِ مشخص را پشتیبانی کند:",
    "- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.":
        "- **ترمزِ خطا:** قوانین/آرای پایه را زنده یا از خودِ پرونده راستی‌آزمایی کنید؛ رویهٔ قضایی تنها با دادگاه، شکلِ رأی، تاریخ، شمارهٔ پرونده و منبعِ آزادانه قابل‌بررسی. هیچ استنادِ کورِ BeckRS، juris، شرح یا مقاله از دانشِ مدل نیاورید.",
    # Ausformulierungspflicht-Block (autogen)
    "<!-- BEGIN ausformulierungspflicht (autogen) -->": "<!-- BEGIN ausformulierungspflicht (autogen) -->",
    "<!-- END ausformulierungspflicht (autogen) -->": "<!-- END ausformulierungspflicht (autogen) -->",
    "> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.":
        "> **الزامِ تمام‌نویسی و استانداردِ قالب.** محصولِ نهایی در **جمله‌های کامل و تمام‌نوشته** تحویل می‌شود — نه اسکلتِ کلیدواژه، نه تنهٔ خالیِ شرط، نه صرفِ فهرست. شرط‌ها به‌صورتِ جمله‌های تمام‌نوشتهٔ بیان‌گرِ اثرِ حقوقی می‌آیند؛ جای‌گیرها مانند `[Name der Mandantin]` روشن علامت می‌خورند و متنِ پیرامون کامل می‌ماند.",
    "> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.":
        "> **شماره‌گذاری:** ساختاربندی منحصراً اعشاری (`1`، `1.1`، `1.1.1` و به همین ترتیب). بدون اعداد رومی، بدون ساختاربندی حرفی یا آمیخته.",
    "> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.":
        "> **شکلِ نوشتار:** هرگاه لایحه، قرارداد، یادداشت، تصمیم، ومرک یا هر سندِ نهاییِ دیگر به‌صورتِ DOCX، PDF یا متنِ قالب‌بندی‌شده بیرون داده شود، باید **Times New Roman ۱۱ pt** به‌عنوانِ قلمِ پایه به‌کار رود. عنوان‌ها در همان قلم می‌مانند و تنها می‌توانند سیاه (بولد) یا پلکانی باشند. در خروجیِ صرفاً Markdown یا چت، این خواستهٔ قالب به‌عنوانِ یادداشتِ برون‌سپاری درج می‌شود.",
}


# ---------------------------------------------------------------------------
# 4. Fachglossar (Phrasen zuerst, dann Einzelbegriffe; longest-match)
# ---------------------------------------------------------------------------

# Mehrwort-Phrasen (werden vor Einzelbegriffen ersetzt)
PHRASES = [
    ("ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt",
     "واقعیات، قانون، بار اثبات، دلایل مقابل و گام بعدی را مرتب می‌کند"),
    ("liefert eine Fristen- und Risikoampel mit Sofortschritten",
     "یک چراغِ مهلت و خطر همراه با گام‌های فوری ارائه می‌دهد"),
    ("prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen",
     "مهلت، شکل، صلاحیت، طریق دادرسی و اقدام‌های فوری را بررسی می‌کند"),
    ("zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition",
     "نتیجه، مهلت، صلاحیت، بار اثبات و موضع مقابل را تجزیه می‌کند"),
    ("ordnet Akteninhalt, Belege, Lücken und Nachforderungen",
     "محتوای پرونده، مدارک، خلأها و درخواست‌های تکمیلی را مرتب می‌کند"),
    ("liefert eine Dokumentenmatrix mit Nachforderungsliste",
     "یک ماتریس اسناد همراه با فهرست درخواست‌های تکمیلی ارائه می‌دهد"),
    ("liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt",
     "یک محصول کاریِ بلافاصله قابل‌استفاده همراه با نقاط بررسی، خطرها و گام بعدی ارائه می‌دهد"),
    ("liefert eine Gegenprüfung mit Fehler-, Beweis- und Fristencheck",
     "یک بازبینیِ متقابل همراه با وارسیِ خطا، اثبات و مهلت ارائه می‌دهد"),
    ("klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill",
     "نقش، هدف، مهلت، مدارک و اسکیلِ تخصصیِ مناسبِ بعدی را روشن می‌کند"),
    ("liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten",
     "یک ماتریس عناصر جرم/دعوا یا ادعا همراه با دلایل مقابل ارائه می‌دهد"),
    ("mit Prüfpunkten, Risiken und nächstem Schritt",
     "همراه با نقاط بررسی، خطرها و گام بعدی"),
    ("Auswahlstichwort", "کلیدواژهٔ انتخاب"),
    ("Arbeitsfeld", "حوزهٔ کار"),
    ("Wenn es um", "وقتی موضوع"),
    ("geht:", "باشد:"),
    ("Normen-/Quellenanker", "لنگر قوانین/منابع"),
    ("Entscheidende Weiche", "انشعابِ تعیین‌کننده"),
    ("Zuständige Stelle", "مرجع صالح"),
    ("nächster Schritt", "گام بعدی"),
    ("nächsten Schritt", "گام بعدی"),
    ("keine Modellwissen-Zitate", "بدون استناد از دانش مدل"),
    ("Live-Check", "بررسی زنده"),
    ("Red-Team", "تیم مقابل (Red-Team)"),
]

# Einzelbegriffe (Fachwortschatz). Longest-first wird beim Bauen sortiert.
TERMS = {
    "Sachverhalt": "واقعیات پرونده",
    "Rechtsfolge": "اثر حقوقی",
    "Tatbestand": "عناصر تشکیل‌دهنده",
    "Beweislast": "بار اثبات",
    "Beweismittel": "ادلّه",
    "Beweis": "اثبات",
    "Gegenargumente": "دلایل مقابل",
    "Gegenargument": "دلیل مقابل",
    "Gegenposition": "موضع مقابل",
    "Zuständigkeit": "صلاحیت",
    "zuständige": "صالح",
    "zuständig": "صالح",
    "Rechtsweg": "طریق دادرسی",
    "Rechtsmittel": "طرق شکایت",
    "Sofortmaßnahmen": "اقدام‌های فوری",
    "Sofortmaßnahme": "اقدام فوری",
    "Sofortschritte": "گام‌های فوری",
    "Risikoampel": "چراغ خطر",
    "Risiko": "خطر",
    "Risiken": "خطرها",
    "Frist": "مهلت",
    "Fristen": "مهلت‌ها",
    "Verjährung": "مرور زمان",
    "Verwirkung": "سقوط حق",
    "Widerspruch": "اعتراض",
    "Einspruch": "ایراد",
    "Klage": "دعوا",
    "Klageerwiderung": "پاسخِ دعوا",
    "Berufung": "تجدیدنظر",
    "Revision": "فرجام",
    "Beschwerde": "شکایت",
    "Anspruch": "ادعا/حق مطالبه",
    "Anspruchsgrundlage": "مبنای مطالبه",
    "Norm": "قانون",
    "Normen": "قوانین",
    "Normtext": "متن قانون",
    "Gesetz": "قانون",
    "Rechtsprechung": "رویهٔ قضایی",
    "Rechtsgebiet": "حوزهٔ حقوقی",
    "Vertrag": "قرارداد",
    "Vertragsurkunde": "سند قراردادی",
    "Kündigung": "فسخ/اخراج",
    "Abmahnung": "اخطار",
    "Mandant": "موکل",
    "Mandantin": "موکل",
    "Mandat": "وکالت/پرونده",
    "Gegner": "طرف مقابل",
    "Gericht": "دادگاه",
    "Behörde": "اداره",
    "Verwaltungsakt": "تصمیم اداری",
    "Verwaltungsakte": "پرونده‌های اداری",
    "Bescheid": "تصمیم اداری",
    "Bescheide": "تصمیم‌های اداری",
    "Schriftsatz": "لایحه",
    "Schriftsätze": "لوایح",
    "Protokoll": "صورت‌جلسه",
    "Sachverständige": "کارشناسان",
    "Sachverständigengutachten": "نظر کارشناسی",
    "Gutachten": "نظر کارشناسی/گزارش حقوقی",
    "Vollmacht": "وکالت‌نامه",
    "Akteneinsicht": "دسترسی به پرونده",
    "Akte": "پرونده",
    "Akteninhalt": "محتوای پرونده",
    "Belege": "مدارک",
    "Beleg": "مدرک",
    "Lücken": "خلأها",
    "Lücke": "خلأ",
    "Nachforderungen": "درخواست‌های تکمیلی",
    "Nachforderung": "درخواست تکمیلی",
    "Prüfung": "بررسی",
    "Prüfpunkte": "نقاط بررسی",
    "Prüfpunkt": "نقطهٔ بررسی",
    "Prüfprogramm": "برنامهٔ بررسی",
    "Arbeitsprodukt": "محصول کار",
    "Arbeitsweg": "مسیر کار",
    "Ausgabe": "خروجی",
    "Entscheidung": "تصمیم",
    "Entscheidungsform": "شکل رأی",
    "Aktenzeichen": "شمارهٔ پرونده",
    "Fundstelle": "نشانی مأخذ",
    "Fundstellen": "نشانی مآخذ",
    "Quelle": "منبع",
    "Quellen": "منابع",
    "Rolle": "نقش",
    "Ziel": "هدف",
    "Output": "خروجی",
    "Adressat": "مخاطب",
    "Adressaten": "مخاطبان",
    "Form": "شکل",
    "Frage": "پرسش",
    "Fragen": "پرسش‌ها",
    "Schritt": "گام",
    "Schritte": "گام‌ها",
    "Modul": "ماژول",
    "Skill": "اسکیل",
    "Einwand": "ایراد",
    "Matrix": "ماتریس",
    "Verwaltungspraxis": "رویهٔ اداری",
    "Rückfrage": "پرسش مجدد",
    "Eilrisiken": "خطرهای فوری",
    "Eilrechtsschutz": "حمایت قضاییِ فوری",
    "Ausschlussfristen": "مهلت‌های انقضا",
    "Ausschlussfrist": "مهلت انقضا",
    "Anzeige": "اعلام/شکایت",
    "Anmeldung": "ثبت/اعلام",
    "Rüge": "ایراد",
    "Grundrechte": "حقوق بنیادین",
    "Grundrecht": "حق بنیادین",
    "Menschenwürde": "کرامت انسانی",
    "Disziplinarverfahren": "دادرسی انتظامی",
    "Disziplinarweg": "مسیر انتظامی",
    "Nachweisführung": "ارائهٔ اثبات",
    "Nachweis": "اثبات",
    "Status": "وضعیت",
    "Besoldung": "حقوق و مزایا",
    "Versorgung": "تأمین/بازنشستگی",
    "Dienstpflicht": "وظیفهٔ خدمتی",
    "Befehl": "دستور (نظامی)",
    "Gehorsam": "اطاعت",
    "Gewissen": "وجدان",
    "Soldat": "سرباز",
    "Vorgesetzter": "مافوق",
    "Vorgesetzten": "مافوق",
    "amtlichen": "رسمی",
    "amtliche": "رسمی",
    "amtlich": "رسمی",
    "Text": "متن",
    "Kontext": "زمینه",
    "Ergebnis": "نتیجه",
    "Systemstelle": "جایگاه سامانه‌ای",
    "Katechismus": "کاتشیزم",
    "Partikularrecht": "حقوق خاص (پارتیکولار)",
    "Dekret": "فرمان",
    "kanonistisches": "کانونی",
    "kanonistisch": "کانونی",
    "mehrsprachig": "چندزبانه",
    "mehrsprachige": "چندزبانه",
    "pastoral": "شبانی",
    "papsttreu": "وفادار به پاپ",
    "katholisch": "کاتولیک",
    "Canon": "کانون (Canon)",
    "Praxistipps": "نکات عملی",
    "Praxis": "عمل",
    "typische": "رایج",
    "Typische": "رایج",
    "Fehler": "خطا",
    "Fallen": "دام‌ها",
    "Fallstricke": "دام‌ها",
    "Übersicht": "نمای کلی",
    "Beispiel": "نمونه",
    "Beispiele": "نمونه‌ها",
    "Hinweis": "یادداشت",
    "Hinweise": "یادداشت‌ها",
    "Checkliste": "سیاههٔ بررسی",
    "Zusammenfassung": "خلاصه",
    "Definition": "تعریف",
    "Definitionen": "تعاریف",
    "Verhältnis": "نسبت",
    "Zweck": "هدف",
    "Vorgehen": "روش اقدام",
    "Grenzen": "مرزها",
    "Anwendungsfall": "مورد کاربرد",
    "Kaltstart": "شروع سرد",
    "Einstieg": "نقطهٔ ورود",
    "Workflow": "روند کار",
    "Auftrag": "دستور کار",
    "Aufgabe": "وظیفه",
    "Rechtsrahmen": "چارچوب حقوقی",
    "Rechtsgrundlagen": "مبانی قانونی",
    "Rechtsgrundlage": "مبنای قانونی",
}


# ---------------------------------------------------------------------------
# 5. Uebersetzungslogik
# ---------------------------------------------------------------------------

# Sortierte Ersetzungsliste (Phrasen + Terme), longest-first
def _build_replacements():
    reps = list(PHRASES)
    for de, fa in TERMS.items():
        reps.append((de, fa))
    reps.sort(key=lambda kv: len(kv[0]), reverse=True)
    compiled = []
    for de, fa in reps:
        # Wortgrenzen fuer alphabetische Begriffe; Phrasen mit Sonderzeichen roh
        if re.match(r"^[\wäöüÄÖÜß -]+$", de):
            pat = re.compile(r"(?<![\wäöüÄÖÜß])" + re.escape(de) + r"(?![\wäöüÄÖÜß])")
        else:
            pat = re.compile(re.escape(de))
        compiled.append((pat, fa))
    return compiled


_REPLACEMENTS = _build_replacements()

_MD_PREFIX_RE = re.compile(r"^(\s*(?:[-*+]\s+|\d+[.)]\s+|>\s+|#{1,6}\s+)?)(.*)$")


def _translate_inline(text):
    """Glossar-/Phrasenersetzung auf bereits maskiertem Text."""
    for pat, fa in _REPLACEMENTS:
        text = pat.sub(fa, text)
    return text


def translate_header(content):
    """content = Ueberschriftstext ohne fuehrende #."""
    c = content.strip()
    # bold-Markup abtrennen
    if c in HEADERS:
        return HEADERS[c]
    for rx, tmpl in HEADER_PATTERNS:
        m = rx.match(c)
        if m:
            rest = m.group(m.lastindex)
            store = []
            rest_m = _protect(rest, store)
            rest_t = _restore(_translate_inline(rest_m), store)
            out = tmpl.replace("{x}", rest_t)
            if "{0}" in out:
                out = out.replace("{0}", m.group(1))
            return out
    # Fallback: Glossar
    store = []
    return _restore(_translate_inline(_protect(c, store)), store)


def translate_line(line):
    """Uebersetzt eine einzelne Markdown-Zeile strukturerhaltend."""
    if not line.strip():
        return line
    # Tabellentrenner unveraendert
    if re.match(r"^\s*\|?[\s:|-]+\|?\s*$", line) and "|" in line:
        return line

    m = _MD_PREFIX_RE.match(line)
    prefix, content = m.group(1), m.group(2)

    # Ueberschrift?
    if prefix.strip().startswith("#"):
        return prefix + translate_header(content)

    # Exakte Volltextzeile (mit oder ohne Praefix)?
    stripped = line.strip()
    if stripped in EXACT_LINES:
        # Praefix erhalten
        lead = line[: len(line) - len(line.lstrip())]
        return lead + EXACT_LINES[stripped]
    if content.strip() in EXACT_LINES:
        return prefix + EXACT_LINES[content.strip()]

    # Tabellenzeile: Zellen einzeln
    if content.strip().startswith("|") or (line.count("|") >= 2 and "|" in content):
        cells = line.split("|")
        out = []
        for cell in cells:
            if cell.strip():
                store = []
                out.append(" " + _restore(_translate_inline(_protect(cell.strip(), store)), store) + " ")
            else:
                out.append(cell)
        return "|".join(out)

    # Standard: maskieren, glossar, entmaskieren
    store = []
    translated = _restore(_translate_inline(_protect(content, store)), store)
    return prefix + translated


def translate_body(body):
    """Uebersetzt den Markdown-Body (ohne Frontmatter)."""
    lines = body.split("\n")
    out = []
    in_code = False
    for line in lines:
        if line.strip().startswith("```"):
            in_code = not in_code
            out.append(line)
            continue
        if in_code:
            out.append(line)  # Code woertlich
            continue
        out.append(translate_line(line))
    return "\n".join(out)


def split_frontmatter(text):
    """Trennt YAML-Frontmatter vom Body. Gibt (frontmatter_or_None, body)."""
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            nl = text.find("\n", end + 1)
            if nl == -1:
                nl = len(text)
            fm = text[: nl + 1]
            body = text[nl + 1 :]
            return fm, body
    return None, text
