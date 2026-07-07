---
name: output-waehlen
description: "Wenn es um Output wählen in ZVG-Zwangsverwaltung - Verwalter-Cockpit geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# انتخاب محصول

## وضعیت کاربرد

این هفته های خروجی برای مدیریت مجبوری Zvg تعیین می کند که آیا یادداشت، درخواست، اسناد، جدول، چراغ خطر، لیست سوالات یا نامه مشتری قدم بعدی مناسب است.

## نقشه تخصصی این افزونه

- `aktenanlage-objektcockpit` - فایل های زیرنویس، کابین اشیاء
- `berichte-beschlagnahme-mietverwaltung-besitz` - گزارش های ضبط اداری اجاره مالکیت
- `berichtswesen-besitzuebernahme-bestellung` - گزارشگری، مالکیت
- `beschlagnahme-fristen-form-und-zustaendigkeit` - زمان های ضبط شکل و صلاحیت
- `beschlagnahme-mietverwaltung-start` - ضبط اداری اجاره شروع
- `beschlagnahme-oeffentliche-lasten` - دستگیری بارهای غیرفعال
- `besitz-dokumentenmatrix-und-lueckenliste` - مالکیت ماتریک اسناد و لیست خالی
- `besitzuebernahme` - انتقال مالکیت
- `bestellung-beschlagnahme` - دستور گرفتن
- `betriebskosten-hausgeld-bieterangebot` - هزینه های عملیاتی پول مسکن پیشنهاد داوطلب
- `bieterangebot-bewertung` - ارزیابی پیشنهادات داوطلبان
- `bieterangebote-mieten-oeffentliche` - پیشنهادات اجاره غیر واقعی
- `gate-fehlerkatalog` - فهرست خطای Gate
- `anschluss-routing` - رویتینگ اتصال
- `dokumente-intake` - اسناد دخول

## مسیر کار

- نوع نتیجه را تعیین کنید: نامه ای به مشتری، مخالفان، دادگاه یا مقام مجاز، هر گونه کارشناسان و مقامات ممکن است باشد، یادداشت مشتریان، گزارش ریسک، طرح قرارداد، قالب تصمیم گیری، تصریحات دولتی - چه چیزی واقعاً برای مشتری نیاز دارد؟
- فرمت های لازم را تعیین کنید: Tenor / درخواست / دلیل (دلیل ادعای، پرونده اعمال ، زیر نظر و نتیجه) ؛ تنظیم نقاط مشخص استاندارد در مدیریت اجباری Zvg (ZVG).
- وضوح مخاطب: زبان، عمق جزئیات و پیشگیری قانونی را در نظر بگیرید؛ برای مشتری بدون آموزش کامل خلاصه ی متن واضح ارائه دهید.
- برنامه های ساخت و ساز (تاریخی، موضوعی، K- و B-پلان) ؛ اشاره ها را به صورت تمیز نشان دهید.
- نوتیزه های منبع و به صورت نقل قولی را تضمین کنید؛ نقاط باز و فرضیه ها را بطور صریح چنین نشان دهید.

## لنگر کیفیت

- قوانین و قضیه `references/quellenhygiene.md` و `references/zitierweise.md` درمان می کنند.
- وقتی یک سوال خاص ظاهر می شود، مهارت مناسب را نام دهید و به طور خلاصه توضیح بدهید که چرا این روش کار درست است.
- در صورت فشار زمان، ابتدا مهلت، صلاحیت، شکل و بار اثبات را تضمین کنید.
