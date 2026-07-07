---
name: vertragsmandat-workspace-kontexttrennung
description: "Wenn es um Mandatsworkspace, Kontexttrennung und Fristensteuerung Vertragsrecht in Vertragsrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# Mandatsworkspace، جداسازی از زمینه و کنترل زمان بندی حقوق قراردادی

## هدف

وکلای مختلف در مواقعی که به عنوان یک وکیل می توانند برای چندین ماموریت کار کنند.
حوزه ی کار اجباری، به صورت دقیق در زمینه یک مشتری یا سفارش قرار می گیرد
این مهارت در مدیریت آن حوزه های کاری است.

در صورت خرید یک وکیل با ساختار چند مأمور (کتابخانه، ماموریت های خارجی)
می خواهد یک منطقه کاری ایجاد کند، تغییر دهد یا از آن جدا شود؛ و
وقتی که یک مهارت دیگر باید بداند چه ماموریت ای را دارد.

**حالۀ استاندارد: غیر فعال شده.** برای وکلا حقوق اتحادیه و
- وکیل (در خانه) با یک مشتری/کارفرما
افزونه خودکار در سطح دفتر.
شرکت های حقوقی و وکلا حرفه ای با ساختار چند نفر فعال می شوند.

## ورودی‌ها

- فرمانده: `neu`, `liste`, `wechseln`, `schließen`, `keine`
- خلاصه نامه: نام کوتاه با خط های کوچک و دارای خطوط متصل
  (به عنوان مثال: `mueller-kaufvertrag-2026`, `meier-agb-prüfung`, `xyz-gmbh-msa`)
- برای `neu`: اطلاعات مربوط به قرارداد (نام، طرف مقابل، نوع قراردادی و اسناد کلیدی)

## چارچوب حقوقی

### قوانین هسته ای

اداره ی صلاحیت ها با قانون حرفه ای وکیل جدایی ناپذیر است
و با محرمانه بودن قانونی همراه است:

- § 43a Abs. 2 BRAO - محامیه ی وکیل؛
  رازداری از مأموریت به عنوان یک تعهد اصلی
- § 203 StGB - نقض راز خصوصی؛ حفاظت از حقوق کیفری
  از رازنامه ی فرمان
- § 50 BRAO - دست نوشته ها؛ نیاز به نگهداری (۵ سال پس از تکمیل)
  در این باره
- § 2 BORA - تعهدات اساسی؛ باید در مورد تضاد منافع بررسی شود
  (در مورد مراجعین سابق یا در عین حال علیه آنها)
  (مقاولین در روش های دیگر)
- DSGVO Art. 525 - حفاظت از اطلاعات با طراحی فنی؛
  اطلاعات شخصی نباید بین دستورات به اشتراک گذاشته شود

### آرای راهنما

- قضیه: هیچ تصمیمی را از دانش نمونه ای نقل نکنید؛ قبل از انتشار با دادگاه، شکل تصمیم گیری و تاریخ آن ها، نشانه های پرونده یا اظهارات قابل اثبات را توسط منبع رسمی یا آزاد تأیید کنید.
  (مکلفیت محرمانه و جبران خسارت در صورت
  در مورد رازداری توسط وکیل؛ § 43a BRAO)
- قضیه: هیچ تصمیمی را از دانش نمونه ای نقل نکنید؛ قبل از انتشار با دادگاه، شکل تصمیم گیری و تاریخ آن ها، نشانه های پرونده یا اظهارات قابل اثبات را توسط منبع رسمی یا آزاد تأیید کنید.
  (مجبوری برای نگهداری اسناد قانونی؛ § 50 BRAO)
