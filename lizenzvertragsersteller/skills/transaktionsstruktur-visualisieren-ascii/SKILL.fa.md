---
name: transaktionsstruktur-visualisieren-ascii
description: "Wenn es um Transaktionsstruktur visualisieren — ASCII in Lizenzvertragsersteller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# تصویر سازی ساختار تراکنش - ASCII

## کنستلاسیون ۱ - مجوز ساده

```
 +-----------------+        Lizenz (IP-Typ)         +-----------------+
 |  Lizenzgeber    | ---> Anlage A IP-Liste -----> |  Lizenznehmer   |
 |  (Licensor)     |                                |  (Licensee)     |
 |                 | <----- Royalty / Pauschale --- |                 |
 +-----------------+                                +-----------------+
```

## کنستلاسیون ۲ - مجوز گروه

```
 +-----------+    Lizenz     +-----------+   Sub-Lizenz   +------------+
 | IP-Holding |--->|  Konzern- |--->| Konzern-   |
 |  GmbH      |              |  Mutter   |              |  Tochter   |
 +-----------+              +-----------+              +------------+
   (Lizenzgeber)            (Hauptlizenz-              (Sub-License,
                             nehmer)                   Definition $ 15 AktG)
```

## کنستلاسیون ۳ - گذرنامه های مختلف (مبادله ی ثبت نام)

```
 +-----------------+   Lizenz Patent A   +-----------------+
 |   Partei A     | -------------------> |   Partei B     |
 |                 | <------------------- |                 |
 +-----------------+   Lizenz Patent B   +-----------------+
   Cross-License, gegenseitig, optional mit Ausgleichszahlung
```

## کنستلاسیون ۴ - مجوز با تضمین

```
                       +-------------------------+
                       |   Bank (Sicherheiten-   |
                       |   nehmer)               |
                       +-------------------------+
                                   ^
                                   | Sicherungsabtretung / Pfandrecht
                                   |
 +-----------------+        Lizenz                +-----------------+
 |  Lizenzgeber    | ---------------------------> |  Lizenznehmer   |
 |  (zugleich      |                              |                 |
 |   Sicherheits-  | <--- Royalty + Sicherheit -- |                 |
 |   geber)        |                              |                 |
 +-----------------+                              +-----------------+
```

## کنستلاسیون پنجم - منبع کد اسکرو

```
 +-----------------+        Lizenz Software       +-----------------+
 |  Lizenzgeber    | ---------------------------> |  Lizenznehmer   |
 +-----------------+                              +-----------------+
       |                                                 ^
       | Hinterlegung Source Code                        | Release bei
       v + Build-Anweisungen                             | Trigger:
 +-------------------+                                   | - Insolvenz LG
 |   Escrow Agent    | --- Release bei Trigger ----------+ - Wartungs-
 |   (Verwahrer)     |                                   |   ausfall
 +-------------------+                                   | - VertragsendeBruch
```

## مجموعه ۶ - پوتین پول (FRAND)

```
                 +-------------------------+
                 |   Pool-Administrator    |
                 +-------------------------+
                     |        |        |
                   ----------       ----
            +-----+|+-----+ +-----+|+-----+
            | Pat |||| Pat ||| Pat ||| ... |
            | A   |||| B   ||| C   |||     |
            +-----+|+-----+ +-----+|+-----+
                     |        |
            FRAND-Lizenz an   Streitschlichtung
            Implementierer    + Kartellrecht
```

## یادداشت‌ها

- تیرها جریان مجوز و پول هستند، هدفمند.
- باکس ها حزب هایی هستند که نقش دارند.
- تضمین/حقوق مبلمان (با `^/v`).
- خط ورشکستگی به طور صریح مشخص شده است.

## اتصال

- ماژول خروجی: `output-vertrag-deutsch-fertigentwurf` (تازه رو به عنوان یک کتاب بزرگ میذاره)
- دو زبان: `output-zweisprachig-bilingual-deutsch-englisch`
