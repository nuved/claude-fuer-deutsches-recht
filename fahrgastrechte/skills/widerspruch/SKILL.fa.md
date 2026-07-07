---
name: widerspruch
description: "Wenn es um Fahrgastrechte-Widerspruch — Skill in Fahrgastrechte geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# اعتراض بر حقوق مسافر - مهارت

## اسناد ورودی

کاربر معمولا سه سند را اپلود می کند:

1. **خطای انکار DB** - نامه ای که در آن DB درخواست را رد می کند (PDF یا عکس).
2. ** درخواست اصلی** - فرم یا تایید حق مسافرتی که توسط کاربر پر شده است (PDF، عکس و تصویر).
3. **تکیت / بلیط** - تکیه اصلی به عنوان اثبات رزرو (PDF از اپلیکیشن DB، اسکن یا عکس)

اسناد می توانند به صورت PDF (دیجیتیل یا اسکن شده) ، عکس های صفحه نمایش و تصاویر باشند. اگر کیفیت کافی برای استخراج اطلاعات مربوطه نباشد، از کاربر بخواهید داده هایی را که در دست نیست وارد کند.

## روند کار

### مرحله ی ۱: شناسایی و خواندن اسناد

فایل های بارگذاری شده را ببینید. هر سند رو شناسایی کنید:

- ** نامه های رد کننده نشان می دهد:** فرستنده "حقای مسافرتی مرکز خدمات"، "DB Dialog" یا محل EVU مشابه؛ عبارت هایی مانند "متأسفانه ما نمی توانیم درخواست شما را برآورده کنیم".
- **حساب درخواست:** اطلاعات فرم با داده های اتصال، تاخیر و IBAN.
- **تکیت را شناسایی کنید:** شماره رزرو (PNR / رقم سفارش) ، اتصال قطار، نرخ سفر, تاریخ سفر و جزئیات ارتباط.

در صورت تصاویر / اسکرین شاټ ها: محتوای را مستقیماً از زمینه بخوانید. برای پی دی اف های سکن شده با استخراج متن ضعیف، صفحات را به عنوان عکس ارائه و ارزیابی بصری کنید.

### مرحله دوم: استخراج داده های مرتبط

از این سه سند، اطلاعات زیر را جمع آوری کنید:

** از بلیط:**

- نوع بلیط: فلیکس، قیمت تخفیف، Super Sparpreis, تکیه بهرنکارد، Germanyticket
- شماره ثبت نام / رقم سفارش
- تاریخ سفر
- اتصال ثبت شده (ازخروج → ورود، نقل و حرکت، شماره قطار)
- قیمت
- پیوند قطار بله/نه (فلیکس قیمت = هیچ اتصال قطار → ارتباطات جایگزین مجاز است)
- کلاس ۱/۲
- مسافران:
- در صورت رقابت با EVU bahn.de (به صورت کتاب)

** از درخواست:**

- ارتباط در معرض خطر است
- تاخیر در رسیدن به هدف نهایی
- تاریخ درخواست
- مبلغ معاوضه/تعدی که درخواست شده است
- هزینه های غذا، تاکسی و هتل

**از نامه رد:**

- شماره ثبت نام / رقم عمل
- تاریخ ارسال
- دلیل معینی برای انکار (نویس دقیق)
- کارگری (اگر مشخص شده)
- آدرس پاسخ

### مرحله سوم: تحلیل حقوقی

برای این افزونه، مرجع را بخوانید (`references/vo-2021-782-uebersicht.md`, `references/evo-2023-uebersicht.md`, `references/db-tarif-und-agb.md`) و به ویژه مشورت می کند `skills/db-ablehnungsgruende-pruefen/SKILL.md` برای این نمونه رد.

نکته های اصلی این تحلیل:

1. ** زمان تأخیر را بررسی کنید:** از 60 دقیقه = 25 درصد قیمت سفر، 120 دقیقه = 50٪.
2. ** شناسایی و رد کردن دلیل عدم پذیرش** - نشان دادن در هر ثبت `db-ablehnungsgruende-pruefen`.
3. **تنظیم نوع بلیط:**
   - قیمت انعطاف پذیر: هیچ اتصال قطار نیست → مسافران می توانند هر ارتباطی را در مسیر بگیرند.
   - هزینه صرفه جویی: پابند شدن با قطار اما در صورت تاخیر پیش بینی شده > 20 دقیقه (دستگاه 9 BB DB) حذف می شود
   - تکیت آلمان / نقشه زمان: پرداخت هزینه های تمام شده به صورت تعرفه (ببینید) `db-tarif-und-agb.md`).
4. ** حقوق مراقبت، تاکسی و هتل:** Art. 18 Abs. 3 (توقتی 100 دقیقه برای حمل و نقل شخصی) Art. 20 (ساعدگی 60 دقیقه) § 11 EVO (SPNV، 20 دقیقه در حد و حداکثر 120 یورو).
5. **آزاد شدن Art. 19 Abs. 10 VO:** اعتصاب کارکنان DB، اقدامات اپراتورهای زیرساخت به طور واضح هیچ دلیل آزادی نیست.

