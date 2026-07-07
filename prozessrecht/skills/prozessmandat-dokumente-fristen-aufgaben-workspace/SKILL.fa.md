---
name: prozessmandat-dokumente-fristen-aufgaben-workspace
description: "Wenn es um Mandatsworkspace, Kontexttrennung und Fristensteuerung in Prozessrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# فضای کار و دستور العمل، جداسازی زمینه ای و کنترل زمان

## هدف

وکلا با چندین مشتری و پروسه در موازی بر مأموریت های مختلف کار می کنند. یک حوزه وظیفه به طور دقیق زمینه ی فرمان را از همه موارد دیگر جدا میکند. این مهارت مدیریت آن مناطق کاری را انجام میدهد. برای درخواستهای اداره دستورات: ایجاد، فهرست کردن، تغییر دادن، بسته شدن و آرکائیو کردن حکم دادگاهی است.

**حالت استاندارد برای وکلا حقوق بشر غیر فعال شده است** (پرداد 46 BRAOبرای این موارد، افزونه به طور خودکار در سطح دفتر می چرخد. `Aktiviert: ✗` در تنظیمات دفتر، این مهارت وضعیت غیرفعال را توضیح می دهد و پیشنهاد یک تغییر مجدد دارد.

## ورودی‌ها

- ** فرماندهی زیر** (ضروری): `neu`, `liste`, `wechseln`, `schließen` یا `keins`
- **نام ماموریت (سلوگ)**: با خط کوچک به همراه خطوط متصل شده `schmidt-gmbh-berufung-2025`)
- ** اطلاعات مامورین** (در `neu`): نامزد، طرف مقابل، نوع فرمان، سطح محرمانه بودن، واقعیت ها، انحرافات خاص در مورد دستور نامه از استاندارد کارگزاری، مجوزهای مرتبط

## چارچوب حقوقی

### قوانین هسته ای

- **پارagraph 43a Abs. 2 BRAO** - محامّت صراحت؛ حریم خصوصی کامل در مورد موکلان، عدم انتقال اطلاعات بین مأموریت ها بدون رضایت.
- **پرداد 50 BRAO** - دست نوشته های وکیل؛ حداقل پنج سال پس از پایان کار (پرداخت 50) Abs. 2 BRAO).
- **پرداد 3 BORA** - ثبت دستورات؛ تا زمان مناسب انتقال، باید پرونده ها را نگه داشت.
- **پرداد 45 BRAO** - ممنوعیت فعالیت در زمینه تضاد منافع؛ کنترل تعارض قبل از زمان تعیین اجاره ضروری است.
- **پرداد 2 Abs. 1 DSGVO i.V.m. بند 1 BDSG** - اطلاعات شخصی در اسناد مأموریت تحت قانون حفاظت از داده ها قرار دارد؛ جداسازی سازمانی یک اقدام فنی و سازماندهی است i.S.d. Art. 32 DSGVO.

### آرای راهنما

- قضیه: هیچ تصمیمی را از دانش نمونه ای نقل نکنید؛ قبل از انتشار با دادگاه، شکل تصمیم گیری و تاریخ آن ها، نشانه های پرونده یا اظهارات قابل اثبات را توسط منبع رسمی یا آزاد تأیید کنید.

### قاعدهٔ منابع

قانون منبع: هیچ جای برای یافتن نظرات، کتابچه یا مقاله از دانش مدل؛ ادبیات فقط با منابع کاربر و یا زیرنویس زنده مجوزff.
## زمان

** پیش:** کار جاری زیر خط استاندارد است. اگر وضعیت مشتری متفاوت باشد (به عنوان "اختیارات استراتژیک" بالا) ، مراحل را به طور مناسب کوتاه کنید، تغییر دهید یا با مهارت دیگری جایگزین نمایید - وارت فلو راهنما نیست نه برنامه اجباری

### مرحله اول: بررسی تنظیمات

بخونید `CLAUDE.md` → بخش `## Mandatsarbeitsbereiche`. `Aktiviert: ✗`:

> "مناطق کار و مامورتی غیرفعال شده است - دفتر اداری به عنوان یک اداره ی تک مهلت (به عنوان مثال، وکیل حقوق اتحادیه ای طبق بند 46) BRAO) به صورت خودکار در سطح دفتر تنظیم و کار می کند. `/prozessrecht:prozessrecht-kaltstart-interview --neu` در این صورت، شرکت های مختلف از سازمانهای دولتی و اداری که به عنوان یک دفتر رسمی یا اداره ای تشکیل می دهند `/mandat-arbeitsbereich` لازم نیست".

### مرحله دوم: انجام فرمان فرعی

#### `neu <slug>`

