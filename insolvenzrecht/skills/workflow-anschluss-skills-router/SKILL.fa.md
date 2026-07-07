---
name: workflow-anschluss-skills-router
description: "Wenn es um Anschluss-Skills Router in Insolvenzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# روتر مهارت های اتصال

## دستور کار

این کار باعث می شود که راه اندازی **Ansolvency Skills Router** در زمینه **Insolvence Law* به صورت فوری قابل اجرا باشد: ابتدا پرونده ها را بخوانید، سپس نقشها، اهداف و مهلت های خود را تنظیم کنید.

## شروع پرونده بدون خالی

1. قبل از پرسیدن سوالات، اسناد موجود، نام های فایل ها، متادیا و زمان بندی قابل تشخیص را ارزیابی کنید.
2. حقایق مطمئن، فرضیه های قابل قبول و ادعاهای متناقض را در چهار کالم جداگانه ثبت کنید.
3. نقش حزب، مخالفان/ مقام های قضایی و دادگاه، صلاحیت، وضعیت کار و نتیجه مورد نظر را به طور خلاصه تعیین می کند.
4. ریسک های فوری را نشان دهید: زمان اضطراری، تحویل/ دسترسی، ممانعت، مجازات، اجرای، تاریخ ثبت / پورتال، از دست دادن شواهد.
5. بعد فقط از این سوال، نکات گمشده را بپرسید که گام بعدی شما را تغییر می دهد.

## لنگرهای تخصصی

- InsO §§ 13، 15a، 17-19، 21، 35، 38، 87 و 129 ff., 174 ff.; StaRUG; شروع GmbHG § 15a/§ 64 a.F اثرات جانبی
- پرداخت قابل، بدهی بیش از حد، حجم، جداسازی/فصل کردن، اعتراض و گزارش طلب و مسئولیت مدیریت را تقسیم کنید.
- همیشه با تاریخ پرداخت، منبع و وضعیت بانکداری، مبلغی، شکاف نقدی و برنامه ریزی اسناد تهیه کنید.

## محصول کار

- ** تشخیص کوتاه:** چه اتفاقی می افتد، کدام سوال حقوقی در این مورد مطرح است؟
- **مطابق مدارکی:** واقعیت، منبع، محل یافت/پلاستی، ارزش اثبات، شکاف، تقاضا.
- ** چراغ خطر:** سبز/ زرد/ قرمز با دلیل تنگ و گام بعدی امن.
- **مخطط:** بر اساس مورد، ایمیل، یادداشت مشتری، نامه های مقامات/ دادگاه، چک لیست، جدول یا برنامه مهلت.
- **براهمز اشتباه:** هیچ استاندارد اختراع نشده، بدون نقل قول های نابینا و بدون اسناد.

## اطلاعات اضافی

## منطق رویتینگ به ماژول های تخصصی افزونه
- **مندانت بدهکار/ مدیرعامل است که سوال درخواست دارد:**
 - `spezial-insolvenzreife-antragspflicht-und-haftung` (§ 15a InsO, § 15b InsO).
 - `spezial-zahlungsunfaehigkeit-tatbestand-beweis-und-belege` (§ 17 InsO، 10 درصد در 3 هفته
 - `spezial-ueberschuldung-fristen-form-und-zuständigkeit` (§ 19 InsOپیش بینی 12 ماه
- **راه عمل:**
 - `spezial-verfahrenstypen-livequellen-und-rechtsprechungscheck` (سرمایه گیری عمومی در مقابل مدیریت شخصی) § 270 InsO در مقابل صفحه محافظ § 270d InsO).
 - `spezial-glaeubigerantrag-risikoampel-und-gegenargumente` (تعارف وامدار) § 14 InsO).
 - `spezial-verbraucherinsolvenz-mehrparteienkonflikt` (§§ 304 ff. InsO).
- ** مرحله عملیاتی:**
 - `spezial-belegmatrix-formular-portal-und-einreichung` (دستور های درخواست)
 - `spezial-tabelle-beweislast-und-darlegungslast` (جدول درخواست)
 - `spezial-glaeubigerausschuss-fristennotiz-und-naechster-schritt` (§ 67 InsO).
- **قطر:**
 - `spezial-inso-schriftsatz-brief-und-memo-bausteine` (بزرگ های متن)
 - `spezial-rechtsquellen-zahlen-schwellen-und-berechnung` (۱۰ درصد ۳ هفته محاسبه)
 - `spezial-triage-mandantenkommunikation-entscheidungsvorlage` (خطاب فرمانده)
- **موقع های ویژه:**
 - `spezial-chronologie-internationaler-bezug-und-schnittstellen` (EUROC 2015/848)
 - `internationales-insolvenzrecht-drittstaaten-inzidentpruefung` (آمریکا/ کانادا/ انگلستان/ سوئیس، منطق فصل 15 نیست) § 343 InsO).
 - `auslaendischer-insolvenzverwalter-register-und-grundbuch` (مؤمن/DIP/ دفتر نگهدارنده در پیشگاه یک نوتر، ثبت تجاری و حسابداری)
 - `spezial-feststellung-sonderfall-und-edge-case`.

## قانون دست
- همیشه اول باید الزامات درخواست را روشن کنیم (§ 15a InsOپس از آن، انتخاب روش ها و بعد مهارت های عملیاتی.
