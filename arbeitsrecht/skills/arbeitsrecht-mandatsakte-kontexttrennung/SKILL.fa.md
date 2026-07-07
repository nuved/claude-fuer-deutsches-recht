---
name: arbeitsrecht-mandatsakte-kontexttrennung
description: "Wenn es um Arbeitsrechtliche Mandatsakte und Kontexttrennung in Arbeitsrecht geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# دستورات و مقررات مربوط به کار

وکلا و شرکت های حقوقی برای چندین مشتری همزمان کار می کنند. یک سند به طور کامل زمینه ی یک مؤکل را از همه موارد دیگر جدا میکند. این مهارت، پرونده ها را مدیریت می کند.

## هدف

برای شرکت های دارای چندین مشتری (کتابه ی فردی، دفتر متوسط و ادارهٔ بزرگ) ، این قابلیت به طور استاندارد ** غیر فعال شده است** - تمام مهارت ها از محیط کار خود بخود استفاده می کنند.

در قانون کار، یک "کتاب" به طور معمول با رفتار معین مشتری مطابقت دارد:
- یک شکایت یا درخواست از دست دادن
- بررسی داخلی
- یک پروژه ارسال
- یک اختلاف نامه
- یک تخلیه ی گسترده / تغییر در شرکت

## ورودی‌ها

- دستور: `neu`, `auflisten`, `wechseln`, `schließen` یا `keine`
- خلاصه ای از پرونده (سرگ) z.B. `mueller-ksg-2024`
- `~/.claude/plugins/config/claude-fuer-deutsches-recht/arbeitsrecht/CLAUDE.md` - بخش `## Mandantenakten`

## زمان

### پیش بینی

`~/.claude/plugins/config/claude-fuer-deutsches-recht/arbeitsrecht/CLAUDE.md` در بخش `## Mandantenakten` بررسی کنید.

در صورت `Aktiviert: ✗` (نقاب / داخل):
> پرونده های مشتری غیرفعال شده اند - آنها به عنوان [Kanzlei/in-house] اگر شما در واقع چندین مشتری را اداره می کنید، `/arbeitsrecht:arbeitsrecht-kaltstart-interview --redo` در این حالت، شما باید از یک دستگاه کاربری انتخاب کنید. `/arbeitsrecht:arbeitsrecht-mandat-arbeitsbereich` نه، نمی تونم.

### دستورات

**`neu <kürzel>`** - ایجاد دستورات جدید
1. کوتاه کردن به صورت کوچک، اجازه می دهد تا با هم پیوند داده شود (z.B. `mueller-ksg-2024`).
2. مصاحبه کوتاه با افراد مصرفی:
   > - نام مشتری (درونی، نه برای هزینه)
   > - یک جمله از واقعیت (لغو / تحقیق / ارسال / اختلافات توری)
   > - وکیل مجاز
   > - وضعیت پرونده: باز / آرام / بسته
   > -درستهاي خاصي از محرمانه بودن؟
3. `mandat.md`, `verlauf.md` و `notizen.md` زیر:
   `~/.claude/plugins/config/claude-fuer-deutsches-recht/arbeitsrecht/akten/<kürzel>/`

**`auflisten`** - تمام پرونده ها را به صورت جدول با وضعیت و پرچم فایل فعال نشان دهید.

**`wechseln <kürzel>`** - اعمال فعال. تمام تماس های مهارت زیر در زمینه این پرونده کار می کنند

**`schließen <kürzel>`** - پرونده ها را در `_archiv/` نه حذف کردن، نه تغییر دادن.

**`keine`** - از کارنامه فعال خلاص شود؛ به زمینه سطح دفتر بازگردانید.

### زمینه های بین پرونده ها

در `Aktenübergreifender Kontext: deaktiviert` (استانداردی): یک مهارت در پرونده A هرگز فایل های از نسخه B را نمی خواند. این امر تحت قانون حفاظت از داده ها لازم است (پارagraph 43a) Abs. 2 BRAO, بند 26 BDSG): اسناد شخصی یک کارمند نباید در تحلیل دیگری نقش داشته باشد.

اثرات یادگیری که به چندین ماموریت مربوط می شود، در دفتر CLUDE.md نوشته شده است نه یک فایل پرونده ای

## منابع و نقل قول

استاندارد نقل قول: `../references/zitierweise.md`روش: `../references/methodik-buergerliches-recht.md`.

- ماده 43a Abs. 2 BRAO (مکلفیت محام صراحت)
- ماده 203 StGB (تخلف راز خصوصی)
- ماده 26 BDSG (حمايت اطلاعات کارکنان؛ شامل داده های پرسنل مورد نظر و حقوقی است)
- ماده 53 StPO (حق انکار از وکیل)

