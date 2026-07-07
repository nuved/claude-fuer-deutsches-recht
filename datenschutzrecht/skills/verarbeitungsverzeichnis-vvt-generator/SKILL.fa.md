---
name: verarbeitungsverzeichnis-vvt-generator
description: "Wenn es um VVT — Verzeichnis von Verarbeitungstätigkeiten in Datenschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# VVT - فهرست فعالیت های پردازش

## ورودی‌ها

- تعداد افراد مشغول
- صنعت / مدل کسب و کار
- قراردادهای AVV موجود
- ارزیابی های DSFA موجود
- بررسی پردازش (چه فرآیندها؟)
- لیست ارائه دهندگان خدمات (مصنوعان سفارش)

## مرحله 1 - دامنه کاربرد Art. 30 Abs. 5 DSGVO

### اصل

- واجبیت VVT برای همه مسئولان و پردازنده های سفارش

### استثنا

- شرکت هایی که کمتر از 250 نفر کار می کنند
- اگر پردازش ** منظم نیست**
- اگر دسته بندی های خاص وجود نداشته باشد Art. 9 یا اطلاعات قانونی
- اگر هیچ خطر برای حقوق و آزادی های افراد مورد توجه وجود نداشته باشد

### پیامدهای عملی

- **قریب تمام شرکت ها** از جمله افراد کار می کنند - واجب VVT
- پردازش منابع انسانی به صورت منظم باعث می شود
- حتی شرکت های کوچک اغلب مجبور به
- ** راه امن:** تولید VVT بدون محدودیت

## مرحله ۲ - وظایف مسئول محتوا Art. 30 Abs. 1

### به طور هر گونه فعالیت های پردازش

(a) **نام و اطلاعات تماس** مسئول ggf. نمایندگان مشترک DSB)

ب) **مقصود** پردازش

(ج) **کتابی** افراد ذینفع

د) ** دسته بندی** اطلاعات شخصی

(هـ) **کتاب** دریافت کنندگان (همچنین در کشورهای خارج از کشور و سازمان های بین المللی).

f) در مورد بررسی های کشورهای ثالث، نام کشور ثالث و ggf. تضمین های مناسب (Art. 46) یا نامگذاری به عنوان انتقال Art. 49

(g) **زمان حذف برنامه ریزی شده** دسته بندی های داده

h) **وصف عمومی اقدامات فنی و سازمانی** Art. 32

## مرحله 3 - وظایف محتوا پردازنده Art. 30 Abs. 2

### به هر سفارش

(a) **نام و اطلاعات تماس** پردازنده ی سفارشات و هر مسئول دیگری که برای آن پردازشگر عمل می کند

ب) **کتاب** فعالیت های پردازش در این پروژه

(ج) **تحقیقات در کشورهای دیگر** مانند معاینه مسئول

د) **صفحه عمومی TOMs**

## مرحله ۴ - ساختار و شکل VVT

### در صورت نوشتن یا الکترونیکی

- **فروش نامه** کافی
- **برنامه های الکترونیکی** بیشتر (مودول CRM اکسل نرم افزار حفاظت از اطلاعات)
- **نمونه** در اختیارات نظارتی Art. 30 Abs. 4 DSGVO

### ساختار توصیه شده

```
VVT [Unternehmens-Name]
Stand: [Datum]
Verantwortlicher: [Name Anschrift]
DSB: [Name]

Aufgenommen: [Datum]
Letzte Änderung: [Datum]

Verarbeitungs-Tätigkeit Nr. [N]:

Zweck der Verarbeitung:
[Konkrete Beschreibung]

Rechtsgrundlage (Art. 6 / 9 DSGVO) — EMPFOHLEN
(Art. 30 fordert das nicht ausdrücklich, ist aber
für Aufsichtsbehörden-Prüfung sehr hilfreich):
[Rechtsgrundlage]

Kategorien Betroffener:
[z.B. Beschäftigte, Kunden, Lieferanten, Bewerber]

Datenkategorien:
[z.B. Stammdaten, Vertragsdaten, Zahlungsdaten,
besondere Kategorien]

Empfänger:
[z.B. Dienstleister IT, Lohnbüro, Behörden]

Drittland-Übermittlung:
[Ja/Nein; bei Ja: Land und Garantien]

Lösch-Frist:
[z.B. 10 Jahre nach Vertragsende — gesetzliche
Aufbewahrungspflicht]

TOMs:
[Verweis auf TOMs-Dokument]
```