### مرحله 4: ایجاد نامه اعتراض

این نامه به صورت سند ساختاری در قالب زیر تهیه می شود:

```
[Name und Adresse der/des Reisenden — aus dem Ticket/Antrag]
[Tel] [E-Mail]
[IBAN]

                                    DB Dialog GmbH
                                    Servicecenter Fahrgastrechte
                                    60647 Frankfurt am Main

[Ort], den [aktuelles Datum]

Betreff: Widerspruch gegen Ablehnung meines Entschädigungsantrags
         Aktenzeichen / Vorgangsnummer: [Nummer aus dem Ablehnungsschreiben]
         Mein Schreiben vom [Datum des Ursprungsantrags]
         Ihr Ablehnungsschreiben vom [Datum]

Sehr geehrte Damen und Herren,

[Absatz 1: Bezugnahme]
mit Schreiben vom [Datum] haben Sie meinen Entschädigungsantrag mit dem
Aktenzeichen [Vorgangsnummer] abgelehnt. Gegen diese Entscheidung lege ich
hiermit Widerspruch ein.

[Absatz 2: Sachverhaltsdarstellung]
Am [Datum] reiste ich mit dem [Zug + Nummer] von [Abfahrtsbahnhof] nach
[Zielbahnhof]. Planmäßige Ankunft war um [HH:MM]. Tatsächlich erreichte
ich das Ziel erst um [HH:MM], was einer Verspätung von [X] Minuten am
Zielort entspricht (gemessen an der Türöffnung am Bahnsteig, Art. 3 Nr. 18
VO (EU) 2021/782).

[Absatz 3 — nur bei Bedarf: Flexpreis-Argument]
Bei meinem Ticket handelt es sich um ein Flexpreis-Ticket ohne Zugbindung.
Ich war daher berechtigt, jeden beliebigen Zug auf meiner gebuchten Strecke
zu nutzen. Die in Ihrem Ablehnungsschreiben angeführte Argumentation, ich
hätte eine andere als die gebuchte Verbindung genutzt, geht ins Leere.
Maßgeblich ist ausschließlich die Verspätung am Zielbahnhof.

[Absatz 3 alternativ — Sparpreis mit Zugbindungsaufhebung]
Zwar handelt es sich um ein Sparpreis-Ticket mit grundsätzlicher Zugbindung.
Da jedoch bereits am Abfahrtsbahnhof eine Verspätung von mehr als 20 Minuten
am Zielort absehbar war, wurde die Zugbindung gemäß Ziffer 9 der
Beförderungsbedingungen der Deutschen Bahn aufgehoben. Ich war berechtigt,
einen alternativen Zug zu nutzen.

[Absatz 4: Rechtliche Begründung]
Gemäß Art. 19 Abs. 1 [lit. a / lit. b] VO (EU) 2021/782 steht mir bei einer
Verspätung von mehr als [60 / 120] Minuten am Zielort eine Entschädigung in
Höhe von [25 / 50] Prozent des Fahrpreises zu. Der von Ihnen angeführte
Ablehnungsgrund "[Grund zitieren]" steht diesem Anspruch nicht entgegen, da
[konkrete Gegenargumentation aus db-ablehnungsgruende-pruefen — mit
Pinpoint auf den entsprechenden Artikel der VO 2021/782 oder § der EVO].

[Absatz 5 — falls Verpflegung / Hotel / Eigenbeförderung]
Darüber hinaus steht mir gemäß [Art. 20 / Art. 18 Abs. 3 Unterabs. 2] VO
(EU) 2021/782 [eine angemessene Verpflegung / eine eigenständige Beförderung]
zu. Da mir [diese von Ihnen nicht bereitgestellt wurde / Sie binnen 100
Minuten keine Alternativverbindung mitgeteilt haben], war ich gezwungen,
[Verpflegung im Wert von / Ersatzbeförderung im Wert von] [Betrag] EUR
selbst zu beschaffen. Ich bitte um Erstattung dieser Kosten.

[Absatz 6: Forderung und Frist]
Ich bitte Sie, meinen Widerspruch innerhalb von vier Wochen ab Zugang dieses
Schreibens zu prüfen und mir die zustehende Entschädigung in Höhe von
[Gesamtbetrag] EUR auf das in meinem ursprünglichen Antrag genannte Konto
zu überweisen.

Sollte meinem Widerspruch nicht entsprochen werden, behalte ich mir vor,
die Schlichtungsstelle Reise & Verkehr e.V. (vormals söp — Schlichtungs-
stelle für den öffentlichen Personenverkehr), Fasanenstraße 81, 10623
Berlin, anzurufen. Das Verfahren ist für mich als Verbraucher kostenfrei
(§§ 4 ff. VSBG). Anschließend werde ich Klage zum zuständigen Amtsgericht
erheben.

Mit freundlichen Grüßen

[Name]

Anlagen:
 K1 Kopie des Originaltickets
 K2 Kopie des ursprünglichen Antrags
 K3 Kopie des Ablehnungsschreibens
 K4 [ggf. Belege Verpflegung / Hotel / Ersatzbeförderung]
```

