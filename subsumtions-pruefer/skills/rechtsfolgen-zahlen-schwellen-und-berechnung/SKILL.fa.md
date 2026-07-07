---
name: rechtsfolgen-zahlen-schwellen-und-berechnung
description: "Wenn es um Rechtsfolgen: Zahlen, Schwellenwerte und Berechnung in Subsumtions-Prüfer geht: rechnet Schwellen, Beträge, Varianten und Kontrollannahmen durch; liefert eine Berechnungstabelle mit Schwellen, Annahmen und Kontrollfragen."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# پیامدهای قانونی: اعداد، محدودیت ها و محاسبه

## مسیر کار

- روشن‌کردن نقش، هدف و محصول کاری خواسته‌شده: چه کسی اقدام می‌کند، چه تصمیمی در پیش است، چه مهلتی در جریان است و چه خروجی‌ای لازم است؟
- نخست علامت‌گذاری مهلت‌ها و خطرهای فوری: تنها از مهلت‌های همان حوزهٔ حقوقی مشخص و همان پرونده استفاده کنید؛ اعتراض (Widerspruch)، دعوا (Klage)، ایراد (Einspruch)، طرق شکایت (Rechtsmittel)، مرور زمان (Verjährung)، سقوط حق (Verwirkung) و مهلت‌های ایراد، اعلام، ثبت و انقضا را به‌دقت جدا کنید و هرگز از حوزهٔ تخصصی دیگری برندارید.
- راستی‌آزماییِ قوانینِ پایه: قوانینِ مرتبط در زمینهٔ افزونه را به‌صورت زنده در gesetze-im-internet.de، dejure.org، eur-lex.europa.eu و درگاه‌های رسمی فدرال/ایالتی بررسی کنید — نشانی مآخذ را در gesetze-im-internet.de، dejure.org، openJur و پایگاه‌های BVerfG/BGH/EuGH به‌صورت زنده وارسی کنید؛ هیچ استنادِ برخاسته از دانش مدل نیاورید.
- تعیین مرجع صالح و انتخاب درست مخاطب: موکل، طرف مقابل، ادارهٔ صالح یا دادگاه، کارشناسان و در صورت لزوم نهاد اتحادیهٔ اروپا/بین‌المللی (به جزئیات اسکیل نگاه کنید).
- گردآوری اسناد و ادلّه و بررسی خلأها: پرونده‌های اداری، اسناد قراردادی، لوایح، تصمیم‌های اداری (Bescheide)، صورت‌جلسه‌ها، نظرهای کارشناسی و ادلّهٔ بیرونیِ همان حوزه — مدارک نبود را از راه دسترسی به پرونده یا پرسش از موکل فراهم کنید، و برای تغییرهای روزِ قوانین و رویهٔ اداری بررسی زنده انجام دهید.

## محدوده های مهم و مبالغ قانونی (حال: دانش مدل؛ بررسی زنده)

| منطقه | حد / مقدار | استاندارد | منبع |
|---|---|---|---|
| صلاحیت AG / LG | تا 5 هزار یورو AGاز 5 هزار یورو LG | §§ 23، 71 GVG | gesetze-im-internet.de |
| مبلغ درخواست | 600 یورو | § 511 Abs. 2 Nr. 1 ZPO | gesetze-im-internet.de |
| شرکت های کوچک | 22000 یورو (از سال 2025: 25،000 دلار) | § 19 UStG | بررسی زنده gesetze-im-internet.de |
| DSGVO-دوباره به حد بالا. | 20 میلیون یورو یا 4 درصد درآمد سالانه | Art. 83 Abs. 5 DSGVO | eur-lex.europa.eu |
| سود بازده | نرخ بهره پایه + 5 پیپ (§ 288 Abs. 1 BGB); + 9 PP برای B2B (§ 288 Abs. 2 BGB) | §§ 288, 247 BGB | gesetze-im-internet.de; Bundesbank.de (حساب بهره اولیه) |
| ضمانت اجاره تا حد زیادی | ۳ اجاره های خالص سرد | § 551 BGB | gesetze-im-internet.de |
| خسارت | هیچ مقدار قانونی نیست؛ § 1a KSchG: 0.5 ماه/سال درآمد | § 1a KSchG | بررسی زنده |
| پول درد | هیچ طرحی نیست؛ از نظر عدالت | § 253 Abs. 2 BGB | BGH-حقیقت را زنده بررسی کنید |

