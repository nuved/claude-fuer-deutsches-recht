---
name: output-waehlen
description: "Wenn es um Output wählen in Aktenaufbereiter Strafrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# انتخاب محصول

## وضعیت کاربرد

این هفته ی محصول برای **قانون کیفری در مورد پرونده ها** تعیین می کند که آیا یادداشت، درخواست، اسناد، جدول، چراغ خطر، لیست سوالات یا نامه مشتری قدم بعدی مناسب است.

## نقشه تخصصی این افزونه

- `aktenaufbereiter-erstpruefung-und-mandatsziel` - تهیه کننده پرونده، اولین بررسی و هدف مأموریت
- `aktenaufbereiter-strafrecht` - قانون کیفری در پرونده
- `akteneinsicht-uebersicht-aktenvorblatt` - نظر پرونده ها بررسي نمايش نامه
- `aktenlektuere-fristennotiz-und-naechster-schritt` - مطالعه پرونده ها، یادداشت زمان و مرحله بعدی
- `aktenvorblatt-erstellen` - ساخت پیش بینی پرونده
- `aktenvorblatt-schriftsatz-brief-und-memo-bausteine` - پیش بینی پرونده نامه و یادداشت ساختمان
- `anklageschrift-zerlegen` - شکستن نامه اتهامات
- `aussageanalyse-aussagepsychologie` - تحلیل بیانات روانشناسی گفتار
- `beweismittel-katalog-beweisverwertungsverbote` - شواهد فهرست ممنوعیت استفاده از مدرک
- `beweisverwertungsverbote-pruefen` - بررسی ممنوعیت استفاده از شواهد
- `beziehungen-spezial-chronologie-ergaenzbar` - روابط خاص زمان شناسی قابل تکرار
- `beziehungsmatrix-personen-taten` - رابطه متریکس افراد اعمال
- `chronologie-compliance-dokumentation-und-akte` - زمان شناسی مطابقت اسناد و پرونده
- `anschluss-routing` - رویتینگ اتصال
- `dokumente-intake` - اسناد دخول

## مسیر کار

- نوع نتیجه را تعیین کنید: نامه ای به مشتری، مخالفان، دادگاه یا مقام مجاز، هر گونه کارشناسان و مقامات ممکن است باشد، یادداشت مشتریان، گزارش ریسک، طرح قرارداد، قالب تصمیم گیری، تصریحات دولتی - چه چیزی واقعاً برای مشتری نیاز دارد؟
- فرمت های لازم را تعیین کنید: Tenor / درخواست / دلیل (دلیل ادعای، پرونده اعمال ، زیر نظر، نتیجه) ؛ نقاط مشخصی استاندارد در قانون کیفری تهیه شده است gesetze-im-internet.de و dejure.org در این زمینه، باید بررسی شود.
- وضوح مخاطب: زبان، عمق جزئیات و پیشگیری قانونی را در نظر بگیرید؛ برای مشتری بدون آموزش کامل خلاصه ی متن واضح ارائه دهید.
- برنامه های ساخت و ساز (تاریخی، موضوعی، K- و B-پلان) ؛ اشاره ها را به صورت تمیز نشان دهید.
- نوتیزه های منبع و به صورت نقل قولی را تضمین کنید؛ نقاط باز و فرضیه ها را بطور صریح چنین نشان دهید.

## لنگر کیفیت

- قوانین و قضیه `references/quellenhygiene.md` و `references/zitierweise.md` درمان می کنند.
- وقتی یک سوال خاص ظاهر می شود، مهارت مناسب را نام دهید و به طور خلاصه توضیح بدهید که چرا این روش کار درست است.
- در صورت فشار زمان، ابتدا مهلت، صلاحیت، شکل و بار اثبات را تضمین کنید.
