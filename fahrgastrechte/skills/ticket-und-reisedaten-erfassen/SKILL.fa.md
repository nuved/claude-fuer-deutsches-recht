---
name: ticket-und-reisedaten-erfassen
description: "Wenn es um Ticket- und Reisedaten erfassen in Fahrgastrechte geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# ثبت اطلاعات بلیط و سفر

## ورودی‌ها

شواهد معمول:

- **حکمت ثبت نام** DB / FlixTrain / ÖBB به صورت PDF/ ایمیل
- **تکیت الکترونیکی** با کد بار IATA/UIC (تصویر، PDF)
- **حفظ صندلی** (مفرقی یا یکپارچه)
- **حکمت ثبت نام** (اسکرین شاټ اپلیکیشن قطار، بلیط چاپ شده)
- ** اطلاع تاخیر یا لغو** از DB (SMS، ایمیل، app push)
- **رساله** با مرکز خدمات DB حقوق مسافر
- **دستگاه های هزینه** (هوتل، تاکسی، غذا) - کارت اعتباری، صورتحساب
- **دانشگاه های صفحه نمایش DB Navigator** با اعلان تاخیر

## رشته های واجب

```yaml
fall-id: FGR-2026-0042
reisedatum: 2026-05-12
reisende:
  - name: Mueller, Hans
    geburtsdatum: 1972-08-15
    rolle: hauptbuchender
  - name: Mueller, Eva
    geburtsdatum: 1975-03-22
    rolle: ehepartner
  - name: Mueller, Lea
    geburtsdatum: 2010-06-18
    rolle: minderjährig

buchungscode: ABC123          # PNR / Auftragsnummer
buchung-bei: DB Vertrieb GmbH # Verkaufender Vertriebsweg (bahn.de, DB Reisezentrum, Reisebüro)
buchungsdatum: 2026-04-12

ticket:
  art: sparpreis              # flexpreis | sparpreis | super-sparpreis | bahncard-100 | deutschlandticket | zeitkarte | reisepass-tarif
  klasse: 2                   # 1 oder 2
  preis-eur: 79.00            # tatsächlich gezahlter Preis
  zugbindung: ja              # bei sparpreis/super-sparpreis grundsätzlich ja
  bahncard: BC50              # null | BC25 | BC50 | BC100

verbindung-gebucht:
  abfahrt:
    bahnhof: Berlin Hbf
    iata-uic: 8011160
    planmaessig: 2026-05-12T08:25:00+02:00
  ziel:
    bahnhof: Muenchen Hbf
    iata-uic: 8000261
    planmaessig: 2026-05-12T13:20:00+02:00
  zuege:
    - nr: ICE 503
      operating-evu: DB Fernverkehr AG
      abschnitt: Berlin Hbf - Muenchen Hbf
  einheitliche-pnr: ja        # → Durchgangsfahrkarte nach Art. 12 VO

verbindung-tatsaechlich:
  abfahrt-ist: 2026-05-12T08:45:00+02:00   # +20 Min
  ankunft-ist: 2026-05-12T15:05:00+02:00   # +1h 45 Min am Endziel
  zug-tatsaechlich: ICE 503                # ggf. anderer Zug bei Umbuchung
  umsteige-bahnhoefe: []
  endziel-verspaetung-min: 105             # ≥ 60 Min → 25 % Anspruch (ab 120: 50 %)

stoerung:
  art: verspaetung            # verspaetung | zugausfall | anschlussverlust | vorverlegung | nichtbefoerderung
  ursache-laut-db: technischer Defekt
  bekanntgabe-am: 2026-05-12T07:50:00+02:00
  bekanntgabe-wie: app        # app | sms | email | aushang | schalter
  ersatz-angebot: ja
  ersatz-detail: Ersatzfahrt im selben ICE 503 mit Verspätung
  hilfeleistung-erhalten:
    verpflegung: nein
    hotel: nein
    transport: nein

auslagen:
  taxi-eur: 0
  hotel-eur: 0
  verpflegung-eur: 12.50
  belege: [belege/2026-05-12/kassenbon-bahnhofsimbiss.pdf]

belege:
  - typ: buchungsbestaetigung
    pfad: belege/2026-05-12/buchung-ICE503.pdf
  - typ: e-ticket
    pfad: belege/2026-05-12/e-ticket-mueller.pdf
  - typ: stoerungsmeldung
    pfad: belege/2026-05-12/db-navigator-verspaetung.png
  - typ: ankunft-anzeigetafel
    pfad: belege/2026-05-12/foto-anzeigetafel-muenchen.jpg
  - typ: kassenbon
    pfad: belege/2026-05-12/kassenbon-bahnhofsimbiss.pdf
```

## استخراج OCR / PDF

- برای بلیط های PDF، استخراج خودکار از PNR / شماره سفارشات ، شماره قطار ، تاریخ و ایستگاه ها.
- در صورت اثبات تصویری OCR، اگر اعتبار کمتر از ۹۰ درصد باشد پرچم بازرسان برای تأیید دستی.
- شماره های سفارش DB به شکل یک آی دی 12 رقمی (تطبيق قطار) یا PNR 6 رقمی برای فروش کلاسیک دارند.
- کد ایستگاه های UIC (8011160 Berlin Hbf، 8000261 München Hbp) را بررسی کنید - در DB Open Data رایگان است.

## ذخیره سازی شواهد زمان واقعی ورود

