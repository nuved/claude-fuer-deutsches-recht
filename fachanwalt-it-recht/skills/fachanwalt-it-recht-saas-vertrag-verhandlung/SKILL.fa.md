---
name: fachanwalt-it-recht-saas-vertrag-verhandlung
description: "Wenn es um SaaS-Vertrag — Prüfung und Verhandlung in Fachanwalt It Recht geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# قرارداد SaaS - بررسی و مذاکره

## سوالات شروع سرد

1. چه کسی ارائه دهنده (Hyperscaler مانند AWS/Azure/Google، نرم افزار های کاری، خدمات و سرویس (CRM, ERP, HR system) چیست؟
2. مشتری از طریق کسب و کار (B2B) یا مصرف کننده (B3C) - سطوح مختلف حفاظت§§ 327 ff. BGB در B2C؟
3. چه حجم قرارداد - اشتراک سالانه یا معامله چند ساله؟ از حدود 50،000 یورو/سال، مذاکره فردی قابل اجرا است.
4. چه دسته هایی از داده ها پردازش می شوند - اطلاعات شخصی مشتری، اطلاعات بهداشتی Art. 9 DSGVOاطلاعات بانکي، راز تجاری؟
5. محل سرور - اتحادیه اروپا/اقتصاد اقتصادی، ایالات متحده آمریکا و سایر کشورهای ثالث؟ دلیل: DSGVO-حدیدات انتقال Art. 46،آزمایش های Schrems II، قانون ابر
6. مدت قرارداد چقدر است و چه مدّت هایی برای فسخ؟ تمدید خودکار؟
7. آیا یک نوع داده مالکیت شده وجود دارد که در آن فروشنده را محصور کند، و امکان صادرات API ندارد؟
8. چه کسی را برای مذاکره با سازنده قرارداد - قانونی، فروش و خرید می توان گفت؟
- ** چه چیزی را واقعاً می خواهد مشتری به دست آورد؟** (نه، آنچه که در راه استاندارد نوشته شده است بلکه: کدام نتیجه برای مشتریان از نظر شخصی/اقتصادی بهترین است ؟ گاهی اوقات مقایسه سریع تر بهتر از روش رسمی "صواب" است.)

## مبانی قانونی

### نوع قرارداد و رژیم های نقص

- قضیه: هیچ تصمیمی را از دانش نمونه ای نقل نکنید؛ قبل از انتشار با دادگاه، شکل تصمیم گیری و تاریخ آن ها، نشانه های پرونده یا اظهارات قابل اثبات را توسط منبع رسمی یا آزاد تأیید کنید.
- **§§ 327-327u BGB** (از 01.01.2022) - قراردادهای مربوط به محتوا و خدمات دیجیتال در B2C: § 327e BGB کمبود امکانات § 327f BGB باید به روز شود § 327j BGB 2 سال، § 327k BGB یک سال در حال بازتاب بار اثبات
- **§§ 305–310 BGB** - کنترل های CTA: § 309 Nr. 7 BGB - در صورت غفلت یا پیش بینی های جدی، از دست دادن مجوز؛ § 309 Nr. 5 BGB - پرداخت مناسب هزینه های خسارت در مجموع § 308 Nr. 4 BGB - هیچ حق یکطرفه ای در تغییر حقوق بدون دلیل واقعی وجود ندارد؛ § 309 Nr. 9 BGB - مدت زمان B2C حداکثر 2 سال + تخفیف ماهانه

### حفاظت از اطلاعات

- **Art. 28 DSGVO** - قرارداد پردازش سفارش (AVV): محتوای اجباریAbs. 3 lit. (a-h) ، به صورت کتبی یا الکترونیکی، توسط پردازنده های ذیلی با مجوز.
- **Art. 32 DSGVO** - TOMs: رمزگذاری، نامزدی سازی، کنترل دسترسی و بازیابی در صورت اضطراری
- **Art. 46 DSGVO** - انتقال به کشور های خارج از اتحادیه: شروط استاندارد قراردادی (SCC 2021) ، حفاظت مناسب، BCR.
- قضیه: هیچ تصمیمی را از دانش نمونه ای نقل نکنید؛ قبل از انتشار با دادگاه، شکل تصمیم گیری و تاریخ آن ها، نشانه های پرونده یا اظهارات قابل اثبات را توسط منبع رسمی یا آزاد تأیید کنید.
- **برنامه ی حفاظت از داده های ایالات متحده آمریکا** (قراری اجرای کمیسیون 2023/1795): تصمیم کافی برای ارائه دهندگان معتبر در امریکا (در سال 2023)
- **قانون ابر آمریکا** - مقامات ایالات متحده می توانند از ارائه دهندگان آمریکایی در سراسر جهان داده های ذخیره شده را درخواست کنند؛ بررسی ابرهای دولتی.

### دیگر

- **§ 9 "Gehg**" - حفاظت از اسرار تجاری در میزبان های کشور ثالث
- **NIS2UmsuCG** - در مورد مراکز KRITIS، نیاز به خدمات ارائه دهنده.
- **ISO/IEC 27001** - استاندارد TOMS؛ BSI C5 (تاریخ معیارهای تعمیل در محاسبات ابر)

### تصمیم گیری

- قضیه: هیچ تصمیمی را از دانش نمونه ای نقل نکنید؛ قبل از انتشار با دادگاه، شکل تصمیم گیری و تاریخ آن ها، نشانه های پرونده یا اظهارات قابل اثبات را توسط منبع رسمی یا آزاد تأیید کنید.

## برنامه آزمایش

| Nr. | نقطه آزمایش | استاندارد | سوال اصلی |
|---|---|---|---|
| 1 | AVV Art. 28 DSGVO | Art. 28 DSGVO | آیا موجود است؟ محتوای کامل؟ فرعی؟ |
| 2 | توم Art. 32 DSGVO | Art. 32 DSGVO | رمزنگاري، کنترل دسترسی يا بازپرداخت؟ |
| 3 | مکان داده + انتقال به کشورهای دیگر | Art. 46 DSGVO | سرورهای اتحادیه اروپا؟ ایالات متحده: SCC + TIA? EU-US DPF گواهینامه |
| 4 | دسترسی به SLA | انتخاب حزب | درصد، تعریف خرابی؟ پنجره های نگهداری؟ |
| 5 | تحریم های SLA | انتخاب حزب | اعتبارات خدمات، از کار در صورت دستخط دائمی؟ |
| 6 | نگهداری و بروزرسانی های امنیتی | §§ 535, 327f BGB | فرکانس، پچ های اضطراری؟ |
| 7 | مالکیت داده | انتخاب حزب | چه کسی مالکی از اطلاعات مشتری است؟ |
| 8 | شقۀ خروج / مهاجرت داده ها | انتخاب حزب | شکل صادرات، زمان بندی، هزینه ها و قابلیت همکاری؟ |
| 9 | محدودیت مسئولیت | §§ 309 Nr. 7, 309 Nr. 5 BGB | 12 ماهگی، مگر قصد و غفلت؟ |
| 10 | زمان تمام شدن / تخلیق | §§ 314 BGB, 309 Nr. 9 BGB | مدت زمان، تمدید خودکار، از کار کردن به صورت غیر معمول؟ |
| 11 | مقررات قیمت سازگاری | § 308 Nr. 4 BGB | دلیل فکری؟ |
| 12 | پشتیبان گیری و بازیابی اضطراری | Art. 32 DSGVO | RPO/RTO تعریف شده؟ |

## گزینه های استراتژیک (پیش از انتخاب قالب)

قبل از اینکه یک به یک پر کنید، باید بررسی کرد که کدام نوع برای کنسلتیون مشتری مناسب است. این قالب شکل احتمالی ای ـه - تنها نیست

| ستاره شناسی | راه توصیه شده |
|---|---|
| استاندارد - مذاکره در مورد قرارداد SaaS | قطعات ساختمانی مذاکره، قالب زیر |
| گزینه A - مشتری، ارائه دهنده است نه کاربر | بررسی CTA در طرف ارائه دهنده؛ سایر اولویت های بند |
| گزینه B - داده های انتقادی در SaaS | DSGVO-برنامه های پردازش سفارش؛ بررسی BSI C5 |
| گزینه C - فسخ قرارداد SaaS جاری | استراتژی خروج؛ حمل و نقل داده ها Art. 20 DSGVO |

اگر کنستلاسیون مشتری ** نمی تواند به طرح استاندارد مطابقت داشته باشد، باید قالب را تغییر دهید یا با مهارت دیگری جایگزین کنید - نه اینکه دستورات را در schema فشار بدهید.


## سنگ های ساختاری

### شق SLA (مطابق مذاکرات B2B)

```
§ [X] Service Level Agreement

1. Verfuegbarkeit
   Der Anbieter sichert eine monatliche Systemverfuegbarkeit
   von mindestens 99,5 % (SaaS Standard) / 99,9 % (Premium)
   zu, gemessen am Netzwerkuebergabepunkt des Anbieters,
   ausschliesslich geplanter Wartungsfenster.

2. Wartungsfenster
   Geplante Wartungsarbeiten werden mindestens 48 Stunden
   im Voraus angekuendigt und in die Zeit Montag bis Freitag
   20:00–06:00 Uhr und Wochenende gelegt. Maximale Dauer:
   6 Stunden/Monat.

3. Definitionen
   "Ausfall" ist die vollstaendige Nichterreichbarkeit oder
   Nicht-Nutzbarkeit wesentlicher Kernfunktionen des Dienstes
   aus Gruenden, die nicht in der Sphaere des Kunden liegen.

4. Service Credits
   Bei Unterschreitung der Verfuegbarkeit erhalt der Kunde:
   - 99,0–99,5 %: 10 % der Monatspauschale
   - 98,0–99,0 %: 20 % der Monatspauschale
   - unter 98 %:  50 % der Monatspauschale als Gutschrift.
   Die Geltendmachung erfolgt mit Antrag binnen 30 Tagen.
   Service Credits schliessen weitergehende gesetzliche
   Ansprueche nicht aus.

5. Ausserordentliche Kuendigung
   Unterschreitet die tatsaechliche Verfuegbarkeit zwei
   aufeinanderfolgende Monate die garantierte Verfueg-
   barkeit um mehr als 2 Prozentpunkte, ist der Kunde
   berechtigt, den Vertrag ohne Frist zu kuendigen.
```

### شقۀ خروج / مهاجرت داده ها

```
§ [X] Datenexport und Beendigung

1. Daten des Kunden
   Alle vom Kunden eingegebenen, generierten oder
   hochgeladenen Daten ("Kundendaten") verbleiben im
   Eigentum des Kunden. Der Anbieter erwirbt kein
   Eigentum und kein dauerhaftes Nutzungsrecht.

2. Datenexport
   Waehrend der gesamten Vertragslaufzeit kann der Kunde
   jederzeit und ohne Mehrkosten alle Kundendaten in einem
   gaengigen Standardformat (CSV, JSON, XML oder
   branchenublichem Format) exportieren.

3. Nach Vertragsende
   Innerhalb von [60 / 90] Tagen nach Vertragsbeendigung
   haelt der Anbieter alle Kundendaten zum Abruf bereit.
   Nach Ablauf dieser Frist werden die Daten unwieder-
   bringlich geloescht; Loeschbestaetigung wird erteilt.

4. Migrations-Unterstuetzung
   Auf Wunsch des Kunden erbringt der Anbieter Migrations-
   unterstuetzung zu einem Pauschalpreis von EUR [X]
   (Datenexport in Zielformat + technische Dokumentation
   der Datenstruktur).

5. API-Zugang
   Dem Kunden steht waehrend der Vertragslaufzeit eine
   dokumentierte REST-API zur Datenabfrage und zum
   Datenexport zur Verfuegung.
```

### چک کوتاه AVV

```
Pflicht-Inhalte AVV Art. 28 Abs. 3 DSGVO — Checkliste

[X] Gegenstand, Dauer, Art und Zweck der Verarbeitung?
[X] Art der personenbezogenen Daten; Kategorien Betroffener?
[X] Verarbeitung nur auf dokumentierte Weisung des Verantwortlichen?
[X] Vertraulichkeit der zur Verarbeitung befugten Personen?
[X] TOMs Art. 32 DSGVO implementiert?
[X] Unterauftragsverarbeiter-Regelung (Genehmigung, Weitergabe Art. 28 Pflichten)?
[X] Drittlandtransfer: SCC oder Angemessenheitsbeschluss vorhanden?
[X] Betroffenenrechte-Unterstuetzung (Auskunft, Loeschung, Berichtigung)?
[X] Sicherheitsvorfallmeldung an Verantwortlichen unverzueglich?
[X] Nachweispflicht TOMs (Audits, Zertifikate)?
[X] Loeschung / Rueckgabe bei Vertragsende?
```

--- قبل از ارسال
1. هدف مذاکره کسل کننده چیست؟ [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. چه خط های سازشی مطلق هستند؟ [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. آیا راه های اتصال مطلوب هستند؟ [Mediation / Direktgespraech / Settlement vor Klageerhebung]

## بار اثبات و ارائه

| سوال | بار | استاندارد |
|---|---|---|
| در این بخش، SLA را زیرنظر بگیرید. | مشتری - مستند سازی زمان های افت | انتخاب حزب؛ § 536 BGB |
| بی اثر بودن CTA | دادگاه از طرف دولت؛ پیشنهاد مشتری | § 306 BGB |
| DSGVO-تجاوز AVV | مسئول - حسابداری | Art. 5 Abs. 2 DSGVO |
| ارزیابی TIA انتقال به کشورهای دیگر | مسئول | Schrems II؛ Guidance DSK |
| نقض قرارداد ارائه دهنده | مشتری | قوانین بار اثبات |

## مهلت ها و مدّت گذاری

| مهلت | مدت زمان | استاندارد |
|---|---|---|
| کاهش اجاره (SaaS) | بدون محدودیت زمان بندی؛ کاهش فوری § 536 BGB | § 536 BGB |
| تعویض خسارت | سه سال §§ 195, 199 BGB | §§ 195, 199 BGB |
| ممانعت خسارت های اجاره B2C | دو سال § 327j BGB | § 327j BGB |
| فسخ قرارداد B2C | 14 روز از زمان بسته شدن قرارداد § 355 BGB | §§ 355، 312گ BGB |
| از کار در صورت نقض دائمی SLA | پس از ورود، دلیل این اعلامیه | § 543 BGB در این زمینه، § 314 BGB |
| درخواست اعتبار خدمات Rüge | قرارداد به طور معمول 30 روز | انتخاب حزب |

## ریسک های متداول و واکنش

| خطر | واکنش |
|---|---|
| AVV کاملاً از بین رفته | نقض مستقل در حفاظت از اطلاعات؛ DSGVO-آزمانی را بررسی کنید؛ فوراً از AVV درخواست دهید |
| سرورهای خارج از اتحادیه اروپا بدون SCC | SCC 2021 (مدل داده ها) + TIA را اضافه کنید؛ جایگزین ارائه دهندگان ابر اتحادیه اروپا |
| بررسی قانونی زنده | هیچ تصمیم گیری از دانش مدل نیست؛ قبل از انتشار منبع را ثبت کنید |
| حق تعدیل قیمت یک طرفه | § 308 Nr. 4 BGB - بدون دلیل و حق اعتراض، غیرفعال است |
| مهاجرت داده ها پس از فسخ صرفاً برای پرداخت هزینه بیشتر | مذاکره: یک پنجره صادرات ۹۰ روزه رایگان به عنوان استاندارد |
| فروشنده های ایالات متحده بدون گواهینامه DPF | حتی TIA + SCC؛ به طور جایگزین: ارائه دهندگان بدون Nexus ایالات متحده |

## ارزش اختلاف و هزینه

- حجم قرارداد به عنوان ارزش متنازع در صورت خروج از کار یا خسارت (§ 3 ZPO).
- خسارت در خرابی که به وسیله SaaS رخ می دهد: سود از دست رفته + هزینه اضافی؛ باید اثبات شود.
- DSGVO-عقوبت برای عدم وجود AVV: تا 10 میلیون یورو یا 2 درصد از درآمد سالانه.
- حقوق وکیل در مذاکره: 200 تا 400 یورو/ساعت؛ 3-8 ساعت به صورت معمول برای هر قرارداد.
- RVG: در صورت درخواست برای اعتبار SLA ارزش متنازع = اجاره سالانه GKG.

## توصیه استراتژیک

| وضعیت | توصیه |
|---|---|
| آزمون اولیه استاندارد | AVV، SLA, شق خروج، مسئولیت به عنوان موارد اولویت بندی؛ ایجاد پروتکل نقص های CETA |
| حجم قرارداد < 20،000 یورو/سال | شرایط استاندارد با تغییرات کمترین؛ AVV همیشه مستقل |
| حجم قرارداد > 100،000 یورو/سال | مذاکره کامل به صورت فردی؛ نمونه های قرارداد خود را وارد کنید |
| از این کار بر اساس SLA دستبردی | § 543 BGB در صورت کمبود قابل توجهی؛ اسناد تمام خرابی + شکایت |
| سازمان CRITIS | درخواست گواهینامه BSI C5 از ارائه دهنده؛ NIS2-متطلبات AVV |

## اسکیل‌های پیوسته

- `cyber-incident-response-72h` - در صورت وجود فرکانس داده ها با ارائه دهنده SaaS
- `fachanwalt-it-recht-cyber-vorfall-sofortmassnahmen` - پاسخ حادثه
- `softwarefehler-mangelhaftung-pruefen` - در صورت نقص فنی

## منابع

- BGB §§ 305-310, 327-327u, 535-548
- DSGVO Art. 28, 32, 46, 83
- قضیه: هیچ تصمیمی را از دانش نمونه ای نقل نکنید؛ قبل از انتشار با دادگاه، شکل تصمیم گیری و تاریخ آن ها، نشانه های پرونده یا اظهارات قابل اثبات را توسط منبع رسمی یا آزاد تأیید کنید.
- تصمیم تطبیقی 2023/1795 (EU-US DPF)
- قضیه: هیچ تصمیمی را از دانش نمونه ای نقل نکنید؛ قبل از انتشار با دادگاه، شکل تصمیم گیری و تاریخ آن ها، نشانه های پرونده یا اظهارات قابل اثبات را توسط منبع رسمی یا آزاد تأیید کنید.
- BSI C5 فهرست مورد نیاز Cloud Computing
- ISO/IEC 27001

## در حال حاضر (v14.2)

- قضیه: هیچ تصمیمی را از دانش نمونه ای نقل نکنید؛ قبل از انتشار با دادگاه، شکل تصمیم گیری و تاریخ آن ها، نشانه های پرونده یا اظهارات قابل اثبات را توسط منبع رسمی یا آزاد تأیید کنید.

---

> قضیه: هیچ تصمیمی را از دانش نمونه ای نقل نکنید؛ قبل از انتشار با دادگاه، شکل تصمیم گیری و تاریخ آن ها، نشانه های پرونده یا اظهارات قابل اثبات را توسط منبع رسمی یا آزاد تأیید کنید.
