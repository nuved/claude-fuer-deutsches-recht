---
name: kommandocenter
description: "Wenn es um Umweltrecht-Kommandocenter in Umweltrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# مرکز فرماندهای حقوق محیط زیست

## مسیر کار

- روشن‌کردن نقش، هدف و محصول کاری خواسته‌شده: چه کسی اقدام می‌کند، چه تصمیمی در پیش است، چه مهلتی در جریان است و چه خروجی‌ای لازم است؟
- اول، مهلت ها و خطرات فوری را مشخص کنید: BImSchG § 10 تفسیر 1 ماه / اعتراضات 1 ماه UmwRG § 4 یک ماه تا زمان شکایت، 1 سال برای بررسی تعمیرات و بازپرداخت.
- بررسی معیارهای مربوط به: BImSchG, KrWG, WHG, BNatSchG, UVPG، BBodSchG, ChemG، اختلالV (12. BIMSCHV), TA هواIED 2010/75, UmwRG, EU-FFH-RL, EU-WRRL - مراکز مربوط به gesetze-im-internet.de, dejure.org،آفتاب BVerfG-/BGH-/EuGH-دیتابیس زنده را بررسی کنید، بدون نقل قول دانش مدل
- تعیین مقام صلاحیت و انتخاب صحیح مخاطبان: شرکت کنندگان، آژانس مجوز، انجمن های زیست محیطی (BUND, NABU) VG, OVG, BVerwG (۷) مجلس نمایندگان، کمیسیون اتحادیه اروپا و کارشناسان.
- جمع آوری اسناد و شواهد و بررسی شکافها: مجوز حفاظت از آلودگی، گزارش UVP، مطالعه سازگاری FFH، برنامه اصلاحات، شکایت اتحادیه ای، درخواست؛ محاسبه صدا/آواز TA-هوا /TA - دریافت مدارک گمشده با مشاهده پرونده یا بازرسی مشتری، چک زنده برای تغییرات روزانه در استانداردها و شیوه های مدیریت.

## ماتریکس سه بعدی - کدام ماژول تخصصی؟

| وضعیت | ماژول تخصصی |
|---|---|
| BImSchG- درخواست یا اعتراض به مجوز | `umweltrecht-immissionsschutz-bimschg` |
| تجارت با انتشار CO2، BEHG, DEHST | `umweltrecht-emissionshandel-tehg` |
| وضعیت زباله KrWG, محصول جانبی, اقتصاد دایره ای | `umweltrecht-abfall-circular-economy` |
| حفاظت از طبیعت، FFH, محافظت از گونه ها § 44 BNatSchG | `umweltrecht-naturschutz-artenschutz` |
| دستگاه زلزله، 12م. | `umweltrecht-stoerfall-anlagen` |
| اجازه آب، بار های قدیمی | `umweltrecht-wasser-bodenschutz` |
| مبادله ی M&A، محیط زیست DD, پرچم های قرمز | `umweltrecht-transaktionen-dd` |
| درخواست اطلاعات UIG/IFG، رد شد | `umweltrecht-umweltinformation-uig-ifg` |
| VG- شکايت، درخواست عجله اي ، شکایت OVG | `umweltrecht-verfahren` |
| حکم جریمه، شنیدن و مجازات | `umweltrecht-bussgeld-sanktionen` |
| تعمیل، مأموریت ها، برنامه آموزشی | `umweltrecht-compliance-schulung` |
| ESG، CSRD، Greenwashing | `esg-greenwashing-csrd` |
| دعوی آب و هوا، دادخواست اتحادیه UmwRG | `klimaklagen-verbandsklage-umwrg` |
| زنجیره تامین، LkSG, CSDDD | `lksg-csddd-lieferkettensorgfalt` |

## سوالات دریافتی (برای هر ماموریت)

1. ** نقش مدیر**: کارکن، سرمایه گذار، شخص ثالث مورد توجه، انجمن محیط زیست، اداره؟
2. ** حوزه ی قانون**: BImSchG, KrWG, WHG، BBodSchG، TEHG BNatSchG - یا چندتا؟
3. **حال عمل**: هنوز هیچ پروسه ای وجود ندارد / روند درخواست در حال اجرا است / اطلاع داده شده است / شکایت زیر نظر؟
4. **زمان مرگ و میر حاد**: اعتراض 1 ماه، شکایت یک ماه، درخواست فوری غیر قابل پیش بینی - اطلاع رسانی؟
5. **مواد اثبات**: چه اسنادی - مجوز، گزارش ها، نامه های دولتی و عکس؟
6. **هدف اقتصادی**: امنیت فعالیت، جلوگیری از سرمایه گذاری، تخفیف خطر، دسترسی به اطلاعات و حفاظت از شهرت؟

## قوانین مرکزی قطعات متقاطع قانون محیط زیست

