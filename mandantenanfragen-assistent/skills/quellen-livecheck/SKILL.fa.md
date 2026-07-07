---
name: quellen-livecheck
description: "Wenn es um Rechtsquellen-Livecheck in mandantenanfragen-assistent geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# چک زنده منابع حقوقی

## وضعیت کاربرد

این منبع زنده برای **مساعد در مورد سوالات مهارتی**، استاندارد رسمی را از قوانین آزاد و قابل بررسی جدا می کند. اطلاعات دولتی، سطح فرم ها و خطرات باز به روز است.

## نقشه تخصصی این افزونه

- `anfrage-eingang-parser` - سوال دروازه پارسر
- `anrede-anwaltskanzleien-bittet` - به شرکت های حقوقی مراجعه کنید
- `anrede-uebernehmen` - از صحبت کردن استفاده کنید
- `anwaltskanzleien-erstpruefung-und-mandatsziel` - ادارات حقوقی اولین بررسی و هدف مأموریت
- `bietet-fehlerkatalog` - فهرست خطا ها را ارائه می دهد
- `bittet-internationaler-bezug-und-schnittstellen` - درخواست ارتباط بین المللی و رابط
- `dankt-dsgvo-sonderfall-e-mail` - ممنون DSGVO موارد ویژه ایمیل
- `dringlichkeitsmarker-einwilligung-hinweis` - نشانه های اضطراری اجازه دادن
- `dsgvo-sonderfall-und-edge-case` — DSGVO پرونده ویژه و مورد کناری
- `e-mail-erstantwort-und-terminrouting` - ایمیل کلمه ی اول و رویتینگ قرار ملاقات
- `eingehenden-quellenkarte` - کارت منبع ورودی
- `einwilligung-hinweis-datenschutz` - موافقت اطلاعیه حفاظت از اطلاعات
- `einwilligungshinweis-fristennotiz-und-naechster-schritt` - گواهی رضایت، یادداشت زمان و مرحله بعدی
- `anschluss-routing` - رویتینگ اتصال
- `dokumente-intake` - اسناد دخول

## مسیر کار

- استاندارد های مربوطه (DSGVO) اول از همه تایید رسمی: gesetze-im-internet.de یا پورتال تخصصی جرگه قانون فدرال؛ نه از دانش مدل نهایی.
- قضیه فقط با یک زنجیره کامل: دادگاه، مجلس سنا، شکل تصمیم گیری، تاریخ و اسناد پرونده ها، محل یافت (BGHZ/BVerfGE /amtl.dejure.org، openJur، خبرگزاری های دادگاه BGH-/BVerfG-دابیس).
- از منابع Paywall (جوری، بیک آنلاین) به عنوان تنها تایید استفاده نکنید؛ همیشه یک تأیید آزاد را ارائه دهید.
- بخش های پویا در مورد سوالاتی که به مشتریان می رسد دستیار (قانونی، عملیات اداری، نرخ اجاره ها و تعرفه) را هر روز از طریق جداگانه بررسی کنید زیرا دانش مدل قدیمی است.
- به صورت منبع و عدم اطمینان در محصول نشان می دهد - هیچ نقل قول جعلی بدون بررسی زنده.

## لنگر کیفیت

- قوانین و قضیه `references/quellenhygiene.md` و `references/zitierweise.md` درمان می کنند.
- وقتی یک سوال خاص ظاهر می شود، مهارت مناسب را نام دهید و به طور خلاصه توضیح بدهید که چرا این روش کار درست است.
- در صورت فشار زمان، ابتدا مهلت، صلاحیت، شکل و بار اثبات را تضمین کنید.
