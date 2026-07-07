---
name: dsfa-rechenschaftspflicht-art-5-ii
description: "Wenn es um DSFA-Dokumentation und Rechenschaftspflicht in Datenschutzrecht geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# اسناد DSFA و پاسخگویی

## این ماژول کِی کمک می‌کند

- پس از تکمیل DSFA، قبل از ثبت
- در صورت درخواست نظارت برای ارائه DSFA
- در صورت انجام حسابرسی توسط DSB یا بازرس های خارجی
- در صورت تغییر DSB یا مسئول - انتقال پرونده
- در صورت تغییر اساسی (ورژن)

## چارچوب حقوقی

- Art. 5 Abs. 2 DSGVO: پاسخگویی - مسئول باید بتواند اثبات کند که اصول اساسی را رعایت کرده است.
- Art. 24 DSGVO: مسئولیت مسئول پردازش
- Art. 30 DSGVO: فهرست فعالیت های پردازش - مرجع DSFA
- Art. 35 Abs. 11 DSGVO: نیاز به بازرسی
- Art. 58 Abs. 1 lit. a DSGVO: اختیار اطلاع رسانی از نظارت
- § 257 HGB, § 147 AO برای زمان نگهداری اسناد تجاری و مالیاتی - DSFA یک سند نیست بلکه به فعالیت های پردازش مرتبط است.

## روش 6 مرحله

1. **صفحه ی پردازش.** چه فرآیند هایی؟
2. **تحققی از تناسب.**حساب اینکه چه اسنادی در پرونده های DSFA قرار دارند - کامل بودن بدون بارگذاری.
3. **تحلیلی از ریسک* * بررسی خطرات اثبات شده - امضا، نسخه های گمشده، تاریخ بندی ها و مسئولیتهای نامعلومه.
4. ** اقدامات* * پرونده های ساختاری در قالب استاندارد (دجیتال امضا شده، با تاریخ و نسخه)
5. **خطر باقیمانده.** ارزیابی ارزش اثبات شده - DSFA در روش های نظارت چقدر امن است؟
6. **مشاوره/ازمویل.** DSB تصدیق کاملیت؛ حفظ و دسترسی را تنظیم می کند.

## ساختار پرونده DSFA

```
DSFA-AKTE Aktenzeichen: [VV-XX-DSFA-YYYY-NN]
Verarbeitung: [BEZEICHNUNG]
Verantwortlicher: [NAME]
DSB: [NAME]

01 Deckblatt mit Versionshistorie
02 Schwellwertanalyse / Triage-Vermerk (Skill dsfa-art-35-dsgvo-trigger-und-anwendungsbereich)
03 Listenabgleich (Skill dsfa-bfdi-und-laender-blacklist)
04 WP-248-Pruefung (Skill dsfa-edpb-leitlinien-9-19-anwendung)
05 Methodenwahl-Memo (Skill dsfa-methodik-cnil-pia-vs-bsfd-bsi)
06 Vollstaendige DSFA (Skill dsfa-template-deutsch-vollvorlage)
07 Risikomatrix (Skill dsfa-risikoanalyse-eintrittswahrscheinlichkeit-schaden)
08 TIA falls Drittlandtransfer (Skill dsfa-für-internationale-datentransfers)
09 KI-FRIA falls Hochrisiko-KI (Skill dsfa-für-ki-systeme-schnittstelle-art-26-kivo)
10 Stakeholder-Konsultation (Skill dsfa-stakeholder-konsultation-art-35-9)
11 DSB-Stellungnahme
12 Vorabkonsultation Art. 36 (falls erfolgt)
13 Freigabe Verantwortlicher
14 Verweis Verarbeitungsverzeichnis Art. 30
15 Revisionsplan (Skill dsfa-update-bei-aenderungen-und-revision)
16 Korrespondenz mit Aufsichtsbehoerde (falls)
17 Beweismittel: Datenflussdiagramm, AVV, SCC, TOM-Konzept

Versionsverzeichnis
| Version | Datum | Aenderung | Autor | Freigabe |

Zugriffskonzept
- Lesend: [Liste der berechtigten Personen]
- Schreibend: [Verantwortlicher, DSB, dokumentierender Mitarbeiter]
- Aufsichtsbehoerde: auf Anforderung Vollzugriff
```

## قوانین نگهداری

- DSFA باید در طول تمام مدت کار پردازش حفظ شود.
- پس از پایان پردازش، حداقل برای مدت زمان ممکن است حق های خود را به دست آورند (Art. 82 DSGVO- توصیه: 5 سال پس از پایان پردازش؛ اغلب 10 سال در اداره های دولتی.
- نسخه های قدیمی را حذف نکنید، بلکه آن ها را ذخیره کنید.
- در صورت تغییر ارائه دهنده: انتقال پرونده ها، از جمله تمام نسخه های آن.
- در مورد پردازش های مربوط به مالیات ggf. § 147 AO ده سال

## معیارهای اثبات شده

- تاریخ و امضای هر سند
- نسخه سازی و تاریخ تغییر
- نویسنده بودن واضح (چه کسی مستند کرده، چه کس تصمیم گرفته؟)
- جلسه DSB با تاریخ مستند
- فهرست منابع (ملاحظات نظارت، دستورالعمل ها و قضیه)
- اشاره به دفترچه و AVV

## خطاهای رایج

- DSFA در ورودی نامه منتشر می شود، اما نه به صورت یک پرونده ساختاری.
- نسخه ها به صورت تکراری نوشته می شوند، و نسخه های قدیمی از بین رفته اند.
- این کار فقط به صورت کلامی انجام می شود، هیچ مدرکی نیست.
- نشانه های ثبت نام از دست رفته - DSFA قابل تشخیص نیست.
- مدت زمان نگهداری تعریف نشده - DSFA با اسناد کارکنان از بین می رود.
- حق دسترسی بدون مقررات - DSFA با مشخصات ریسک شخصی قابل مشاهده است.
- مدارک (تاریخ جریان داده ها) همراه نیست - DSFA به صورت انتزاعی باقی می ماند.

## وضعیت منابع 06/2026

- Art. 5 Abs. 2 DSGVO
- Art. 24, 30, 35, 58, 82 DSGVO
- § 147 AO; § 257 HGB (مدت های مربوطه)
- دستورالعمل های EDSA WP 248 rev.01
- BfDI / مقامات دولتی - اطلاعات مربوط به پاسخگویی
- قضیه: اقتباس از تصمیم به دانش مدل نیست؛ قبل از انتشار تایید
- ادبیات: مکان های نظرات و مقالات فقط با منبع خود