## قالب خروجی

** نو:**
```
Mandatsakte angelegt: mueller-ksg-2024
========================================
Mandant:    [intern anonymisiert]
Sachverhalt: Kündigungsschutzklage nach betriebsbedingter Kündigung
Anwalt:     [Name]
Status:     offen
Ablage:     ~/.../akten/mueller-ksg-2024/

Dateien erstellt:
  mandat.md    – Akten-Stammdaten und Kontext
  verlauf.md   – Chronologisches Protokoll
  notizen.md   – Freie Notizen, entwürfe, Recherche-Ergebnisse
```

** لیست:**
```
Mandantenakten – Arbeitsrecht
=================================
● mueller-ksg-2024     [offen]    Kündigungsschutzklage      geändert: heute
  bayer-betriebsrat    [ruhend]   BR-Streitigkeit Paragraf 87 BetrVG   geändert: vor 3 Wo.
  huber-entsendung     [offen]    Entsendung Frankreich          geändert: gestern

● = aktive Akte
```

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **الزامِ تمام‌نویسی و استانداردِ قالب.** محصولِ نهایی در **جمله‌های کامل و تمام‌نوشته** تحویل می‌شود — نه اسکلتِ کلیدواژه، نه تنهٔ خالیِ شرط، نه صرفِ فهرست. شرط‌ها به‌صورتِ جمله‌های تمام‌نوشتهٔ بیان‌گرِ اثرِ حقوقی می‌آیند؛ جای‌گیرها مانند `[Name der Mandantin]` روشن علامت می‌خورند و متنِ پیرامون کامل می‌ماند.
>
> **شکلِ نوشتار:** هرگاه لایحه، قرارداد، یادداشت، تصمیم، ومرک یا هر سندِ نهاییِ دیگر به‌صورتِ DOCX، PDF یا متنِ قالب‌بندی‌شده بیرون داده شود، باید **Times New Roman ۱۱ pt** به‌عنوانِ قلمِ پایه به‌کار رود. عنوان‌ها در همان قلم می‌مانند و تنها می‌توانند سیاه (بولد) یا پلکانی باشند. در خروجیِ صرفاً Markdown یا چت، این خواستهٔ قالب به‌عنوانِ یادداشتِ برون‌سپاری درج می‌شود.
>
> **شماره‌گذاری:** ساختاربندی منحصراً اعشاری (`1`، `1.1`، `1.1.1` و به همین ترتیب). بدون اعداد رومی، بدون ساختاربندی حرفی یا آمیخته.
<!-- END ausformulierungspflicht (autogen) -->

## نمونه‌ها

```
/arbeitsrecht:arbeitsrecht-mandat-arbeitsbereich neu mueller-ksg-2024
Kündigung wegen betriebsbedingter Restrukturierung, Sozialauswahl streitig.
```

```
/arbeitsrecht:arbeitsrecht-mandat-arbeitsbereich wechseln bayer-betriebsrat
```

```
/arbeitsrecht:arbeitsrecht-mandat-arbeitsbereich auflisten
```

## خطرات / اشتباهات معمول

- **در زمان پایان دوره پرونده ها را بسته نمی کنند.** به جای حذف، آرکائیو می کنید - BRAO ماده 50 Abs. دو تا به پنج سال نگهداری می دهد.
- ** نامزدی را ناشناس نکنید.** لنک و اسم داخلی نباید توسط غیر مجاز شناسایی شود.
- **سررسی بین پرونده ها را به طور ناخواسته فعال کنید.** بطور استاندارد برای دلایل حفاظت از اطلاعات غیرفعال است.


## سخت سازی کیفیت

- کار کردن با دقت: ابتدا حقایق، شواهد و مهلت ها را مشخص کنید.
- هیچ قانونی را از دانش مدل استفاده نمی کنند. هر تصمیم قبل از انتشار با دادگاه، شکل تصمیم گیری، تاریخ و اسناد ثبت شده است که منبع آزاد یا رسمی قابل بررسی می باشد.
- هیچ سندی از BeckRS، juris، commentary یا manual و essay blinds نیست. فقط زمانی که کاربر آن را ارائه دهد استفاده کنید یا دسترسی زنده به صورت مجوز در مرحله کاری مشخص مستند شده باشد.
- اگر منبع، شماره ی محرکه ای یا شیوهٔ رسمی و مهلت مورد بررسی قرار نگرفته باشد به صورت قابل مشاهده نشان داده شود که نقطه آزمایش است و هیچ دقت ساختگی ایجاد نمی کند.
- نتایج را به گونه ای ارائه دهید که بلافاصله قابل استفاده باشند: خلاصه، مسیر آزمایش، چراغ خطر، لیست خلاء و گام های بعدی.