## مرحله 5 - فعالیت های معمولی پردازش

### امور انسانی

- ** مدیریت متقاضی**
- ** اطلاعات شخصی**
- **حساب حقوق**
- ** زمان ضبط**
- ** توسعه ی پرسنل**
- **دارایی بیماری**

### روابط با مشتریان

- **پذیری قرارداد**
- ** انجام قرارداد**
- ** خدمات مشتری**
- **بازاریابی / خبرنامه**
- **ملاحظات مشتری**

### تامین کنندگان

- **حرف قرارداد**
- ** انجام قرارداد**
- **حرکت های پرداخت**
- **کنترل تحریم ها**

### پردازش شخصی

- ** حسابداری**
- **قرارنامه مالیاتی**
- ** مطابق با قانون**
- ** مدیریت ریسک**
- **گوشه های امنیتی IT**

### وب سایت و آنلاین

- ** کوکی ها و ردیابی**
- **حساب وب**
- ** خبرنامه**
- ** فرم تماس**

## مرحله ۶ - انتقال به کشور ثالث در VVT

### وظایف

- **دولت های دیگر را نشان می دهد**
- ** نام گیرنده**
- **پروژه تضمین Art. 46 DSGVO** مشخص کنید:
 - SCC (مجموعه های استاندارد قرارداد)
 - قوانین مربوط به شرکت ها
 - قوانین رفتاری Art. 40
 - گواهینامه Art. 42
 - توافقنامه های بین المللی (z.B. چارچوب داده های خصوصی ایالات متحده و اتحادیه اروپا)
- در Art. 49 استثنا (موافقیت قرارداد منافع حیاتی و غیره)

### در این گزارش، "مجموعه ای از شرکت های مختلف و با توجه به میزان سودآوری آن ها" ذکر شده است.

- در هر انتقال به کشور ثالث
- مهارت `drittlandstransfer-pruefung`

## مرحله 7 - مدیریت بروزرسانی

### فرصت های بروزرسانی

- **کارگردانی جدید**z.B. ابزار جدید استفاده شده)
- **مقصد تغییر یافته**z.B. (ملاحظه بازاریابی)
- **رئیس جدید** (موضوع AVV)
- **مبادله کشورهای ثالث**
- **زمان حذف تغییر شده**
- **کتاب های جدید داده**

### فرکانس

- **در هر تغییر** به زودی
- **حداقل یک سالانه کامل**
- **پرداخت DSFA**

### مسئولان

- **DSB** هماهنگی
- **مجال** برای بروزرسانی محتوا
- **IT** برای تایید TOMs

## مرحله ۸ - ارتباط با AVV Art. 28 DSGVO

### پردازش سفارشات در VVT

- هر AVV → ثبت در VVT
- محتوای AVV که بخشی از آن ها به صورت مستقیم قابل انتقال است
- ثبت آغاز/ختم قرارداد

### فرعی پردازنده

- در صورت تأیید، فرعی - موقعیت جدید VVT
- در مورد تغییر پردازنده فرعی - VVT Update

## مرحله 9 - ارتباط با DSFA Art. 35

### پردازش های واجب DSFA

- خطر بالا برای حقوق و آزادی ها
- به ویژه در VVT نشان دادن
- مستند کردن نتیجه DSFA
- گرفتن TOMs از DSFA

### سیستم هوش مصنوعی با ریسک بالا

