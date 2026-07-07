---
name: output-waehlen
description: "Wenn es um Output wählen in Phishing-Vorfall-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# انتخاب محصول

## وضعیت کاربرد

این هفته های خروجی برای **محقق فاشیگ** می تواند تعیین کند که آیا یادداشت، درخواست، اسناد، جدول، چراغ خطر، لیست پرسش یا نامه مشتری قدم بعدی مناسب است.

## نقشه تخصصی این افزونه

- `675u-675w-banking` - بانکداری
- `675v-quellenkarte` - 675v کارت منبع
- `675w-zahlen-schwellen-und-berechnung` - 675w اعداد تله و محاسبه
- `arbeitnehmer-haftung-bgb-675u-phish-ceo` - مسئولیت کارکنان BGB 675u Phish CEO
- `aufsicht-bafin-bank-strategie-banking-app` - نظارت بانک Bafin استراتژی بانکی APP
- `banking-behoerden-gericht-und-registerweg` - بانکداري مقامات دادگاه و ثبت
- `bankpflichten-beweislast-bgb` - تعهدات بانکی و بار اثبات BGB
- `bea-notfall-bgb-675v-erstkontakt-mandant` - بی ای اے اضطراری BGB 675v تماس اول
- `beweislast-mandantenkommunikation-entscheidungsvorlage` - شواهد و مدارک ارتباطات مشتری تصمیم گیری
- `bgb-schriftsatz-brief-und-memo-bausteine` — BGB نامه و یادداشت ساختمان
- `call-interessen-faelle-freistehender` - تماس با منافع Faelle آزاد استاندار
- `faelle-abschlussprodukt-und-uebergabe` - محصول نهایی و انتقال
- `fahrlaessigkeit-fehlerkatalog` - خطا در فهرست
- `anschluss-routing` - رویتینگ اتصال
- `dokumente-intake` - اسناد دخول

## مسیر کار

- نوع نتیجه را تعیین کنید: نامه ای به مشتری، مخالفان، دادگاه یا مقام مجاز، هر گونه کارشناسان و مقامات ممکن است باشد، یادداشت مشتریان، گزارش ریسک، طرح قرارداد، قالب تصمیم گیری، تصریحات دولتی - چه چیزی واقعاً برای مشتری نیاز دارد؟
- فرمت های لازم را تعیین کنید: Tenor / درخواست / دلیل (دلیل ادعای، پروندهٔ اعمال ، زیر نظر و نتیجه) ؛ نقاط مشخصی در مورد یک رویداد فاشیینگBGB, § 675u,, § 675v,, § 675w، pushTAN، call) را به کار می گیرند.
- وضوح مخاطب: زبان، عمق جزئیات و پیشگیری قانونی را در نظر بگیرید؛ برای مشتری بدون آموزش کامل خلاصه ی متن واضح ارائه دهید.
- برنامه های ساخت و ساز (تاریخی، موضوعی، K- و B-پلان) ؛ اشاره ها را به صورت تمیز نشان دهید.
- نوتیزه های منبع و به صورت نقل قولی را تضمین کنید؛ نقاط باز و فرضیه ها را بطور صریح چنین نشان دهید.

## لنگر کیفیت

- قوانین و قضیه `references/quellenhygiene.md` و `references/zitierweise.md` درمان می کنند.
- وقتی یک سوال خاص ظاهر می شود، مهارت مناسب را نام دهید و به طور خلاصه توضیح بدهید که چرا این روش کار درست است.
- در صورت فشار زمان، ابتدا مهلت، صلاحیت، شکل و بار اثبات را تضمین کنید.
