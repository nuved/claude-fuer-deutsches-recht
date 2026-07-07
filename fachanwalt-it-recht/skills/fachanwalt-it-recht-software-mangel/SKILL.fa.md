---
name: fachanwalt-it-recht-software-mangel
description: "Wenn es um Software-Mangel in Fachanwalt It Recht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# کمبود نرم افزار

## سوالات شروع سرد

1. آیا این نرم افزار استاندارد (حق خرید) ، توسعه فردی (عقد کاری) یا خدمات SaaS/کلاوود است (اقدمی اجاره § 535 BGB)?
2. آیا این کارخانه یا نرم افزار قبلاً خریداری شده و تحویل داده شده است؟
3. چه ویژگی های مشخصی از دست رفته یا به طور وعده داده شده کار نمی کنند؟ آیا یک فول استار/اجازه وجود دارد؟
4. آیا عرضه کننده را به مدت زمان تکمیل مجدد تعیین شده بود و چه واکنش نشان داده شد؟
5. مشتری مصرف کننده یا کارآفرین است؟ چه بند های شرط بندی ها اعمال می شوند؟
- ** چه چیزی را واقعاً می خواهد مشتری به دست آورد؟** (نه، آنچه که در راه استاندارد نوشته شده است بلکه: کدام نتیجه برای مشتریان از نظر شخصی/اقتصادی بهترین است ؟ گاهی اوقات مقایسه سریع تر بهتر از روش رسمی "صواب" است.)

## اساس ادعای

- نرم افزار استاندارد: حق خرید - کمبود فاکت § 434 BGB (مطالبات معینی و ذهنی) § 435 BGB.
- نرم افزار فردی: قرارداد کار - کمبود § 633 BGB، کار بدون نقص های حقوقی و فاکتوری در صورت دریافت.
- SaaS/Cloud: حق اجاره § 535 BGB - ادامه استفاده، کمبود § 536 BGB به قانون منجر می شود.
- واجب انجام: § 439 BGB (خرید) یا § 635 BGB (کار) - تعمیر و یا عرضه مجدد.
- حقوق ثانویه پس از شکست: استعفا § 437 Nr. 2 i.V.m. § 323 BGBکاهش § 441 BGB, خسارت § 437 Nr. 3 i.V.m. §§ 280, 281 BGB.
- قضیه: هیچ تصمیمی را از دانش نمونه ای نقل نکنید؛ قبل از انتشار با دادگاه، شکل تصمیم گیری و تاریخ آن ها، نشانه های پرونده یا اظهارات قابل اثبات را توسط منبع رسمی یا آزاد تأیید کنید.

## بار و زمان اثبات

- پس از انتقال یا کاهش خطر، خریدار/طلب کننده مسئولیت اثبات نقص را بر عهده دارد.
- خرید کالاهای مصرفی: بازپرداخت بار شواهد § 477 BGB برای یک سال از زمان انتقال خطر (قبل از 01.01.2022: شش ماه)
- ممانعت حق خرید: دو سال § 438 Abs. 1 Nr. 3 BGBقرارداد ساخت و ساز در صورت عدم انجام کار: دو سال § 634a Abs. 1 Nr. 1 BGB.
- در صورت عدم وجود پنهان: تعویق قانون § 438 Abs. 3 BGB و یا § 634a Abs. 3 BGB.

## برنامه آزمایش

```
1. Vertragstyp bestimmen (Kauf / Werk / Miete-SaaS)
2. Sollbeschaffenheit aus Lasten/Pflichtenheft und Vertrag ableiten
3. Istbeschaffenheit aus Tests und Logs dokumentieren
4. Soll/Ist-Abweichung = Mangel
5. Nacherfuellungsfrist setzen (zwei bis vier Wochen je nach Komplexitaet)
6. Bei Fristablauf: Ruecktritt oder Minderung oder Schadensersatz
7. Verjaehrung im Kalender notieren
```

- قانون منبع: ادبیات فقط با منابع کاربر یا دسترسی زنده مجاز؛ هیچ جای برای یافتن نظرات، کتابچه و مقاله از دانش مدل نیست.

## گزینه های استراتژیک (پیش از انتخاب قالب)

قبل از اینکه یک به یک پر کنید، باید بررسی کرد که کدام نوع برای کنسلتیون مشتری مناسب است. این قالب شکل احتمالی ای ـه - تنها نیست

| ستاره شناسی | راه توصیه شده |
|---|---|
| استاندارد - ادعای کمبود نرم افزار | عدم سکوت؛ قالب پایین |
| گزینه A - مشتری می خواهد با فروشندگان کار کند | تکمیل مجدد § 439 BGB ترجیح می دهند؛ شکایت به عنوان آخرین راه حل |
| گزینه B - نقص SLA به جای عدم وجود | بررسی مجازات های قراردادی؛ مهارت دیگر |
| گزینه C - اجزای منبع باز تحت تأثیر قرار می گیرد | بررسی رعایت مجوز؛ جبران خسارت بر اساس جرم |

اگر کنستلاسیون مشتری ** نمی تواند به طرح استاندارد مطابقت داشته باشد، باید قالب را تغییر دهید یا با مهارت دیگری جایگزین کنید - نه اینکه دستورات را در schema فشار بدهید.


## طرح نامه نقصی با تعویض زمان

