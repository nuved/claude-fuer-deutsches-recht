---
name: mandat-arbeitsbereich
description: "Wenn es um /mandat-arbeitsbereich in diesem Spezialbereich geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Beweislast- und Substantiierungsmatrix."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# /مناطق کار و وظیفه

## مسیر کار

- روشن‌کردن نقش، هدف و محصول کاری خواسته‌شده: چه کسی اقدام می‌کند، چه تصمیمی در پیش است، چه مهلتی در جریان است و چه خروجی‌ای لازم است؟
- اولین زمان و ریسک های فوری را نشان دهید: آغاز اعمال AI-VO02.2025 ممنوعه، دو08.2025 GPAI، 02.08.2026 خطر بالا (پاینده ای) در مورد حادثه جدی 15 روز DSGVO از قبل، دپیا
- بررسی استانداردهای عملی:VO 2024/1689 Art. 9، 10، 14، 22، 27 و 50، ISO/IEC 42001، NIST AI RMF 1.0، اصول OECD AI DSGVO Art. 22، 35، محصول مسئولیتRL 2024/2853 - یافته های مربوط به gesetze-im-internet.de, dejure.org،آفتاب BVerfG-/BGH-/EuGH-دیتابیس زنده را بررسی کنید، بدون نقل قول دانش مدل
- تعیین و انتخاب صحیح مقامات: مدیران، افسران هوش مصنوعی، مامور حفاظت از داده ها، سازمان های تعمیل، شورای نظارت، بازار کنترل، حسابرسی خارجی، افراد ذی اهمیت.
- جمع آوری اسناد و شواهد، بررسی شکاف ها: فهرست هوش مصنوعی، تحلیل ریسک، FRIA (مؤخثرات حقوق اساسی) ، سیاست حاکمیت هوش مصنوعی, مدل کارتها، گزارش حسابرسی DSGVO-DPIA، مدرک آموزش: دریافت شواهد از طریق بررسی پرونده ها یا بازرسی با مشتری؛ چک زنده برای تغییرات روزانه در استانداردهای فعلی و شیوه های مدیریت.

## هدف

کارکنان شرکت با چندین مشتری و مأموریت ها همکاری می کنند.
در این زمینه، یک مشتری یا سفارش از هر کس دیگری جدا شده است - برای
§ 43a Abs. 2 BRAO (مکلفیت محرمانه) و § 203 StGB (سرآهنگی فرمانده)
این مهارت، مدیریت فضای کار را انجام می دهد.

## ورودی‌ها

- پروفایل عملی `~/.claude/plugins/config/claude-fuer-deutsches-recht/ki-governance/CLAUDE.md`
 (قسم) `## Mandate-Workspaces`)
- دستور فرعی و لغز اختیاری از طرف کاربر

## زمان

