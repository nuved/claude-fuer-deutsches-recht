---
name: output-waehlen
description: "Wenn es um Output wählen in JVEG-Kostenprüfer geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# انتخاب محصول

## وضعیت کاربرد

این هفته ی محصول برای **Jveg Cost Auditor** تعیین می کند که آیا یادداشت، درخواست، گزارش نامه، جدول، چراغ خطر، سوالنامه یا خط مشتری قدم بعدی مناسب است.

## نقشه تخصصی این افزونه

- `aktenstripper` - کارنامه ی کلاهبردار
- `anspruchsberechtigung-antragsgenerator` - قابلیت درخواست ژنراتور
- `antragsgenerator` - ژنراتور درخواست
- `belegfeste-formular-portal-und-einreichung` - پورتال و ارسال فرم ثابت
- `beschwerde-dolmetscher-sonderfall` - شکایت مترجم
- `dolmetscher-sonderfall-und-edge-case` - تفسیر قضیه ویژه و Edge Case
- `dolmetscher-uebersetzer` - مترجم
- `dolmetscher-uebersetzer-fahrtkosten` - مترجم و ترجمه کننده هزینه سفر
- `dolmetscherkosten-zahlen-schwellen-und-berechnung` - هزینه های مترجم، اعداد و تراشه ها
- `fahrtkosten` - هزینه سفر
- `fahrtkosten-festsetzung-interessen` - هزینه سفر تعیین منافع
- `festsetzung-beschwerde` - ثبت شکایت
- `festsetzung-mehrparteien-konflikt-und-interessen` - تعیین چند طرفه ای درگیری و منافع
- `anschluss-routing` - رویتینگ اتصال
- `dokumente-intake` - اسناد دخول

## مسیر کار

- نوع نتیجه را تعیین کنید: نامه ای به مشتری، مخالفان، دادگاه یا مقام مجاز، هر گونه کارشناسان و مقامات ممکن است باشد، یادداشت مشتریان، گزارش ریسک، طرح قرارداد، قالب تصمیم گیری، تصریحات دولتی - چه چیزی واقعاً برای مشتری نیاز دارد؟
- فرمت های لازم را تعیین کنید: تنور / درخواست / دلیل (دلیل ادعای، پروندهٔ اعمال ، جمع بندی و نتیجه) ؛ نقاط مشخصی استاندارد در Jveg هزینهJVEG) را در نظر بگیرید.
- وضوح مخاطب: زبان، عمق جزئیات و پیشگیری قانونی را در نظر بگیرید؛ برای مشتری بدون آموزش کامل خلاصه ی متن واضح ارائه دهید.
- برنامه های ساخت و ساز (تاریخی، موضوعی، K- و B-پلان) ؛ اشاره ها را به صورت تمیز نشان دهید.
- نوتیزه های منبع و به صورت نقل قولی را تضمین کنید؛ نقاط باز و فرضیه ها را بطور صریح چنین نشان دهید.

## لنگر کیفیت

- قوانین و قضیه `references/quellenhygiene.md` و `references/zitierweise.md` درمان می کنند.
- وقتی یک سوال خاص ظاهر می شود، مهارت مناسب را نام دهید و به طور خلاصه توضیح بدهید که چرا این روش کار درست است.
- در صورت فشار زمان، ابتدا مهلت، صلاحیت، شکل و بار اثبات را تضمین کنید.
