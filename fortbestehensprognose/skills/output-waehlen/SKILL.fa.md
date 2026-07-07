---
name: output-waehlen
description: "Wenn es um Output wählen in Fortbestehensprognose geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# انتخاب محصول

## وضعیت کاربرد

این هفته های پیدایش برای پیش بینی **مستقبل** تعیین می کند که آیا یادداشت، درخواست، گزارش نامه، جدول، چراغ خطر، لیست سوالات یا خط مشتری قدم بعدی مناسب است.

## نقشه تخصصی این افزونه

- `annahmen-behoerden-gericht-und-registerweg` - فرضیه های مقامات دادگاه و ثبت
- `annahmen-belastbarkeit-plausibilisieren` - فرضیه های تحمل پذیری
- `annahmen-sammeln-bilanzieller-status` - فرضیه جمع آوری وضعیت مالی
- `ausloesendes-ereignis-erfassen` - شناسایی رویداد آغاز کننده
- `bilanzieller-status-aufnehmen` - ثبت وضعیت مالی
- `bilanzstatus-risikoampel-und-gegenargumente` - وضعیت مالی، نشانه های ریسک و استدلال مقابل
- `comfortletter-sonderfall-edge` - Comfortletter حالت ویژه Edge
- `comfortletter-weich-erzeugen` - نرم تولید
- `eskalation-sonderfall-und-edge-case` - اسکالاسي مورد خاص و قضيه کناره
- `fbp-bankenkommunikation-waiver-integrierte` - FBP ارتباطات بانکی معافیت متمایز
- `fbp-integrierte-planung-bauleiter` - FBP برنامه ریزی متمایز سازنده
- `fbp-stresstest-szenarien-leitfaden` - راهنمای سناریوهای تست استرس FBP
- `fbp-zahlungsunfaehigkeit` - بی کفایتی FBP
- `anschluss-routing` - رویتینگ اتصال
- `dokumente-intake` - اسناد دخول

## مسیر کار

- نوع نتیجه را تعیین کنید: نامه ای به مشتری، مخالفان، دادگاه یا مقام مجاز، هر گونه کارشناسان و مقامات ممکن است باشد، یادداشت مشتریان، گزارش ریسک، طرح قرارداد، قالب تصمیم گیری، تصریحات دولتی - چه چیزی واقعاً برای مشتری نیاز دارد؟
- فرمت های لازم را تعیین کنید: تنور / درخواست / دلیل (بنیاد ادعای، پروندهٔ اعمال ، زیر نظر و نتیجه) ؛ نقاط مشخصی استاندارد در پیش بینی ادامه حیاتInsO, StaRUG, § 19 (ب) کار کردن
- وضوح مخاطب: زبان، عمق جزئیات و پیشگیری قانونی را در نظر بگیرید؛ برای مشتری بدون آموزش کامل خلاصه ی متن واضح ارائه دهید.
- برنامه های ساخت و ساز (تاریخی، موضوعی، K- و B-پلان) ؛ اشاره ها را به صورت تمیز نشان دهید.
- نوتیزه های منبع و به صورت نقل قولی را تضمین کنید؛ نقاط باز و فرضیه ها را بطور صریح چنین نشان دهید.

## لنگر کیفیت

- قوانین و قضیه `references/quellenhygiene.md` و `references/zitierweise.md` درمان می کنند.
- وقتی یک سوال خاص ظاهر می شود، مهارت مناسب را نام دهید و به طور خلاصه توضیح بدهید که چرا این روش کار درست است.
- در صورت فشار زمان، ابتدا مهلت، صلاحیت، شکل و بار اثبات را تضمین کنید.
