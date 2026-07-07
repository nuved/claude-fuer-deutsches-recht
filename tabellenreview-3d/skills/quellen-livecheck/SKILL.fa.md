---
name: quellen-livecheck
description: "Wenn es um Rechtsquellen-Livecheck in Tabellenreview 3D geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# چک زنده منابع حقوقی

## وضعیت کاربرد

این بررسی زنده منابع برای **تابل ریویو 3d**، از نسخه های رسمی استاندارد، قانونی که می تواند به طور آزاد مورد آزمایش قرار گیرد، اطلاعات دولتی، سطح فرم و خطرات باز بروز جدا میکند.

## نقشه تخصصی این افزونه

- `aggregation-spaltenprompts-definieren` - جمع بندی تعویض پرامپت
- `arbeitsblatt-perspektiven-definieren` - تعریف چشم انداز
- `arbeitsblatt-schriftsatz-brief-memo-bausteine` - ورق کاری نامه خط یادداشت ساختمان
- `arbeitsblatt-schriftsatz-brief-und-memo-bausteine` - ورق کاری نامه و یادداشت ساختمان
- `audit-trail-protokoll` - پروتکل آدیتی ترول
- `belegkette-rueckverfolgung` - تعقیب ثابت
- `belegkette-rueckverfolgung-caching-rerun` - ردیابی زنجیره ای
- `caching-und-teil-rerun` - کیشینگ و بخش ریرن
- `chronologie-und-belegmatrix` - زمان شناسی و ماتریس مدارک
- `datenpunkt-dokument-excel-beweislast` - داتا نقطه سند اکسل بار اثبات
- `datenpunkt-dokumentenmatrix-lueckenliste` - نقطه داده ها متریک اسناد
- `dokument-behoerden-gericht-und-registerweg` - سند مقامات دادگاه و ثبت
- `dokumentstapel-aufnehmen` - ثبت اسناد
- `anschluss-routing` - رویتینگ اتصال
- `dokumente-intake` - اسناد دخول

## مسیر کار

- استاندارد های مربوط به این رشته را در ادامه بخوانید gesetze-im-internet.de و dejure.org اول از همه، تایید رسمی: gesetze-im-internet.de یا پورتال تخصصی جرگه قانون فدرال؛ نه از دانش مدل نهایی.
- قضیه فقط با یک زنجیره کامل: دادگاه، مجلس سنا، شکل تصمیم گیری، تاریخ و اسناد پرونده ها، محل یافت (BGHZ/BVerfGE /amtl.dejure.org، openJur، خبرگزاری های دادگاه BGH-/BVerfG-دابیس).
- از منابع Paywall (جوری، بیک آنلاین) به عنوان تنها تایید استفاده نکنید؛ همیشه یک تأیید آزاد را ارائه دهید.
- بخش های پویا در بررسی جدول 3D (قانونی، عملیات اداری، نرخ اجاره ها و تعرفه) را به طور جداگانه روزانه بررسي کنید زیرا دانش مدل سازی از زمان گذشته است.
- به صورت منبع و عدم اطمینان در محصول نشان می دهد - هیچ نقل قول جعلی بدون بررسی زنده.

## لنگر کیفیت

- قوانین و قضیه `references/quellenhygiene.md` و `references/zitierweise.md` درمان می کنند.
- وقتی یک سوال خاص ظاهر می شود، مهارت مناسب را نام دهید و به طور خلاصه توضیح بدهید که چرا این روش کار درست است.
- در صورت فشار زمان، ابتدا مهلت، صلاحیت، شکل و بار اثبات را تضمین کنید.
