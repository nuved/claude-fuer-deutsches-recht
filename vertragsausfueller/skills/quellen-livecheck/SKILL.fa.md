---
name: quellen-livecheck
description: "Wenn es um Rechtsquellen-Livecheck in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# چک زنده منابع حقوقی

## وضعیت کاربرد

این چک زنده منابع برای **موفقین قرارداد**، از نسخه های رسمی استاندارد، قانونی که می تواند به طور آزاد بررسی شود، اطلاعات دولتی، سطح فرم و خطرات آشکار بروزرسانی جدا میکند.

## نقشه تخصصی این افزونه

- `altvertraege-dokumentenmatrix-und-lueckenliste` - قرارداد های قدیمی متریک اسناد و لیست خالی
- `altvertrag-nachziehen` - از قرارداد گذشته باز پس
- `ausdruecklicher-fristennotiz-und-naechster-schritt` - نوتیفکیشن صریح و مرحله بعدی
- `batch-modus-docx-stripper-einfuehrung` - راه اندازی حالت Batch Docx Stripper
- `bsag-mietvertrag-klauselentscheidung` - قرارداد اجاره
- `changes-beweislast-docx-erkennen` - تغییر بار اثبات
- `clean-output` - محصول پاک
- `docx-stripper` -داکس استریپر
- `docx-tatbestand-beweis-und-belege` - اسناد و مدارک
- `einfuehrung-prozess` - آغاز پروسه
- `erkennen-schriftsatz-brief-und-memo-bausteine` - شناسایی نامه و یادداشت ساختمان
- `erzeugen-red-fassungen-sonderfall-felder` - تولید نسخه های قرمز
- `fassungen-sonderfall-und-edge-case` - نسخه های مورد خاص و Edge Case
- `anschluss-routing` - رویتینگ اتصال
- `dokumente-intake` - اسناد دخول

## مسیر کار

- استاندارد های مربوطه (BGB §§ 133(۱۵۷، ۳۰۵-۳۱۰، ۳۱۱ ب، ۳١۱c، ۴۳۳،۴۸۸، ۵۳۵، ۶۳۱،۶۵۱a، ۷۶۵ قانون و مقررات عمومی) gesetze-im-internet.de یا پورتال تخصصی جرگه قانون فدرال؛ نه از دانش مدل نهایی.
- قضیه فقط با یک زنجیره کامل: دادگاه، مجلس سنا، شکل تصمیم گیری، تاریخ و اسناد پرونده ها، محل یافت (BGHZ/BVerfGE /amtl.dejure.org، openJur، خبرگزاری های دادگاه BGH-/BVerfG-دابیس).
- از منابع Paywall (جوری، بیک آنلاین) به عنوان تنها تایید استفاده نکنید؛ همیشه یک تأیید آزاد را ارائه دهید.
- بخش های پویا در تکمیل قرارداد (تغییرات قراردادی) (قانونی، شیوه ی اداری، سطح اجاره و تعرفه ها) را به طور جداگانه روزانه بررسی کنید زیرا دانش مدل از دست رفته است.
- به صورت منبع و عدم اطمینان در محصول نشان می دهد - هیچ نقل قول جعلی بدون بررسی زنده.

## لنگر کیفیت

- قوانین و قضیه `references/quellenhygiene.md` و `references/zitierweise.md` درمان می کنند.
- وقتی یک سوال خاص ظاهر می شود، مهارت مناسب را نام دهید و به طور خلاصه توضیح بدهید که چرا این روش کار درست است.
- در صورت فشار زمان، ابتدا مهلت، صلاحیت، شکل و بار اثبات را تضمین کنید.
