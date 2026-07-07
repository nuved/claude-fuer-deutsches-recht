---
name: recherchebericht-erstellen
description: "Wenn es um recherchebericht-erstellen in patentrecherche geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Berechnungstabelle mit Schwellen, Annahmen und Kontrollfragen."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# تهیه گزارش تحقیقاتی

## مسیر کار

- روشن‌کردن نقش، هدف و محصول کاری خواسته‌شده: چه کسی اقدام می‌کند، چه تصمیمی در پیش است، چه مهلتی در جریان است و چه خروجی‌ای لازم است؟
- اولین اینکه زمان و ریسک های فوری را مشخص کنید: PatG § 41 اولویت ۱۲ ماه، USPTO موقت 12 ماه، گزارش تحقیقاتی EPO نوع ۶ ماه.
- بررسی معیارهای مربوط به: PatG §§ 1، ۳، ۴، ۹، ۱۰، ۱۳۹ Art. 54, 56, 64, 69, 87 ff., توافق نامه IPC استراسبرگ, PCT, دسترسی به پایگاه داده Espacenet gesetze-im-internet.de, dejure.org،آفتاب BVerfG-/BGH-/EuGH-دیتابیس زنده را بررسی کنید، بدون نقل قول دانش مدل
- تعیین مقام اختصاصی و انتخاب صحیح مخاطب: ثبت کننده، وکیل اختراع، معاینه کار DPMA، بازرس EPO، USPTO، WIPO، رقبا.
- جمع آوری اسناد و شواهد، بررسی شکاف ها: گزارش تحقیقاتی، نظرثانی FTO، تحلیل چشم انداز ثبت اختراع، اسپاسنت/DEPATISnet/Patentscope/PatFT-برنامه، IPC - درخت طبقه بندی برای دریافت مدارک از طریق بازرسی پرونده یا پرسیدن مشتری ، چک زنده در مورد تغییرات روزانه استانداردها و شیوه های مدیریت.

## ساخت و ساز

### ۱. ورق پوسته

```
Recherchebericht
================

Mandant: [Mandantenname]
Aktenzeichen: [Aktenzeichen]
Recherchezweck: [Stand der Technik / Neuheit / FTO / Monitoring / Bescheidantwort]
Stichtag: [Datum des Berichts]
Erstellt durch: [Patentanwältin / Patentanwalt]
 [Kanzlei]
```

### 2- توضیحات سفارش

- مشتری
- اختراع / محصول / روش (در یک پاراگراف)
- هدف تحقیق (در یک پاراگراف)
- فضای قانونی / بازار هدف
- تاریخ تعیین شده

### روش سوم

- چه پایگاه های اطلاعاتی مورد جستجو قرار گرفته اند (اسپاسنت، گوگل پتانس، DPMAregister, DEPATISnet، EPO Register، WIPO PATENTSCOPE، USPTO)
- چه کلاس هایی (CPC، IPC) - بیش از `klassifikation-cpc-ipc`
- چه کلمات کلیدی
- چه مدت (روز ثبت نام / انتشار)
- زبان جستجو (DE، EN, FR؛ ترجمه های ماشین برای JP، CN و KR)
- بانک های اطلاعاتی پرداخت که ** غیر** در آن ها قرار گرفته اند
- چه ادبیات غیر ثبت شده مورد استفاده قرار گرفته است (تدریس، لنز، arXiv و غیره)

### ۴- اسناد ملاقات

جدول های ساختاری با کالم: Veröff.-Nr., ثبت کننده، تاریخ ثبت نام ، کلاس, عنوان، وضعیت، علامت جستجو (X/Y/A/P/E) یا چراغ روشن (قرمز / زرد / سبز), Pinpoint, Link.

برای هر ضربه ای که به طور خاص مربوط باشد، یک پرونده در نیمه صفحه با پنپایت و جدول مشخصه (از `neuheit-pruefen` / `freedom-to-operate-recherche`).

### ۵. خانواده های ثبت اختراع

اگر افراد مرتبط با ضربات خانواده باشند: جدول خانوادگی برای هر ضربتی که دارای کشورهای تأیید کننده و وضعیت قانونی است. `patentfamilien-analyse` و `rechtsstand-pruefen`.

### ۶. ارزیابی

- در **حال تحقیقات فنی:** چند X / Y / A / P / E؟ چه محدودیت ای برای حفظ نوآوری و خلاقیت لازم است؟
- در مورد **تجزیه نوین:** به هر گونه ادعای مربوطه - جدید یا نه؟
- در **آزمایش فعالیت های اختراع:** رویکرد حل مسئله، نتیجه هر ادعا.
- در مورد تحقیقات FTO:** چند تا قرمز / زرد / سبز؟ چه حقوق محافظت کننده ورود به بازار را مسدود می کند؟ کجا نیاز به اقدام است؟
- در هنگام آماده سازی تصمیم:** طرح ورودی به عنوان ضمیمه.

### ۷. توصیه

در سه تا پنج جمله، چه کاری باید کرد؟

- درخواست را به صورت برنامه ریزی ارسال کنید
- درخواست محدود شده را ارسال کنید
- درخواست را ارسال نکنید (پرداخت استفاده، بررسی محرمانه بودن)
- ورود به بازار آزاد
- ورود به بازار فقط با طراحی تخلفات / مجوز
- اعتراض - مهلت [Datum]
- در نظر گرفتن درخواست باطل
- نظارت بیشتر بر رقبای خود
- تحقیقات بیشتری در حوزه پایگاه های داده پرداخت مورد نیاز است

