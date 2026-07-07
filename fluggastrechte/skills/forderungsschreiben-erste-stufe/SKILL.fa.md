---
name: forderungsschreiben-erste-stufe
description: "Wenn es um Forderungsschreiben Erste Stufe in Fluggastrechte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

```

Der Skill `fluggastrechte-anlagen-bauen` liest die im Schriftsatz erwähnten Anlagen in Reihenfolge der Erwähnung, konvertiert jede Rohdatei zu PDF, stempelt oben rechts in Arial 12 FETT (= Helvetica-Bold 12pt) den Bezeichner "Anlage K 1", "Anlage K 2" usw. und benennt die Ausgabedatei nach demselben Schema (`Anlage_K_1.pdf`). Optional wird ein Sammel-PDF mit Schriftsatz vorne und durchlaufenden Lesezeichen erzeugt.
