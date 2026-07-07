---
name: regulatorik-mandatssteckbrief-behoerden-fristen
description: "Wenn es um Regulatorisches Mandat: Behörden, Fristen und Rollen in Regulatorisches Recht – Plugin für deutsches geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# مأموریت های نظارتی: مقامات، زمان بندی و نقش

## هدف

این مهارت برای مدیریت فضای کار اجباری شرکت های متعدد است. در قانون نظارتی، "اجازه" به طور معمول:
- یک قانون خاص که به مشتری توصیه می شود (به عنوان مثال اجرای MaRisk Novella)
- یک روش باز برای مشاوره و ارائه نظر
- یک بررسی BaFin یا تحلیل DORA-GAP برای مشتری خاص
- یک روش یا درخواست تعیین سرپایه به مقامات

**استفاده کنندگان داخلی:** این مهارت مربوط نیست.

## ورودی‌ها

- پروفایل فعال عمل با فضای کار اجباری فعال
 - فرمانده فرعي: `new | لیست | تغییر | بسته شدن | هیچکدوم 
- گزینه: نام کاربری، نامزد، حوزه قضایی، زمان

## زمان

### فرمانده فرعي: `neu`

پرسش:
```
1. Mandant (intern: nur Kürzel, kein vollständiger Name in Logs)
2. Mandat-Bezeichnung / Slug (z. B. bafin-prüfung-2025-mandantA)
3. Art des Mandats:
   a) Gap-Analyse gegen Regulierungsakt
   b) Konsultationsbeitrag
   c) Richtlinienneufassung
   d) Behördenanfrage
   e) Sonstiges
4. Zuständige Behörde(n)
5. Leitfrist (falls bekannt)
```

دستور العمل را ایجاد کنید:
```
~/.claude/plugins/config/claude-fuer-deutsches-recht/regulatorisches-recht/mandate/<mandat-slug>/
├── mandat.md          # Mandat-Fakten und Übersteuerungen
├── gap-tracker.yaml   # Mandat-spezifische Gaps
├── comment-tracker.yaml
└── verification-log.md
```

`mandat.md` طرح:
```markdown
# Mandat: [Bezeichnung]
Erstellt: [TT.MM.JJJJ]
Mandant: [Kürzel]
Art: [Typ]
Behörde(n): [Liste]
Leitfrist: [TT.MM.JJJJ]
Status: aktiv

## Mandat-spezifische Fakten
[Abweichungen vom Praxisprofil; Mandant-spezifische Materialitätsschwelle usw.]

