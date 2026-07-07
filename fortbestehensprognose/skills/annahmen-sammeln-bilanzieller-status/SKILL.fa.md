---
name: annahmen-sammeln-bilanzieller-status
description: "Wenn es um Annahmen sammeln (Fortführung) in Fortbestehensprognose geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# جمع آوری مفاهیم (ملاحظه)

## مسیر کار

- روشن‌کردن نقش، هدف و محصول کاری خواسته‌شده: چه کسی اقدام می‌کند، چه تصمیمی در پیش است، چه مهلتی در جریان است و چه خروجی‌ای لازم است؟
- اولین نشانه هایی که باید در مورد مهلت ها و خطرات فوری قرار گیرد: IDW S 11 پیش بینی 12 ماه از تاریخ ثبت، § 15a InsO شش هفته در مورد بدهی های زیاد، سه هفته آزمون افزایش نقدینگی، تازه کاری سالانه.
- بررسی معیارهای مربوط به: InsO § 19 Abs. 2 (مطابق دو مرحله ای) ، IDW S 11 (متطلبات) ، HGB § 252 Abs. 1 Nr. 2 (به نگرانی می رود) BGH II ZR 296/05 (تین هفته فاصله) StaRUG §§ 1، 102 - یافته های مربوط به gesetze-im-internet.de, dejure.org،آفتاب BVerfG-/BGH-/EuGH-دیتابیس زنده را بررسی کنید، بدون نقل قول دانش مدل
- سازمان های مربوطه را تعیین و به درستی مخاطب خود را انتخاب کنند: مدیرعامل، مشاور مالیاتی، حسابرسی، مشاوره در زمینه بازسازی، IV (اگر استخدام شده باشد) ، بانک، شرکت کنندگان.
- جمع آوری اسناد و شواهد، بررسی شکاف ها: گزارش پیش بینی باقیمانده (P&L, BS, CF) 12+ ماهه ، سناریوهای تست استرس زا، مفهوم بازسازی IDW S 6، ارزیابی های تعمیرات، اعلامیه GF - دریافت مدارک از طریق بازرسی پرونده یا درخواست مشتری برای اثبات عدم وجود آنها، چک زنده تغییرات روزانه در استانداردها و شیوه مدیریت.

## رشته های لازم برای پذیرش

```yaml
annahmen:
 - bezeichnung: Umsatzentwicklung Hauptgeschaeft
 art: umsatz
 horizont-monate: 12
 werte:
 - monat: 2026-06
 wert: 195000
 - monat: 2026-07
 wert: 180000
 # ...
 begruendung: |
 Vorjahreswerte plus 3% Wachstum bei stabiler Auftragslage.
 Auftragsbestand zum 20.05.2026 deckt bis September 2026.
 belege:
 - auftragsbestand-2026-05-20.xlsx
 - kundenbestätigung-grossauftrag-X.pdf
 risiko: mittel # niedrig / mittel / hoch
 sensitivitaet:
 negativ-szenario: -15% Umsatz waehrend zweier Monate
 positiv-szenario: +10% Umsatz
```

## حوزه های پذیرش

### ۱. رشد در درآمد

- **مجموعه سفارشات** تا روز تعیین شده
- **پایپلین مشتری** دستورات عملی مطمئن
- **موسمي** تاريخي سه سال
- **مجموعه ی بالا مشتری** خطر در صورت از دست دادن.

### ۲. تحول هزینه ها

- ** هزینه مواد** قیمت تامین کنندگان انرژی
- ** هزینه های کارگری** افزایش تعرفه ها
- ** اجاره** بررسی قرارداد
- ** انرژی** قیمت فعلی و مدت زمان قرارداد.

### ۳. سرمایه کاری

- ** زمان های پرداخت بدهی** روزهای بازده (DSO).
- **حجم ذخایر** مدت زمان بسته بندی
- **هدف پرداخت تامین کنندگان** ggf. از بحران بدتر شده است (DPO).

### ۴. سرمایه گذاری و بازپرداخت

- ** سرمایه گذاری های برنامه ریزی شده** و تامین مالی آنها
- ** سرمایه گذاری** فروش دارایی های غیر ضروری

### ۵. تأمین مالی

- ** خط های موجود وام** حجم بهره برداری مادی
- ** برنامه های پرداخت** وام موجود
- ** پیشنهادات جدید مالی** بانک تعهد های نوشته شده
- **مصالحه*** اعلامیه های کارفرما

### 6- اقدامات بازسازی

- ** اقدامات آغاز شده** (کم کردن هزینه ها و کاهش نیروی کار)
- ** برنامه ریزی شده** اقدامات با زمان و تاثیر
- **مقابل تامین هزینه های بازسازی**

## جدایی بین فرضیه ها و خواسته های

** فرضیه**: یک انتظار قابل درک و معقول با دلیل و اثبات.

آرزوی: یک امید خوش بین بدون مدرک.

در این بحث (مانند بعد از محاکمه مسئولیت) بررسی دقیق می شود که آیا خواسته ها یا فرضیه هایی بوده اند.§ 43 GmbHG, § 15b InsO).

