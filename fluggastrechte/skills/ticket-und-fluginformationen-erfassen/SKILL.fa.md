---
name: ticket-und-fluginformationen-erfassen
description: "Wenn es um Ticket- und Fluginformationen erfassen in Fluggastrechte geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# اطلاعات بلیط و پرواز را جمع آوری کنید

## ورودی‌ها

چه چیزی می تواند آپلود شود:

- ** تایید کتاب بندی** به صورت PDF / ایمیل.
- **تکتی الکترونیکی** با تنظیمات استاندارد IATA
- ** گذرگاه سوار شدن** عکس یا پی دی اف
- ** اطلاع خطری** از طرف هواپیمایی.
- **مراسل با هواپیمای (برنامه ایمیل)
- ** اسناد سفر مجزا** در صورت رزرو از طریق سازمان مسافرتی.

## رشته های واجب

برای هر قسمت پرواز:

```yaml
fall-id: FG-2026-0042
reisedatum: 2026-05-12
passagiere:
 - name: Mueller, Hans
 geburtsdatum: 1972-08-15
 rolle: hauptbuchender
 - name: Mueller, Eva
 geburtsdatum: 1975-03-22
 rolle: ehepartner
 - name: Mueller, Lea
 geburtsdatum: 2010-06-18
 rolle: minderjährig

buchungscode: ABC123 # PNR
buchung-bei: Lufthansa # vermarktende Airline
buchungsdatum: 2026-04-12

flug:
 flugnummer: LH 1234 # Code des operating carrier
 operating-carrier: Lufthansa
 marketing-carrier: Lufthansa
 abflughafen: MUC (München)
 zielflughafen: LIS (Lissabon)
 geplante-abflugzeit: 2026-05-12T08:25:00+02:00
 geplante-ankunftszeit: 2026-05-12T11:00:00+01:00
 tatsaechliche-abflugzeit: null
 tatsaechliche-ankunftszeit: null
 flugklasse: economy
 distanz-km: 2280 # Skill `distanz-und-ausgleich-berechnen`

stoerung:
 art: annullierung # annullierung / verspätung / nichtbefoerderung / umbuchung / abweichender-flug
 bekanntgabe-am: 2026-05-12T06:30:00+02:00
 bekanntgabe-wie: SMS # SMS / E-Mail / Schalter-Mitteilung
 begruendung-airline: technischer Defekt
 ersatzangebot: Flug am 13.05.2026 LH 1234
 ersatz-tatsaechlich-genutzt: ja

belege:
 - typ: buchungsbestätigung
 pfad: belege/2026-05-12/buchung-LH1234.pdf
 - typ: boardingpass
 pfad: belege/2026-05-12/boardingpass-mueller.pdf
 - typ: stoerungsbenachrichtigung
 pfad: belege/2026-05-12/sms-annullierung.png
 - typ: ersatzboardingpass
 pfad: belege/2026-05-13/boardingpass-mueller-ersatz.pdf
```

## استخراج OCR / PDF

- برای بلیط های PDF، استخراج خودکار از شماره پرواز PNR تاریخ و فرودگاه.
- در صورت اثبات تصویری OCR، اگر اعتبار کمتر از ۹۰ درصد باشد پرچم بازرسان برای تأیید دستی.
- کد های IATA (LH BA AF AZ) و کد فرودگاه ها (FRA MUC CDG MAD) را در مقابل لیست استاندارد معتبر کنید.

## مقایسه اطلاعات عمومی

- ** زمان برنامه ریزی پرواز** وقت های تایید رزرو - معتبر.
- ** زمان موجود** می توانید از پرچم گذرنامه ی فرودگاه، پیامک های کوتاه و ایمیل با اطلاع رسانی در مورد تاخیر استفاده کنید.
- منابع عمومی مربوط به مصرف کنندگان، بطور منظم ** واجب پرداخت و غیر مجاز** (FlightAware FlightRadar24 وغیرہ) هستند؛ در این بحث شواهد مهم است که ** تایید ورود هواپیمایی** و اطلاع رسمی ** تاخیر/لغو شدن پرواز**.
- در صورت زمان واقعی متناقض: توصیه ** دستاویزات دستی روز رویداد** (تصاویر صفحه نمایش پیامک) به عنوان شواهد بعدی.

## تصمیمات اصلی جمع آوری اطلاعات

- قضیه: هیچ تصمیمی را از دانش نمونه ای نقل نکنید؛ قبل از انتشار با دادگاه، شکل تصمیم گیری و تاریخ آن ها، نشانه های پرونده یا اظهارات قابل اثبات را توسط منبع رسمی یا آزاد تأیید کنید.

## خروجی

- `fallakte.yaml` با تمام داده های اصلی.
- `belegliste.md` با پرچم معاینه برای شواهد فاقد اثبات.
- `naechste-schritte.md` توصیه به مهارت های بعدی (`annullierung-oder-verspaetung-einordnen`).

## چند مسافر

در هر پرواز، یک مورد حقوق با چندین مسافر ثبت می شود. اما هر مسافری دارای حق تعویض خاص خود است** (Art. 7 VO 261/2004 در این صورت، هر مسافر درخواست خود را می کند (ممکنه است یک اتحادیه باشد). `vollmacht-familienmitglieder`.
آډیت ۲۷05.2026
بررسی قانونی در صورت زنده: هیچ تصمیمی را از دانش نمونه ای نقل نکنید؛ قبل از انتشار با دادگاه، شکل تصمیم گیری، تاریخ و نشانه های پرونده ها و اظهارات قابل تحمل توسط منبع رسمی یا آزاد تأیید کنید.
موضوع واقعی dejure.org: Pešková و Peška/Travel Service - ضربات پرنده به عنوان یک شرایط غیر معمول i.S.v. Art. 5 Abs. 3 VO 261/2004.
اقدام: با موضوع و مکان صحیح EU:C:2017:342 جایگزین کنید.
-->

## قوانین و رویهٔ قضایی

به طور مشخص باید بررسی شود:

- VO (EG) Nr. 261/2004 (حقوق پرواز)
- Art. 5 VO 261/2004 (تغییر)
- Art. 6 VO 261/2004 (تأخیر)
- Art. 7 VO 261/2004 (حساب پرداخت 250/400/600 یورو)
- EuGH در مورد این موضوع، ما می خواهیم که به نظر برسد.