- **§§ 3-10 BImSchG** - تعهدات اساسی در زمینه حفاظت از انتشار گازهای گلخانه ای
- **§§ 4 9 10 BBodSchG** - مسئولیت و بازسازی بار های قدیمی
- **§§ 8 9 10 WHG** - مجوزهای قانونی در مورد آب
- **§§ 14 15 34 44 BNatSchG** - مداخله، FFH, حفاظت از گونه ها
- **§ 2 UmwRG** - شکایت های اتحادیه
- **§ 4 UmwRG** - اشتباهات در روش ها به عنوان دلیل حذف
- **§ 80 Abs. 5 VwGO** - حفاظت از حق عجله در برابر مجوز قابل اجرا

## تصمیمات اصلی (ملاحظه)

- قضیه: هیچ تصمیمی را از دانش نمونه ای نقل نکنید؛ قبل از انتشار با دادگاه، شکل تصمیم گیری و تاریخ آن ها، نشانه های پرونده یا اظهارات قابل اثبات را توسط منبع رسمی یا آزاد تأیید کنید.

## ارزیابی ریسک آمپلتریکس (آمپلیت استاندارد)

| خطر | چراغ | مهلت ها | مسئول | بعدی |
|---|---|---|---|---|
| [THEMA 1] | سرخ | [DATUM] | [PERSON] | [HANDLUNG] |
| [THEMA 2] | نارنجی | [DATUM] | [PERSON] | [HANDLUNG] |
| [THEMA 3] | سبز | — | [PERSON] | نظارت |

## نماد محصول: دستور کار قانون محیط زیست

** آدرس:** پرونده / یادداشت داخلی - صدا: ساختار یافته، با کلمات کلیدی

```
MANDATSKARTE UMWELTRECHT
Stand: [DATUM]
Akte: [AKTENZEICHEN]

MANDANT: [NAME], [ROLLE: Betreiber/Nachbar/Verband]
GEGNER/BEHOERDE: [NAME/STELLE]
ANLAGE: [BEZEICHNUNG], [ORT], [TYP]

RECHTSRAHMEN:
- Hauptnorm: § [X] [GESETZ]
- Nebenrecht: [weitere Normen]

VERFAHRENSSTAND:
- [DATUM]: Genehmigung erteilt / Antrag gestellt / Bescheid erhalten
- [DATUM]: Widerspruch eingelegt / Klage erhoben
- [DATUM]: Naechster Termin [Erörterungstermin / VG / OVG]

FRISTEN:
- [DATUM]: Klagefrist / Einwendungsfrist / TEHG-Abgabe

RISIKEN:
- ROT: [Konkrete Gefahr, z.B. Praeklusion mangels Einwendung]
- ORANGE: [Risiko mit Einschaetzung Wahrscheinlichkeit]

NAECHSTE HANDLUNG:
1. [Konkrete Massnahme, Verantwortlich, Deadline]
2. [Weitere Massnahme]

OFFENE FRAGEN / BENOETIGT:
- [Dokument / Information]
```

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **الزامِ تمام‌نویسی و استانداردِ قالب.** محصولِ نهایی در **جمله‌های کامل و تمام‌نوشته** تحویل می‌شود — نه اسکلتِ کلیدواژه، نه تنهٔ خالیِ شرط، نه صرفِ فهرست. شرط‌ها به‌صورتِ جمله‌های تمام‌نوشتهٔ بیان‌گرِ اثرِ حقوقی می‌آیند؛ جای‌گیرها مانند `[Name der Mandantin]` روشن علامت می‌خورند و متنِ پیرامون کامل می‌ماند.
>
> **شکلِ نوشتار:** هرگاه لایحه، قرارداد، یادداشت، تصمیم، ومرک یا هر سندِ نهاییِ دیگر به‌صورتِ DOCX، PDF یا متنِ قالب‌بندی‌شده بیرون داده شود، باید **Times New Roman ۱۱ pt** به‌عنوانِ قلمِ پایه به‌کار رود. عنوان‌ها در همان قلم می‌مانند و تنها می‌توانند سیاه (بولد) یا پلکانی باشند. در خروجیِ صرفاً Markdown یا چت، این خواستهٔ قالب به‌عنوانِ یادداشتِ برون‌سپاری درج می‌شود.
>
> **شماره‌گذاری:** ساختاربندی منحصراً اعشاری (`1`، `1.1`، `1.1.1` و به همین ترتیب). بدون اعداد رومی، بدون ساختاربندی حرفی یا آمیخته.
<!-- END ausformulierungspflicht (autogen) -->

## مهارت های رابط

- `fachanwalt-verwaltungsrecht-orientierung` - بررسی عمومی قانون مدیریتی
- `energieanlagen-bimschg-genehmigung-verfahren` - انرژی تخصصیBImSchG
- `energietrassen-planfeststellung-rechtsschutz` - تعیین برنامه انرژی
- `esg-greenwashing-csrd` - گزارش های پایداری
- `klimaklagen-verbandsklage-umwrg` - دعوه های آب و هوایی
