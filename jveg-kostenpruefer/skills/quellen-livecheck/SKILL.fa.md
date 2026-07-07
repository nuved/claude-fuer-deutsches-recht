---
name: quellen-livecheck
description: "Wenn es um Rechtsquellen-Livecheck in JVEG-Kostenprüfer geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# چک زنده منابع حقوقی

## وضعیت کاربرد

این چک زنده منابع برای معاینه گران **Jveg هزینه**، از نسخه رسمی استاندارد، قانونی که می تواند به طور آزاد بررسی شود، اطلاعات دولتی، سطح فرم و خطرات آشکار بروز رسانی جدا میکند.

## نقشه تخصصی این افزونه

- `aktenstripper` - کارنامه ی کلاهبردار
- `anspruchsberechtigung-antragsgenerator` - قابلیت درخواست ژنراتور
- `antragsgenerator` - ژنراتور درخواست
- `belegfeste-formular-portal-und-einreichung` - پورتال و ارسال فرم ثابت
- `beschwerde-dolmetscher-sonderfall` - شکایت مترجم
- `dolmetscher-sonderfall-und-edge-case` - تفسیر قضیه ویژه و Edge Case
- `dolmetscher-uebersetzer` - مترجم
- `dolmetscher-uebersetzer-fahrtkosten` - مترجم و ترجمه کننده هزینه سفر
- `dolmetscherkosten-zahlen-schwellen-und-berechnung` - هزینه های مترجم، اعداد و تراشه ها
- `fahrtkosten` - هزینه سفر
- `fahrtkosten-festsetzung-interessen` - هزینه سفر تعیین منافع
- `festsetzung-beschwerde` - ثبت شکایت
- `festsetzung-mehrparteien-konflikt-und-interessen` - تعیین چند طرفه ای درگیری و منافع
- `anschluss-routing` - رویتینگ اتصال
- `dokumente-intake` - اسناد دخول

## مسیر کار

- استاندارد های مربوطه (JVEG) اول از همه تایید رسمی: gesetze-im-internet.de یا پورتال تخصصی جرگه قانون فدرال؛ نه از دانش مدل نهایی.
- قضیه فقط با یک زنجیره کامل: دادگاه، مجلس سنا، شکل تصمیم گیری، تاریخ و اسناد پرونده ها، محل یافت (BGHZ/BVerfGE /amtl.dejure.org، openJur، خبرگزاری های دادگاه BGH-/BVerfG-دابیس).
- از منابع Paywall (جوری، بیک آنلاین) به عنوان تنها تایید استفاده نکنید؛ همیشه یک تأیید آزاد را ارائه دهید.
- بخش های پویا در جگ از معاینه گران هزینه (قانونی، عملیات اداری، نرخ اجاره ها و تعرفه) را به طور جداگانه روزانه بررسی می کنند زیرا دانش مدل سازی قدیمی شده است.
- به صورت منبع و عدم اطمینان در محصول نشان می دهد - هیچ نقل قول جعلی بدون بررسی زنده.

## لنگر کیفیت

- قوانین و قضیه `references/quellenhygiene.md` و `references/zitierweise.md` درمان می کنند.
- وقتی یک سوال خاص ظاهر می شود، مهارت مناسب را نام دهید و به طور خلاصه توضیح بدهید که چرا این روش کار درست است.
- در صورت فشار زمان، ابتدا مهلت، صلاحیت، شکل و بار اثبات را تضمین کنید.
