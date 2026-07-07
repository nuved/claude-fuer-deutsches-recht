---
name: dsfa-update-bei-aenderungen-und-revision
description: "Wenn es um DSFA Update bei Änderungen und Revision in Datenschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# DSFA در حال بروزرسانی و اصلاح

## این ماژول کِی کمک می‌کند

- در صورتی که اهداف پردازش تغییر کند
- در مورد پردازنده جدید یا فرعی
- در صورت انتقال جدید به کشور خارج از کشور
- در مورد تکنولوژی جدید (مودول هوش مصنوعی، بیومتری)
- در مورد یک دسته داده جدید یا گروه مربوطه
- در مورد جریمه های جدید یا شیوه ی نظارتی
- در صورت مقدار داده های بسیار طولانی یا زمان نگهداری
- در صورت وقوع (Art. 33 - بازبینی ارزیابی ریسک

## چارچوب حقوقی

- Art. 35 Abs. 11 DSGVO: مدیر، در صورت لزوم یک بررسی را انجام می دهد تا ارزیابی کند که آیا پردازش مطابق با DSFA انجام شده است؛ حداقل اگر خطر مربوط به فرآیندها تغییر یابد.
- Art. 5 Abs. 2 DSGVO پاسخگویی - تاریخچه نسخه و دلیل بررسی مجدد.
- Art. 30 DSGVO در این بخش، فهرست پردازش - تغییرات باید نمایش داده شود.
- دستورالعمل های EDSA WP 248 rev.01.

## روش 6 مرحله

1. **صفحه ی پردازش.**حالی حال کار را ثبت کنید و با نسخه ی DSFA مستند مقایسه نمایید.
2. **حساب تناسب* * تغییر مهم؟
 - هدف جدید یا گم شده
 - دسته بندی جدید داده ها
 - دریافت کنندگان جدید یا انتقال های جدیدی به کشورهای دیگر
 - تکنولوژی جدید
 - مدت نگهداری جدید (> 50 درصد تمدید)
 - تغییر در نظر گرفتن مقامات نظارتی یا قوانین
3. **تحقیق ریسک* *تحلیل مجدد خطر با روش مهارت های اولیه DSFA؛ ماترسیز خطرات قبل و بعد از اقدامات دوباره.
4. ** اقدامات* * بررسی اینکه آیا اقداماتی که در حال انجام هستند کافی است یا باید به آن ها پاسخ داده شود.
5. **خطر بازده* * مقایسه ریسک های قدیمی با جدید ggf. جدید Art. 36 مشورت
6. **معاونیت / مجوز.** DSB شنیدن، انتشار و نسخه سازی؛ ورژن های قدیمی را بایگانی کنید نه حذف.

## متن نمونه / قالب برنامه بازبینی

```
DSFA-REVISIONSPLAN [DATUM]

Verarbeitung: [BEZEICHNUNG]
DSFA-Version aktuell: [X.Y]
DSFA-Version neu: [X.Y+1]
Verantwortlicher: [NAME]

1. Aenderungsanlass
[ ] Zweckaenderung
[ ] Neue Datenkategorie
[ ] Neuer Empfaenger / Sub-AV
[ ] Neuer Drittlandtransfer
[ ] Neue Technologie (z. B. KI-Modul)
[ ] Aufbewahrungsfrist
[ ] Rechtsprechungs- / Aufsichtspraxis-Update
[ ] Vorfall (Art. 33 DSGVO)
[ ] Routine-Revision (Datum: [DATUM])

2. Aenderungsanalyse
[Konkrete Beschreibung der Aenderung im Vergleich zur Vorversion]

3. Auswirkungen auf Schwellwertanalyse
[ ] Schwellwert unveraendert
[ ] Schwellwert neu erreicht (z. B. neues EDSA-Kriterium)
[ ] Schwellwert entfallen (z. B. Anonymisierung)

4. Risikoreassessment
- Risiken neu identifiziert: [Liste]
- Risikomatrix aktualisiert: ja / nein
- Restrisiko aendert sich: ja / nein
- Vorab-Konsultation Art. 36 ggf. neu erforderlich: ja / nein

5. Massnahmen
[Liste der zusaetzlichen oder geaenderten Massnahmen]

6. Freigabe
- DSB-Anhörung: [Datum, Stellungnahme]
- Genehmigung Verantwortlicher: [Name, Datum]
- Aufsicht informiert (falls Art. 36): [Datum]
- Eintrag Verarbeitungsverzeichnis aktualisiert: [Datum]
- Naechste Routine-Revision: [DATUM]

Unterschrift Verantwortlicher: ____________________
Unterschrift DSB: ____________________

Versionshistorie
| Version | Datum | Aenderung | Autor | Freigabe |
| 1.0 | [...] | Erstfassung | [...] | [...] |
| 1.1 | [...] | [...] | [...] | [...] |
| 2.0 | [...] | [...] | [...] | [...] |
```

## میزان بازبینی توصیه شده

- بازبینی معمول: یک بار در سال، حتی اگر هیچ تغییری نداشته باشد.
- بازبینی مربوط به موقع: پیش بینی نشده پس از تحریک
- پردازش های هوش مصنوعی: هر شش ماه (به دلیل تغییرات مدل و داده)
- در این زمینه، BetrVG-حساب نامه: پس از هر توافق عملیاتی
- انتقال به کشورهای دیگر: پس از هر نتیجه گیری یا بروزرسانی EDSA

## خطاهای رایج

- DSFA یک بار ایجاد می شود و هرگز به روز نمی گردد - نقض در برابر Art. 35 Abs. 11 DSGVO.
- تغییرات در سند اصلی نوشته می شود - تاریخچه نسخه از دست داده می شود.
- بازبینی روتینی را از دست داده می شود چون هیچ تغییری نکرده است - بدون مستند سازی، اثبات نمی کند.
- در واقع، تگ ها به روند مدیریت تغییر ادغام نمی شوند.
- بر اساس تعداد داده ها (Art. 33) از DSFA بررسی نمی شود.
- تازه سازی مدل هوش مصنوعی به عنوان یک محرک شناخته نمی شود.

## وضعیت منابع 06/2026

- Art. 35 Abs. 11 DSGVO
- Art. 5 Abs. 2, Art. 30, Art. 33 DSGVO
- دستورالعمل های EDSA WP 248 rev.01
- تصمیمه ای از نظر سازمان EDSA 28/2024 برای مدل های هوش مصنوعی (اپدیت تگگر)
- BfDI / مقامات دولتی - دستورالعمل های قانونی
- قضیه: اقتباس از تصمیم به دانش مدل نیست؛ قبل از انتشار تایید
- ادبیات: مکان های نظرات و مقالات فقط با منبع خود