#### دستورالعمل های سبک نامه

- **حتما و قطع**، نه تهاجمی اما واضح در تقاضا.
- **نوردی از قوانین خاص** (VO (EU) 2021/782 با مقالات، EVO با پاراگراف و مقررات تعرفه ای با پیامی).
- **به طور خاص به دلیل عدم پذیرش** - نه استدلال کردن با صدای بلند. `db-ablehnungsgruende-pruefen` به عنوان یک اشاره.
- **حداقت:** درخواست پاسخ در زمان مناسب. Art. 19 Abs. 7 ویو یک ماه است، چهار هفته کوتاه تر (28 روز) و در صورت اختلاف درباره تأخیر می تواند مضر باشد.
- ** مقام تسلیحات یادآوری کنید:** اشاره به مکان تسلیحی سفر و حمل و نقل e.V (پخواني سوپ)
- **در صورت رسمی اما نه در مورد قانون زیاد** - باید نامه از یک فرد خصوصی باشد، که لزوماً وکیل نیست.

### مرحله 5: خرج و انتقال سرمایه

1. نامه آماده به عنوان `widerspruch-<datum>.md` و در پرونده ی موردی، PDF را قرار دهید.
2. در عین حال، مهارت `fahrgastrechte-anlagen-bauen` صدا می زنند.

**خطای انتقال سرمایه گذاری:**

```yaml
schriftsatz: widerspruch-<datum>.md
rohbelege_verzeichnis: <fall>/belege/
ausgabeverzeichnis: <fall>/anlagen/
bundle: true                       # Sammel-PDF Schriftsatz_mit_Anlagen.pdf
schriftgrad_stempel: 12
schrift_stempel: Arial-Bold        # Arial 12 FETT oben rechts
bezeichnung: "Anlage K"
```

3. به کاربر خلاصه ای کوتاه بدهیم:
   - دلیل انکار مشخص شده
   - با استفاده از نقطه ی معیاری، چه استدلال های ضد مورد استفاده قرار گرفته اند
   - چه نوع خسارت مورد نیاز است
   - توصیه برای گام های بعدی (مقرّر مجدد عدم پذیرش در مورد سفرهای مسافرت و حمل و نقل - مهارت) `schlichtung-reise-verkehr-anrufen`)

## اطلاعات ندیده شده

اگر اطلاعات مهمی از اسناد به دست نیاید، کاربران را با هدف بپرسید - برای مثال:

- "در ایستگاه مقصد چقدر دیر شده بودید؟"
- "آیا شما یک ارتباط جایگزین را انتخاب کرده اید؟ اگر بله، کدام؟"
- "تو هزینه های غذا، تاکسی یا هتل داری؟ اگر بله، چقدر؟"
- "آدرس نامه شما چطوره؟"
- " آیا این قطار در مسافرت های دور (ICE / IC / FlixTrain) یا حمل و نقل محلی بود؟"

نه همه اطلاعات را در یک لحظه، فقط چیزی که واقعاً از دست می رود.

## نکته های مهم

- **هیچ گونه اخطار قانونی در نامه وجود ندارد** - این نامه باید به نظر برسد که یک اعتراض عادی از طرف شخص خصوصی است.
- **اما به کاربر در چت می گویند:** "این مشاوره حقوقی نیست. اگر شک دارید، با وکیل یا مرکز مصرف کننده مشورت کنید".
- ** تاریخ:** همیشه از تاریخ فعلی استفاده کنید، نه تاریخ نامه رد.
- **مدت شکایت Art. 27 VO:** سه ماهه یک زمان قانونی است - نه برای حذف حق مالی. § 195 BGB (3 سال) همچنان مهم است.
- **در زمان استخدام وکیل** در پایان نامه، عبارت استاندارد CLAUDE.md را نیز شامل کنید: نام حرفه ای, نسبت کار و هزینه (RVG . توافق نامه حقوقي

## اسکیل‌های پیوسته

- اگر DB به مخالفت یا عدم پاسخ دادنش: `schlichtung-reise-verkehr-anrufen`.
- اگر شکایت لازم باشد: `klage-amtsgericht-fahrgast`.
- برای تحلیل دلایل انکار: `db-ablehnungsgruende-pruefen`.

## منابع

- در این باره، نظرسنجی از سوی دولت های مختلف و کشورهای عضو اعلام شده است. eur-lex.europa.eu (CELEX 32021R0782)
- EVO 2023 - gesetze-im-internet.deدر سال 2023
- شرایط حمایت از DB bahn.de/acb
- محل تسلیحات سفر و حمل و نقل e.V schlichtungsstelle-reise-verkehr.de

قضیه: هیچ تصمیمی را از دانش نمونه ای نقل نکنید؛ قبل از انتشار با دادگاه، شکل تصمیم گیری و تاریخ آن ها، نشانه های پرونده یا اظهارات قابل اثبات را توسط منبع رسمی یا آزاد تأیید کنید.
