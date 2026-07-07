---
name: bilanzieller-status-aufnehmen
description: "Wenn es um Bilanzieller Status aufnehmen in Fortbestehensprognose geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# ثبت وضعیت مالی

## مسیر کار

- روشن‌کردن نقش، هدف و محصول کاری خواسته‌شده: چه کسی اقدام می‌کند، چه تصمیمی در پیش است، چه مهلتی در جریان است و چه خروجی‌ای لازم است؟
- اولین نشانه هایی که باید در مورد مهلت ها و خطرات فوری قرار گیرد: IDW S 11 پیش بینی 12 ماه از تاریخ ثبت، § 15a InsO شش هفته در مورد بدهی های زیاد، سه هفته آزمون افزایش نقدینگی، تازه کاری سالانه.
- بررسی معیارهای مربوط به: InsO § 19 Abs. 2 (مطابق دو مرحله ای) ، IDW S 11 (متطلبات) ، HGB § 252 Abs. 1 Nr. 2 (به نگرانی می رود) BGH II ZR 296/05 (تین هفته فاصله) StaRUG §§ 1، 102 - یافته های مربوط به gesetze-im-internet.de, dejure.org،آفتاب BVerfG-/BGH-/EuGH-دیتابیس زنده را بررسی کنید، بدون نقل قول دانش مدل
- سازمان های مربوطه را تعیین و به درستی مخاطب خود را انتخاب کنند: مدیرعامل، مشاور مالیاتی، حسابرسی، مشاوره در زمینه بازسازی، IV (اگر استخدام شده باشد) ، بانک، شرکت کنندگان.
- جمع آوری اسناد و شواهد، بررسی شکاف ها: گزارش پیش بینی باقیمانده (P&L, BS, CF) 12+ ماهه ، سناریوهای تست استرس زا، مفهوم بازسازی IDW S 6، ارزیابی های تعمیرات، اعلامیه GF - دریافت مدارک از طریق بازرسی پرونده یا درخواست مشتری برای اثبات عدم وجود آنها، چک زنده تغییرات روزانه در استانداردها و شیوه مدیریت.

## هدف

** وضعیت بدهی های بیش از حد، شرط برای بررسی بدهی ها در مورد بی نقصیت** است. § 19 Abs. 2 InsO دو مرحله را جدا کنید:

1. ** وضعیت بدهی های بیش از حد** (نظر سنجه روز تخفیف) دارایی کمتر از مصروف؟
2. ** بدهی های بیش از حد در مورد بی نقص*§ 19 InsO) فقط در صورتی که بدهی های مالی وجود داشته باشد و پیش بینی مثبت برای ادامه زندگی نداشته باشد.

## حسابداري روز بازي

```yaml
stichtag: 2026-05-20 # oder Bilanzstichtag des letzten Jahresabschlusses
bilanzansatz: hgb # hgb / ifrs / mischung

aktiva:
 a-anlagevermoegen:
 immaterielle: 50000
 sachanlagen: 320000
 finanzanlagen: 0
 b-umlaufvermoegen:
 vorraete: 180000
 forderungen-laul: 120000
 sonstige-forderungen: 15000
 fluessige-mittel: 18000
 c-rechnungsabgrenzung: 5000
 aktiva-summe: 708000

passiva:
 a-eigenkapital:
 gezeichnetes-kapital: 25000
 kapitalruecklage: 0
 gewinnruecklagen: 0
 bilanzergebnis: -107000 # negativ
 eigenkapital-summe: -82000 # negativ
 b-rueckstellungen:
 pensionen: 0
 sonstige: 22000
 c-verbindlichkeiten:
 banken: 250000
 lieferanten: 410000
 sonstige: 38000
 steuern: 25000
 sozialversicherung: 45000
 d-rechnungsabgrenzung: 0
 passiva-summe: 708000

bilanzielle-ueberschuldung: ja # Aktiva = Passiva aber EK negativ = bilanzielle Überschuldung
hoehe-bilanzielle-ueberschuldung: 82000
```

## ذخایر خاموش

دارایی هایی که ارزش حسابداری آنها کمتر از ارزشی تجاری است.

```yaml
stille-reserven:
 - position: CNC-Anlage
 buchwert: 95000
 verkehrswert: 180000
 stille-reserve: 85000
 - position: Betriebsgrundstueck
 buchwert: 120000
 verkehrswert: 210000
 stille-reserve: 90000
summe-stille-reserven: 175000
```

## بار خاموش

بدهی هایی که در تراکنش های تجاری غیرمستقیم یا بسیار پایین هستند.

```yaml
stille-lasten:
 - position: Drohende Inanspruchnahme aus Bürgschaft
 bilanziell: 0
 insolvenzrechtlich: 50000
 - position: Pensionsrückstellung Erfüllungsbetrag versus Bilanzwert
 bilanziell: 0
 insolvenzrechtlich: 30000
summe-stille-lasten: 80000
```

