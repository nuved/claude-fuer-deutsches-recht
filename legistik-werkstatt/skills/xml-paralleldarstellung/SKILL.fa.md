---
name: xml-paralleldarstellung
description: "Wenn es um XML-Paralleldarstellung in Legistik-Werkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# تنظیم موازی XML

## لنگرهای قانونی

تمرکز کار: **موازات XML**. این لنگرها را در مورد واقعیت بررسی کنید؛ فقط معیارهای مشابهی که همان محصول، زمان بندی یا سوال اثبات دارند تکمیل نمایید

- `Art. 20 Abs. 3 GG` -قانون پيروي مي کنه
- `Art. 76 Abs. 1 GG` -قانون سازي
- `Art. 77 Abs. 1 GG` -قانونیه
- `Art. 80 Abs. 1 GG` - فرماندهی
- `Art. 84 Abs. 1 GG` -در زندان اداري
- `§ 42 Abs. 1 GGO` -تعدادات قانون سازي
- `§ 43 Abs. 1 GGO` -حسرت ريسور
- `§ 44 Abs. 1 GGO` -آنها قانون هستند.
- `§ 45 GGO` -مشاركت
- `§ 46 GGO` -قانونیه

رویهٔ قضایی را تنها هنگامی بیفزایید که دادگاه، تاریخ، شمارهٔ پرونده و یک منبعِ آزادانه قابل‌بررسی موجود باشد؛ از استنادهای کورِ BeckRS/juris استفاده نکنید.

## طرح ها

### اتحاد

- **eNorm** فدرال (XML schema BMJ)
- **LegalDocML.de** (بنیاد Akoma Ntoso، استاندارد OASIS)

### کشور

پورتال های قانونی کشور، از فرمتهای XML خود استفاده می کنند. LegalDocML.de.

## ساختار حداقل

```xml
<akomaNtoso xmlns="http://docs.oasis-open.org/legaldocml/ns/akn/3.0">
 <act name="entwurf-paragraf-33a-hgb">
 <meta>
 <identification source="#bmj">
 <FRBRWork>
 <FRBRthis value="/akn/de/act/2026/pflichtpostfachg"/>
 <FRBRuri value="/akn/de/act/2026/pflichtpostfachg"/>
 <FRBRdate date="2026-05-23" name="Auftragsdatum"/>
 <FRBRauthor href="#bmj"/>
 <FRBRcountry value="de"/>
 </FRBRWork>
 </identification>
 </meta>
 <body>
 <article eId="art_1">
 <num>Artikel 1</num>
 <heading>Aenderung des Handelsgesetzbuchs</heading>
 <paragraph eId="art_1__para_1">
 <content>
 <p>Das Handelsgesetzbuch ... wird wie folgt geaendert: ...</p>
 </content>
 </paragraph>
 </article>
 </body>
 </act>
</akomaNtoso>
```

## بررسی

تایید طرح از طریق xmllint:

```
xmllint --schema akomaNtoso-3.0.xsd --noout entwurf.xml
```

## قضیه فعلی و اصول

- قضیه: هیچ تصمیمی را از دانش نمونه ای نقل نکنید؛ قبل از انتشار با دادگاه، شکل تصمیم گیری و تاریخ آن ها، نشانه های پرونده یا اظهارات قابل اثبات را توسط منبع رسمی یا آزاد تأیید کنید.

## استاندارد های مرکزی (سلسلۀ پاراگراف)

§§ 1-5 eGovG (قانون دولت الکترونیکی، واجبات دیجیتالی شدن) §§ 3a، 3ب VwVfG (آیا به صورت الکترونیکی مدیریت شود) § 2 ERV (متطلبات فرمت سند) - ISO 8879 (استانداردهای SGML/XML) - استانداردهای LegalDocML (OASIS، قوانین پارلمان)

## خروجی

فایل XML و پروتکل اعتبارسنجی. در صورت خطا اصلاح کنید و دوباره تأیید نمایید

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **الزامِ تمام‌نویسی و استانداردِ قالب.** محصولِ نهایی در **جمله‌های کامل و تمام‌نوشته** تحویل می‌شود — نه اسکلتِ کلیدواژه، نه تنهٔ خالیِ شرط، نه صرفِ فهرست. شرط‌ها به‌صورتِ جمله‌های تمام‌نوشتهٔ بیان‌گرِ اثرِ حقوقی می‌آیند؛ جای‌گیرها مانند `[Name der Mandantin]` روشن علامت می‌خورند و متنِ پیرامون کامل می‌ماند.
>
> **شکلِ نوشتار:** هرگاه لایحه، قرارداد، یادداشت، تصمیم، ومرک یا هر سندِ نهاییِ دیگر به‌صورتِ DOCX، PDF یا متنِ قالب‌بندی‌شده بیرون داده شود، باید **Times New Roman ۱۱ pt** به‌عنوانِ قلمِ پایه به‌کار رود. عنوان‌ها در همان قلم می‌مانند و تنها می‌توانند سیاه (بولد) یا پلکانی باشند. در خروجیِ صرفاً Markdown یا چت، این خواستهٔ قالب به‌عنوانِ یادداشتِ برون‌سپاری درج می‌شود.
>
> **شماره‌گذاری:** ساختاربندی منحصراً اعشاری (`1`، `1.1`، `1.1.1` و به همین ترتیب). بدون اعداد رومی، بدون ساختاربندی حرفی یا آمیخته.
<!-- END ausformulierungspflicht (autogen) -->

## اتصال

`folgenabschaetzung-erfuellungsaufwand`.
