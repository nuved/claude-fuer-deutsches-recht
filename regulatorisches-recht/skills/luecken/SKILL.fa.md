---
name: luecken
description: "Wenn es um Gap-Tracker in Regulatorisches Recht – Plugin für deutsches geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# ردیاب های گاپ

## مسیر کار

- روشن‌کردن نقش، هدف و محصول کاری خواسته‌شده: چه کسی اقدام می‌کند، چه تصمیمی در پیش است، چه مهلتی در جریان است و چه خروجی‌ای لازم است؟
- نخست علامت‌گذاری مهلت‌ها و خطرهای فوری: تنها از مهلت‌های همان حوزهٔ حقوقی مشخص و همان پرونده استفاده کنید؛ اعتراض (Widerspruch)، دعوا (Klage)، ایراد (Einspruch)، طرق شکایت (Rechtsmittel)، مرور زمان (Verjährung)، سقوط حق (Verwirkung) و مهلت‌های ایراد، اعلام، ثبت و انقضا را به‌دقت جدا کنید و هرگز از حوزهٔ تخصصی دیگری برندارید.
- بررسی معیارهای مربوط به: WpHGاین در حالی است که از نظر آن، می توان به عنوان یک منبع برای اطلاعات و بررسی های مربوطه gesetze-im-internet.de, dejure.org،آفتاب BVerfG-/BGH-/EuGH-دیتابیس زنده را بررسی کنید، بدون نقل قول دانش مدل
- تعیین مرجع صالح و انتخاب درست مخاطب: موکل، طرف مقابل، ادارهٔ صالح یا دادگاه، کارشناسان و در صورت لزوم نهاد اتحادیهٔ اروپا/بین‌المللی (به جزئیات اسکیل نگاه کنید).
- گردآوری اسناد و ادلّه و بررسی خلأها: پرونده‌های اداری، اسناد قراردادی، لوایح، تصمیم‌های اداری (Bescheide)، صورت‌جلسه‌ها، نظرهای کارشناسی و ادلّهٔ بیرونیِ همان حوزه — مدارک نبود را از راه دسترسی به پرونده یا پرسش از موکل فراهم کنید، و برای تغییرهای روزِ قوانین و رویهٔ اداری بررسی زنده انجام دهید.

## ورودی‌ها

- فایل ردیابی گاپ: `~/.claude/plugins/config/claude-fuer-deutsches-recht/regulatorisches-recht/gap-tracker.yaml`
- گزینه ای: فیلتر (به شدت، زمان ، مالکیت و وضعیت)
- گزینه ای: Gap ID برای بروزرسانی هدفمند

## زمان

### ۱. خواندن ردیاب

در صورت عدم وجود آن،
```
Noch keine Gaps erfasst. Starten Sie mit /regulatorisches-recht:lücken-aufzeiger,
um eine Gap-Analyse gegen eine Aufsichtsverlautbarung durchzuführen.
```

### ۲. بررسی وضعیت

```
Gap-Übersicht – Stand: TT.MM.JJJJ

Gesamt: N | 🔴 Blockierend: N | 🟠 Hoch: N | 🟡 Mittel: N | 🟢 Gering: N
Offen: N | In Bearbeitung: N | Geschlossen: N | Überfällig: N
```

### 3- انتشار جدول گاپ مرتب شده

| شناسه گاپ | اعلامیه | نیاز (مجموعه کوتاه) | وزن | مهلت | مالک | وضعیت |
|---|---|---|---|---|---|---|
| گپ ۲۰۲۵-۰۰۱ | موریسک AT 4.3.2 | ذخیره سازی داده ها 10 سال | 🔴 | 31.12.2025 | تعمیل | باز |

دسته بندی: اول 🔴، بعد به بالا رفتن.

### ۴. ارائه ی اقدامات

بر اساس این گزارش:
```
Was möchten Sie tun?
a) Gap schließen (Gap-ID angeben)
b) Eigentümer setzen / ändern
c) Status aktualisieren (offen → in Bearbeitung → geschlossen)
d) Richtlinienneufassung für einen Gap starten → /richtlinien-neufassung
e) Eskalationsnotiz für überfällige Gaps erstellen
f) Alle geschlossenen Gaps archivieren
```

### ۵. به روز رسانی ردیاب ها

ذخیره تغییرات در فایل YAML و یادداشت کردن زمان تغییر

## قضیه فعلی و اصول

- قضیه: هیچ تصمیمی را از دانش نمونه ای نقل نکنید؛ قبل از انتشار با دادگاه، شکل تصمیم گیری و تاریخ آن ها، نشانه های پرونده یا اظهارات قابل اثبات را توسط منبع رسمی یا آزاد تأیید کنید.

## استاندارد های مرکزی (سلسلۀ پاراگراف)

Art. 20 Abs. 3 GG (مرتبط بودن با قانون و حقوق، روشن شدن در مورد حقایق) §§ 133, 157 BGB (قانون های اساسی) § 5 EGBGB (مثل در مورد شکاف های حقوقی در قانون خصوصی) §§ 13, 31 ENWG (تناقضات در استانداردهای تنظیم کننده)

## منابع و نقل قول

به عبارت دیگر: `../../../references/zitierweise.md`

این مهارت تنها اطلاعات ردیابی داخلی را می خواند و نوشته؛ هیچ اقتباس خاصی برای معیارهای مورد نیاز نیست. `luecken-aufzeiger`-باید بریم

## نمونه

** وارد کردن:** `/regulatorisches-recht:lücken`

**درآمدی:**
```
Gap-Übersicht – Stand: 01.06.2025

Gesamt: 7 | 🔴 2 | 🟠 3 | 🟡 2 | 🟢 0
Offen: 5 | In Bearbeitung: 2 | Geschlossen: 0 | Überfällig: 0

| Gap-ID | Verlautbarung | Anforderung | Schwere | Frist | Eigentümer | Status |
|-------------|----------------------|---------------------|---------|------------|-------------|---------------|
| GAP-2025-001| MaRisk AT 4.3.2 | Datenhaltung 10 J. | 🔴 | 31.12.2025 | Compliance | offen |
| GAP-2025-002| MaRisk BTR 3.2 | ESG-Integration | 🔴 | 31.03.2026 | Risiko | in Bearbeitung|
| GAP-2025-003| MaRisk BTO 1.2.4 | Kreditvergabe | 🟠 | 30.06.2026 | Kredit | offen |
```

## خطرات / اشتباهات معمول

- **تراکر قدیمی:** بدون استفاده منظم `luecken-aufzeiger`-جنگ ها که ردیابی می کند، قدیمی است.
- ** مالکیت غیر قابل اجرا:** شکاف های بدون صاحب اعمال نمی شود.
- ** تجاوز بدون افزایش:** برای شکاف های متأخر، گزینه ی نوتیفیکیشن ارتفاع را به طور خودکار برجسته کنید.