### 8 . نامزدی

```
HINWEIS ZUR RECHERCHE

Diese Patentrecherche ist eine KI-gestützte Vorrecherche und KEINE
amtliche Recherche im Sinne einer DPMA- oder EPA-Recherche. Vollständigkeit
kann nicht garantiert werden, insbesondere:

- Treffer in nicht durchsuchten Sprachen (JP, CN, KR, RU usw.) können verfehlt werden;
- Geheime ältere Anmeldungen (§ 3 Abs. 2 PatG / Art. 54 Abs. 3 EPUe) sind erst
 18 Monate nach Prioritaetstag öffentlich;
- Bezahl-Datenbanken (PatBase, STN, Orbit, Questel u. a.) sind in diese Recherche
 nicht eingeflossen, sofern nicht ausdrücklich vermerkt;
- Nicht-Patent-Literatur ist nur über Standard-Schnittstellen (Google Scholar,
 Lens.org, arXiv, PubMed) erfasst.

Die finale Bewertung der Patentierbarkeit, der Verletzungsfreiheit und des Rechts-
stands muss durch eigenständige Prüfung der Patentanwältin / des Patentanwalts
abgesichert werden. Dieser Bericht ersetzt nicht die anwaltliche Prüfung und ist
keine Rechtsberatung gegenüber dem Endmandanten außerhalb der zuständigen Kanzlei.
```

### 9 .

- لیست رشته های جستجو در هر پایگاه داده
- کلاس های CPC و IPC با تعریف
- لیست منابع با تاریخ بازخواهی
- گlossار (X/Y/A/P/E، INPADOC, Pinpoint)

## زمان

### مرحله اول: جمع آوری ورودی

از مهارت های قبلی:

- `patentrecherche-kaltstart-interview` → دفتر اداری، معاون
- `klassifikation-cpc-ipc` → کلاس ها
- `agentische-datenbank-recherche` → لیست ها و رشته های جستجو
- `stand-der-technik-recherche` → ارزیابی X/Y/A/P/E
- `neuheit-pruefen` → تحلیل ویژگی ها
- `erfinderische-taetigkeit-pruefen` → استدلال PSA
- `freedom-to-operate-recherche` → ارزیابی چراغ
- `patentfamilien-analyse` → جدول های خانوادگی
- `rechtsstand-pruefen` → اطلاعات حقوقی

### مرحله دوم: تولید اسناد مارک داون

ساختارش مثل اون بالا، با تمام جدول ها و پرونده هاي موجود

### مرحله سوم: بررسی بلاک های متهم

در گزارش، سه بار اعلامیه ای (تلاحظی از ورق پوشش، روش کار و بخش 8) - افزونه نمی تواند آن را حذف کند.

### مرحله چهارم: فرمت محصول

فایل مارکدوین `recherchebericht_<aktenzeichen>_<datum>.md` در دفترچه کاری. یک وکیل ثبت اختراع می تواند آن را به Word یا PDF تبدیل کند - این تغییر از طریق ابزار خارجی انجام می شود (به عنوان مثال Pandoc، MS Word "از مارکdown باز کنید").

## یادداشت‌ها

- **برای مشتری قابل درک است.** اگر مشتری وکیل ثبت اختراع نیست: متن های توضیحاتی در مورد X/Y/A، ویژگی های حقوق و حفاظت.
- **سروری* * گزارش ها شامل اختراعات مشتری - محرمانه بودن § 39a PAO و § 203 StGB فقط از طریق کانال های مجاز گزارش می دهند.
- **فرسایش.** در جستجوی بعدی، علامت پرونده و تاریخ ارقام نام فایل متفاوت است - نباید بیش از حد نوشته شود.

## اعلامیه

> همونطور که در گزارش نوشته شده

## سوالات سه بعدی قبل از تهیه گزارش تحقیق

قبل از اینکه گزارش را شکل دهید، باید:
1. آیا تمام نتایج تحقیقاتی از مهارت های قبلی (تجربات نوین، فعالیت اختراع کننده و FTO) کامل است؟
2. آیا آدرس گزارش (مندانی، وکیل ثبت اختراع، دادگاه) مشخص شده است؟
3. آیا همه سه بلوک اعلامیه در گزارش وجود دارد (برنامه، روش و نتیجه گیری) ؟
4. آیا تاریخ تعیین شده تحقیق در نام فایل و گزارش به درستی مشخص می شود؟

## رویهٔ قضایی روز

> قضیه: هیچ تصمیمی را از دانش نمونه ای نقل نکنید؛ قبل از انتشار با دادگاه، شکل تصمیم گیری و تاریخ آن ها، نشانه های پرونده یا اظهارات قابل اثبات را توسط منبع رسمی یا آزاد تأیید کنید.

> قضیه: هیچ تصمیمی را از دانش نمونه ای نقل نکنید؛ قبل از انتشار با دادگاه، شکل تصمیم گیری و تاریخ آن ها، نشانه های پرونده یا اظهارات قابل اثبات را توسط منبع رسمی یا آزاد تأیید کنید.

> **DPMA، اعلامیه 2022 (رپورتی استفاده):** در رابطه با ارزیابی های ثبت اختراع و تحقیقات برای خرید نمونه کارها از IP ، DPMA انتظار دارد اطلاعات کامل درباره حقوق رقبای شناخته شده داشته باشد؛ گزارش که نقاط برخورد معروف را ذکر نکند می تواند به عنوان اطلاعاتی نامکمل و نقض واجبات حرفه ای محسوب شود.
