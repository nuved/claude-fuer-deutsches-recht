---
name: output-waehlen
description: "Wenn es um Output wählen in Insolvenzforderungsanmeldungsprüfung geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# انتخاب محصول

## وضعیت کاربرد

این هفته های خروجی برای بررسی گزارشات بی نقصیت تعیین می کند که آیا یادداشت، درخواست، اسناد، جدول، خط مشمول خطر، لیست سوالات یا نامه مشتری قدم بعدی مناسب است.

## نقشه تخصصی این افزونه

- `aktenanlage-batchregister` - پرونده های مجموعه ی دسته بندی
- `beleg-und-urkundencheck` - مدارک و چک اسناد
- `bestreiten-interessen-betrag` - مبلغ سود متنازع
- `bestreiten-mehrparteien-konflikt-und-interessen` - با اختلافات و منافع چند طرفه
- `betrag-behoerden-gericht-und-registerweg` - مقدار مقامات دادگاه و ثبت
- `dubletten-serienforderungen` - دو عدد از مطالب سری
- `feststellung-forderungsgrund-rang-grund` - تعیین دلیل ادعای
- `forderungsanmeldung-mandantenkommunikation-redteam-qualitygate` - ثبت درخواست ارتباطات مشتری Redteam Qualitygate
- `vbuh-verhandlung-vergleich-und-eskalation` - گزارش درخواست در مورد مذاکرات مقایسه افزایش
- `forderungsgrund-rang-und-belegpruefung` - پایه ی مطالبه و بررسی مدارک
- `formalpruefung-174` - آزمون رسمی 174
- `grund-betrag-zinsen` - اصل مقدار سود
- `grund-risikoampel-und-gegenargumente` - دلیل خطر و استدلال های ضد
- `anschluss-routing` - رویتینگ اتصال
- `dokumente-intake` - اسناد دخول

## مسیر کار

- نوع نتیجه را تعیین کنید: نامه ای به مشتری، مخالفان، دادگاه یا مقام مجاز، هر گونه کارشناسان و مقامات ممکن است باشد، یادداشت مشتریان، گزارش ریسک، طرح قرارداد، قالب تصمیم گیری، تصریحات دولتی - چه چیزی واقعاً برای مشتری نیاز دارد؟
- فرمت های لازم را تعیین کنید: تنور / درخواست / دلیل (بنیاد ادعای، پروندهٔ اعمال ، جمع بندی و نتیجه) ؛ نقاط مشخصی استاندارد در بررسی گزارشات بادی§ 174 InsO, مدارک, دلیل، مقدار, درجه بندی, vbuH, تقاضاها, واردات جدول
- وضوح مخاطب: زبان، عمق جزئیات و پیشگیری قانونی را در نظر بگیرید؛ برای مشتری بدون آموزش کامل خلاصه ی متن واضح ارائه دهید.
- برنامه های ساخت و ساز (تاریخی، موضوعی، K- و B-پلان) ؛ اشاره ها را به صورت تمیز نشان دهید.
- نوتیزه های منبع و به صورت نقل قولی را تضمین کنید؛ نقاط باز و فرضیه ها را بطور صریح چنین نشان دهید.

## لنگر کیفیت

- قوانین و قضیه `references/quellenhygiene.md` و `references/zitierweise.md` درمان می کنند.
- وقتی یک سوال خاص ظاهر می شود، مهارت مناسب را نام دهید و به طور خلاصه توضیح بدهید که چرا این روش کار درست است.
- در صورت فشار زمان، ابتدا مهلت، صلاحیت، شکل و بار اثبات را تضمین کنید.
