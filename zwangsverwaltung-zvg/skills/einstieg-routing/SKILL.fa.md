---
name: einstieg-routing
description: "Wenn es um Einstieg und Routing in ZVG-Zwangsverwaltung - Verwalter-Cockpit geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# ورود و رویتینگ

## وضعیت کاربرد

این راه اندازی **ادارۀ اجباری Zvg** را از واقعیت اول به نقش، زمان بندی ها، مقام کاربری، مسیر تخصصی مناسب و محصول بعدی کاری هدایت می کند.

## نقشه تخصصی این افزونه

- `aktenanlage-objektcockpit` - فایل های زیرنویس، کابین اشیاء
- `berichte-beschlagnahme-mietverwaltung-besitz` - گزارش های ضبط اداری اجاره مالکیت
- `berichtswesen-besitzuebernahme-bestellung` - گزارشگری، مالکیت
- `beschlagnahme-fristen-form-und-zustaendigkeit` - زمان های ضبط شکل و صلاحیت
- `beschlagnahme-mietverwaltung-start` - ضبط اداری اجاره شروع
- `beschlagnahme-oeffentliche-lasten` - دستگیری بارهای غیرفعال
- `besitz-dokumentenmatrix-und-lueckenliste` - مالکیت ماتریک اسناد و لیست خالی
- `besitzuebernahme` - انتقال مالکیت
- `bestellung-beschlagnahme` - دستور گرفتن
- `betriebskosten-hausgeld-bieterangebot` - هزینه های عملیاتی پول مسکن پیشنهاد داوطلب
- `bieterangebot-bewertung` - ارزیابی پیشنهادات داوطلبان
- `bieterangebote-mieten-oeffentliche` - پیشنهادات اجاره غیر واقعی
- `gate-fehlerkatalog` - فهرست خطای Gate
- `anschluss-routing` - رویتینگ اتصال
- `dokumente-intake` - اسناد دخول

## مسیر کار

- نقش و هدف را مشخص کنید: کدام طرف توسط متقاضی نمایندگی می شود، چه نوع نتیجه ای مورد استفاده قرار گیرد (پشت نامه ، بررسی اطلاعیه ، طرح قرارداد ، نظر) که چگونه عمل یا سند وجود دارد؟
- مهلت های تعویض شده: که به صورت واجبتی از قبل مهلتهای مربوطه در زمینه ی تخصصی و عملی را مشخص می کنند، نه اینکه با دانش مدل ای نهایی شوند.
- انتخاب حرفه: لنگرهای اصلی در مدیریت اجباری Zvg ZVG هستند. بر اساس واقعیت به یک کلستر تخصصی راه می رود و مهارت های ویژه مناسب را از نقشه منطقه ی کار فوق نام می دهد.
- مقام اختصاصی: متقاضی، مخالفان، دادگاه یا اداره مجاز و هرگاه که این موضوع را مطرح کنند.
- فقط این سوال ها را بپرسید که واقعاً مسیر بعدی رو تغییر می دهد.

## لنگر کیفیت

- قوانین و قضیه `references/quellenhygiene.md` و `references/zitierweise.md` درمان می کنند.
- وقتی یک سوال خاص ظاهر می شود، مهارت مناسب را نام دهید و به طور خلاصه توضیح بدهید که چرا این روش کار درست است.
- در صورت فشار زمان، ابتدا مهلت، صلاحیت، شکل و بار اثبات را تضمین کنید.