1. بررسی کنید که آیا سلوگ هنوز در `mandate/<slug>/` یا `mandate/_archiviert/<slug>/` در صورت برخورد، اجازه دادن به دیگران انتخاب کنند.
2. مصاحبه ی ثبت نام:
   - **مندت** (به طرف نماینده یا بخش داخلی وکیل سندیکی)
   - **طرف مقابل** (یک یا چند)
   - ** نوع دستورات**: دعوای مدنی | قضیه حقوق کار | روش های مدیریت | دفاعی کیفری | در مورد حقوق مالیاتی (FGO) | در مورد حقوق اجتماعی (SGG) | اختلافات مربوط به مالکیت ملک | دیگر 
   - ** سطح اطمینان**: استاندارد | افزایش | تیم پاک 
   - **سروق کسب و کار** (2-5 جمله: موضوع، شرکت کنندگان، ارزش اختلاف/خطر، ویژگی ها)
   - **مختلفات مربوط به ماموریت از استاندارد خدمات اداری** (مثلا "دستیاب گزارش های وضعیت هفتگی را می طلبد"، "طرف مقابل شریک تجاری است - صدای کاهش سطح")
   - **منتظرات مرتبط** (بخش های مربوطه)
3. `mandate/<slug>/akte.md` در زیر این مقاله، به صورت نمونه ای نوشته شده است.
4. `mandate/<slug>/verlauf.md` با ثبت افتتاحیه
5. خالی `mandate/<slug>/notizen.md` -بذارید .
6. به طور خودکار تغییر نکنید - بپرسید: "می خواهم `<slug>` تغییر می کنند؟`/prozessrecht:prozessrecht-mandat-arbeitsbereich wechseln <slug>`)"

#### `liste`

`mandate/*/akte.md` فهرست بندی کنید. جدول را به صورت زیر بزنید:

| خروجی | مشتری | نوع فرمان | وضعیت | باز شده | فعال |
|---|---|---|---|---|---|

مأموریت فعال `*` این امر در زیر عنوان جداگانه "آرشیو شده" است.

#### `wechseln <slug>`

1. تایید کنید که `mandate/<slug>/akte.md` وجود دارد.
2. `Aktives Mandat:`-خطي در دفتر اداري`CLAUDE.md` به `<slug>` می دانی؟
3. خلاصه ی `akte.md` این گزارش را برای تایید ارسال کنید.

#### `schließen <slug>`

1. تایید کنید که `mandate/<slug>/` وجود دارد.
2. نوشته "منته ای که انجام شده" `mandate/<slug>/verlauf.md` با تاریخ امروز قرار دهید.
3. `mandate/<slug>/` بعد از `mandate/_archiviert/<slug>/` تعویض (نه حذف) - بند 50 Abs. 2 BRAO).
4. آیا این فرمان بسته فعال بود؟ `Aktives Mandat:` به `keins — nur Kanzleiebene` می دانی؟

#### `keins`

`Aktives Mandat:` در دفتر اداری`CLAUDE.md` به `keins — nur Kanzleiebene` قرار دادن. تایید را نشان دهید

## گزینه های استراتژیک (پیش از انتخاب قالب)

قبل از اینکه یک به یک پر کنید، باید بررسی کرد که کدام نوع برای کنسلتیون مشتری مناسب است. این قالب شکل احتمالی ای ـه - تنها نیست

| ستاره شناسی | راه توصیه شده |
|---|---|
| استاندارد - ایجاد فضای کار اجباری در زمینه قوانین قانونی | فضای کاری به ترتیب طرح، قالب زیر |
| گزینه A - تنها به عنوان مشاور، نه برای شکایت | دستور مشاوره؛ حذف قالب های دادگاه |
| گزینه B - چند دفعه در موازی | ساختار وركسبیس بین محله ها؛ قسمت های جداگانه پرونده |
| گزینه C - دادگاه بین المللی | فضای کار در دادگاه های داوری؛ استفاده از مهارتهای دیگر به طور همزمان |

اگر کنستلاسیون مشتری ** نمی تواند به طرح استاندارد مطابقت داشته باشد، باید قالب را تغییر دهید یا با مهارت دیگری جایگزین کنید - نه اینکه دستورات را در schema فشار بدهید.

## قالب خروجی

### طرح `akte.md`

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **الزامِ تمام‌نویسی و استانداردِ قالب.** محصولِ نهایی در **جمله‌های کامل و تمام‌نوشته** تحویل می‌شود — نه اسکلتِ کلیدواژه، نه تنهٔ خالیِ شرط، نه صرفِ فهرست. شرط‌ها به‌صورتِ جمله‌های تمام‌نوشتهٔ بیان‌گرِ اثرِ حقوقی می‌آیند؛ جای‌گیرها مانند `[Name der Mandantin]` روشن علامت می‌خورند و متنِ پیرامون کامل می‌ماند.
>
> **شکلِ نوشتار:** هرگاه لایحه، قرارداد، یادداشت، تصمیم، ومرک یا هر سندِ نهاییِ دیگر به‌صورتِ DOCX، PDF یا متنِ قالب‌بندی‌شده بیرون داده شود، باید **Times New Roman ۱۱ pt** به‌عنوانِ قلمِ پایه به‌کار رود. عنوان‌ها در همان قلم می‌مانند و تنها می‌توانند سیاه (بولد) یا پلکانی باشند. در خروجیِ صرفاً Markdown یا چت، این خواستهٔ قالب به‌عنوانِ یادداشتِ برون‌سپاری درج می‌شود.
>
> **شماره‌گذاری:** ساختاربندی منحصراً اعشاری (`1`، `1.1`، `1.1.1` و به همین ترتیب). بدون اعداد رومی، بدون ساختاربندی حرفی یا آمیخته.
<!-- END ausformulierungspflicht (autogen) -->

