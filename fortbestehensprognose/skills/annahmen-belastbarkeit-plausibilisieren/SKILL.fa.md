---
name: annahmen-belastbarkeit-plausibilisieren
description: "Wenn es um Annahmen plausibilisieren in Fortbestehensprognose geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# فرضیه ها را توجّه کنید

## مسیر کار

- روشن‌کردن نقش، هدف و محصول کاری خواسته‌شده: چه کسی اقدام می‌کند، چه تصمیمی در پیش است، چه مهلتی در جریان است و چه خروجی‌ای لازم است؟
- اولین نشانه هایی که باید در مورد مهلت ها و خطرات فوری قرار گیرد: IDW S 11 پیش بینی 12 ماه از تاریخ ثبت، § 15a InsO شش هفته در مورد بدهی های زیاد، سه هفته آزمون افزایش نقدینگی، تازه کاری سالانه.
- بررسی معیارهای مربوط به: InsO § 19 Abs. 2 (مطابق دو مرحله ای) ، IDW S 11 (متطلبات) ، HGB § 252 Abs. 1 Nr. 2 (به نگرانی می رود) BGH II ZR 296/05 (تین هفته فاصله) StaRUG §§ 1، 102 - یافته های مربوط به gesetze-im-internet.de, dejure.org،آفتاب BVerfG-/BGH-/EuGH-دیتابیس زنده را بررسی کنید، بدون نقل قول دانش مدل
- سازمان های مربوطه را تعیین و به درستی مخاطب خود را انتخاب کنند: مدیرعامل، مشاور مالیاتی، حسابرسی، مشاوره در زمینه بازسازی، IV (اگر استخدام شده باشد) ، بانک، شرکت کنندگان.
- جمع آوری اسناد و شواهد، بررسی شکاف ها: گزارش پیش بینی باقیمانده (P&L, BS, CF) 12+ ماهه ، سناریوهای تست استرس زا، مفهوم بازسازی IDW S 6، ارزیابی های تعمیرات، اعلامیه GF - دریافت مدارک از طریق بازرسی پرونده یا درخواست مشتری برای اثبات عدم وجود آنها، چک زنده تغییرات روزانه در استانداردها و شیوه مدیریت.

## فراسورهای آزمایش به صورت پذیرش

### ۱. مقایسه با گذشته

- آیا این پذیرش با ** سه سال گذشته** BWA / SuSa/ حسابداری سالانه مطابقت دارد؟
- در صورت تغییر، آیا این تغییرات به طور مشخصی توجیه شده است؟
- در صورت تغییر چشم انداز خوش بینی ** بدون دلیل جدید**: کاهش به سطح تاریخی در سناریو پلازی.

### ۲. توسعه بازار و صنعت

- **در حال حاضر شاخص صنعتی** وجود دارد؟ (به عنوان مثال، آفو شاخص اقلیم تجاری DESTATIS اعداد صنعت).
- **مجموعه سفارشات صنعت**
- ** شاخص های ماکرو** نرخ بهره اقتصادی قیمت انرژی

### 3- ثبات داخلی

- فروش افزایش می یابد، اما هزینه مواد ثابت خواهد ماند؟
- هزینه های نیروی کار افزایش می یابد اما تعداد افراد کاهش پیدا می کند؟
- سرمایه کاری به سرعت بهبود می یابد؟

### ۴- اثبات بودن اقدامات

- آیا اثر اصلاحات موثر است؟
- آیا زمان بندی واقعی است (به عنوان مثال، 60 روز تعطیل محل) ؟
- آیا هزینه های یک بار واقعی است؟

### ۵. توافق های ثالث

- بیانیه های کارفرما / نامهای تسلیحاتی: قبلاً امضا شده یا فقط در حال مذاکره است؟
- وام های شرکت دارایی که از رتبه عقب نشینی می کنند: آیا سند ثبت نام وجود دارد؟
- اعتراضی بانکی: به صورت نوشتاری یا شفاهی؟

## پلاکایبیتی با توجه به پذیرش

```yaml
plausibilisierung:
 - annahme-id: umsatz-hauptsegment
 band: realistisch # konservativ / realistisch / ambitioniert / nicht-belastbar
 begruendung: |
 Auftragsbestand bis 09/2026 belegt; ab 10/2026 Modellfortschreibung
 auf Basis Vorjahr +3%
 risiko: mittel
 sensitivitaet-szenario:
 negativ: 10% Umsatzrückgang ab 10/2026
 effekt-eur: -190000 (kumuliert)

 - annahme-id: kostensenkung-standort
 band: ambitioniert
 begruendung: |
 Kündigung Standortmietvertrag erfordert 9-Monats-Kündigungsfrist;
 Schliessung bis 08/2026 nur möglich wenn Mieter Aufhebung akzeptiert.
 Aktuell in Verhandlung — nicht belegt.
 risiko: hoch
 sensitivitaet-szenario:
 negativ: Schliessung gelingt nicht im Planhorizont
 effekt-eur: 50000 monatliche Mehrkosten

 - annahme-id: bankenzusage-erhöhung-kreditlinie
 band: nicht-belastbar
 begruendung: |
 Verhandlung mit Bank laeuft. Bisher keine schriftliche Zusage.
 Bank verweist auf laufendes Rating-Verfahren.
 risiko: hoch
 sensitivitaet-szenario:
 negativ: Kreditlinie wird nicht erhöht
 effekt-eur: keine zusätzliche Liquidität 80000 EUR
```

