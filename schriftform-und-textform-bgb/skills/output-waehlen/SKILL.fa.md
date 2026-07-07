---
name: output-waehlen
description: "Wenn es um Output wählen in Schriftform und Textform im BGB geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# انتخاب محصول

## وضعیت کاربرد

این هفته خروجی برای **پرداخت و متن Bgb** تعیین می کند که آیا یادداشت، درخواست، گزارش نامه، جدول، چراغ خطر، لیست سوالات یا خط مشتری قدم بعدی مناسب است.

## نقشه تخصصی این افزونه

- `amtlicher-formkern-bgb-zpo-check` - هسته رسمی شکل BGB ZPO چک
- `anspruchsformulierungen-formverstoss` - شکلی که در آن صورت ثبت شده است
- `arbeitsrecht-befristung-schriftform-checker` - حقوق کار زمان بندی
- `befristungsabrede-qes-rechtsprechung` - به مدت زمان کمی از قوه قضایی
- `befristungsabrede-qes-rechtsprechung-stand-2026` - زمان بندی QES قضیه وضعیت 2026
- `bgb-mehrparteien-konflikt-und-interessen` — BGB چند طرفه درگیری و منافع
- `buergschaft-verbraucherdarlehen-und-andere-strenge-formen` - تضمین وام های مصرفی و سایر اشکال سختگیرانه
- `checklisten-schriftsatz-brief-und-memo-bausteine` - چک لیست نامه و یادداشت ساختمان
- `dokumentations-und-beweisarchitektur` - مستندات و معماری شواهد
- `elektronische-paragraph-formerfordernisse` - برقی بخش فرمت های ضروری
- `empfangsbeduerftiger-international` - بین المللی نیازمند پذیرش
- `empfangsbeduerftiger-international-schnittstellen` - رابط های بین المللی که نیاز به پذیرش دارند
- `form-checker-fuer-vertrag-oder-willenserklaerung` - فرم چک برای قرارداد یا وصیت
- `anschluss-routing` - رویتینگ اتصال
- `dokumente-intake` - اسناد دخول

## مسیر کار

- نوع نتیجه را تعیین کنید: نامه ای به مشتری، مخالفان، دادگاه یا مقام مجاز، هر گونه کارشناسان و مقامات ممکن است باشد، یادداشت مشتریان، گزارش ریسک، طرح قرارداد، قالب تصمیم گیری، تصریحات دولتی - چه چیزی واقعاً برای مشتری نیاز دارد؟
- فرمت های لازم را تعیین کنید: Tenor / درخواست / دلیل (دلیل ادعای، پرونده ی کارنامه ، زیرنویس و نتیجه) ؛ نقاط مشخصی استاندارد در صورت نوشته شده و متن Bgb gesetze-im-internet.de و dejure.org در این زمینه، باید بررسی شود.
- وضوح مخاطب: زبان، عمق جزئیات و پیشگیری قانونی را در نظر بگیرید؛ برای مشتری بدون آموزش کامل خلاصه ی متن واضح ارائه دهید.
- برنامه های ساخت و ساز (تاریخی، موضوعی، K- و B-پلان) ؛ اشاره ها را به صورت تمیز نشان دهید.
- نوتیزه های منبع و به صورت نقل قولی را تضمین کنید؛ نقاط باز و فرضیه ها را بطور صریح چنین نشان دهید.

## لنگر کیفیت

- قوانین و قضیه `references/quellenhygiene.md` و `references/zitierweise.md` درمان می کنند.
- وقتی یک سوال خاص ظاهر می شود، مهارت مناسب را نام دهید و به طور خلاصه توضیح بدهید که چرا این روش کار درست است.
- در صورت فشار زمان، ابتدا مهلت، صلاحیت، شکل و بار اثبات را تضمین کنید.
