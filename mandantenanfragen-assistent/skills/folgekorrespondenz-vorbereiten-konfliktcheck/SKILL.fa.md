---
name: folgekorrespondenz-vorbereiten-konfliktcheck
description: "Wenn es um Folgekorrespondenz-Vorbereiten in mandantenanfragen-assistent geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# آماده سازی نامه های بعدی

## مسیر کار

- روشن‌کردن نقش، هدف و محصول کاری خواسته‌شده: چه کسی اقدام می‌کند، چه تصمیمی در پیش است، چه مهلتی در جریان است و چه خروجی‌ای لازم است؟
- اول، مهلت ها و خطرات فوری را مشخص کنید: BRAO § 44 پذیرش/پذیرفتن فوری، RVG § 34 مشاوره اولیه حداکثر 190 یورو (مصرف کنندگان) DSGVO Art. 13 اطلاعات در هنگام جمع آوری.
- بررسی معیارهای مربوط به: BRAO §§ 43a، 44، 49b BORA §§ 2, 11, BGB §§ 145 ff., 280, 627, 675, GwG §§ 10, 11, RVG §§ 1، 4، 34 (مجلس اول) DSGVO Art. 613 - یافته های مربوط به gesetze-im-internet.de, dejure.org،آفتاب BVerfG-/BGH-/EuGH-دیتابیس زنده را بررسی کنید، بدون نقل قول دانش مدل
- اداره ی صلاحیت را تعیین کنید و به درستی مخاطب ها را انتخاب نمایید: درخواست کننده (مهم) ، وکیل، دفترچه، مأموریت رعایت مقررات، مدیر مشتری.
- جمع آوری اسناد و شواهد، بررسی شکاف ها: فرم تماس اول، غربالگری درگیری، قرارداد اجاره ای، فرماندهی، توافق نامه حقوق، پرونده ی متقاضی، اطلاعیه حریم خصوصی - دریافت مدارک از طریق بازرسی یا درخواست به متقاضیان ، چک زنده برای تغییرات روزانه استاندارد و شیوه های مدیریت.

## دانش ویژه

بر اساس درخواست ورودی پر شده، یک سکلوت کامل برای سیستم CRM یا مجموعه دستی پرونده ها ایجاد شود. هدف: کارکنان سکرتاری می توانند بلافاصله عمل را ادامه دهند بدون اینکه نیاز به جستجوی مجدد اطلاعات از ایمیل اصلی داشته باشند.

## سه بعدی در آغاز
1. آیا تمام فیلدهای لازم (اسم، ایمیل، نگرانی ها، اضطراری و تاریخ) از پارسینگ موجود است؟
2. چه CRM یا ساختار فایل هایی استفاده می شود (DATEV، RA-MICRO، Advoware، دستی) ؟
3. آیا چک های تعارض انجام شده است یا باید در ثبت CRM به عنوان بازماندگان نشان داده شود؟
4. آیا این ثبت باید به صورت خودکار یا با اجازه دستی ذخیره شود؟

## رویهٔ قضایی روز
- قضیه: هیچ تصمیمی را از دانش نمونه ای نقل نکنید؛ قبل از انتشار با دادگاه، شکل تصمیم گیری و تاریخ آن ها، نشانه های پرونده یا اظهارات قابل اثبات را توسط منبع رسمی یا آزاد تأیید کنید.

## قوانین محوری
- Art. 6 Abs. 1 lit. ب DSGVO - شروع قرارداد به عنوان یک اساس قانونی برای ذخیره سازی CRM
- Art. 5 Abs. 1 lit. e DSGVO - محدودیت حافظه: ثبت CRM فقط تا زمانی که برای هدف لازم باشد
- § 43 BRAO - وظیفه دقت: مستند سازی کامل و فوری پرونده ها/CRM
- § 51 BRAO - مسئولیت: عدم وجود اسناد به عنوان نقض تعهدات سازمان

## ورودی اسکلت: شکل استاندارد

