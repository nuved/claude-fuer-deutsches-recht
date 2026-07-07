---
name: mermaid-flowchart-pruefung
description: "Wenn es um Mermaid Flowchart Prüfung in Verhältnismäßigkeitsprüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# آزمایش طرح جریان مرموز

## خاشق زمینی

```mermaid
flowchart TD
    A[Eingriff in Grundrecht] --> B{Stufe 1 Legitimer Zweck}
    B -->|verboten| Z1[Verstoss]
    B -->|legitim| C{Stufe 2 Geeignetheit}
    C -->|ungeeignet| Z2[Verstoss]
    C -->|geeignet| D{Stufe 3 Erforderlichkeit}
    D -->|milderes Mittel| Z3[Verstoss]
    D -->|erforderlich| E{Stufe 4 Angemessenheit}
    E -->|unangemessen| Z4[Verstoss]
    E -->|angemessen| OK[Verhaeltnismaessig]
```

## گزینه با محدودیت های مطلق

```mermaid
flowchart TD
    A[Eingriff] --> B[Absolute Grenze pruefen]
    B -->|Wuerde Wesensgehalt| ABS[Ohne Abwaegung verfassungswidrig]
    B -->|kein Verstoss| C{Stufe 1 Zweck}
    C -->|legitim| D{Stufe 2 Geeignet}
    D -->|geeignet| E{Stufe 3 Erforderlich}
    E -->|erforderlich| F{Stufe 4 Angemessen}
    F -->|angemessen| OK[Zulaessig]
```

## متغیر تعهد حفاظت (حظر حداقل)

```mermaid
flowchart TD
    A[Schutzpflicht aus Grundrecht] --> B{Schutzkonzept evident unzureichend?}
    B -->|Ja| Z[Untermassverbot verletzt]
    B -->|Nein| C{Konzept effektiv geprueft?}
    C -->|effektiv| OK[Schutzpflicht erfuellt]
    C -->|ineffektiv| Z2[Nachbesserungspflicht]
```

## نکات استفاده

- در فایل مارک داون بین سه تا بک تیک با شیرخوار قرار گرفته.
- GitHub به طور خودکار Mermaid را در ویکی و نسخه های عادی ارائه می دهد.
- در صورت امتحان، به عنوان یک طرح روی کاغذ قابل تکرار است.
- گره هایی که شماره های موردی برای هر یک از آنها را بررسی می کنند
  در مورد واقعیت.