```markdown
[ARBEITSERGEBNIS-KOPFZEILE — gemäß Kanzleikonfiguration]

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen fuer ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.

# Mandat: [Mandant] — [Kurzbeschreibung]

**Slug:** [slug]
**Eröffnet:** [JJJJ-MM-TT]
**Status:** aktiv
**Vertraulichkeit:** [standard / erhöht / clean-team]

---
## Parteien

**Mandant:** [Name]
**Gegenseite:** [Name(n)]

## Mandatstyp

[Zivilstreitigkeit | Arbeitsrechtssache | Verwaltungsverfahren | Strafverteidigung | FGO | SGG | IP | sonstiges — mit einzeiliger Begründung]

## Sachverhalt

[2–5 Sätze: Gegenstand, Beteiligte, Streitwert/Risiko, Besonderheiten gegenüber dem Kanzleistandard.]

## Mandatsspezifische Abweichungen

*Abweichungen vom Kanzleistandard, die nur für dieses Mandat gelten.*

- [z. B. "Prozesskostenfondlimit: Mandant besteht auf max. 50.000 EUR, nicht Standard 100.000 EUR."]
- [z. B. "Ton: deeskalierend — Gegenseite ist Geschäftspartner."]
- [z. B. "Gerichtsstand: Hamburg; abweichend vom Standardsitz München."]

## Verwandte Mandate

- [slug — ein Satz zur Verbindung]

## Vertraulichkeitshinweise

[Bei erhöhter Vertraulichkeit oder Clean-Team: Begründung. Wer darf die Mandatsakte einsehen. Ob mandatsübergreifender Kontext trotz globaler Aktivierung untersagt ist.]
```

### دانه `verlauf.md`

```markdown
# Verlauf: [Mandant] — [Kurzbeschreibung]

Chronologisches Ereignisprotokoll. Jüngster Eintrag oben.

---

## [JJJJ-MM-TT] — Mandat eröffnet

Aufnahme abgeschlossen. Slug: `[slug]`. Status: aktiv.
[Weiterer Anfangskontext — z. B. "Eröffnet nach Zustellung Klageschrift durch [Gegenseite] am [Datum]."]
```

## نمونه

**پرسش:** "پذیری جدید از کار: دادگاه تجدید نظر Müller GmbH علیه Bauer AG, OLG میونخ، ارزش مورد بحث 250.000 یورو.

** فرماندهی زیر:** `neu muellerGmbH-bauer-berufung-2025`

** نتیجه:** `akte.md` با عنوان "منافع مدنی" ، رازداری "استانداردی"، واقعیت اطلاعات ایجاد می شود. `verlauf.md` با شروع به نوشتن امروز. سوال: "در `muellerGmbH-bauer-berufung-2025` تغییر می کنند؟"

## خطرات و اشتباهات معمول

- **پرداخت اطلاعات بین ماموریت ها:** بدون جداسازی دقیق، ممکن است اطلاعاتی از فرمان A در هنگام پردازش فرمان B قابل مشاهده باشد - نقض بخش 43a Abs. 2 BRAO. پرچم `Mandatsübergreifender Kontext: aus` (معیاری) از این کار جلوگیری می کند.
- ** حذف به جای ثبت:** دستورات محفوظ شده نمی توانند حذف شوند (پارagraph 50 Abs. 2 BRAO: 5 سال نگهداری `schließen` فقط حرکت می کنه.
- **کنترول درگیری ها وظیفه این مهارت نیست:** ثبت اطلاعات وکیل را می گیرد؛ کنترول مستقل درگیری نمی تواند پلگ ان را جایگزین کند.
- ** برخورد با سلفی که در آن ثبت شده است:** استفاده مجدد از یک سلفه `_archiviert/` در این مورد، آیا دستورات زیر `_archiviert/<slug>/` در ادامه می توان آن را خواند.
- ** نگه داشتن:** بسته شدن به صورت آرشیو شده؛ زمان حذف طبق بند 50 BRAO و DSGVO Art. 17 این موضوع مربوط به دفتر است.

## تعهد به منبع

- متن قانون: بند 43a، 45 و 46 BRAO; بند 3 BORA; Art. 32 DSGVO; بند 1 BDSG
- قضیه: هیچ تصمیمی را از دانش نمونه ای نقل نکنید؛ قبل از انتشار با دادگاه، شکل تصمیم گیری و تاریخ آن ها، نشانه های پرونده یا اظهارات قابل اثبات را توسط منبع رسمی یا آزاد تأیید کنید.
- قانون منبع: ادبیات فقط با منابع کاربر یا دسترسی زنده مجاز؛ هیچ جای برای یافتن نظرات، کتابچه و مقاله از دانش مدل نیست.

توجه: این مهارت جایگزین مشاوره حقوقی در یک مورد خاص نیست.
