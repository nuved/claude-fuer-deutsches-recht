---
name: output-waehlen
description: "Wenn es um Output wählen in Geldwäscheprävention, AML und KYC geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# انتخاب محصول

## وضعیت کاربرد

این هفته ی خروجی برای **مصرفی های نقدینگی Aml Kyc** تعیین می کند که آیا یادداشت، درخواست، خط نامه، جدول، پرچم خطر، لیست سوالات یا نام مشتری قدم بعدی مناسب است.

## نقشه تخصصی این افزونه

- `aml-kryptotransaktionen-mica-spezial` - ام ال کریپتو تراکنش های Mica خاص
- `aml-kyc-start-chronologie-fristen` - AML KYC شروع زمان بندی
- `aml-trade-based-money-laundering-spezial` - امل تجارت مبتنی بر پولشویی تخصصی
- `aml-verdachtsmeldung-fiu-leitfaden` - AML گزارش شکافی FIU راهنما
- `awareness-zahlen-schwellen-und-berechnung` - آگاهی ارقام تله ها و محاسبه
- `behoerdenverfahren-schriftsatz-brief-und-memo-bausteine` - اداریات و اسناد نامه
- `geldwaesche-audit-internal-datenqualitaet` -آدیت پول نقدی داخلی کیفیت داده
- `geldwaesche-behoerdenverfahren` - روش های دولتی در مورد پول نقد
- `geldwaesche-bussgeld-reputation` - شهرت پول نقدی
- `geldwaesche-datenqualitaet-register` - ثبت کیفیت داده های پول نقد
- `geldwaesche-gruppenweite-compliance` - مبلغی و اجتماعی
- `geldwaesche-immobilien-gueterhaendler` - املاک و مستغلات پول نقدی
- `geldwaesche-krypto-zahlungsdienstleister` - ارائه دهندگان خدمات پرداخت رمزنگاری شده پول
- `anschluss-routing` - رویتینگ اتصال
- `dokumente-intake` - اسناد دخول

## مسیر کار

- نوع نتیجه را تعیین کنید: نامه ای به مشتری، مخالفان، دادگاه یا مقام مجاز، هر گونه کارشناسان و مقامات ممکن است باشد، یادداشت مشتریان، گزارش ریسک، طرح قرارداد، قالب تصمیم گیری، تصریحات دولتی - چه چیزی واقعاً برای مشتری نیاز دارد؟
- تعیین فرمت های لازم: Tenor / درخواست / دلیل (دلیل ادعای، پرونده اعمال ، زیر نظر و نتیجه)GwG) را در نظر بگیرید.
- وضوح مخاطب: زبان، عمق جزئیات و پیشگیری قانونی را در نظر بگیرید؛ برای مشتری بدون آموزش کامل خلاصه ی متن واضح ارائه دهید.
- برنامه های ساخت و ساز (تاریخی، موضوعی، K- و B-پلان) ؛ اشاره ها را به صورت تمیز نشان دهید.
- نوتیزه های منبع و به صورت نقل قولی را تضمین کنید؛ نقاط باز و فرضیه ها را بطور صریح چنین نشان دهید.

## لنگر کیفیت

- قوانین و قضیه `references/quellenhygiene.md` و `references/zitierweise.md` درمان می کنند.
- وقتی یک سوال خاص ظاهر می شود، مهارت مناسب را نام دهید و به طور خلاصه توضیح بدهید که چرا این روش کار درست است.
- در صورت فشار زمان، ابتدا مهلت، صلاحیت، شکل و بار اثبات را تضمین کنید.