- قضیه: هیچ تصمیمی را از دانش نمونه ای نقل نکنید؛ قبل از انتشار با دادگاه، شکل تصمیم گیری و تاریخ آن ها، نشانه های پرونده یا اظهارات قابل اثبات را توسط منبع رسمی یا آزاد تأیید کنید.
  (حمايت اسناد دفاعي؛ وکيل § 97 StPO (به طور مشابه)

### قاعدهٔ منابع

قانون منبع: هیچ جای برای یافتن نظرات، کتابچه یا مقاله از دانش مدل؛ ادبیات فقط با منابع کاربر و یا زیرنویس زنده مجوزff.
## زمان

### فرماندهان

- `/vertragsrecht:vertragsrecht-mandat-arbeitsbereich neu <kuerzel>` - حوزه ی جدید کار در زمینه ماموریت
  برای انجام ضبط کوتاه، `mandat.md` نوشتن
- `/vertragsrecht:vertragsrecht-mandat-arbeitsbereich liste` - تمام فرمان های دارای وضعیت و
  لیست کوتاه فعال
- `/vertragsrecht:vertragsrecht-mandat-arbeitsbereich wechseln <kuerzel>` - در حال انجام ماموریت فعال
- `/vertragsrecht:vertragsrecht-mandat-arbeitsbereich schließen <kuerzel>` - پرونده ی دستور
  (به سمت `_archiv/`، هرگز حذف نمی شود)
- `/vertragsrecht:vertragsrecht-mandat-arbeitsbereich keine` - از مأموریت فعال جدا شدن
  در دفتر اداری کار می کنند

### مرحله ۱ - بررسی مشخصات اداری

بخونید `~/.claude/plugins/config/klotzkette/vertragsrecht/CLAUDE.md`. بررسی کنید
بخش `## Mandatsarbeitsbereiche`اگه `Aktiviert: ✗`، به عقل
به این نکته اشاره می کند:

> بخش های کار در اختیار است - آنها به عنوان یک عمل داخلی غیر فعال هستند
> با یک مشتری پیکربندی شده است؛ افزونه به طور خودکار در
> اگر شما با چندین مشتری کار می کنید،
> شما را هدایت کنید `/vertragsrecht:vertragsrecht-kaltstart-interview --redo` انتخاب و برگزاری
> در غیر این صورت، شما نیاز به
> `/mandat-arbeitsbereich` نه، نمی تونم.

### مرحله 2 - اجرای فرمان فرعی

حل پس از اولین توکن `$ARGUMENTE`:

- `neu` → انجام ضبط `mandate/<kuerzel>/mandat.md` نوشتن
  `verlauf.md` و `notizen.md` راه اندازی
- `liste` → `mandate/*/mandat.md` شمارش، میز گذاری
  نشان دادن ماموریت فعال
- `wechseln` → خط `Aktives Mandat:` در پروفایل اداری، به روز رسانی
- `schließen` → `mandate/<kuerzel>/` بعد از `mandate/_archiv/<kuerzel>/`
  پس از اینکه تاریخ تکمیل آن را به `verlauf.md` ثبت
- `keine` → `Aktives Mandat:` به `keine — Kanzleiebene` قرار دادن

### مرحله سوم - تایید نامه

به کاربر قبل از هر تغییر فایل نشان دهید که چه چیزی در حال تغییر است و
برای تایید.

### منطق زیر فرمان: `neu <kuerzel>`

1. بررسی کنید که آیا این لنک هنوز در `mandate/<kuerzel>/` یا
   `mandate/_archiv/<kuerzel>/` در صورت استفاده مجدد:
   در مورد این موضوع، من می خواهم که به شما بگویم.
2. انجام کوتاه مدت:
   - **منتظرم** (طرف نمایندگی یا واحد تجاری داخلی در محل)
   - **طرف مقابل** (در طرف دیگر - ممکن است چند باشد)
   - **نوع قرارداد** (عقد عرضه کننده / خدمات/ NDA)
     اشتراک SaaS / افزونه / تمدید / دیگر)
   - **مستقیمیت** (استاندارد / افزایش یافته / تیم پاک)
   - **حقیقت های کلیدی** (2-5 جمله: موضوع، شرکت کنندگان، ویژگی ها)
     نسبت به کتاب استاندارد
   - **مختلفات مشخصی از دستور کار در کتاب بازی** (به عنوان مثال "منظور موجود است)
     در این زمینه، باید به عنوان یک شرکت از بین بردن حقوق و مسئولیت های اجتماعی برای 24 ماهه (به جای 12 ماه) ، با همکاری
     " مشارکت")
   - **منتظرات مرتبط** (سرقت منتظره های متصل)
3. `mandate/<kuerzel>/mandat.md` در زیر این مقاله، به صورت نمونه ای نوشته شده است.
4. `mandate/<kuerzel>/verlauf.md` با یک نوشته "آفتاد" ایجاد کنید.
5. خالی `mandate/<kuerzel>/notizen.md` و به دست آوردن آن ها.
6. **نه** به طور خودکار برای تغییر ماموریت جدید.
   "آیا باید الان `<kuerzel>` تغییر می کنند؟"

### منطق زیر فرمان: `liste`

`mandate/*/mandat.md` شماره گذاری کنید. اولین خط هر فایل را برای وضعیت بخوانید
جدول را منتشر کنید:

| کوتاه | مشتری | نوع قرارداد | وضعیت | باز شده | فعال |
|---|---|---|---|---|---|

