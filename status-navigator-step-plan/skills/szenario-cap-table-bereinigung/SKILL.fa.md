---
name: szenario-cap-table-bereinigung
description: "Wenn es um Szenario Cap Table Bereinigung in Plugin: status-navigator-step-plan geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# تصفیه سناریو Cap Table

## نقش و تمرکز
تصحیح چندین جدول Cap متناقض. حالت Navigator، مقایسه کردن CAP با یکدیگر و قرارداد های زیرنویس است

## نمونه ای از کاربرد
لوسیتز (Storage Cap Table) سه نسخه `diskrepanzen-aufdecken`) نشان دهنده نوسان NordCap 48/51/48 %. بررسی نتیجه: هیچ تغییر مستند نشده است؛ v2 از فضای داده NordCap آمده و شامل یک خطای تایپ در کنسورسیوم Stadtwerke Cottbus سهم; v3 نسخه تازه سرمایه گذار اشتباه اصلاح شده است. توصیه Soll-cap table = v3 با اشاره

## ماژول‌های خروجی
- جدول هدف با منبع هر خط
- یادداشت انحراف در مورد نسخه های متفاوت
- انتقال به مهارت `dokumententyp-beschluesse` در صورت تغییر احتمالی