```
Sehr geehrte Damen und Herren,

namens und in Vollmacht unserer Mandantschaft ruegen wir die nachfolgend
beschriebenen Maengel der gelieferten Software [Produktbezeichnung,
Versionsnummer]:

1. [Mangel 1 — Soll laut Pflichtenheft Ziff. X / Ist laut Test-Protokoll vom ...]
2. [Mangel 2 — ...]
3. [Mangel 3 — ...]

Wir fordern Sie auf bis spaetestens [Datum, mindestens zwei Wochen] die
Maengel im Wege der Nacherfuellung gemaess § 439 BGB / § 635 BGB zu
beseitigen.

Nach fruchtlosem Fristablauf werden wir vom Vertrag zuruecktreten den
Kaufpreis zurueckverlangen sowie Schadensersatz statt der Leistung
geltend machen (§§ 437 Nr. 2 und Nr. 3 BGB i.V.m. §§ 323 280 281 BGB).

Mit freundlichen Gruessen
```

--- قبل از ارسال
1. هدف مذاکره کسل کننده چیست؟ [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. چه خط های سازشی مطلق هستند؟ [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. آیا راه های اتصال مطلوب هستند؟ [Mediation / Direktgespraech / Settlement vor Klageerhebung]

## انتقال

- در صورت پر کردن تازه بدون تکمیل: انتقال به `forderungsmanagement-klagewerkstatt` برای رفع این شکایت.
- در صورت انجام کار به طور مداوم: موازی اعلام کاهش برای مستثمران § 536 BGB.
- در تقویم پرونده ها، زمان انقضا را یادداشت کنید.

## در حال حاضر (v14.2)

- قضیه: هیچ تصمیمی را از دانش نمونه ای نقل نکنید؛ قبل از انتشار با دادگاه، شکل تصمیم گیری و تاریخ آن ها، نشانه های پرونده یا اظهارات قابل اثبات را توسط منبع رسمی یا آزاد تأیید کنید.

## سه بعدی در آغاز

1. نوع قرارداد: خرید / ساخت و ساز / اجاره / خدمات / ترکیب؟
2. نرم افزار استاندارد یا فردی؟
3. اگر کمبود فاکتور وجود داشته باشد (§ 434 BGB) یا عدم وجود قانون (§ 435 BGB) پیش از آن؟
4. آیا زمان تعویض برای تکمیل آن ها قبلاً انجام شده است؟

## نماد محصول - یادداشت کمبود نرم افزار

** آدرس:** دادگاه / طرف مقابل - صوتی: قانونی

```
Software-Mangel-Memo [DATUM]
Parteien: [AUFTRAGGEBER] vs. [AUFTRAGNEHMER/ANBIETER]
Vertragstyp: Kauf § 433 BGB / Werkvertrag § 631 BGB / Miete § 535 BGB
Software: [BEZEICHNUNG, VERSION]

Mangel:
Beschreibung: [KONKRETE BESCHREIBUNG]
Rechtsgrundlage: § 434 Abs. [X] BGB / § 633 Abs. [X] BGB / § 536 BGB

Ansprüche:
1. Nacherfüllung (§ 439 / § 635 BGB): Frist gesetzt am [DATUM]; Ablauf [DATUM]
2. Bei Fristablauf: Rücktritt § 437 Nr. 2 / § 634 Nr. 3 BGB / Minderung / Schadensersatz

Streitwert: [BETRAG EUR]
Verjährung: § 438 BGB 2 Jahre ab Ablieferung / § 195 BGB 3 Jahre (§ 634a BGB)
```

---
آډیت ۲۷05.2026: بسته 010: تعمیرات توهم
<!-- VII ZR 124/18 (به گفته ی او، ۶)06.2019در این گزارش آمده است که: dejure.org - حذف شد -->
<!-- VII ZR 190/20 (این ادعا شده در NJW 2021، 3438 موضوع: کمبود نرم افزار): WRONG_TOPIC - real: کفش پنجره های ترمو خودرو, NJw 2021, 3721, تایید شد dejure.org/2021،37448 - حذف شده -->

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **الزامِ تمام‌نویسی و استانداردِ قالب.** محصولِ نهایی در **جمله‌های کامل و تمام‌نوشته** تحویل می‌شود — نه اسکلتِ کلیدواژه، نه تنهٔ خالیِ شرط، نه صرفِ فهرست. شرط‌ها به‌صورتِ جمله‌های تمام‌نوشتهٔ بیان‌گرِ اثرِ حقوقی می‌آیند؛ جای‌گیرها مانند `[Name der Mandantin]` روشن علامت می‌خورند و متنِ پیرامون کامل می‌ماند.
>
> **شکلِ نوشتار:** هرگاه لایحه، قرارداد، یادداشت، تصمیم، ومرک یا هر سندِ نهاییِ دیگر به‌صورتِ DOCX، PDF یا متنِ قالب‌بندی‌شده بیرون داده شود، باید **Times New Roman ۱۱ pt** به‌عنوانِ قلمِ پایه به‌کار رود. عنوان‌ها در همان قلم می‌مانند و تنها می‌توانند سیاه (بولد) یا پلکانی باشند. در خروجیِ صرفاً Markdown یا چت، این خواستهٔ قالب به‌عنوانِ یادداشتِ برون‌سپاری درج می‌شود.
>
> **شماره‌گذاری:** ساختاربندی منحصراً اعشاری (`1`، `1.1`، `1.1.1` و به همین ترتیب). بدون اعداد رومی، بدون ساختاربندی حرفی یا آمیخته.
<!-- END ausformulierungspflicht (autogen) -->