مأموریت فعال `*` این در نظر گرفته شده است که به عنوان یک نمونه از
"منتظرات محفوظ شده" را به صورت جداگانه انجام دهید.

### منطق زیر فرمان: `wechseln <kuerzel>`

1. بررسی اینکه آیا `mandate/<kuerzel>/mandat.md` اگر وجود نداشته باشد:
   `/vertragsrecht:vertragsrecht-mandat-arbeitsbereich neu <kuerzel>` پیشنهاد می کنم.
2. `Aktives Mandat:`-در پروفایل دفتر اداری `<kuerzel>` می دانی؟
3. `mandat.md`- خلاصه را نشان دهید تا کاربر بتواند اطلاعات صحیح
   فرمان تایید شد

### منطق زیر فرمان: `schließen <kuerzel>`

1. وجود `mandate/<kuerzel>/` بررسی کنید.
2. ثبت نهایی با تاریخ امروز در `mandate/<kuerzel>/verlauf.md` اضافه کردن.
3. `mandate/<kuerzel>/` بعد از `mandate/_archiv/<kuerzel>/` پس از آن، حرکت کنید.
4. آیا این فرمان بسته فعال بود؟ `Aktives Mandat:` به
   `keine — Kanzleiebene` می دانی؟

### منطق زیر فرمان: `keine`

`Aktives Mandat:` در پروفایل اداری `keine — Kanzleiebene` می دانی؟
با کاربران تایید کنید.

## قالب خروجی

### طرح `mandat.md`

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **الزامِ تمام‌نویسی و استانداردِ قالب.** محصولِ نهایی در **جمله‌های کامل و تمام‌نوشته** تحویل می‌شود — نه اسکلتِ کلیدواژه، نه تنهٔ خالیِ شرط، نه صرفِ فهرست. شرط‌ها به‌صورتِ جمله‌های تمام‌نوشتهٔ بیان‌گرِ اثرِ حقوقی می‌آیند؛ جای‌گیرها مانند `[Name der Mandantin]` روشن علامت می‌خورند و متنِ پیرامون کامل می‌ماند.
>
> **شکلِ نوشتار:** هرگاه لایحه، قرارداد، یادداشت، تصمیم، ومرک یا هر سندِ نهاییِ دیگر به‌صورتِ DOCX، PDF یا متنِ قالب‌بندی‌شده بیرون داده شود، باید **Times New Roman ۱۱ pt** به‌عنوانِ قلمِ پایه به‌کار رود. عنوان‌ها در همان قلم می‌مانند و تنها می‌توانند سیاه (بولد) یا پلکانی باشند. در خروجیِ صرفاً Markdown یا چت، این خواستهٔ قالب به‌عنوانِ یادداشتِ برون‌سپاری درج می‌شود.
>
> **شماره‌گذاری:** ساختاربندی منحصراً اعشاری (`1`، `1.1`، `1.1.1` و به همین ترتیب). بدون اعداد رومی، بدون ساختاربندی حرفی یا آمیخته.
<!-- END ausformulierungspflicht (autogen) -->

```markdown
[ARBEITSERGEBNIS-KENNZEICHNUNG — gemäß Kanzleiprofil ## Ausgaben]

# Mandat: [Mandant] — [Kurzbeschreibung]

**Kürzel:** [kürzel]
**Eröffnet:** [JJJJ-MM-TT]
**Status:** aktiv
**Vertraulichkeit:** [Standard / erhöht / Clean-Team]

---
## Parteien

**Mandant:** [Name]
**Gegenpartei:** [Name(n)]

## Vertragsart

[Lieferantenvertrag / Dienstleistungsvertrag / NDA / SaaS-Abonnement /
Nachtrag / Verlängerung / Sonstiges — mit einem Satz Begründung]

## Schlüsselfakten

[2–5 Sätze: Vertragsgegenstand, beteiligte Personen, Risikolage,
Besonderheiten gegenüber dem Standard-Playbook.]

## Mandatsspezifische Abweichungen vom Playbook

*Jede Abweichung vom kanzleiweiten Playbook, die nur dieses Mandat betrifft.*

- [z. B. "Haftungsobergrenze: Mandant besteht auf 24 Monate, nicht
  Kanzleistandard 12."]
- [z. B. "Ton: beziehungserhaltend — Gegenpartei ist strategischer Partner."]
- [z. B. "Gerichtsstand: muss München sein."]

## Verwandte Mandate

- [Kürzel — ein Satz warum verwandt]

## Vertraulichkeitshinweise

[Bei erhöhter Vertraulichkeit oder Clean-Team: Begründung, wer Einsicht hat,
ob mandatsübergreifender Kontext trotz globaler Einstellung unzulässig ist.]
```

