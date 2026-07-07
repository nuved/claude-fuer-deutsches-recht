---
name: quellen-livecheck
description: "Wenn es um Rechtsquellen-Livecheck in ZVG-Zwangsverwaltung - Verwalter-Cockpit geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# چک زنده منابع حقوقی

## وضعیت کاربرد

این منبع زنده برای مدیریت مجبوری Zvg**، از نسخه های رسمی استاندارد، قانونی که می تواند به طور آزاد بررسی شود، اطلاعات دولتی، سطح فرم و خطرات آشکار بروزرسانی جدا میکند.

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

- اول، استاندارد های کاربردی (SNV) را تایید کنند: gesetze-im-internet.de یا پورتال تخصصی جرگه قانون فدرال؛ نه از دانش مدل نهایی.
- قضیه فقط با یک زنجیره کامل: دادگاه، مجلس سنا، شکل تصمیم گیری، تاریخ و اسناد پرونده ها، محل یافت (BGHZ/BVerfGE /amtl.dejure.org، openJur، خبرگزاری های دادگاه BGH-/BVerfG-دابیس).
- از منابع Paywall (جوری، بیک آنلاین) به عنوان تنها تایید استفاده نکنید؛ همیشه یک تأیید آزاد را ارائه دهید.
- حوزه های پویا در مدیریت اجباری Zvg (قانونی، عمل اداری، میزان کرایه و تعرفه) را به طور جداگانه روزانه بررسی می کنند زیرا دانش مدل ها قدیمی شده است.
- به صورت منبع و عدم اطمینان در محصول نشان می دهد - هیچ نقل قول جعلی بدون بررسی زنده.

## لنگر کیفیت

- قوانین و قضیه `references/quellenhygiene.md` و `references/zitierweise.md` درمان می کنند.
- وقتی یک سوال خاص ظاهر می شود، مهارت مناسب را نام دهید و به طور خلاصه توضیح بدهید که چرا این روش کار درست است.
- در صورت فشار زمان، ابتدا مهلت، صلاحیت، شکل و بار اثبات را تضمین کنید.
