---
name: stufenbaum-ascii-art
description: "Wenn es um Stufenbaum als ASCII-Visualisierung in Verhältnismäßigkeitsprüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# درخت مرحله ای به عنوان تصویربرداری ASCII

> نمایش فشرده شده کل ساخت و ساز آزمون. قابل چاپ، می تواند به صورت نوشته ای ضمیمه شود، برای کار روی تخته استفاده میشود

## درختان کامل

```
                  +-----------------------------------+
                  |  GRUNDRECHTSPRUEFUNG               |
                  +-----------------------------------+
                                |
                                v
 +-----------------------------+------------------------------+
 |  Vorpruefung                                               |
 |   1. Schutzbereich eroeffnet? (persoenlich + sachlich)      |
 |   2. Eingriff (klassisch oder modern)?                     |
 |   3. Schranke vorhanden (Vorbehalt oder verfassungsimm.)?  |
 +-----------------------------+------------------------------+
                                |
                                v
 +-----------------------------+------------------------------+
 |  Formelle Verfassungsmaessigkeit                            |
 |   - Kompetenz, Verfahren, Form                              |
 |   - Bestimmtheit / Normklarheit                             |
 |   - Wesentlichkeitstheorie / Parlamentsvorbehalt            |
 |   - Zitiergebot Art 19 I 2 GG                               |
 +-----------------------------+------------------------------+
                                |
                                v
 +-----------------------------+------------------------------+
 |  Materielle Verfassungsmaessigkeit: Schranken-Schranke      |
 +-----------------------------+------------------------------+
                                |
                                v
            +-------------------+-------------------+
            |                                       |
   +--------+--------+                     +--------+--------+
   | Stufe 1         |                     | Stufe 2         |
   | Legitimer Zweck |                     | Geeignetheit    |
   +--------+--------+                     +--------+--------+
            |                                       |
            +-------------------+-------------------+
                                |
                                v
            +-------------------+-------------------+
            |                                       |
   +--------+--------+                     +--------+--------+
   | Stufe 3         |                     | Stufe 4         |
   | Erforderlichkeit|                     | Angemessenheit  |
   +--------+--------+                     +--------+--------+
            |                                       |
            +-------------------+-------------------+
                                |
                                v
 +-----------------------------+------------------------------+
 |  Absolute Grenzen (Pruefung endet hier, wenn verletzt)      |
 |   * Menschenwuerde Art 1 I GG (Objektformel)                |
 |   * Wesensgehalt Art 19 II GG (Kernbereich)                 |
 |   * Existenzminimum Art 1 I iVm Art 20 I GG                 |
 +-----------------------------+------------------------------+
                                |
                                v
                  +-----------------------------------+
                  |  Ergebnis: verfassungsmaessig?     |
                  +-----------------------------------+
```

## درخت کوتاه برای زراعت های متنی

```
[Schutzbereich] -> [Eingriff] -> [Schranke]
    -> [Bestimmtheit/Wesentlichkeit/Zitiergebot]
    -> [Zweck] -> [Geeignet] -> [Erforderlich] -> [Angemessen]
    -> [Absolute Grenzen]
    -> [Ergebnis]
```

## درخت کمان برای کار در صفحه

```
+ Eingriffsmassnahme ?
|
+--- Schutzbereich beruehrt ?
|       +--- nein  -> Pruefung endet
|       +--- ja    -> weiter
|
+--- Eingriff ?
|       +--- nein  -> Pruefung endet
|       +--- ja    -> weiter
|
+--- Schranke einschlaegig ?
|       +--- vorbehaltlos -> verfassungsimmanente Schranke ?
|       +--- einfach      -> jedes verf.maessige Gesetz
|       +--- qualifiziert -> nur fuer genannte Zwecke
|
+--- Bestimmtheit / Wesentlichkeit / Zitiergebot ?
|       +--- nein -> verfassungswidrig
|       +--- ja   -> weiter
|
+--- Stufen 1-4 ?
|       +--- Zweck            -> legitim ?
|       +--- Geeignet         -> foerdert Zweck ?
|       +--- Erforderlich     -> milderes Mittel ?
|       +--- Angemessen       -> Abwaegung ?
|
+--- Absolute Grenzen ?
|       +--- Wuerde / Wesensgehalt / Existenzminimum
+--- Ergebnis
```

## استفاده

- در نوشته های قبل از قسمت امتحان به عنوان راهنما قرار دهید.
- در آزمون ها به عنوان کمک داخلی برای طبقه بندی (نه کپی کردن در بخش امتحان)
- در آموزش ها به عنوان یک صفحه با یادداشت های موردی

## خویشاوند

- `mermaid-flowchart-pruefung` برای نسخه ی مرموز.
- `ascii-pruefungsschema` برای نسخه کمپیکت جدول.
- `padlet-vier-stufen-tafel` برای همکاری در تیم.
