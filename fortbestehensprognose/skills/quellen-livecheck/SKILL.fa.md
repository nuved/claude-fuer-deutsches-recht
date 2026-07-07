---
name: quellen-livecheck
description: "Wenn es um Rechtsquellen-Livecheck in Fortbestehensprognose geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# چک زنده منابع حقوقی

## وضعیت کاربرد

این بررسی زنده منابع پیش بینی **موقعیت**، از استاندارد رسمی، قانونی که می تواند به طور آزاد مورد آزمایش قرار گیرد، اطلاعات دولتی، وضعیت فرم و خطرات باز بروز جدا میکند.

## نقشه تخصصی این افزونه

- `annahmen-behoerden-gericht-und-registerweg` - فرضیه های مقامات دادگاه و ثبت
- `annahmen-belastbarkeit-plausibilisieren` - فرضیه های تحمل پذیری
- `annahmen-sammeln-bilanzieller-status` - فرضیه جمع آوری وضعیت مالی
- `ausloesendes-ereignis-erfassen` - شناسایی رویداد آغاز کننده
- `bilanzieller-status-aufnehmen` - ثبت وضعیت مالی
- `bilanzstatus-risikoampel-und-gegenargumente` - وضعیت مالی، نشانه های ریسک و استدلال مقابل
- `comfortletter-sonderfall-edge` - Comfortletter حالت ویژه Edge
- `comfortletter-weich-erzeugen` - نرم تولید
- `eskalation-sonderfall-und-edge-case` - اسکالاسي مورد خاص و قضيه کناره
- `fbp-bankenkommunikation-waiver-integrierte` - FBP ارتباطات بانکی معافیت متمایز
- `fbp-integrierte-planung-bauleiter` - FBP برنامه ریزی متمایز سازنده
- `fbp-stresstest-szenarien-leitfaden` - راهنمای سناریوهای تست استرس FBP
- `fbp-zahlungsunfaehigkeit` - بی کفایتی FBP
- `anschluss-routing` - رویتینگ اتصال
- `dokumente-intake` - اسناد دخول

## مسیر کار

- استاندارد های مربوطه (InsO, StaRUG, § 19 (ب) اول، تایید رسمی: gesetze-im-internet.de یا پورتال تخصصی جرگه قانون فدرال؛ نه از دانش مدل نهایی.
- قضیه فقط با یک زنجیره کامل: دادگاه، مجلس سنا، شکل تصمیم گیری، تاریخ و اسناد پرونده ها، محل یافت (BGHZ/BVerfGE /amtl.dejure.org، openJur، خبرگزاری های دادگاه BGH-/BVerfG-دابیس).
- از منابع Paywall (جوری، بیک آنلاین) به عنوان تنها تایید استفاده نکنید؛ همیشه یک تأیید آزاد را ارائه دهید.
- حوزه های پویا در پیش بینی بقای (قانونی، عملیات اداری، نرخ اجاره ها و تعرفه) را به طور جداگانه روزانه بررسی کنید زیرا دانش مدل از دست رفته است.
- به صورت منبع و عدم اطمینان در محصول نشان می دهد - هیچ نقل قول جعلی بدون بررسی زنده.

## لنگر کیفیت

- قوانین و قضیه `references/quellenhygiene.md` و `references/zitierweise.md` درمان می کنند.
- وقتی یک سوال خاص ظاهر می شود، مهارت مناسب را نام دهید و به طور خلاصه توضیح بدهید که چرا این روش کار درست است.
- در صورت فشار زمان، ابتدا مهلت، صلاحیت، شکل و بار اثبات را تضمین کنید.
