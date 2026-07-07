---
name: output-waehlen
description: "Wenn es um Output wählen in Immobilienrechtspraxis geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# انتخاب محصول

## وضعیت کاربرد

این هفته های خروجی برای **عملیات حقوقی املاک** تعیین می کند که آیا یادداشت، درخواست، اسناد، جدول، چراغ خطر، لیست پرسش یا نامه مشتری قدم بعدی مناسب است.

## نقشه تخصصی این افزونه

- `betriebskostenabrechnung-erstellen-asset-management` - حساب هزینه های عملیاتی ایجاد مدیریت دارایی
- `betriebskostenabrechnung-pruefen-asset-management` - حسابداري هزینه های عملیاتی بررسی مدیریت دارایی
- `case-gegen-grundbuchanalyse` - پرونده مقابل تحلیل کتاب اساسی
- `case-management-grundbuchanalyse-immo` - مدیریت پرونده های اساسی
- `gegen-verhandlung-vergleich-und-eskalation` - در مقابل مذاکره مقایسه و افزایش
- `grundbuchanalyse` - تحلیل کتاب های اساسی
- `grundbuchanalyse-zahlen-schwellen-und-berechnung` - تحلیل کتابی اساسی، اعداد تله و محاسبه
- `immo-aufteilungsplan-weg` - برنامه تقسیم بندی IMMO WEG
- `immo-bauliche-veraenderung-energieausweis` - تغییر ساختمانی گواهی انرژی
- `immo-bauvertrag-vob-kaufvertrag-grundstueck` - قرارداد ساخت و ساز VOB قرارداد خرید زمین
- `immo-energieausweis` - گواهی انرژی
- `immo-gewerbliche-mieter-konkurs` - شرکت های تجاری در حال ورشکستگی
- `immo-grundschuld-bestellung-makler-honorar` - Immo بدهی اصلی سفارش دلال هزینه
- `anschluss-routing` - رویتینگ اتصال
- `dokumente-intake` - اسناد دخول

## مسیر کار

- نوع نتیجه را تعیین کنید: نامه ای به مشتری، مخالفان، دادگاه یا مقام مجاز، هر گونه کارشناسان و مقامات ممکن است باشد، یادداشت مشتریان، گزارش ریسک، طرح قرارداد، قالب تصمیم گیری، تصریحات دولتی - چه چیزی واقعاً برای مشتری نیاز دارد؟
- تعیین فرمت های لازم: Tenor / درخواست / دلیل (دستگاه ادعای، پرونده اعمال ، زیر نظر، نتیجه) ؛ نقاط مشخصی از استاندارد در شیوه قوانین املاک و مستغلات gesetze-im-internet.de و dejure.org در این زمینه، باید بررسی شود.
- وضوح مخاطب: زبان، عمق جزئیات و پیشگیری قانونی را در نظر بگیرید؛ برای مشتری بدون آموزش کامل خلاصه ی متن واضح ارائه دهید.
- برنامه های ساخت و ساز (تاریخی، موضوعی، K- و B-پلان) ؛ اشاره ها را به صورت تمیز نشان دهید.
- نوتیزه های منبع و به صورت نقل قولی را تضمین کنید؛ نقاط باز و فرضیه ها را بطور صریح چنین نشان دهید.

## لنگر کیفیت

- قوانین و قضیه `references/quellenhygiene.md` و `references/zitierweise.md` درمان می کنند.
- وقتی یک سوال خاص ظاهر می شود، مهارت مناسب را نام دهید و به طور خلاصه توضیح بدهید که چرا این روش کار درست است.
- در صورت فشار زمان، ابتدا مهلت، صلاحیت، شکل و بار اثبات را تضمین کنید.
