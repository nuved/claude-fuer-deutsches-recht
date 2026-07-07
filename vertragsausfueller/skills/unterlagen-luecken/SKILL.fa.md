---
name: unterlagen-luecken
description: "Wenn es um Unterlagen und Lücken in Vertragsausfüller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# اسناد و شکاف ها

## وضعیت کاربرد

این بررسی اسناد برای **موفقین قرارداد**، نامی از دست دادن سند ها، حقایق متنازع، خطرات اثبات و آخرین درخواست مطمئن را مشخص می کند.

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

- فهرست بندی: برای تکمیل قرارداد های خاص (مطابق توافق، جدول زمان، کالوگ بند، پیمان قدیمی، طرح تغییرات) چه اسنادی لازم است؟
- مقایسه است: چه اسناد موجود هستند، کدامها از دست رفته اند؟
- این لیست را به ترتیب: فریسترلایت (به لحاظ قرارداد) اولویت بندی کنید. § 195 BGB 3 سال سن قانونی § 14 BGB- اطلاعات 14 روز) ، قابل اثبات، با توجه به زمان.
- طرح نامه های بازرسی به مشتری، شرکای قرارداد، بخش حقوقی و نوتر در صورت نیاز - چه کسی سند را دارد؟ از کجا می توان آن را دریافت کرد؟ تا کی؟
- در مورد شکاف های دولتی: حق بررسی پرونده ها (به عنوان مثال § 29 VwVfG, § 147 StPO, § 25 SGB (X) بررسی و استفاده

## لنگر کیفیت

- قوانین و قضیه `references/quellenhygiene.md` و `references/zitierweise.md` درمان می کنند.
- وقتی یک سوال خاص ظاهر می شود، مهارت مناسب را نام دهید و به طور خلاصه توضیح بدهید که چرا این روش کار درست است.
- در صورت فشار زمان، ابتدا مهلت، صلاحیت، شکل و بار اثبات را تضمین کنید.
