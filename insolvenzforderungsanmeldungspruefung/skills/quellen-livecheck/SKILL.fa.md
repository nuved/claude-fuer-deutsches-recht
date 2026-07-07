---
name: quellen-livecheck
description: "Wenn es um Rechtsquellen-Livecheck in Insolvenzforderungsanmeldungsprüfung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# چک زنده منابع حقوقی

## وضعیت کاربرد

این چک زنده منابع برای بررسی گزارش های بی نقصی**، بیان رسمی استاندارد را از قوانین آزاد و قابل بازرسی جدا می کند.

## نقشه تخصصی این افزونه

- `aktenanlage-batchregister` - پرونده های مجموعه ی دسته بندی
- `beleg-und-urkundencheck` - مدارک و چک اسناد
- `bestreiten-interessen-betrag` - مبلغ سود متنازع
- `bestreiten-mehrparteien-konflikt-und-interessen` - با اختلافات و منافع چند طرفه
- `betrag-behoerden-gericht-und-registerweg` - مقدار مقامات دادگاه و ثبت
- `dubletten-serienforderungen` - دو عدد از مطالب سری
- `feststellung-forderungsgrund-rang-grund` - تعیین دلیل ادعای
- `forderungsanmeldung-mandantenkommunikation-redteam-qualitygate` - ثبت درخواست ارتباطات مشتری Redteam Qualitygate
- `vbuh-verhandlung-vergleich-und-eskalation` - گزارش درخواست در مورد مذاکرات مقایسه افزایش
- `forderungsgrund-rang-und-belegpruefung` - پایه ی مطالبه و بررسی مدارک
- `formalpruefung-174` - آزمون رسمی 174
- `grund-betrag-zinsen` - اصل مقدار سود
- `grund-risikoampel-und-gegenargumente` - دلیل خطر و استدلال های ضد
- `anschluss-routing` - رویتینگ اتصال
- `dokumente-intake` - اسناد دخول

## مسیر کار

- استاندارد های مربوطه (§ 174 InsO, اسناد، دلیل, مقدار, درجه, vbuH, الزامات, واردات جدول gesetze-im-internet.de یا پورتال تخصصی جرگه قانون فدرال؛ نه از دانش مدل نهایی.
- قضیه فقط با یک زنجیره کامل: دادگاه، مجلس سنا، شکل تصمیم گیری، تاریخ و اسناد پرونده ها، محل یافت (BGHZ/BVerfGE /amtl.dejure.org، openJur، خبرگزاری های دادگاه BGH-/BVerfG-دابیس).
- از منابع Paywall (جوری، بیک آنلاین) به عنوان تنها تایید استفاده نکنید؛ همیشه یک تأیید آزاد را ارائه دهید.
- بخش های پویا در بررسی گزارشات ورشکستگی (قانونی، قانونی، مالیاتی، نرخ اجاره) را به طور جداگانه روزانه بررسي کنید زیرا دانش مدل ها از دست رفته است.
- به صورت منبع و عدم اطمینان در محصول نشان می دهد - هیچ نقل قول جعلی بدون بررسی زنده.

## لنگر کیفیت

- قوانین و قضیه `references/quellenhygiene.md` و `references/zitierweise.md` درمان می کنند.
- وقتی یک سوال خاص ظاهر می شود، مهارت مناسب را نام دهید و به طور خلاصه توضیح بدهید که چرا این روش کار درست است.
- در صورت فشار زمان، ابتدا مهلت، صلاحیت، شکل و بار اثبات را تضمین کنید.