1. CLAUDE.md را بخوانید - تایید کنید که بخش `## Mandate-Workspaces` وجود دارد.
 در صورت `Aktiviert` = `✗`:
 > فضای کار سفارش داده شده غیر فعال است - آنها به عنوان یک عمل داخلی با مشتری هستند
 > این افزونه به طور خودکار از زمینه عملی کار می کند.
 > در واقع برای چندین مشتری کار کنید `/ki-governance:ki- governance سردستارت مصاحبه
 > --redo` neu aus und wählen einen Kanzleikontext. Andernfalls benötigen Sie `حوزه کاری
 > نه، نمی تونم.

2. در اولین توکن های `$ARGUMENTS` شاخه:
 - `new` → شروع مصاحبه ثبت نام `mandat.md` نوشتن `verlauf.md` و `notizen.md`
 شروع کردن.
 - `list` همه `mandate/*/mandat.md` فهرست بندی، چاپ نمودار ها و نشان دادن ماموریت فعال.
 - `switch` → `Aktives Mandat:`-در CLAUDE.md به روز رسانی خط ها
 - `close` → `mandate/<slug>/` بعد از `mandate/_archiv/<slug>/` تعویض؛ تاریخ بسته شدن
 در `verlauf.md` ثبت اطلاعات
 - `none` → `Aktives Mandat:` به `keines – nur Praxiskontext` می دانی؟

3. به کاربر نشان دهید که چه چیزی تغییر کرده است و قبل از نوشتن آن را تایید کنید.

## فرمان های زیر

- `/ki-governance:ki-governance-mandat-arbeitsbereich new <slug>` - ایجاد فضای کار جدید برای ماموریت ها، کوتاه مدت
 مصاحبه ثبت نام `mandat.md` نوشتن
- `/ki-governance:ki-governance-mandat-arbeitsbereich list` - فهرست ماموریت های دارای وضعیت و پرچم فعال
- `/ki-governance:ki-governance-mandat-arbeitsbereich switch <slug>` - در حال انجام ماموریت فعال
- `/ki-governance:ki-governance-mandat-arbeitsbereich close <slug>` - ثبت سفارش (به عنوان
 `~/.claude/plugins/config/claude-fuer-deutsches-recht/ki-governance/mandate/_archiv/` (به صورت متداول، هرگز حذف نکنید)
- `/ki-governance:ki-governance-mandat-arbeitsbereich none` - از مأموریت فعال جدا شدن، فقط در سطح عملی
 کار کردن

## طرح ذخیره سازی

```
~/.claude/plugins/config/claude-fuer-deutsches-recht/ki-governance/
├── CLAUDE.md # praxisweites Praxisprofil
└── mandate/
 ├── <slug>/
 │ ├── mandat.md # Mandant, Gegenseite, Mandatstyp, Kernfakten, Abweichungen
 │ ├── verlauf.md # datiertes Log von Ereignissen, Entscheidungen, Entwürfen
 │ ├── notizen.md # freie Arbeitsnotizen
 │ └── outputs/ # Skill-Ausgaben für dieses Mandat (optionaler Unterordner)
 └── _archiv/
 └── <slug>/ # geschlossene Mandate – lesbar, aber nicht aktiv
```

در این بخش، slugs با خطوط کوچک نوشته شده است. `mueller-ki-review-2026`,
`xyz-gmbh-aia`, `vendor-openai-avv`.

## منطق زیر فرمان

### `new <slug>`

1. تایید کنید که سلوگ قبلاً در `mandate/<slug>/` یا `mandate/_archiv/<slug>/`
 در صورت استفاده مجدد، از یک سلوگ دیگر انتخاب کنید.
2. شروع مصاحبه ثبت نام:
 - **منتظرم** (طرفی که ما نمایندگی می کنیم یا واحد داخلی در محل)
 - **طرف مقابل** (صفحه دیگر - ممکن است چند باشد)
 - **منتظره ی دستورات** (برای حکومت: مورد استفاده داخلی از هوش مصنوعی) | بررسی هوش مصنوعی فروشنده | ارزیابی نتیجه | تغییر مقررات | طرح دستورالعمل | (مختلف) 
 - ** سطح اطمینان** (استانداردی) | افزایش | تیم پاک - افزایش نیاز به ویژه 
 در موقعیت های مختلف مراقب باشید)
 - **حقیقت های اصلی** (2-5 جمله: در این فرمان چه می شود، طرفین سهامدار کیست؟
 (به عنوان مثال، در مورد آنچه که می تواند انجام شود)
 - **مختلفات مشخصی از دفتر بازی** (به عنوان مثال "تعارف طلب 24 ماهه)
 "دستشرکت های استراتژیک - در رابطه با یک شرکت دیگر"
 صدا"§ 203 StGB: مکانیسم های ویژه ای برای محافظت مورد نیاز است")
 - **منتخب های مرتبط** (سرگ دیگر منتظم ها)
3. `mandate/<slug>/mandat.md` با این طرح زیر بنویسید.
4. `mandate/<slug>/verlauf.md` با یک مطلب "آفتاد" شروع کنید.
5. خالی `mandate/<slug>/notizen.md` -بذارید .
6. ** نه** به طور خودکار برای تغییر در ماموریت جدید.
 `<slug>` تغییر می کنند؟`/ki-governance:ki-governance-mandat-arbeitsbereich switch <slug>`)"

### `list`

`mandate/*/mandat.md` جدول:

| خروجی | مشتری | نوع فرمان | وضعیت | باز شده | فعال |
|---|---|---|---|---|---|

مأموریت فعال `*` نشان دادن `_archiv/*` در زیر عنوان جداگانه "آرشیو شده"
در صورت وجود آن ها.

### `switch <slug>`

1. تایید کنید که `mandate/<slug>/mandat.md` در غیر این صورت، `/منتظره
 به شما پیشنهاد می کنم
2. `Aktives Mandat:`-در CLAUDE.md `Aktives Mandat: <slug>` می دانی؟
3. به کاربران خلاصه mandat.md را نشان دهید تا بتوانند تایید کنند که
 در زمان مناسب قرار دادن.

### `close <slug>`

1. تایید کنید که `mandate/<slug>/` وجود دارد.
2. "آغاز" با تاریخ امروز `mandate/<slug>/verlauf.md` و از آن استفاده کنید.
3. `mandate/<slug>/` → `mandate/_archiv/<slug>/` پس از آن، حرکت کنید.
4. اگر فرمان بسته فعال بود، `Aktives Mandat:` به
 `keines – nur Praxiskontext` می دانی؟

### `none`

`Aktives Mandat:` در CLAUDE.md `keines – nur Praxiskontext` با کاربران تایید کنید.

## `mandat.md`-تازه

```markdown
[ARBEITSPRODUKT-HEADER – gemäß Plugin-Konfiguration; Vertraulichkeitsmarkierung beachten]

### Mandat: [Mandant] – [Kurzbeschreibung]

**Slug:** [slug]
**Eröffnet:** [JJJJ-MM-TT]
**Status:** aktiv
**Vertraulichkeit:** [standard / erhöht / clean-team]
**§ 203 StGB:** [Schweigepflicht beachtet – Schutzmechanismen: [Beschreibung]]

---

## Parteien

**Mandant:** [Name]
**Gegenseite:** [Name(n)]

## Mandatstyp

[KI-Anwendungsfall intern | Vendor-AI-Review | KI-Folgenabschätzung (FRIA/DSFA) | Regulierungsänderung | Richtlinienprojekt | Sonstiges – mit einzeiliger Begründung]

## Kernfakten

[2–5 Sätze. Worum geht es. Wer sind die Stakeholder. Was steht auf dem Spiel. Was es vom
Standard-Playbook unterscheidet.]

## Mandatsspezifische Abweichungen

*Jede Abweichung vom praxisweiten Playbook, die nur für dieses Mandat gilt.*

- [z. B. "Haftungshöchstbetrag: Mandant verlangt 24 Monate, nicht Hausstandard 12."]
- [z. B. "Ton: beziehungserhaltend – Gegenseite ist strategischer Partner."]
- [z. B. "Rechtswahl: muss deutsches Recht sein."]
- [z. B. "§ 203 StGB: nur On-Premise-Verarbeitung, kein Drittanbieter-KI-System ohne AVV."]

## Verbundene Mandate

- [slug – ein Satz, warum verbunden]

## Vertraulichkeitshinweise

[Falls erhöht oder clean-team, erläutern warum. Wer Mandatsdateien einsehen darf. Ob
mandatsübergreifender Kontext trotz globaler Aktivierung zulässig ist.]
```

## `verlauf.md`- شروع کردن

```markdown
### Verlauf: [Mandant] – [Kurzbeschreibung]

Nur-Anhänge-Ereignisprotokoll. Neuestes oben.

---

## [JJJJ-MM-TT] – Mandat eröffnet

Aufnahme abgeschlossen. Slug: `[slug]`. Status: aktiv.
[Anfangskontext über mandat.md hinaus – z. B. "Eröffnet als Reaktion auf eingehenden
Vendor-KI-Vertrag von [Gegenseite]."]
```

## زمینه های بین المللی

CLAUDE.md یک `Mandatsübergreifender Kontext:`-پرچم `aus` (معیاری) یک مهارت در خواندن
در دستور A ** هرگز** پرونده ها را وارد کنید `mandate/B/`این تضمین محرمانه ای برای
این امر در مورد § 43a Abs. 2 BRAO و § 203 StGB.

در `an` یک مهارت فقط می تواند فایل های بین المللی را در صورت اینکه کاربر به طور صریح
در این زمینه می خواهد (به عنوان مثال "موازنه ی موقعیت ما با بالاترین میزان مسئولیت نسبت به آخرین موارد
در این زمینه، به عنوان مثال: `an` این استاندارد است که فقط دستور فعال را بارگذاری کنید.

## منابع و نقل قول

متعهد به نقل قول `../references/zitierweise.md`.

- § 43a Abs. 2 BRAO - محرمانه بودن حقوقی `[Primärquelle]`
- § 203 StGB - راز مشتری در مورد استفاده از هوش مصنوعی `[Primärquelle]`
- § 53 StPO - حق انکار گواهی `[Primärquelle]`

## چه چیزی این مهارت نمی کند

- **هیچ بررسی در مورد تضاد منافع وجود ندارد.** تعارضات با کارآموزی/کتاب است؛
 این فرم ثبت نام، آنچه را که کاربر وارد می کند ضبط میکند.
- **هیچ گونه اجباری برای نگهداری نیست.** بسته شدن یک دستور را به صورت آرشیو می کند؛ آن را حذف نمی کند.
 این دستورالعمل ذخیره سازی خارج از حوزه کاربرد است.
- **هیچ راهنمای هزینه ای نیست.** مهارت محتوا تصمیم می گیرد که به کجا بنویسد؛
 این مهارت به او می گوید که کدام پوشه فعال است.
- **هیچ تصمیمی درباره اجازه ی میان مدت نیست.**
 ازش پیروی کن.

## خطرات / اشتباهات معمول

- **§ 203 StGB در مورد استفاده از هوش مصنوعی.** وقتی اطلاعات مشتری را به سیستم های هوشمندی شخص ثالث وارد می کنید
 به عنوان یک Art. 28 DSGVO و مطابقت با § 203 StGB در دستور کار.md
 اسناد را ثبت کنید.
- ** استفاده مجدد از سلوگ* * منجر به مخلوط شدن زمینه می شود. همیشه دوباره بررسی کنید که آیا سلگ آزاد است یا خیر
- **از بین بردن و حذف کردن* *منظورات ارجاعی برای مقاصد درگیری و ذخیره سازی
 هرگز ازش نکشید.

## در حال حاضر (v14.2)
- قضیه: هیچ تصمیمی را از دانش نمونه ای نقل نکنید؛ قبل از انتشار با دادگاه، شکل تصمیم گیری و تاریخ آن ها، نشانه های پرونده یا اظهارات قابل اثبات را توسط منبع رسمی یا آزاد تأیید کنید.

## استاندارد های مرکزی (سلسلۀ پاراگراف)
- § 43a Abs. 2 BRAO - محمّد صراحت می کند
- § 203 StGB - راز مشتری
- § 50 BRAO - واجب ثبت نام (۵ سال)
- Art. 28 DSGVO - پردازش سفارشات با ارائه دهندگان خدمات خارجی

## سه بعدی در آغاز
1. آیا این یک شرکت است (چند مشتری) یا وضعیت داخلی (یک مشتری)?
2. آیا این مجوز در حال حاضر صادر شده است یا باید دوباره ایجاد شود؟
3. در صورت وجود تضاد منافع، بررسی این اختلافات انجام شده است (§ 43a BRAO) انجام شد؟
4. آیا یک فرمان نهایی باید بازداشت یا فعال سازی شود؟
5. بعد از این، چه مهارت هایی در زمینه ماموریت انجام می شود؟

## قالب محصول - سیستم ورک اسپیس دستورات
** آدرس:** دفتر داخلی - صداي کوتاه، ساختار
```
MANDATS-WORKSPACE
Slug: [SLUG]
Angelegt: [DATUM] — Letzte Aktivitaet: [DATUM]
Status: [AKTIV / ARCHIVIERT]

Mandant: [NAME MANDANT]
Gegenseite: [NAME GEGNER]
Mandatstyp: [IT-Recht / KI-Governance / Datenschutz / ...]
Sachgebiet: [KURZBEZEICHNUNG]

Aktenzeichen: [AKTENZEICHEN]
Zustaendige RA/RAin: [NAME]
Konflikt-Check: [DURCHGEFUEHRT AM DATUM — KEIN KONFLIKT / KONFLIKT: BESCHREIBUNG]

Kernfakten: [KURZBEZEICHNUNG 1-3 SAETZE]
Naechste Frist: [DATUM — ART DER FRIST]
Aktiver Skill: [SKILL-NAME]
```

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **الزامِ تمام‌نویسی و استانداردِ قالب.** محصولِ نهایی در **جمله‌های کامل و تمام‌نوشته** تحویل می‌شود — نه اسکلتِ کلیدواژه، نه تنهٔ خالیِ شرط، نه صرفِ فهرست. شرط‌ها به‌صورتِ جمله‌های تمام‌نوشتهٔ بیان‌گرِ اثرِ حقوقی می‌آیند؛ جای‌گیرها مانند `[Name der Mandantin]` روشن علامت می‌خورند و متنِ پیرامون کامل می‌ماند.
>
> **شکلِ نوشتار:** هرگاه لایحه، قرارداد، یادداشت، تصمیم، ومرک یا هر سندِ نهاییِ دیگر به‌صورتِ DOCX، PDF یا متنِ قالب‌بندی‌شده بیرون داده شود، باید **Times New Roman ۱۱ pt** به‌عنوانِ قلمِ پایه به‌کار رود. عنوان‌ها در همان قلم می‌مانند و تنها می‌توانند سیاه (بولد) یا پلکانی باشند. در خروجیِ صرفاً Markdown یا چت، این خواستهٔ قالب به‌عنوانِ یادداشتِ برون‌سپاری درج می‌شود.
>
> **شماره‌گذاری:** ساختاربندی منحصراً اعشاری (`1`، `1.1`، `1.1.1` و به همین ترتیب). بدون اعداد رومی، بدون ساختاربندی حرفی یا آمیخته.
<!-- END ausformulierungspflicht (autogen) -->

