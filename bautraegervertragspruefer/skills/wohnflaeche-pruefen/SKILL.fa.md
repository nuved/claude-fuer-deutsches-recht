---
name: wohnflaeche-pruefen
description: "Wenn es um Wohnfläche prüfen in Bauträgervertragspruefer geht: rechnet Schwellen, Beträge, Varianten und Kontrollannahmen durch; liefert eine Berechnungstabelle mit Schwellen, Annahmen und Kontrollfragen."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# بررسی مساحت زندگی

## وقتی این مهارت به دست می آید

هر گونه ذکر مسکونی در قرارداد یا توضیحات ساختمان، به ویژه اگر فقط "تقریباً" نوشته شود، روش محاسبه را از دست داده و یک کلوزی تحمل وجود دارد.

## قوانین اجباری

- ماده 633 BGB: عدم وجود مادی در صورتی که شرایط توافق شده - اینجا مکان سکونت- از دست رفته باشد.
- ماده 307 BGB: شقوعی تحمل شکلی که توافق نامه ی شکل و نوع مساحت زندگی را تضعیف می کند، غیرفعال است. روش محاسبه و محدودیت انحراف باید آشکار شود
- ماده 650k، بند 2 BGB: عدم وضوح در مورد مساحت زندگی و روش محاسبه به زیان سازنده است.
- قانون مساحت زندگی (WoFlV): استاندارد برای مساحات سکونت و اغلب به صورت قراردادی از آن پیمان می شود.
- DIN 277: روش حسابداری جایگزین با نتایج دیگر؛ ترکیب بدون تعیین مشخص باعث عدم شفافیت می شود.

## فرستر های آزمایش

1. ** روش محاسبه**: WoFlV یا DIN 277؟ میتود گمشده باوسول شکاف است؛ مشکوک به پارagraf 650k (2) BGB در این صورت، روش سودمندتر برای خریدار مورد استفاده قرار می گیرد.
2. ** لیست اتاق ها**: آیا همه ی فضای مربوطه (خزانۀ نشیمن، خوابگاه، آشپزخانه، حمام، بالکان/برزوی متفرقه، زیرزمین و خلاء) با مساحت های جداگانه مشخص شده است؟
3. **کلاژول تحمل**: قرارداد چه تضمینی را در نظر می گیرد؟ BGB به طور انتقادی؛ پیش از انتشار زنده، وضعیت قضایی را بررسی کنید.
4. **تغییر مساحت پس از اتمام**: در صورت انحراف بیش از مقدار تحمل - حق کاهش طبق بند 634 BGB در ارتباط با بند 633 BGB.
5. ** بالکان، تراس و لوجیا**: حسابداری سهمی به موجب WoFlV معمولا 25 تا 50 درصد؛ بررسی مقررات مختلف قرارداد.
6. ** مکان و حق استفاده ویژه**: محل زندگی متعلق به مساحت نیست؛ جداسازی واضح را نیاز دارد.
7. **موضوع بهره وری انرژی**: مساحت زندگی بر اثبات مصرف برق، حمایت از خودروها و محاسبه هزینه های عملیاتی تاثیر می گذارد؛ انحراف دارای پیامدهای اقتصادی است.

## آرای راهنما

هیچ منبع تایید نشده BGH-قرارهای مربوط به محدودیت تحمل در قراردادهای سازنده، از طریق میگاپرومپتر منتشر شده است.

## محصول کار

جدول آزمون مساحت های زندگی با مقایسه هدف، محاسبه تحمل و حق کاهش ggf. درخواست حذف شقایق تحمل

## سنگ ساختمانی نمونه ای

```text
Wohnflächen-Prüfung

Vereinbarte Wohnfläche (Vertrag):      [X m² nach WoFlV / DIN 277 / Methode unklar]
Berechnungsgrundlage im Vertrag:       [WoFlV / DIN 277 / fehlend → Bausoll-Lücke nach Paragraf 650k Absatz 2 BGB]
Tatsächlich gemessene Fläche:          [Y m² nach [Methode] gemessen am [Datum] durch [Sachverständiger]]
Abweichung:                            [Z m² entsprechen [Prozent] der vereinbarten Fläche]
Toleranzklausel im Vertrag:            [Originalwortlaut; Ampel wenn über Bagatellbereich]

Minderungsberechnung (bei erheblicher Abweichung):
Kaufpreis: EUR X. Minderungsquote: [Prozent] × EUR X = Minderungsbetrag EUR Y.
Rückforderungsanspruch: EUR Y (sofern bereits vollständig gezahlt).

Streichungsverlangen:
Die Toleranzklausel "[Originalwortlaut]" ist nach Paragraf 307 BGB unwirksam, weil sie die vereinbarte Wohnfläche als Beschaffenheitsmerkmal praktisch entwertet. Bitte streichen Sie die Klausel. Für unvermeidbare Messungenauigkeiten ist eine Toleranz von maximal [X Prozent] mit klarer Methoden- und Raumliste ausreichend.
```