- DSFA + ارزیابی حقوق اساسی (Art. 27 (آریانه)
- مهارت `ki-verordnung-compliance`

## مرحله 10 - نمونه کاری لازم برای یک سازمان نظارت

### فرصت ها

- **پرسش از مقامات نظارتی** اطلاعات استاندارد
- ** گزارش صفحه داده** با اشاره به VVT
- **DSGVO-آژید
- **در دادگاهی که مجازات می شود**

### شکل این طرح

- در صورت الکترونیکی
- کامل بودن
- حالا
- زبان آلمانی

### در صورت کمبود

- پس از Art. 83 Abs. 4 lit. a DSGVO (تا 10 میلیون یورو یا 2 درصد از کل درآمد)
- درخواست اصلاحات پس از زمان

## مرحله 11 - اقدامات عملی برای ایجاد

### مرحله 1 - جمع آوری

- کارگاه با تمام رشته های تخصصی
- فهرست پردازش
- نمودار جریان داده

### مرحله دوم: ساختار

- لیست فعالیت ها
- دسته بندی
- نقشه برداری از دسته بندی های داده

### مرحله 3 - مستند سازی

- پر کردن قالب VVT
- بررسی DSB
- آزادسازی مدیریت

### مرحله ۴ - بروز رسانی

- فرآیند مدیریت تغییر
- بازبینی های دوره ای
- بروزرسانی های مبتنی بر تگر

## مرحله 12 - توصیه ابزار

### بر اساس اکسل

- برای سازمان های کوچک کار می کند
- طرح های BfDI / مقامات نظارتی

### نرم افزار حفاظت از اطلاعات

- اوتری
- DataGuard
- فعال کردن
- با توجه به استاندارد BSI تایید شده است

### یکپارچه سازی CRM/IT

- شناسایی خودکار پردازش
- ارتباط با پایگاه داده AVV
- اتصال به ابزار DSFA

## مرحله 13 - نمونه فعالیت های پردازش

```
Verarbeitungs-Tätigkeit Nr. 5: Newsletter-Versand

Zweck: Information bestehender und potentieller
Kunden über Produkt-Updates und Branchen-Themen

Rechtsgrundlage: Art. 6 Abs. 1 lit. a DSGVO
(Einwilligung); § 7 Abs. 2 Nr. 3 UWG bei
Bestandskunden

Kategorien Betroffener: Kunden, Interessenten,
Newsletter-Abonnenten

Datenkategorien:
- E-Mail-Adresse
- Vor- und Nachname (optional)
- Einwilligungs-Datum und -Inhalt
- Anrede (optional)
- Click-Verhalten (Öffnungsrate, Click-Tracking)

Empfänger:
- Newsletter-Versand-Dienstleister Mailchimp Inc. (USA)
- Interne Vertriebs- und Marketing-Abteilung

Drittland-Übermittlung:
USA, Mailchimp Inc.
Garantie: EU-US Data Privacy Framework
(Aktualisierung 2023)
TIA durchgeführt: ja, Skill drittlandstransfer-pruefung

Lösch-Frist:
- Aktive Abonnenten: Bis zum Widerruf
- Nach Widerruf: 3 Jahre Aufbewahrung der
 Widerrufs-Information (Beweis-Funktion)
- Click-Verhalten: 13 Monate (Statistik-Auswertung)

TOMs:
- HTTPS-Verschlüsselung
- Pseudonymisiertes Tracking
- Mailchimp ISO 27001 zertifiziert
- AVV vorhanden gem. Art. 28 DSGVO
```

## ارتباط با مهارت های دیگر

- `dsfa-erstellung` - در مورد پردازش های DSFA واجب
- `avv-pruefung` - در زمان پردازش سفارشات
- `drittlandstransfer-pruefung` - در مورد کشورهای دیگر
- `ki-verordnung-compliance` - در مورد پردازش هوش مصنوعی
- `anwendungsfall-triage` - در مورد استفاده مجدد
- `datenpanne-meldung` - در صورت وقوع

## خروجی

- `vvt-{unternehmen}.md` ساخت و ساز VVT
- اولین نسخه ی اکسل یا مارک داون
- لیست محرکات بروزرسانی
- آماده سازی پاسخ های نظارت
- زمان در دفتر تاریخ (برسال بررسی کامل)

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **الزامِ تمام‌نویسی و استانداردِ قالب.** محصولِ نهایی در **جمله‌های کامل و تمام‌نوشته** تحویل می‌شود — نه اسکلتِ کلیدواژه، نه تنهٔ خالیِ شرط، نه صرفِ فهرست. شرط‌ها به‌صورتِ جمله‌های تمام‌نوشتهٔ بیان‌گرِ اثرِ حقوقی می‌آیند؛ جای‌گیرها مانند `[Name der Mandantin]` روشن علامت می‌خورند و متنِ پیرامون کامل می‌ماند.
>
> **شکلِ نوشتار:** هرگاه لایحه، قرارداد، یادداشت، تصمیم، ومرک یا هر سندِ نهاییِ دیگر به‌صورتِ DOCX، PDF یا متنِ قالب‌بندی‌شده بیرون داده شود، باید **Times New Roman ۱۱ pt** به‌عنوانِ قلمِ پایه به‌کار رود. عنوان‌ها در همان قلم می‌مانند و تنها می‌توانند سیاه (بولد) یا پلکانی باشند. در خروجیِ صرفاً Markdown یا چت، این خواستهٔ قالب به‌عنوانِ یادداشتِ برون‌سپاری درج می‌شود.
>
> **شماره‌گذاری:** ساختاربندی منحصراً اعشاری (`1`، `1.1`، `1.1.1` و به همین ترتیب). بدون اعداد رومی، بدون ساختاربندی حرفی یا آمیخته.
<!-- END ausformulierungspflicht (autogen) -->

## منابع

- DSGVO Art. 30 5 6 9 30 32 35 46 49
- BDSG-تعدیلات
- آای-او Art. 27
- نمونه های BfDI
- DSK اسناد کوتاه مربوط به VVT
- دستورالعمل های EDSA
- BVerfG-خط های مسئولیت حفاظت از اطلاعات

## در حال حاضر (v14.2)

- قضیه: هیچ تصمیمی را از دانش نمونه ای نقل نکنید؛ قبل از انتشار با دادگاه، شکل تصمیم گیری و تاریخ آن ها، نشانه های پرونده یا اظهارات قابل اثبات را توسط منبع رسمی یا آزاد تأیید کنید.

## سه بعدی در آغاز

1. اولین بار که VVT ها را نصب می کنید یا به روز می شوید؟
2. از نظر مسئول (Art. 30 Abs. 1 DSGVO) یا پردازنده (Art. 30 Abs. 2)?
3. آیا سازمان وظیفه دارد؟Art. 30 Abs. 5 DSGVO: کمتر از 250 نفر فقط در مورد برخی کارزارها)
4. چه منابع موجود هستند؟ (سیستم های موجود، مجموعه AVV و فهرست داراییهای فناوری اطلاعات)