## میزان محافظه کار

پیش بینی های دوام، جای خوش بینانه ای نیست.BGH-Rspr* * نیاز به یک اندازه گیری محتاط و معمولی دارد.

- در صورت تردید، فرضیه های محافظه کار را انتخاب کنید.
- اگر یک پیش بینی ** امتیجیت شده** یا ** غیر قابل تحمل* باشد و برای نتیجه ی پیشبینی مهم است: نتایج آن ** غیرقابل استفاده* به عنوان پیش بینی مثبت ادامه می باشند.

## سناریوهای حساسیت

```yaml
szenarien:
 basisszenario:
 annahmen: alle wie in annahmen.yaml
 ergebnis-12-monate-liquiditaet: positiv
 bemerkung: Plan-Szenario

 negativ-szenario:
 annahmen: alle ambitioniert-Annahmen reduziert auf konservativ
 ergebnis-12-monate-liquiditaet: knapp positiv # vor Maßnahmen
 bemerkung: Risiko-Szenario; bei Eintritt sind Zusatzmaßnahmen erforderlich

 stress-szenario:
 annahmen: zusätzlich Wegfall Top-Kunde
 ergebnis-12-monate-liquiditaet: negativ
 bemerkung: Reines Stress-Szenario; in der Plausibilisierung
 als unwahrscheinlich eingeschaetzt
```

## موارد خاص

### ذخایر خاموشی که برای تمدید استفاده می شود

اگر وضعیت ذخایر خاموش را در بر دارد (ملاحظه) `bilanzieller-status-aufnehmen`) باید نقدی را از طریق فروش به صورت واقعی بدست آورد:

- آیا ارزیابی های ترافیک وجود دارد؟
- واقعاً در افق نقشه قابل فروش؟
- تاثیر بر فعالیت (به عنوان مثال فروش یک ماشین منجر به خرابی در تولید می شود) ؟

### نامه های تسلی بخش

- ** نرم ترین کمفورت* (بهترین تلاش) در حالت ** غیر** باید مورد توجه قرار گیرد.
- **قرارنامه ی سخت کارفرما* با تخفیف در صورت ورشکستگی قابل توجه است - ببینید مهارت `patronatserklaerung-extern-hart-erzeugen`.

## خروجی

- `plausibilisierung.md` با هر فرض ارزیابی می شود (بند حساسیت خطر).
- سه سناریوی (بزنس منفی استرس) با نتیجه نهایی.
- توصیه: برای بیش از دو فرضیه غیر قابل تحمل یا بلند پروازانه که نتیجه را به ارمغان می آورند، پیش بینی ** نه مثبت** باید ارزیابی شود.
- فهرست اقدامات خاص برای بهبود انعطاف پذیری (تغییر کردن هزینه)

## تصمیمات اصلی فعلی - فرضیه های پلاسبی

- قضیه: هیچ تصمیمی را از دانش نمونه ای نقل نکنید؛ قبل از انتشار با دادگاه، شکل تصمیم گیری و تاریخ آن ها، نشانه های پرونده یا اظهارات قابل اثبات را توسط منبع رسمی یا آزاد تأیید کنید.

## خط پاراگراف فرضیه

§ 19 Abs. 2 InsO (توقع زنده ماندن) § 15b InsO (حساب پذیری در صورت پیش بینی اشتباه) → IDW S 11 Rn. 45 ff. (مطابق با کیفیت) → IDW S 6 Rn. 90 ff. (مطالعه ی بازیافت)

## سه بعدی - بررسی فرضیه

قبل از شروع، آماده کنید:

1. ** آزمون ثبات:** آیا رشد درآمدی با هزینه های نیروی کار و مواد سازگار است؟ (بازده +10 درصد بدون افزایش کارکنان از زمان استفاده کامل → نامناسب)
2. **موازنه گذشته:** در سه سال اخیر چه میزان رشد واقعی به دست آمده است؟
3. ** تست حساسیت:** چه فرضیه ای بسیار مهم است؟ اگر مشتری اصلی ۲۰ درصد کاهش یابد، چی می شود؟
4. ** سناریوی مورد اول:** پیش بینی حتی با بدترین فرضیه ها هم مثبت است؟

## قوانین و رویهٔ قضایی

### کتابخانهٔ گزیدهٔ قوانین

- § 43 GmbHG
- § 3a EStG
- § 102 StaRUG
- § 266a StGB
- § 1 StaRUG
- § 93 AktG
- § 2 HRG
- § 4 HRG
- § 7 HRG
- § 15 HRG
- § 16 HRG
- § 70 VwG

### آرای راهنما

- BGH II ZR 296/05
- BGH IX ZR 285/14
- BGH IX ZR 56/22
- BGH II ZR 206/22
- BGH IV ZR 66/25
