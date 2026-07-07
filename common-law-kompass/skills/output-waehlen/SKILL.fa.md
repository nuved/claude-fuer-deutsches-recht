---
name: output-waehlen
description: "Wenn es um Output wählen in Common-Law-Kompass für deutsche Wirtschaftsjuristen geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# انتخاب محصول

## وضعیت کاربرد

این هفته های خروجی برای **Common Law Compass** تعیین می کند که آیا یادداشت، درخواست، گزارش نامه، جدول، چراغ خطر، لیست سوالات یا خط مشتری قدم بعدی مناسب است.

## نقشه تخصصی این افزونه

- `begriffe-uebersetzung-bilingual-contract` - ترجمه اصطلاحات
- `bilingual-contract-review` - بررسی قرارداد دو زبان
- `bilinguale-client-commercial-sonderfall` - دو زبان کلائنت تجاری
- `cl-discovery-doc-production-spezial` - CL Discovery DOC تولید ویژه
- `cl-mandantenuebersicht-cl-prozesskostenrisiko` - CL برآورد مشتری
- `cl-prozesskostenrisiko-each-party-bears-own` - CL خطر هزینه های دادگاه هر حزب را دارد
- `cl-spezial-precedent-vs-statute` - CL خصوصی پیشینه VS قانون
- `cl-vertragsklauseln-vertragsbegriffe-cl` - CL بند های قرارداد
- `client-explainer` - توضیح دهنده مشتری
- `client-mandantenkommunikation-entscheidungsvorlage` - مشتری ارتباطات مشتریان تصمیم گیری
- `commercial-sonderfall-und-edge-case` - قضیه ویژه تجاری و Edge Case
- `common-consideration-discovery` - Common Consideration Discovery
- `consideration-behoerden-gericht-und-registerweg` - نظر مقامات دادگاه و ثبت
- `anschluss-routing` - رویتینگ اتصال
- `dokumente-intake` - اسناد دخول

## لنگرهای تنظیم و منبع

پیش از هر نتیجه‌گیریِ حقوقی، این لنگرها را با متنِ روزِ قانون بسنجید؛ حقوقِ خاص و حقوقِ ایالتی را تنها زمانی بیفزایید که دستورِ کارِ مشخص را پشتیبانی کند:

- `UCC § 2-201` -قانون کلاهبرداری در خرید کالاها
- `UCC § 2-313` -وارانتي هاي صريحه
- `UCC § 2-314` - تضمین متضمن فروش.
- `Restatement (Second) of Contracts § 17` -تشکيل با سودمندی
- `Restatement (Second) of Contracts § 71` -نظر گرفتن
- `Restatement (Second) of Contracts § 90` -به عنوان یک وعده ای
- `CISG Art. 14` -من پیشنهاد میکنم
- `CISG Art. 18` -فکر کنم
- `CISG Art. 25` - نقض اساسی
- `CISG Art. 35` -معاونیت قرارداد.

رویهٔ قضایی را تنها هنگامی بیفزایید که دادگاه، تاریخ، شمارهٔ پرونده و یک منبعِ آزادانه قابل‌بررسی موجود باشد؛ از استنادهای کورِ BeckRS/juris استفاده نکنید.

## مسیر کار

- نوع نتیجه را تعیین کنید: نامه ای به مشتری، مخالفان، دادگاه یا مقام مجاز، هر گونه کارشناسان و مقامات ممکن است باشد، یادداشت مشتریان، گزارش ریسک، طرح قرارداد، قالب تصمیم گیری، تصریحات دولتی - چه چیزی واقعاً برای مشتری نیاز دارد؟
- فرمت های لازم را تعیین کنید: Tenor / درخواست / دلیل (دلیل ادعای، پرونده ی اعمال ، زیر نظر و نتیجه) ؛ نقاط مشخصی استاندارد در کامپوس قانون مشترک gesetze-im-internet.de و dejure.org در این زمینه، باید بررسی شود.
- وضوح مخاطب: زبان، عمق جزئیات و پیشگیری قانونی را در نظر بگیرید؛ برای مشتری بدون آموزش کامل خلاصه ی متن واضح ارائه دهید.
- برنامه های ساخت و ساز (تاریخی، موضوعی، K- و B-پلان) ؛ اشاره ها را به صورت تمیز نشان دهید.
- نوتیزه های منبع و به صورت نقل قولی را تضمین کنید؛ نقاط باز و فرضیه ها را بطور صریح چنین نشان دهید.

## لنگر کیفیت

- قوانین و قضیه `references/quellenhygiene.md` و `references/zitierweise.md` درمان می کنند.
- وقتی یک سوال خاص ظاهر می شود، مهارت مناسب را نام دهید و به طور خلاصه توضیح بدهید که چرا این روش کار درست است.
- در صورت فشار زمان، ابتدا مهلت، صلاحیت، شکل و بار اثبات را تضمین کنید.
