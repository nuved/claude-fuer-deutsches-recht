---
name: unterlagen-luecken
description: "Wenn es um Unterlagen und Lücken in Insolvenzforderungsanmeldungsprüfung geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# اسناد و شکاف ها

## وضعیت کاربرد

این بررسی اسناد برای **مطالعه ثبت نام در مورد ورشکستگی**، مدارک گمشده را مشخص می کند، حقایق متنازع و خطرات اثبات شده و آخرین درخواست مطمئن.

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

- فهرست هدف: برای پرسش های بررسی درخواست ورشکستگی (مطالعات قرارداد، اسناد و مدارک، پرونده های اداری، پروتکل ها، تصمیمات و شواهد خارجی مربوط به تخصص) چه سند هایی لازم است؟
- مقایسه است: چه اسناد موجود هستند، کدامها از دست رفته اند؟
- این لیست را به ترتیب: فرسترلایت (که زمان های مربوطه در زمینه ی تخصصی و عملی را باید پیش از آن مشخص کنند، نه اینکه با دانش مدل ای نهایی شوند) ، ثابت کننده، شکل ساز.
- نامه های بازرسی به مشتری، مخالفان، دادگاه یا مقام مجاز و هر گونه کارشناسان یا سازمان هایی که ممکن است در اختیار داشته باشند طراحی می شود - چه کسی سند را دارد؟ از کجا می توان آن را بدست آورد؟ تا کی؟
- در مورد شکاف های دولتی: حق بررسی پرونده ها (به عنوان مثال § 29 VwVfG, § 147 StPO, § 25 SGB (X) بررسی و استفاده

## لنگر کیفیت

- قوانین و قضیه `references/quellenhygiene.md` و `references/zitierweise.md` درمان می کنند.
- وقتی یک سوال خاص ظاهر می شود، مهارت مناسب را نام دهید و به طور خلاصه توضیح بدهید که چرا این روش کار درست است.
- در صورت فشار زمان، ابتدا مهلت، صلاحیت، شکل و بار اثبات را تضمین کنید.
