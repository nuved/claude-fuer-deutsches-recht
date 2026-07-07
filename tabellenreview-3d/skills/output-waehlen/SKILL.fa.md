---
name: output-waehlen
description: "Wenn es um Output wählen in Tabellenreview 3D geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# انتخاب محصول

## وضعیت کاربرد

این هفته های خروجی برای **Tabletreview 3d** تعیین می کند که آیا یادداشت، درخواست، اسناد، جدول، چراغ خطر، لیست سوالات یا نامه مشتری قدم بعدی مناسب است.

## نقشه تخصصی این افزونه

- `aggregation-spaltenprompts-definieren` - جمع بندی تعویض پرامپت
- `arbeitsblatt-perspektiven-definieren` - تعریف چشم انداز
- `arbeitsblatt-schriftsatz-brief-memo-bausteine` - ورق کاری نامه خط یادداشت ساختمان
- `arbeitsblatt-schriftsatz-brief-und-memo-bausteine` - ورق کاری نامه و یادداشت ساختمان
- `audit-trail-protokoll` - پروتکل آدیتی ترول
- `belegkette-rueckverfolgung` - تعقیب ثابت
- `belegkette-rueckverfolgung-caching-rerun` - ردیابی زنجیره ای
- `caching-und-teil-rerun` - کیشینگ و بخش ریرن
- `chronologie-und-belegmatrix` - زمان شناسی و ماتریس مدارک
- `datenpunkt-dokument-excel-beweislast` - داتا نقطه سند اکسل بار اثبات
- `datenpunkt-dokumentenmatrix-lueckenliste` - نقطه داده ها متریک اسناد
- `dokument-behoerden-gericht-und-registerweg` - سند مقامات دادگاه و ثبت
- `dokumentstapel-aufnehmen` - ثبت اسناد
- `anschluss-routing` - رویتینگ اتصال
- `dokumente-intake` - اسناد دخول

## مسیر کار

- نوع نتیجه را تعیین کنید: نامه ای به مشتری، مخالفان، دادگاه یا مقام مجاز، هر گونه کارشناسان و مقامات ممکن است باشد، یادداشت مشتریان، گزارش ریسک، طرح قرارداد، قالب تصمیم گیری، تصریحات دولتی - چه چیزی واقعاً برای مشتری نیاز دارد؟
- فرمت های لازم را تعیین کنید: Tenor / درخواست / دلیل (دلیل ادعای، پروندهٔ اعمال ، زیر نظر و نتیجه) ؛ نقاط مشخصی استاندارد در جدول بررسی 3D gesetze-im-internet.de و dejure.org در این زمینه، باید بررسی شود.
- وضوح مخاطب: زبان، عمق جزئیات و پیشگیری قانونی را در نظر بگیرید؛ برای مشتری بدون آموزش کامل خلاصه ی متن واضح ارائه دهید.
- برنامه های ساخت و ساز (تاریخی، موضوعی، K- و B-پلان) ؛ اشاره ها را به صورت تمیز نشان دهید.
- نوتیزه های منبع و به صورت نقل قولی را تضمین کنید؛ نقاط باز و فرضیه ها را بطور صریح چنین نشان دهید.

## لنگر کیفیت

- قوانین و قضیه `references/quellenhygiene.md` و `references/zitierweise.md` درمان می کنند.
- وقتی یک سوال خاص ظاهر می شود، مهارت مناسب را نام دهید و به طور خلاصه توضیح بدهید که چرا این روش کار درست است.
- در صورت فشار زمان، ابتدا مهلت، صلاحیت، شکل و بار اثبات را تضمین کنید.
