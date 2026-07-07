---
name: output-waehlen
description: "Wenn es um Output wählen in anwaltlichem Berufsrecht und Vertragsprüfung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# انتخاب محصول

## وضعیت کاربرد

این هفته ی محصول برای **حقوق حرفه ای Ki امتحان قرارداد** تعیین می کند که آیا یادداشت، درخواست، اسناد، جدول، چراغ خطر، لیست سوالات یا نامه مشتری قدم بعدی مناسب است.

## نقشه تخصصی این افزونه

- `ai-act-rollen-kanzlei-provider-deployer-api` - AI ACT نقش های شرکت ارائه دهنده API
- `anbietern-belehrung-sonderfall-edge` - ارائه دهندگان آموزش حالت ویژه Edge
- `anbietern-schriftsatz-brief-memo-bausteine` - ارائه دهنده نامه خط یادداشت ساختمان
- `art-50-ki-vo-schriftsatz-marketing-chatbot` - آرتی 50 KI VO نوشته های بازاریابی چت
- `avv-grenzpruefung-brki-anbieter-eu` - AVV مرزی برکی ارائه دهنده اتحادیه اروپا
- `avv-grenzpruefung-datenschutz` -آویز سرحدی حفاظت از اطلاعات
- `belehrung-abschlussprodukt-uebergabe` - آموزش محصول نهایی انتقال
- `belehrung-abschlussprodukt-und-uebergabe` - آموزش محصول نهایی و انتقال
- `berufsrecht-sonderfall-edge-case` - قانون حرفه ای قضیه ویژه Edge Case
- `berufsrecht-sonderfall-und-edge-case` - قانون حرفه ای قضیه ویژه و Edge Case
- `berufsrechtliche-bnoto-interessen-brao` - حقوق حرفه ای BRAO
- `bnoto-interessen` - منافع بین المللی
- `bnoto-mehrparteien-konflikt-und-interessen` - سازمان ملل متحد چند طرفه درگیری و منافع
- `anschluss-routing` - رویتینگ اتصال
- `dokumente-intake` - اسناد دخول

## مسیر کار

- نوع نتیجه را تعیین کنید: نامه ای به مشتری، مخالفان، دادگاه یا مقام مجاز، هر گونه کارشناسان و مقامات ممکن است باشد، یادداشت مشتریان، گزارش ریسک، طرح قرارداد، قالب تصمیم گیری، تصریحات دولتی - چه چیزی واقعاً برای مشتری نیاز دارد؟
- تعیین فرمت های لازم: Tenor / درخواست / دلیل (دلیل ادعای، پرونده اعمال ، زیر نظر و نتیجه) ؛ نقاط مشخصی در قانون حرفه ای§ 203 StGB، مصرف کننده § 43e BRAO.) در کنار هم کار می کنند.
- وضوح مخاطب: زبان، عمق جزئیات و پیشگیری قانونی را در نظر بگیرید؛ برای مشتری بدون آموزش کامل خلاصه ی متن واضح ارائه دهید.
- برنامه های ساخت و ساز (تاریخی، موضوعی، K- و B-پلان) ؛ اشاره ها را به صورت تمیز نشان دهید.
- نوتیزه های منبع و به صورت نقل قولی را تضمین کنید؛ نقاط باز و فرضیه ها را بطور صریح چنین نشان دهید.

## لنگر کیفیت

- قوانین و قضیه `references/quellenhygiene.md` و `references/zitierweise.md` درمان می کنند.
- وقتی یک سوال خاص ظاهر می شود، مهارت مناسب را نام دهید و به طور خلاصه توضیح بدهید که چرا این روش کار درست است.
- در صورت فشار زمان، ابتدا مهلت، صلاحیت، شکل و بار اثبات را تضمین کنید.