## بازپسین در رتبه های واجد شرایط

مطالبات با کاهش درجه بندی (§ 19 Abs. 2 S. 2 InsO) در وضعیت بدهی های زیاد ** غیرفعال می شوند**.

```yaml
qualifizierter-rangruecktritt:
 - glaeubiger: Hauptgesellschafter Karl Mueller
 forderung: Gesellschafterdarlehen vom 15.03.2024
 nennbetrag: 120000
 rangruecktritt-erklaert-am: 2026-05-22
 rangruecktritt-form: notarielle Urkunde # idealtypisch
 bgh-konform: ja # siehe Skill gesellschafterdarlehen-rangrücktritt
```

## وضعیت بدهی های بیش از حد در مورد ورشکستگی

```
Aktiva (Handelsbilanz) 708.000 EUR
+ stille Reserven 175.000 EUR
- stille Lasten -80.000 EUR
= Insolvenzrechtliche Aktiva 803.000 EUR

Passiva (Handelsbilanz) 790.000 EUR (Aktiva minus EK)
- qualifizierter Rangrücktritt -120.000 EUR
= Insolvenzrechtliche Passiva 670.000 EUR

Differenz 133.000 EUR positiv
```

نتیجه: با وجود بدهی های بیش از 82,000 یورو**، پایه ی بیکاری **بسیاری مثبت است** زیرا ذخایر خاموش و کاهش رتبه ها این را خنثی می کند. `annahmen-sammeln-fortfuehrung`).

## نکته های مهم

- در مورد **شركات شخصی بدون مالکیت کامل طبیعی** (به عنوان مثال GmbH و Co. KG (به طور انحصاری با شرکت های مکمل) § 19 InsO به همین ترتیب.
- در مورد **کاسب­فراد** یا شرکت شخصی با مالکیت کامل طبیعی § 19 InsO **غیر قابل اجرا** - واجبیت پرداخت صرفاً از عدم توانایی در پرداخت می شود § 17 InsO.
- تهیه وضعیت **مهمیت مدیرعامل**. در صورت نقص های حسابداری (حالا هیچ موقعیت قابل اجرا نیست) ، فلاس می شود § 283b StGB در نظر گرفته شده است.

## قضیه

- قضیه: هیچ تصمیمی را از دانش نمونه ای نقل نکنید؛ قبل از انتشار با دادگاه، شکل تصمیم گیری و تاریخ آن ها، نشانه های پرونده یا اظهارات قابل اثبات را توسط منبع رسمی یا آزاد تأیید کنید.

## خروجی

- `bilanzieller-status.yaml` با حسابداري روز تخفیف ذخایر، کاهش رتبه بندی و اساس ترازنامه ی نهی شدن.
- اولین اعلامیه ی نتایج (بعد از این که در حق مبلغ ورشکستگی، مثبت یا منفی است).
- توصیه: در صورت ترازو منفی بدون پیش بینی ادامه **مستقیم** وکیل ورشکستگی § 15a InsO مدت شش هفته شروع به اجرا می شود.

## تصمیمات اصلی فعلی - وضعیت مالی

- قضیه: هیچ تصمیمی را از دانش نمونه ای نقل نکنید؛ قبل از انتشار با دادگاه، شکل تصمیم گیری و تاریخ آن ها، نشانه های پرونده یا اظهارات قابل اثبات را توسط منبع رسمی یا آزاد تأیید کنید.

## زنجیره پاراگراف وضعیت مالی

§ 19 Abs. 2 InsO (ظاهر بدهی) § 19 Abs. 2 S. 2 InsO (از رتبه های واجد شرایط دستبرد) § 35 Abs. 1 InsO (معمولی مفهوم ذخایر خاموش) HGB §§ 252-255 (مطابق ارزیابی) → IDW S 11 Rn. 20-42 (تحقیق وضعیت)

## سه بعدی - وضعیت مالی

1. **حساب تاریخ:** ماهیت وضعیت چیست؟ (درحال حاضرترین زمان با داده های حذف شده)
2. **حساب ذخایر ثابت را شناسایی کنید:** زمین ها در برابر ارزش حسابداری به نسبت قیمت تجاری؛ مطالبات با مقایسه با نرخ بازار، سهام.
3. **بایدارهای غیرمستقیم:** بازنشستگی، ضمانت و خسارت های ثابت نشده از معاملات شناور.
4. **حالات اصلاحی را در بر می گیرد؟** وام های شرکت دارایی که از رتبه عقب نشینی، اعلام کارفرما یا سرمایه گذاری دارند - موجود است و یا برنامه ریزی شده اند؟
