---
name: output-waehlen
description: "Wenn es um Output wählen in Fachanwalt Strafrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# انتخاب محصول

## وضعیت کاربرد

این هفته ی محصول برای **شخص وکیل حقوق کیفری** تعیین می کند که آیا یادداشت، درخواست، اسناد، جدول، چراغ خطر، لیست سوالات یا نامه مشتری قدم بعدی مناسب است.

## نقشه تخصصی این افزونه

- `workflow-redteam-qualitygate` - روش های ادغام
- `strafrecht-spezial-aussagepsychologie-staatsanwaltschaft-replik` - روانشناسی بیان دادستان
- `chatcontrol-csam-anwaltsgeheimnis-53-stpo` - Chatcontrol Csam آماده کردن ورود
- `ergaenzt-mandantenkommunikation-entscheidungsvorlage` - بازپرداخت وکیل فقیر درخواست ورشکستگی RED تیم اصلاح
- `fa-strafrecht-quellen-frist-next` - FA قانون کیفری منابع تاریخ بعدی
- `freiheitsstrafe-paragraf-57-stgb` - مجازات زندان بند 57
- `hauptverhandlung-quellenkarte` - اصلی بحث منبع کارت
- `strafrecht-spezial-koerperverletzung-223-stgb-grund` - آسیب به بدن STGB مرگ
- `mandat-triage-strafrecht` - مهلت سه بعدی آماده سازی
- `nebenklage-compliance-dokumentation-und-akte` - دادخواست جانبی قانون جنایی
- `notwehr-paragraf-32-stgb` - در برابر قانون 32 STGB
- `orientierung-mandat-fachanwaltschaft` - راهنما
- `strafrecht-spezial-raub-249-stgb` - دزدی از دست دادن
- `anschluss-routing` - رویتینگ اتصال
- `dokumente-intake` - اسناد دخول

## مسیر کار

- نوع نتیجه را تعیین کنید: نامه ای به متهم، وکیل قانونی، دادستان، قاضی بازرسی، رئیس جمهور، خالق، شاهد، مدعی جانبی، JVA، یادداشت مشتری، گزارش ریسک، طرح قرارداد، قالب تصمیم گیری، تصریح مقامات - چه چیزی واقعاً برای مؤکل نیاز دارد؟
- فرمت های لازم را تعیین کنید: Tenor / درخواست / دلیل (دلیل ادعای، پرونده اعمال ، زیر نظر و نتیجه) ؛ نقاط مشخصی در قانون کیفری و قانونیStGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 53در این مقاله به عنوان مثال، از نظر تعداد افراد که با استفاده از آن ها کار می کنند ، باید بر اساس میزان و مقدار آنها را مشخص کنیم.
- وضوح مخاطب: زبان، عمق جزئیات و پیشگیری قانونی را در نظر بگیرید؛ برای مشتری بدون آموزش کامل خلاصه ی متن واضح ارائه دهید.
- برنامه های ساخت و ساز (تاریخی، موضوعی، K- و B-پلان) ؛ اشاره ها را به صورت تمیز نشان دهید.
- نوتیزه های منبع و به صورت نقل قولی را تضمین کنید؛ نقاط باز و فرضیه ها را بطور صریح چنین نشان دهید.

## لنگر کیفیت

- قوانین و قضیه `references/quellenhygiene.md` و `references/zitierweise.md` درمان می کنند.
- وقتی یک سوال خاص ظاهر می شود، مهارت مناسب را نام دهید و به طور خلاصه توضیح بدهید که چرا این روش کار درست است.
- در صورت فشار زمان، ابتدا مهلت، صلاحیت، شکل و بار اثبات را تضمین کنید.
