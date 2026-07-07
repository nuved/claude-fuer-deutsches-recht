---
name: output-waehlen
description: "Wenn es um Output wählen in patentrecherche geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# انتخاب محصول

## وضعیت کاربرد

این هفته ی پیدایش برای **Patent Search** تعیین می کند که آیا یادداشت، درخواست، اسناد، جدول، چراغ خطر، لیست سوالات یا نامه مشتری قدم بعدی مناسب است.

## نقشه تخصصی این افزونه

- `agentisch-fristen-form-und-zustaendigkeit` - زمان بندی آژانس شکل و صلاحیت
- `agentische-datenbank-recherche` - پایگاه داده آژانس تحقیقات
- `depatisnet-verhandlung-vergleich-und-eskalation` - Depatisnet مذاکره مقایسه و افزایش
- `dpmaregister-epue-beweislast-erfinderische` - ثبت کننده ی اداری و مدارک
- `epo-opposition-strategie` - EPO اپوزیشن استراتژی
- `epo-quellenkarte` - کارت منبع EPO
- `epue-beweislast-und-darlegungslast` - بار اثبات و ارائه
- `erfinderische-sonderfall-und-edge-case` - پرونده ی ویژه ای با اختراعات و قضیهٔ کناری
- `erfinderische-taetigkeit-freedom-to-ki-patent` - اختراع کردن آزادی به دانش آموزی
- `espacenet-google-neuheit-red-team-korrektur` - اسپاسنت گوگل خبر رید تیم اصلاح
- `freedom-to-operate-recherche` - آزادی برای تحقیق عملیاتی
- `google-risikoampel-und-gegenargumente` - گوگل نشان خطر و استدلال های ضد
- `kaltstart-interview` - مصاحبه سرد شروع
- `anschluss-routing` - رویتینگ اتصال
- `dokumente-intake` - اسناد دخول

## مسیر کار

- نوع نتیجه را تعیین کنید: ثبت نام به درخواست دهنده های حق اختراع، وکیل حقوق انحصاری، معاینه کننده DPMA، بازرسان EPO، USPTO، WIPO، یادداشت مشتری، گزارش ریسک، طرح قرارداد، قالب تصمیم گیری، تصریحات مقامات - چه چیزی واقعاً برای مؤکل نیاز دارد؟
- فرمت های لازم را تعیین کنید: Tenor / درخواست / دلیل (دلیل ادعای، پرونده و نتیجه) ؛ نقاط مشخصی در تحقیقات ثبت نامPatG §§ 1، ۳، ۴، ۹، ۱۰، ۱۳۹ Art. 54, 56, 64, 69, 87 ff.در این زمینه، به توافق نامه های IPC استراسبورگ نیز ادامه می دهیم.
- وضوح مخاطب: زبان، عمق جزئیات و پیشگیری قانونی را در نظر بگیرید؛ برای مشتری بدون آموزش کامل خلاصه ی متن واضح ارائه دهید.
- برنامه های ساخت و ساز (تاریخی، موضوعی، K- و B-پلان) ؛ اشاره ها را به صورت تمیز نشان دهید.
- نوتیزه های منبع و به صورت نقل قولی را تضمین کنید؛ نقاط باز و فرضیه ها را بطور صریح چنین نشان دهید.

## لنگر کیفیت

- قوانین و قضیه `references/quellenhygiene.md` و `references/zitierweise.md` درمان می کنند.
- وقتی یک سوال خاص ظاهر می شود، مهارت مناسب را نام دهید و به طور خلاصه توضیح بدهید که چرا این روش کار درست است.
- در صورت فشار زمان، ابتدا مهلت، صلاحیت، شکل و بار اثبات را تضمین کنید.