## مشخصه بودن

هر فرضیه باید:

- ** تعداد** (در یورو یا درصد و روز) - هیچ محدوده ای جز در حساسیت.
- ** دوره** - ماه یا سه ماهه
- دلیلش از کجا می آید؟
- **دستگاه** - Excel مجموعه سفارشات تایید مشتری قرارداد اجاره و غیره

## مجموعه ای از مفاهیم

```yaml
prognose-id: FP-2026-0001
stichtag: 2026-05-20
horizont-monate: 12 # gesetzlicher Maßstab seit SanInsFoG 2021

annahmen:
 umsatz:
 - bezeichnung: Hauptsegment Produktion
 monatswerte: [195000, 180000, 220000, 240000, 230000, 200000, 190000, 195000, 210000, 220000, 215000, 225000]
 begruendung: Auftragsbestand bis September 2026; Mai-Oktober historisch +10% über Schnitt
 belege: [auftragsbestand-2026-05-20.xlsx]
 risiko: mittel

 kosten:
 - bezeichnung: Material und Energie
 basismonats-wert: 95000
 jahressteigerung: 3%
 begruendung: Lieferantenverträge bis 06/2027 Indexbindung 3%
 belege: [lieferantenverträge-übersicht.xlsx]
 risiko: niedrig
 - bezeichnung: Personalkosten
 basismonats-wert: 78000
 jahressteigerung: 4%
 begruendung: Tarifabschluss Metall 04/2026 4% per 01.07.2026
 belege: [tarifabschluss-04-2026.pdf]
 risiko: niedrig

 working-capital:
 forderungstage-soll: 30
 forderungstage-ist: 42
 vorratsreichweite-soll: 60
 vorratsreichweite-ist: 75
 begruendung-abweichung: kundenseits verzoegerte Zahlungen seit Q1 2026
 massnahmen: Mahnwesen verschärft

 investitionen:
 - bezeichnung: Ersatzinvestition CNC
 betrag: 80000
 monat: 2026-09
 finanzierung: Sale-and-Lease-back

 finanzierung:
 bank-kreditlinie: 150000
 ausnutzung-ist: 92%
 gesellschafterdarlehen-mit-rangruecktritt: 120000
 weitere-massnahmen: keine

 sanierungsmassnahmen:
 - bezeichnung: Standortschliessung Nebenwerk
 effekt-monatlich: 12000
 ab-monat: 2026-08
 einmalkosten: 60000
 einmalkosten-monat: 2026-07
```

## خروجی

- `annahmen.yaml` با تمام زمینه های لازم.
- اشاره به مهارت `annahmen-belastbarkeit-plausibilisieren` به عنوان قدم بعدی.
- فهرست مدارک از دست رفته به عنوان پرچم بازرسی.
- توصیه: در صورت یک فرضیه که نشان داده شده است غیرقابل اثبات، *نه* را به نقدی منتقل کنید - یا بطور صریح "مثال بدون مدرک" نام ببرید.

## تصمیمات اصلی فعلی - جمع آوری فرضیه پیش بینی ادامه

- قضیه: هیچ تصمیمی را از دانش نمونه ای نقل نکنید؛ قبل از انتشار با دادگاه، شکل تصمیم گیری و تاریخ آن ها، نشانه های پرونده یا اظهارات قابل اثبات را توسط منبع رسمی یا آزاد تأیید کنید.

## سه بعدی - فرضیه های کامل

1. ** صفحه درآمد کامل؟** مجموعه سفارشات، قراردادهای چارچوبی، خطوط جدید مشتری - همه قابل اثبات هستند؟
2. ** صفحه هزینه ها به طور کامل؟** کارکنان (از جمله SV) ، استفاده از مواد و کالاها، هزینه های ثابت، اجاره، هزینه مالی - همه در یک واحد است.
3. **کارگری سرمایه؟** زمان ماندگاری بدهکاران، مدت ماندگار شدن وام دهندگان، ذخایر سهام - به عنوان اثر نقدی ثبت شده است؟
4. **حوادث فوق العاده؟** سرمایه گذاری، پرداخت هزینه ها، ساعات فا در حال اجرا و واجد شرایطی است.

## زنجیره پاراگراف

§ 19 Abs. 2 InsO (توقع زنده ماندن) → IDW S 11 Rn. 30 تا 65 (بنیاد بر فرض) § 43 GmbHG (مهمیت مراقبتی GF در پیش بینی)

## قوانین و رویهٔ قضایی

### کتابخانهٔ گزیدهٔ قوانین

- § 43 GmbHG
- § 3a EStG
- § 102 StaRUG
- § 266a StGB
- § 1 StaRUG
- § 93 AktG
- § 2 HRG
- § 4 HRG
- § 7 HRG
- § 15 HRG
- § 16 HRG
- § 70 VwG

### آرای راهنما

- BGH II ZR 296/05
- BGH IX ZR 285/14
- BGH IX ZR 56/22
- BGH II ZR 206/22
- BGH IV ZR 66/25
