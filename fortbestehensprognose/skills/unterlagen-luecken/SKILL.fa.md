---
name: unterlagen-luecken
description: "Wenn es um Unterlagen und Lücken in Fortbestehensprognose geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# اسناد و شکاف ها

## وضعیت کاربرد

این بررسی اسناد پیش بینی **موقع وجود**، نامی از دست دادن سند ها، حقایق متنازع، خطرات اثبات و آخرین درخواست مطمئن را مشخص می کند.

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

- فهرست هدف: برای پرسش های پیش بینی زنده ماندن واقعی چه اسنادی لازم است (مصارف قرارداد، پرونده ها، سوابق اداری، پروتکلها، تصمیمات و شواهد خارجی مربوط به حوزه تخصص) ؟
- مقایسه است: چه اسناد موجود هستند، کدامها از دست رفته اند؟
- این لیست را به ترتیب: فرسترلایت (که زمان های مربوطه در زمینه ی تخصصی و عملی را باید پیش از آن مشخص کنند، نه اینکه با دانش مدل ای نهایی شوند) ، ثابت کننده، شکل ساز.
- نامه های بازرسی به مشتری، مخالفان، دادگاه یا مقام مجاز و هر گونه کارشناسان یا سازمان هایی که ممکن است در اختیار داشته باشند طراحی می شود - چه کسی سند را دارد؟ از کجا می توان آن را بدست آورد؟ تا کی؟
- در مورد شکاف های دولتی: حق بررسی پرونده ها (به عنوان مثال § 29 VwVfG, § 147 StPO, § 25 SGB (X) بررسی و استفاده

## لنگر کیفیت

- قوانین و قضیه `references/quellenhygiene.md` و `references/zitierweise.md` درمان می کنند.
- وقتی یک سوال خاص ظاهر می شود، مهارت مناسب را نام دهید و به طور خلاصه توضیح بدهید که چرا این روش کار درست است.
- در صورت فشار زمان، ابتدا مهلت، صلاحیت، شکل و بار اثبات را تضمین کنید.
