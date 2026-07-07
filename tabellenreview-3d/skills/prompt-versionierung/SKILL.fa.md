---
name: prompt-versionierung
description: "Wenn es um /tabellenreview-3d:prompt-versionierung in Tabellenreview 3D geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. Auswahlstichwort: Prompt Versionierung; Arbeitsfeld: Tabellenreview 3D."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# /tablereview-3d: نسخه فوری

## سه بعدی در آغاز

1. این عملیات به چه قسمت از ریشه سه بعدی مربوطه؟
2. آیا عملیات مورد بررسی قرار می گیرد؟
3. آیا نتیجه این کار در دستور العمل ثبت می شود؟
4. آیا باید به وظایف مراقبت حرفه ای احترام بگذاریم؟§ 43 BRAO, § 50 BRAO)

## اصول حقوقی

- قضیه: هیچ تصمیمی را از دانش نمونه ای نقل نکنید؛ قبل از انتشار با دادگاه، شکل تصمیم گیری و تاریخ آن ها، نشانه های پرونده یا اظهارات قابل اثبات را توسط منبع رسمی یا آزاد تأیید کنید.

## طرح ورژن

اسم ورژن سیمانیک در هر پرامپت: `<spalte-id>@<major>.<minor>.<patch>`

### پیچ (`x.y.Z+1`)

- وحدت های متن بدون تغییر در معنی (خطای تایپ / اصلاح سبک / مثال)
- سلول های موجود غیر معتبر
- توصیه: حفظ سلول های موجود

### (مناور)`x.Y+1.0`)

- تغییر نوع پاسخ (به عنوان مثال متن آزاد به جواب بله-نه)
- تغییر قانون ضیاع (توانین تعویض)
- اضافه کردن ابعاد پاسخ (به عنوان مثال، دریافت درآمدی اضافی به صورت یورو)
- سلول های موجود به `nachprüfen` قرار داده شده
- توصیه: باز کردن کالم های آسیب دیده (تولید جزئي)

### (مگروه)`X+1.0.0`)

- تغییر در ابعاد آزمایش (به عنوان مثال، کالم "فعالیت TCDD" به "فعالی" و "نظام قابل اجرا TCDS) تقسیم می شود.
- نام کالم یا ترکیب
- سلول های موجود را غیرفعال می کنند
- توصیه: سلول های تحت تاثیر را کاملاً دوباره محاسبه کنید

## فعال کردن و غیرفعال سازی

- فقط یک نسخه در هر کالم همزمان فعال است (`aktive-prompts.yaml`)
- نسخه های قدیمی در `prompt-historie.yaml` با `gültig-bis`-موعد
- تغییر دادن پرامپتی فعال، مسیر مهاجرت سلول های موجود را وارد می کند.

## فیلرهای لازم برای نسخه فوری

```yaml
- spalte-id: change-of-control
 version: "2.1.0"
 wortlaut: |
 Enthält der Vertrag eine Klausel die bei Kontrollwechsel ...
 antworttyp: zitat-mit-fundstelle-und-schwelle
 ampel-regel:
 rot: "Klausel vorhanden + harte Kündigungsfolge ohne Heilung"
 gelb: "Zustimmungsvorbehalt mit unklarer Schwelle"
 gruen: "Keine Klausel oder branchenübliche Schwelle"
 geaendert-am: "2026-05-20"
 geaendert-von: "anwalt-x"
 migrationspfad: "Patch-Änderung — bestehende Zellen behalten gültig."
```

## یکپارچه سازی با مسیر حسابرسی

هر تغییر فوری باعث ایجاد یک `prompt.geändert` واردات در `audit-trail-protokoll` با شماره نسخه و دلیل.

## مرزها

نسخه سازی از پیام های بد جلوگیری نمی کند، بلکه آنها را به چشم می گذارد. معاینه کننده تصمیم می گیرد که آیا مهاجرت لازم است یا نه.