## نماد محصول - ورودی VVT (مقاول)

** آدرس:** DSB / اداره نظارت - صدا: ساختار واقعی

```
VVT-Eintrag [DATUM]
Verantwortlicher: [NAME, ADRESSE, VERTRETER]
DSB: [NAME, KONTAKT] (falls bestellt)

Verarbeitungstätigkeit: [BEZEICHNUNG]
Zweck(e): [ZWECKE nach Art. 30 Abs. 1 lit. b]
Betroffene Gruppen: [GRUPPEN nach Art. 30 Abs. 1 lit. c]
Datenkategorien: [KATEGORIEN nach Art. 30 Abs. 1 lit. c]
Empfaenger (Kategorien): [EMPFAENGER nach Art. 30 Abs. 1 lit. d]
Drittlandtransfer: [LAND / Schutzmechanismus nach Art. 30 Abs. 1 lit. e]
Loeschfristen: [FRISTEN nach Art. 30 Abs. 1 lit. f]
TOM (Verweis): Art. 32 DSGVO — Anlage [X]
Rechtsgrundlage (Empfehlung): Art. [X] DSGVO [§ BDSG]
```

قضیه: هیچ تصمیمی را از دانش نمونه ای نقل نکنید؛ قبل از انتشار با دادگاه، شکل تصمیم گیری و تاریخ آن ها، نشانه های پرونده یا اظهارات قابل اثبات را توسط منبع رسمی یا آزاد تأیید کنید.
