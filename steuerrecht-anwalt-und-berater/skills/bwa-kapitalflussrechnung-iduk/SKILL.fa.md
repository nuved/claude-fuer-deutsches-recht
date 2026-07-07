---
name: bwa-kapitalflussrechnung-iduk
description: "Wenn es um Kapitalflussrechnung nach DRS 21 indirekte Methode in Steuerrecht – Steuerberater und Anwälte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# محاسبه جریان سرمایه در DRS 21 روش غیر مستقیم

## لنگر تخصصی

- **نوردها:** § 6a, § 297 HGB, § 19 InsO.
- **سرگرمی تصمیم گیری/برچسب:** استفاده از قضیه ی معتبر فقط با دادگاه، تاریخ و نشانه های پرونده ای که می تواند به طور آزاد بررسی شود؛ هیچ گونه تصمیم را بر اساس دانش مدلی اجبار نکنید.
- ** بهداشت منابع:** `references/quellenhygiene.md` و `references/zitierweise.md` توجه کنید.

## مواد هسته ای

حسابداری جریان سرمایه در طبق DRS 21 جزء اجباری از گزارشات گروه است (§ 297 HGBاین روش غیر مستقیم، نقدی را از پس انداز سالانه با حذف موارد غیرفعال و در نظر گرفتن تغییرات ترازو حسابداری بازمی گردد. § 19 InsO.

## سوالات شروع سرد

1. چه مناسبی؟ شرکت های مالی، طرح بازسازی، گزارش بانک ها یا ساخت داوطلبانه.
2. آیا بازبینی آغاز و پایان، BWA/GuV وجود دارد؟
3. کدام روش - غیر مستقیم (استانداردی) یا مستقیماً (درد بار) ؟
4. چه کنسولیداسیون؟ تک فرد یا گروه
5. اثرات ویژه (فروخت سرمایه، دفع خصوصی و افزایش سرمایه) ؟
6. چه صندوق هایی - نقدی (بانک+صندوق) ، مالی دیگر (بشمول سهام و دارایی ها) ؟
7. چه دوره ای را مقایسه می کنیم؟
8. آدرس: کنترل داخلی، انتشار خارجی، ارزیابی های بازسازی؟

## چارچوب حقوقی

### قوانین اولیه

**§ 297 HGB** - حسابداري گروه؛ محاسبه جریان سرمایه واجب است.

**§ 264 HGB** - حسابداري: جمع بندی تکملي؛ محاسبه پول خودخواه.

**§ 252 HGB** - اصول ارزیابی

**§ 19 Abs. 2 InsO** - پیش بینی باقیمانده با توجه به نقدی.

### استانداردها

- DRS 21 - حسابداري جریان سرمایه (برابر به صورت هر دو مورد در سالنامه ی شرکت؛ مشابه با موارد واحد)
- IDW S 6 - مفهوم بازسازی؛ حسابداری نقدی واجب است.
- IDW PS 305 - تشخیص پیش از خطر
- IAS 7 - گزارشات نقدی (در مورد گزارش بین المللی گروه)

## روند کار

### مرحله 1 - پایگاه داده

- شروع و پایان حسابداری (دو روز پیش)
- GV/BWA دوره
- آینه های سیستم با ورودی، خروج و افا
- حسابداري در مورد تغییر سرمایه
- حساب های جزئی برای موقعیت های فوق العاده.

### مرحله 2 - ساختار DRS 21

```
KAPITALFLUSSRECHNUNG nach DRS 21 (indirekte Methode)

I. CASHFLOW AUS LAUFENDER GESCHAEFTSTAETIGKEIT
 Jahresueberschuss/Fehlbetrag [X]
 +/- Abschreibungen/Zuschreibungen Anlagevermoegen [X]
 +/- Veraenderung Rueckstellungen [X]
 +/- Sonstige nicht-zahlungswirksame Aufwendungen/Ertraege [X]
 +/- Veraenderung Vorraete [X]
 +/- Veraenderung Forderungen LuL [X]
 +/- Veraenderung sonstige Aktiva [X]
 +/- Veraenderung Verbindlichkeiten LuL [X]
 +/- Veraenderung sonstige Passiva [X]
 +/- Gezahlte/Erstattete Ertragsteuern [X]
 = Cashflow aus laufender Geschaeftstaetigkeit [X]

II. CASHFLOW AUS INVESTITIONSTAETIGKEIT
 - Auszahlungen für Investitionen Sachanlagen [X]
 - Auszahlungen für Investitionen immat. WG [X]
 - Auszahlungen für Investitionen Finanzanlagen [X]
 + Einzahlungen aus Abgang Sachanlagen [X]
 + Einzahlungen aus Abgang Finanzanlagen [X]
 = Cashflow aus Investitionstaetigkeit [X]

III. CASHFLOW AUS FINANZIERUNGSTAETIGKEIT
 + Einzahlungen aus Kapitalerhoehung [X]
 + Aufnahme Darlehen Kreditinstitute [X]
 - Tilgung Darlehen Kreditinstitute [X]
 - Ausschuettungen an Gesellschafter [X]
 = Cashflow aus Finanzierungstaetigkeit [X]

IV. VERAENDERUNG FINANZMITTELFONDS [X]
 + Finanzmittelfonds zu Beginn der Periode [X]
 = Finanzmittelfonds am Ende der Periode [X]
```

### مرحله 3 - حرکت های منحرف

| پست ها | تحقیق |
|---|---|
| تغییر در ذخایر | پایان ذخایر مخزن کمتر آغاز (توسع دارایی کاهش نقدی) |
| تغییر مطالبات | مبلغ در پایان minus آغاز (توسع به کاهش نقدی) |
| تغییر بدهی ها | بدهی های پایان minus آغاز (توسع افزایش نقد) |
| کاهش ها | از سطح سرمایه گذاری؛ غیرفعال پرداخت → بازمی گردد |
| تغییر در ذخایر | پس انداز پایان minus آغاز؛ غیرفعال |

### مرحله ۴ - اثرات ویژه

- فروش سرمایه گذاری: تفاوت در ارزش حسابداری/آموزش از فروش به عنوان یک پست ویژه؛ محاسبه سود و بهره های جاری.
- پرداخت ویژه: در فعالیت های مالی، نه در کسب و کار جاری.
- سرمایه گذاری: در فعالیت های مالی، نه درآمد.
- اخراجات: در فعالیت های مالی، هیچ هزینه ای.

### مرحله پنجم: بررسی امکان پذیر بودن

- سالدو نهایی صندوق های مالی = حسابداري "مال نقد" تا روز پایان؟ (باید مطابقت داشته باشد)
- مقایسه سال گذشته: نشان دادن تغییرات غیر معمول
- بررسی تعاملات با تراز حرکتی.

### مرحله 6 - توضیح و ارسال

- توضیح بخش های اصلی در این مقاله (مانند فعالیت سرمایه گذاری)
- در صورت گزارش دادن بانک/سرمایه دار، قالب پیش بینی (یک صفحه و توضیحات)
- مفهوم بازسازی IDW S6: با برنامه 24 ماهه نقدی همراه است.

## استراتژی و نکات عملی

- در مورد شرکت های متوسط: حسابداری جریان سرمایه به صورت استاندارد، بر حسب خواسته ی شریک بانک.
- گزارش های شرکت: تعهد مطابق با DRS 21 - غیر قابل معامله
- در مورد گروه های مبتنی بر IFRS: به طور متوازی IAS 7 را ارائه دهید.
- نکته عملی: نقدی از فعالیت های جاری، شاخص بهره وری ارگانیک است؛ بسیار زیر سالانہ برآمد = مشکل سرمایه کاری.
- StBVV: حسابداري جریان سرمایه به عنوان یک سفارش جداگانه (بزرگ بر صورت سالیانه).
- نوع DATEV: دیتو حسابداری شرکت / مدول سالی با محاسبه جریان سرمایه؛ در صورت ثبت یک واحد، دستکاری.

## منابع و بروزرسانی

حالت: 05/2026.

- HGB §§ 264, 297.
- DRS 21
- IDW S6، IDW PS 305
- IAS 7 (بین المللی)
- InsO § 19.
