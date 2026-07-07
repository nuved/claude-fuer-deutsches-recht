---
name: output-waehlen
description: "Wenn es um Output wählen in Insolvenzplan- und StaRUG-Planwerkstatt geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# انتخاب محصول

## وضعیت کاربرد

این هفته های خروجی برای **خطاب ورشکست گیری استارگ برنامه** تعیین می کند که آیا یادداشت، درخواست، خط نامه، جدول، چراغ خطر، لیست سوالات یا نام مشتری قدم بعدی مناسب است.

## نقشه تخصصی این افزونه

- `abstimmung-anlagen-interessen-cram` - هماهنگی سرمایه گذاری منافع Cram
- `abstimmung-mehrheiten-anlagenpaket` - توافق اکثریت بسته سرمایه گذاری
- `anlagen-mehrparteien-konflikt-und-interessen` - سرمایه گذاری چندطرفه درگیری و منافع
- `anlagenpaket` - بسته بندی
- `asset-deals-im-plan-grundstuecke-marken-kundendaten` - معامله های دارایی در طرح زمین ها مارک داده مشتری
- `cram-formular-portal-und-einreichung` - Cram Formular Portal و ارسال
- `cramdown-obstruktion-datenraum-register` - Cramdown Obstruction Data Room Register
- `darstellender-quellenkarte` - نقشه منبع نمایش
- `darstellender-teil` - بخش نمایش
- `datenraum-register` - دفترچه فضای داده
- `down-red-gestaltender-gruppen` - گروه های تشکیل دهنده
- `gerichtliche-schritte-kommandocenter` - دادگاه اقدامات مرکز فرماندهی
- `gestaltender-teil` - بخش شکل دهنده
- `anschluss-routing` - رویتینگ اتصال
- `dokumente-intake` - اسناد دخول

## مسیر کار

- نوع نتیجه را تعیین کنید: نامه ای به مشتری، مخالفان، دادگاه یا مقام مجاز، هر گونه کارشناسان و مقامات ممکن است باشد، یادداشت مشتریان، گزارش ریسک، طرح قرارداد، قالب تصمیم گیری، تصریحات دولتی - چه چیزی واقعاً برای مشتری نیاز دارد؟
- تعیین فرمت های لازم: تنور / درخواست / دلیل (دستگاه ادعای، پرونده اعمال ، زیر نظر و نتیجه) ؛ نقاط مشخص استاندارد در برنامه ی گشایش استارگStaRUG) را در نظر بگیرید.
- وضوح مخاطب: زبان، عمق جزئیات و پیشگیری قانونی را در نظر بگیرید؛ برای مشتری بدون آموزش کامل خلاصه ی متن واضح ارائه دهید.
- برنامه های ساخت و ساز (تاریخی، موضوعی، K- و B-پلان) ؛ اشاره ها را به صورت تمیز نشان دهید.
- نوتیزه های منبع و به صورت نقل قولی را تضمین کنید؛ نقاط باز و فرضیه ها را بطور صریح چنین نشان دهید.

## لنگر کیفیت

- قوانین و قضیه `references/quellenhygiene.md` و `references/zitierweise.md` درمان می کنند.
- وقتی یک سوال خاص ظاهر می شود، مهارت مناسب را نام دهید و به طور خلاصه توضیح بدهید که چرا این روش کار درست است.
- در صورت فشار زمان، ابتدا مهلت، صلاحیت، شکل و بار اثبات را تضمین کنید.