```
=== NEUER VORGANG — ERSTANFRAGE ===
Eingangsdatum: [DATUM UND UHRZEIT]
Eingangskanal: E-Mail

--- KONTAKT ---
Name: [NACHNAME, VORNAME] | [Titel falls vorhanden]
E-Mail: [ABSENDER-ADRESSE]
Telefon: [TELEFONNUMMER oder "nicht genannt"]
Postanschrift: [ADRESSE oder "nicht genannt"]
Sprache: [DE / EN / FR / IT / Sonstiges]

--- ANLIEGEN ---
Rechtsgebiet: [Ersteinschätzung: z. B. Arbeitsrecht / Mietrecht / Strafrecht]
Stichwörter: [Kommagetrennte Liste — max. 5 Begriffe]
Beteiligte: [Gegner / Behörde / weitere Parteien oder "nicht genannt"]
Sachverhalt-Kurzfassung:
 [2-4 Sätze aus dem Parsing — wortwörtlich oder eng paraphrasiert]

--- DRINGLICHKEIT ---
Stufe: [HOCH / MITTEL / NIEDRIG / UNBEKANNT]
Begründung: [Frist, Termin, Eile-Signal oder "kein Hinweis"]
Massnahme: [Sofortiger Anwaltsrückruf erforderlich / Normale Bearbeitung / Abwarten]

--- STATUS ---
Spam-Check: [KLAR / VERDÄCHTIG / SPAM]
Konfliktcheck: [AUSSTEHEND — vor Terminvergabe durchführen!]
Erstantwort: [VERSENDET am DATUM / AUSSTEHEND]
Transkription: [AKTIV / NICHT AKTIV]

--- INTERNE NOTIZEN ---
[Platz für manuelle Ergänzungen der Sekretariatsmitarbeitenden]

=== ENDE SKELETON-EINTRAG ===
```

## زمینه های دقیق

### تاریخ ورود و کانال

- خودکار با زمان فعلی پر می شود (ISO 8601: `YYYY-MM-DD HH:MM`)
- کانال ورود: ایمیل، تلفن، فرم تماس، پست - برای سوالات مبتنی بر ایمیل همیشه "میل"

### زمینه های تماس

از مهارت پارسینگ (`anfrage-eingang-parser`) را به دست آورده اند. فیلدهای فاقد نام "نه گفته" نشان داده می شود و برای تکمیل دستی برجسته شده است.

### مقدماتی که در حوزه حقوقی انجام می شود

** مهم:** این یک ارزیابی اولیه غیرمربوطی از الگوریتم پارسینگ است. برای پیشگیری در دفتر اداری استفاده می شود و نباید به عنوان تخمین قانونی به فرد درخواست کننده منتقل گردد.

حوزه های قانونی که ممکن است وجود داشته باشد (انتخاب):
- حقوق کار، قوانین اجاره، قانون خانواده، قانونی و کیفری
- حقوق شرکت، قانون قرارداد، خسارت
- حقوق اداری، قانون اجتماعی و مالیات
- حقوق ترافیک، حق ورشکستگی و حقوق مالکیت
- غیر از این / نامعلوم

### سطح اضطراری

| سطح | توضیحات | اقدام فوری |
|---|---|---|
| خیلی زیاد | زمان مشخص شده، خطر مسئولیت، دادگاه در حال حاضر | وکلش فوراً به شما زنگ می زند |
| در میان | فشار زمان وجود دارد اما هیچ وقت فوری نیست | پاسخ در عرض 24 ساعت |
| کم | هیچ فشار زمانی قابل تشخیص نیست | پاسخگویی در جریان عادی |
| نامعلوم | هیچ گونه اظهارات فوری ممکن نیست | چگونه میتوانیم |

### وضعیت چک درگیری

به طور استاندارد: `AUSSTEHEND`. بعد از انجام چک درگیری، کارمند دفترچه:
- `KLAR — kein Konflikt erkannt` یا
- `KONFLIKT — Mandat nicht möglich` یا
- `KONFLIKT — Rücksprache mit RA erforderlich`

### وضعیت نقل

- `AKTIV` اگر درخواست کننده از سرویس نقل استفاده کند
- `NICHT AKTIV` در مورد روش های استاندارد با گزارشات صورتحالی

## ادغام در سیستم های CRM رایج

این مهارت یک اسکلت مبتنی بر متن را می دهد که در هر سیستم معمول قابل استفاده است:

- **RA-MICRO:** به عنوان یک فایل جدید ایجاد کنید؛ فیلدها را دستی انتقال دهید.
- **Advoware:** دستور جدید ایجاد کنید؛ اطلاعات تماس را انتقال دهید. حالت خود را بر روی "تغییر اول" قرار دهید
- **DATEV وکیل:** شروع به کار جدید؛ ایجاد پرونده های متقاضی.
- ** توسعه شخصی / اکسل:** خط جدول؛ امکان واردات CSV

## خروجی

```
SKELETON-EINTRAG BEREIT
Für CRM-System oder manuelle Akte kopieren und einfügen.
Ausstehende Felder sind mit [BITTE ERGÄNZEN] markiert.
Konfliktcheck: AUSSTEHEND — vor Terminvergabe durchführen!
```

## اشاره به مهارت های دیگر

- `anfrage-eingang-parser` - منبع داده
- `dringlichkeitsmarker` - درجه اضطراری و دلیل
- `spam-und-massen-anfrage-filter` - وضعیت چک اسپم
- `konfliktcheck-vorab` - اشاره به چک های نزاعی که در انتظار هستند