### طرح `verlauf.md` (بزرگ)

```markdown
# Verlauf: [Mandant] — [Kurzbeschreibung]

Append-only Ereignisprotokoll. Aktuellster Eintrag oben.

---

## [JJJJ-MM-TT] — Mandat eröffnet

Aufnahme abgeschlossen. Kürzel: `[kürzel]`. Status: aktiv.
[Anfangskontext — z. B. "Eröffnet auf eingehenden MSA-Entwurf von
[Gegenpartei]."]
```

## ساختار سپرده

```
~/.claude/plugins/config/klotzkette/vertragsrecht/
├── CLAUDE.md                       # Kanzleiprofil
└── mandate/
    ├── <kuerzel>/
    │   ├── mandat.md               # Mandantenangaben, Schlüsselfakten, Abweichungen
    │   ├── verlauf.md              # Datiertes Protokoll (Ereignisse, Entscheidungen, Entwürfe)
    │   ├── notizen.md              # Freie Arbeitsnotizen
    │   └── ausgaben/               # Skill-Ausgaben für dieses Mandat (optional)
    └── _archiv/
        └── <kuerzel>/               # Geschlossene Mandate — lesbar, nicht aktiv
```

کوتاه حرف های کوچک با خط بند هستند.
`mueller-kaufvertrag-2026`, `meier-agb-prüfung`, `xyz-gmbh-nda`.

## زمینه های بین المللی

پروفایل اداری شامل یک `Mandatsübergreifender-Kontext:`-اختیاری
به طور استاندارد `aus` - مهارتي که در مهلت A کار ميکنه، نميشه
فایل های موجود `mandate/B/`این تضمین محرمانه است.

در `ein` می تواند یک مهارت را در میان دوره های تحصیلی به زبان صریح ** فقط**
درخواست کاربر. پس هم به طور استاندارد فقط یک دستور فعال را بارگذاری کنید
مگر اینکه کاربر به طور صریح نظر بین المللی را بپرسد.

## نمونه

**حالات:** شرکت بررسی یک قرارداد خدمات IT را انجام می دهد
برای شرکت Mandantin GmbH در مقابل تامین کننده X.

```
/vertragsrecht:vertragsrecht-mandat-arbeitsbereich neu mueller-it-vertrag-2026
```

خلاصه این است که:
- مشتری: مولر GmbH
- در این میان، شرکت های مالی و دیگر که با آن ها همکاری می کنند
- نوع قرارداد: قراردادی برای خدمات
- خصوصیت: مشتری متعهد به تضمین نامحدود برای
  قطعات حیاتی در زمینه حفاظت از داده ها

خروجی `mueller-it-vertrag-2026` با انحراف:
"ضمان: هیچ تخفیف برای قطعنامه های حفاظت از اطلاعات".

## خطرات و اشتباهات معمول

- **هیچ چکِ تضاد منافع* * این مهارت به صورت خودکار انجام نمی شود
  و این کار وکیل است.
  آنچه که کاربر توضیح می دهد، جایگزین بررسی نمی شود § 43a BRAO, § 3
  BORA.
- * حذف ممنوعه* * بسته شدن به معنای آرکائیو کردن است.
  حذف دستور العمل - حفظ آن § 50 BRAO (۵ سال)
- **مطالعه اختصار بررسی می شود.**
  در این صورت، از دستورات زیر استفاده می شود. `_archiv/<kuerzel>/` .بگذارید
- **حالت های بین ماموریت ها حذف می شود.**
  در حال فعال شدن، هرگز فایل های مأموریت دیگری را نخواند.

## تعهد به منبع

در مورد اطلاعات مربوط به مأموریت، برای حفظ یا محرمیت:
- § 43a Abs. 2 BRAO (رازداری) § 50 BRAO (حرف دست)
- قضیه: هیچ تصمیمی را از دانش نمونه ای نقل نکنید؛ قبل از انتشار با دادگاه، شکل تصمیم گیری و تاریخ آن ها، نشانه های پرونده یا اظهارات قابل اثبات را توسط منبع رسمی یا آزاد تأیید کنید.
- قانون منبع: ادبیات فقط با منابع کاربر یا دسترسی زنده مجاز؛ هیچ جای برای یافتن نظرات، کتابچه و مقاله از دانش مدل نیست.

توجه: این مهارت جایگزین مشاوره حقوقی در یک مورد خاص نیست.

---

آډیت ۲۷05.2026
منبع: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=17.12.1998&Aktenzeichen=IX+ZR+196%2F97
بندل: bundle_047.json
-->