*دروازه ای در ایستگاه مقصد*Art. 3 Nr. 18 VO 2021/782) شواهد:

1. **DB Navigator** زمان واقعی ورود را در زیر "تفصیلات اتصال" ذخیره می کند - Screenshot به موقع.
2. **فارم حقوق مسافر DB Rail**: اگر در DB درخواست تاخیر شود، سیستم یک تایید تأخری با داده های خود DB را تولید می کند. این شواهد قوی ترین دلیل بحث است.
3. **مطالبات تله** در هنگام لغو / تأخیر (راه قدیمی)
4. ** عکس صفحه نمایش ایستگاه ها** با زمان و ساعت آمد واقعی نشان داده شده (در صورت اختلاف، اثبات).
5. شاهدان - همنشینان

## ردیابی DB (در داخل DB)

DB دارای سوابق داخلی از تمام حرکات قطار (دتابیس عملیاتی LeiDis-NK / DiRail) است. در این پرونده می توان درخواست داد§§ 421 ff. ZPO شواهد اسناد) اطلاعات پیش از عمل در مورد § 242 BGB (محمله های ثانویه)

## چند مسافر

**یک* پرونده ی حقوق در هر سفر با چندین مسافر ثبت می شود.Art. 19 ویو شخصی است؛ حداقل 4 یورو نیز برای هر بلیط. § 60 ZPO) اختیار در مورد `vollmacht-mitreisende`.

## از دست دادن اتصال در کارت عبور

اگر رزرو چند قطار با یک PNR (Art. 12 Abs. 3 VO 2021/782در این مورد، اگر به طور کلی تاخیر در هدف نهایی مهم باشد نه اینکه یک قطار از زمان عبور کند. `umsteige-bahnhoefe` و به دست آوردن آن.

**در مورد چندین بلیط جداگانه** (PNR های مستقل) هر قرارداد باید به صورت جداگانه بررسی شود - تضمین پیوستن قابل قبول نیست، مگر اینکه فروشنده ی بلیت/ورگراه کننده این را صریحاً وعده داده باشد.Art. 12 Abs. 4 و

## بررسی EVU عملیاتی

- DB فروش همچنین بلیط های رقابتی را می فروشد. در مورد خطوط NWB، ÖBB و FlixTrain سیستم توزیع DB: **Operating EVU شرکت واقعی رانندگی است** - نه DB راه دور
- همیشه مخالف این حق است که EVU اجرا کند.Art. 19 Abs. 1 و
- در DB Regio: اغلب توسط کشورهای فدرال سفارش داده می شود؛ به صورت غیرفعالانه، DB Region قانونی باقی مانده است.
- در FlixTrain: فلیکس ترین GmbH، برج 16 Friedenheimer 80639 مونیخ.

## مجموعه ی مسافرت های کلی

اگر سفر قطار بخشی از یک مسافرتی است (سازنده ی مسافرت) ، حقوق مربوط به VO 2021/782 (به نسبت به EVU) و §§ 651a ff. BGB (به سوی سازمان های مسافرتی) `verspaetung-und-anschlussverlust-einordnen` و ggf. اشاره به `prozessrecht` یا `verbraucherschutzrecht-pruefer`.

## خروجی

- `fallakte.yaml` با تمام داده های اصلی.
- `belegliste.md` با پرچم معاینه برای شواهد فاقد اثبات.
- `naechste-schritte.md` توصیه به مهارت های بعدی (`verspaetung-und-anschlussverlust-einordnen` یا مستقیماً `entschaedigung-berechnen` در صورت وجود شواهد واضح

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **الزامِ تمام‌نویسی و استانداردِ قالب.** محصولِ نهایی در **جمله‌های کامل و تمام‌نوشته** تحویل می‌شود — نه اسکلتِ کلیدواژه، نه تنهٔ خالیِ شرط، نه صرفِ فهرست. شرط‌ها به‌صورتِ جمله‌های تمام‌نوشتهٔ بیان‌گرِ اثرِ حقوقی می‌آیند؛ جای‌گیرها مانند `[Name der Mandantin]` روشن علامت می‌خورند و متنِ پیرامون کامل می‌ماند.
>
> **شکلِ نوشتار:** هرگاه لایحه، قرارداد، یادداشت، تصمیم، ومرک یا هر سندِ نهاییِ دیگر به‌صورتِ DOCX، PDF یا متنِ قالب‌بندی‌شده بیرون داده شود، باید **Times New Roman ۱۱ pt** به‌عنوانِ قلمِ پایه به‌کار رود. عنوان‌ها در همان قلم می‌مانند و تنها می‌توانند سیاه (بولد) یا پلکانی باشند. در خروجیِ صرفاً Markdown یا چت، این خواستهٔ قالب به‌عنوانِ یادداشتِ برون‌سپاری درج می‌شود.
>
> **شماره‌گذاری:** ساختاربندی منحصراً اعشاری (`1`، `1.1`، `1.1.1` و به همین ترتیب). بدون اعداد رومی، بدون ساختاربندی حرفی یا آمیخته.
<!-- END ausformulierungspflicht (autogen) -->

## تصمیمات اصلی جمع آوری داده ها

قضیه: هیچ تصمیمی را از دانش نمونه ای نقل نکنید؛ قبل از انتشار با دادگاه، شکل تصمیم گیری و تاریخ آن ها، نشانه های پرونده یا اظهارات قابل اثبات را توسط منبع رسمی یا آزاد تأیید کنید.
