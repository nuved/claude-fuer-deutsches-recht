---
name: output-waehlen
description: "Wenn es um Output wählen in Strafbefehl-Verteidiger geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# انتخاب محصول

## وضعیت کاربرد

این هفته ی خروجی برای **مطالبات مجازات مدافع** تعیین می کند که آیا یادداشت، درخواست، گزارش نامه، جدول، خطری نشان دهنده، لیست سوالات یا نام مشتری قدم بعدی مناسب است.

## نقشه تخصصی این افزونه

- `aktenanlage-fehlerkatalog` - پرونده ی خطا
- `akteneinsicht-behoerden-gericht-und-registerweg` - ادارات پرونده ها دادگاه و ثبت
- `deal-beweislast-einspruch` - معامله بار اثبات اعتراض
- `einspruch-risikoampel-und-gegenargumente` - اعتراض به خطر و استدلال های ضد
- `einspruchsentscheidung-und-folgen` - تصمیم گیری در مورد اعتراض و پیامدهای آن
- `einstellung-153a-hauptverhandlung` - قرار دادن 153a
- `einstellung-fahrerlaubnis` - تعویض مجوز رانندگی
- `fahrerlaubnis-mandantenentscheidung` - مجوز رانندگی تصمیم گیرنده
- `hauptverhandlung-international-schnittstellen` - مکالمات اصلی بین المللی
- `mandantenkommunikation-redteam-qualitygate` - ارتباطات مشتری Redteam Qualitygate
- `nebenfolgen-fahrerlaubnis-strafbefehl` - پیامدهای جانبی مجوز رانندگی حکم مجازات
- `nebenfolgen-strafbefehl-strafbefehls` - پیامدهای حکم مجازات
- `pflichtverteidigung-quellenkarte` - دفاعی واجب است
- `anschluss-routing` - رویتینگ اتصال
- `dokumente-intake` - اسناد دخول

## مسیر کار

- نوع نتیجه را تعیین کنید: نامه ای به مشتری، مخالفان، دادگاه یا مقام مجاز، هر گونه کارشناسان و مقامات ممکن است باشد، یادداشت مشتریان، گزارش ریسک، طرح قرارداد، قالب تصمیم گیری، تصریحات دولتی - چه چیزی واقعاً برای مشتری نیاز دارد؟
- تعیین فرمت های لازم: Tenor / درخواست / دلیل (دستگاه ادعای، پرونده اعمال ، زیر نظر, نتیجه) ؛ نقاط مشخصی استاندارد در حکم مجازات مدافع gesetze-im-internet.de و dejure.org در این زمینه، باید بررسی شود.
- وضوح مخاطب: زبان، عمق جزئیات و پیشگیری قانونی را در نظر بگیرید؛ برای مشتری بدون آموزش کامل خلاصه ی متن واضح ارائه دهید.
- برنامه های ساخت و ساز (تاریخی، موضوعی، K- و B-پلان) ؛ اشاره ها را به صورت تمیز نشان دهید.
- نوتیزه های منبع و به صورت نقل قولی را تضمین کنید؛ نقاط باز و فرضیه ها را بطور صریح چنین نشان دهید.

## لنگر کیفیت

- قوانین و قضیه `references/quellenhygiene.md` و `references/zitierweise.md` درمان می کنند.
- وقتی یک سوال خاص ظاهر می شود، مهارت مناسب را نام دهید و به طور خلاصه توضیح بدهید که چرا این روش کار درست است.
- در صورت فشار زمان، ابتدا مهلت، صلاحیت، شکل و بار اثبات را تضمین کنید.