## طرح های محاسبه

### طرح 1 - سود تاخیر

```
Hauptforderung: EUR X
Fälligkeit: TT.MM.JJJJ (bei Mahnung oder vertraglicher Bestimmung)
Verzugsbeginn: Mahnung (§ 286 Abs. 1 BGB) oder 30 Tage nach Fälligkeit (§ 286 Abs. 3 BGB)
Zinssatz: Basiszinssatz (Bundesbank.de, aktuell prüfen) + 5 PP (B2C) / + 9 PP (B2B)
Zinsen pro Tag: Hauptforderung × Zinssatz / 365
Gesamtzinsen: Zinsen pro Tag × Anzahl Tage Verzug
```

### طرح 2 - خسارت § 249 BGB

```
Naturalrestitution (§ 249 Abs. 1 BGB): Zustand wie ohne schädigendes Ereignis
Differenzschaden: Vermögen mit schädigendem Ereignis vs. ohne
Positiver Schaden (damnum emergens): tatsächlich entstandene Kosten
Entgangener Gewinn (lucrum cessans): § 252 BGB; üblicher Gewinn oder wahrscheinliche Entwicklung
Abzug: Mitverschulden § 254 BGB; Vorteilsausgleichung
```

### جدول 3 - RVG-تولیه (والد؛ بررسی زنده)

```
Streitwert (§ 2 RVG) → Gebührentabelle (Anlage 2 RVG)
Geschäftsgebühr (Nr. 2300 RVG VV): 0,5–2,5; Regelgebühr 1,3
Verfahrensgebühr (Nr. 3100 RVG VV): 1,3
Terminsgebühr (Nr. 3104 RVG VV): 1,2
Einigungsgebühr (Nr. 1000, 1003 RVG VV): 1,5
Hinweis: RVG-Tabellen und Gebührensätze live prüfen unter gesetze-im-internet.de (RVG Anlage 2)
```

## محاسبه ارزش اختلاف

- دعوی در مورد خدمات: ارزش داعشی = درخواست دادخواست
- درخواست دریافت: تخفیف (BGH: حدود ۲۰ تا ۸۰ درصد از اصلیت قابل محاسبه؛ بررسی زنده)
- دعوی تخلیه: اجاره سالانه (§ 9 ZPO)
- شکایت عدم رعایت: منافع کلی متقاضیان؛ بدون طرحی سخت

## نقطهٔ ورود

اگر اسناد وجود داشته باشد، ابتدا از آنها استفاده کنید. فقط سؤالات را بپرسید که مسیر بعدی رو تغییر دهند:

1. چه نوع قانونی را باید محاسبه کنیم (عوض، سود، جریمه و هزینه ها) ؟
2. چه ارقام و داده هایی وجود دارد (تعریف اصلی، زمان بندی، نرخ سود پایه) ؟
3. آیا این در نظر گرفته شده توسط مقامات است یا شواهد تخمین زده می شود؟
4. چه اسناد، اسعار و نمودار هایی این اعداد را نشان می دهند؟
5. چه محصولی مورد نیاز است: محاسبه در فایل، اطلاعات مشتری، جدول؟

## روند کار

1. ** تصویر موردی:** به یک ماتریس کوتاه، موقعیت ها و نقشها و زمان بندی و اعداد را در نظر بگیرید.
2. ** چارچوب های حقوقی:** بررسی استانداردهای قانونی و حسابداری
3. **در حال بررسی نکات آزمون:** چه مبالغ هایی تضمین شده اند؟
4. ** ارزیابی ریسک:** سبز/ زرد/ قرمز با دلایل، مفروضات و راه های جایگزین.
5. ** ساخت ارتباط:** پیشنهاد مهارت های مناسب دیگر.