## Datenschutz-Hinweis
§ 43a Abs. 2 BRAO, § 203 StGB. Dieser Ordner enthält mandantenbezogene Daten.
Cross-Mandat-Kontext: deaktiviert (Standard).
```

### فرمانده فرعي: `auflisten`

تمام دستورات را فهرست کنید:
```
Aktive Mandate:
| Slug | Mandant | Art | Behörde | Leitfrist | Status |
|---|---|---|---|---|---|
| bafin-prüfung-2025-A | Mandant A | Gap-Analyse | BaFin | 31.12.2025 | aktiv |
```

### فرمانده فرعي: `wechseln`

```
Zu welchem Mandat wechseln?
[Liste der aktiven Mandate anzeigen]
```
پس از انتخاب: قرار دادن ماموریت فعال در پروفایل. مهارت ها را اکنون بخوانید `mandat.md` این فرمان را.

### فرمانده فرعي: `schließen`

```
Mandat [Slug] schließen?
Hinweis: Dateien bleiben erhalten. Status wird auf 'geschlossen' gesetzt.
Lernerkenntnisse ins Praxisprofil übertragen? (ja/nein)
```

### فرمانده فرعي: `keiner`

مهار فعال را غیرفعال کنید → مهارت ها به سطح عملی باز می گردند.

## منابع و نقل قول

به عبارت دیگر: `../../../references/zitierweise.md`

قوانین مربوط به حقوق حرفه ای:
- § 43a Abs. 2 BRAO (مطالب به حفظ صراحت)
- § 203 StGB (تخلف راز خصوصی)
- § 50 BRAO (در پرونده ها)
- BORA § 2 (استقلال) § 6 (حرف دست)

## قالب خروجی

- تایید اقدام (تخلیق / تغییر/ پایان)
- وضعیت فعلی ورکسپیس
- قدم بعدی توصیه شده (مانند "مندت فعال - شروع کنید با `/regulatorisches-recht:lücken-aufzeiger`")

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **الزامِ تمام‌نویسی و استانداردِ قالب.** محصولِ نهایی در **جمله‌های کامل و تمام‌نوشته** تحویل می‌شود — نه اسکلتِ کلیدواژه، نه تنهٔ خالیِ شرط، نه صرفِ فهرست. شرط‌ها به‌صورتِ جمله‌های تمام‌نوشتهٔ بیان‌گرِ اثرِ حقوقی می‌آیند؛ جای‌گیرها مانند `[Name der Mandantin]` روشن علامت می‌خورند و متنِ پیرامون کامل می‌ماند.
>
> **شکلِ نوشتار:** هرگاه لایحه، قرارداد، یادداشت، تصمیم، ومرک یا هر سندِ نهاییِ دیگر به‌صورتِ DOCX، PDF یا متنِ قالب‌بندی‌شده بیرون داده شود، باید **Times New Roman ۱۱ pt** به‌عنوانِ قلمِ پایه به‌کار رود. عنوان‌ها در همان قلم می‌مانند و تنها می‌توانند سیاه (بولد) یا پلکانی باشند. در خروجیِ صرفاً Markdown یا چت، این خواستهٔ قالب به‌عنوانِ یادداشتِ برون‌سپاری درج می‌شود.
>
> **شماره‌گذاری:** ساختاربندی منحصراً اعشاری (`1`، `1.1`، `1.1.1` و به همین ترتیب). بدون اعداد رومی، بدون ساختاربندی حرفی یا آمیخته.
<!-- END ausformulierungspflicht (autogen) -->

## نمونه

** وارد کردن:** `/regulatorisches-recht:regulatorisches-recht-mandat-arbeitsbereich neu`

**درآمدی:**
```
Neues Mandat anlegen.

Mandant-Kürzel (nur intern sichtbar): MandantA
Mandat-Bezeichnung: MaRisk-GAP-2025-MandantA
Art: Gap-Analyse
Zuständige Behörde: BaFin
Leitfrist: 31.12.2025

Mandat angelegt unter:
~/.../mandate/mairisk-gap-2025-mandanta/

Aktives Mandat: MaRisk-GAP-2025-MandantA

Nächster Schritt: /regulatorisches-recht:lücken-aufzeiger
```

## خطرات / اشتباهات معمول

- **مطابق عبور از دستورات به طور تصادفی فعال شد:** مهارت ها هرگز نباید اطلاعات را در میان ماموریتها متصل کنند، اگر زمینه انتقال از دستوراتی غیرفعال باشد (بعد از استاندارد).
- ** نام های مشخص در مسیرها:** از نامهای روشن مشتری استفاده نکنید. فقط لنک بندی کنید
- **منتظرات غیر بسته:**تفتیش و پایان دادن به مهلت های فعال قدیمی بدون زمان مشخص؛ جلوگیری از اشتباه با اطلاعات زمینه ای کهنه شده.
- ** راز فرمانده:** محتویات `mandat.md` و ردیاب های اختصاصی به دستورات، با اطمینان از § 43a Abs. 2 BRAOهرگز به صورت مشترک یا پروتکل صادر نکنید.
## قضیه فعلی و اصول

- قضیه: هیچ تصمیمی را از دانش نمونه ای نقل نکنید؛ قبل از انتشار با دادگاه، شکل تصمیم گیری و تاریخ آن ها، نشانه های پرونده یا اظهارات قابل اثبات را توسط منبع رسمی یا آزاد تأیید کنید.

**نوردهای اصلی:** §§ 611-630 BGB (عقد خدمات، قانون فرماندهی) §§ 48-49 VwVfG — §§ 3-7 BORA (قانون حرفه ای و حقوق انتخاب شده)

- قانون منبع: ادبیات فقط با منابع کاربر یا دسترسی زنده مجاز؛ هیچ جای برای یافتن نظرات، کتابچه و مقاله از دانش مدل نیست.
