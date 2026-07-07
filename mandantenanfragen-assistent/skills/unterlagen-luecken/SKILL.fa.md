---
name: unterlagen-luecken
description: "Wenn es um Unterlagen und Lücken in mandantenanfragen-assistent geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# اسناد و شکاف ها

## وضعیت کاربرد

این بررسی اسناد برای **مساعد در مورد درخواست های ماموریت**، نامی از دست دادن سند ها، حقایق متنازع، خطرات اثبات و آخرین تقاضا را مشخص می کند.

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

- فهرست هدف: برای سوالات معینی از مشتریان چه اسنادی را لازم دارم؟
- مقایسه است: چه اسناد موجود هستند، کدامها از دست رفته اند؟
- این لیست را به ترتیب: فرسترلایت (که زمان های مربوطه در زمینه ی تخصصی و عملی را باید پیش از آن مشخص کنند، نه اینکه با دانش مدل ای نهایی شوند) ، ثابت کننده، شکل ساز.
- نامه های بازرسی به مشتری، مخالفان، دادگاه یا مقام مجاز و هر گونه کارشناسان یا سازمان هایی که ممکن است در اختیار داشته باشند طراحی می شود - چه کسی سند را دارد؟ از کجا می توان آن را بدست آورد؟ تا کی؟
- در مورد شکاف های دولتی: حق بررسی پرونده ها (به عنوان مثال § 29 VwVfG, § 147 StPO, § 25 SGB (X) بررسی و استفاده

## لنگر کیفیت

- قوانین و قضیه `references/quellenhygiene.md` و `references/zitierweise.md` درمان می کنند.
- وقتی یک سوال خاص ظاهر می شود، مهارت مناسب را نام دهید و به طور خلاصه توضیح بدهید که چرا این روش کار درست است.
- در صورت فشار زمان، ابتدا مهلت، صلاحیت، شکل و بار اثبات را تضمین کنید.
