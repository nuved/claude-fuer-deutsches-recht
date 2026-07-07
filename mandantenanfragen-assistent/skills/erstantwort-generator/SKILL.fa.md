---
name: erstantwort-generator
description: "Wenn es um Erstantwort-Generator in mandantenanfragen-assistent geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# ژنراتور کلمه اول

## مسیر کار

- روشن‌کردن نقش، هدف و محصول کاری خواسته‌شده: چه کسی اقدام می‌کند، چه تصمیمی در پیش است، چه مهلتی در جریان است و چه خروجی‌ای لازم است؟
- اول، مهلت ها و خطرات فوری را مشخص کنید: BRAO § 44 پذیرش/پذیرفتن فوری، RVG § 34 مشاوره اولیه حداکثر 190 یورو (مصرف کنندگان) DSGVO Art. 13 اطلاعات در هنگام جمع آوری.
- بررسی معیارهای مربوط به: BRAO §§ 43a، 44، 49b BORA §§ 2, 11, BGB §§ 145 ff., 280, 627, 675, GwG §§ 10, 11, RVG §§ 1، 4، 34 (مجلس اول) DSGVO Art. 613 - یافته های مربوط به gesetze-im-internet.de, dejure.org،آفتاب BVerfG-/BGH-/EuGH-دیتابیس زنده را بررسی کنید، بدون نقل قول دانش مدل
- اداره ی صلاحیت را تعیین کنید و به درستی مخاطب ها را انتخاب نمایید: درخواست کننده (مهم) ، وکیل، دفترچه، مأموریت رعایت مقررات، مدیر مشتری.
- جمع آوری اسناد و شواهد، بررسی شکاف ها: فرم تماس اول، غربالگری درگیری، قرارداد اجاره ای، فرماندهی، توافق نامه حقوق، پرونده ی متقاضی، اطلاعیه حریم خصوصی - دریافت مدارک از طریق بازرسی یا درخواست به متقاضیان ، چک زنده برای تغییرات روزانه استاندارد و شیوه های مدیریت.

## دانش ویژه

این مهارت اصلی، ایمیل رسمی کامل اولین کلمه را به یک مشتری بالقوه می سازد. تمام توانایی های جزئی را هماهنگ کرده و تولید آن ها را در نامه ای که آماده چاپ است جمع آوری کند.

## سه بعدی در آغاز
1. آیا تمام مهارت های جزئی (پیرسنگ، بررسی اسپام، بی سر و جویی، سخنرانی، زبان) انجام شده است؟
2. چه نوع اضطراری را در صورت ارسال اطلاعات فوری وارد ایمیل کرده اید؟
3. آیا یک رابطه ی دستور وجود دارد یا این اولین سوال است (حتی که هیچ نوع مجوز لازم نیست) ؟
4. آیا باید اشاره ی سرویس نقل را فعال کنید (تغییر: درخواست کوتاه/شکافی است یا کاربر نمی تواند بنویسد) ؟

## رویهٔ قضایی روز
- قضیه: هیچ تصمیمی را از دانش نمونه ای نقل نکنید؛ قبل از انتشار با دادگاه، شکل تصمیم گیری و تاریخ آن ها، نشانه های پرونده یا اظهارات قابل اثبات را توسط منبع رسمی یا آزاد تأیید کنید.

## قوانین محوری
- § 49b Abs. 5 BRAO - نیاز به بررسی هزینه ها: اشاره به کل پیش بینی شده قبل از پذیرش مجوز
- Art. 13 DSGVO - نیاز به اطلاع رسانی: اولین جمع آوری اطلاعات شخصی، نیازمند ضرورت فوری برای ارائه اطلاعاتی است
- § 43 BRAO - وظیفه دقت: پاسخ به سوالات در زمان و کامل
- § 43a Abs. 2 BRAO - محرمانه بودن: در مقابل مشتری بالقوه نیز صدق می کند

## دوره (مهمیت های بخشی)

1. ** پارسینگ:** مهارت `anfrage-eingang-parser` در ابتدا به شما می دهد و داده های ساختاری را ارائه میدهد.
2. ** چک اسپام:** مهارت `spam-und-massen-anfrage-filter` - در مورد اسپام: جواب ایجاد نکنید، پرچم های خارج از گروه را بگذارید.
3. **حاجت:** مهارت `dringlichkeitsmarker` - در HOCH: تماس فوری با وکیل را اولویت بندی کنید، اشاره ای به ایمیل وارد نمایید.
4. ** سخنراني:** مهارت `anrede-uebernehmen` - به صورت رسمی حرف می زند.
5. ** زبان:** مهارت `mehrsprachige-antwort` - در صورت درخواست غیر آلمانی، تغییر زبان.
6. ** ساخت ایمیل:** این مهارت تمام عناصر را به هم می پیوندد.
7. **درآمدی CRM:** مهارت `folgekorrespondenz-vorbereiten` در حال شروع به عمل است.

## ساخت ایمیل اول کلمه

### موضوع

```
Re: [Original-Betreff der Eingangsmail]
```
یا اگر موضوعی وجود نداشته باشد:
```
Ihre Anfrage an [KANZLEI-NAME] — Eingangsbestätigung
```

### بدن پست (ساخت نمونه)

```
[ANREDEZEILE],

vielen Dank für Ihre Anfrage, die uns heute zugegangen ist.

[DRINGLICHKEITS-HINWEIS — nur wenn HOCH: Absatz einfügen, sonst weglassen]

Wir begleiten potenzielle Mandanten gern dabei, die richtigen
nächsten Schritte zu finden. Bitte beachten Sie, dass [MANDATSVERHAELTNIS-DISCLAIMER-KURZFORM].

Für eine erste Terminabsprache stehen wir Ihnen telefonisch zur Verfügung:

 Sekretariat: [SEKRETARIATS-TELEFON]
 Erreichbarkeit: [ERREICHBARKEITSZEITEN]

Um Ihren Fall bestmöglich vorzubereiten, bitten wir Sie, uns vorab Ihren
Sachverhalt in einer kurzen E-Mail zusammenzufassen:

 — Was ist der Kern Ihres Anliegens?
 — Wann hat das zugrunde liegende Ereignis stattgefunden?
 — Gibt es Fristen, Termine oder Bescheide, die wir kennen sollten?
 — Wer ist die Gegenseite (Person, Unternehmen, Behörde)?

[TRANSKRIPTIONS-ABSCHNITT — nur wenn Anfragende nicht schreiben kann/mag:]

Falls Ihnen eine schriftliche Schilderung schwerfällt, bieten wir Ihnen
einen automatisierten Transkriptionsservice an. Sie rufen dort an und schildern
Ihr Anliegen mündlich. Die Aufnahme wird automatisch verschriftlicht und uns
vertraulich übermittelt.

Wichtiger Hinweis zur Datenverarbeitung: [EINWILLIGUNGS-TEXT-KURZFORM]

Transkriptionsservice: [TRANSKRIPTIONS-TELEFON]

[/TRANSKRIPTIONS-ABSCHNITT]

Mit freundlichen Grüßen

[UNTERZEICHNENDE-RA]
[KANZLEI-NAME]
[KANZLEI-ADRESSE]
[KANZLEI-TELEFON]
[KANZLEI-E-MAIL]

---
[MANDATSVERHAELTNIS-FUSSZEILE]
```

## قطعات ساختمانی به جزئیات

### عبارت شکر

استاندارد: "از پرسش شما که امروز به ما رسید، تشکر می کنم".

گزینه های مختلف:
- در مورد درخواست فوری: "ممنون از شما برای سوال. ما به عنوان یک نیاز ضروری توجه کردیم".
- در مورد توصیه: "ممنون از سوال شما که ما را به [Quelle, soweit genannt] نزدیک شد".

### اطلاع اضطراری (تنها در صورت HOCH)

```
WICHTIG: Aus Ihrer Anfrage haben wir entnommen, dass möglicherweise eine
Frist oder ein Termin unmittelbar bevorsteht. Bitte rufen Sie uns
umgehend unter [SEKRETARIATS-TELEFON] an, damit wir die Situation sofort
einschätzen können. Warten Sie bitte nicht auf eine schriftliche Rückmeldung.
```

### قرار دادن وقت تلفنی

بخشی از اجباری است.
- شماره تلفن دفتر (از مهارت) `telefon-konfiguration`)
- زمان های دسترسی (از `kanzlei.json`)

### در مورد این موضوع خلاصه ای از واقعیت ها را درخواست کنید

سوالات فرم (در بالا)
"لطفا به ما در چند جمله، تاریخ رویداد و طرف های درگیر، مهلت ها و هدف خود را توضیح دهید".

### اطلاع از سرویس نقل

فقط اگر:
- درخواست کننده به وضوح می گوید که نمی تواند یا نمیتواند بنویسد، و
- کارمند دفتر دستی به صورت دستکاری فعال می شود.

شامل: شماره تلفن سرویس نقل، بیانیه کوتاه در مورد زمان رسانی DSGVO-تصدیق رضایت در شکل کوتاه (طول از مهارت) `einwilligung-hinweis-datenschutz`).

### معافیت در رابطه با مأموریت

خلاصه در ایمیل: "لطفا توجه داشته باشید که این تاییدیه ی ورود، نه یک سند استوار و نه مشاوره حقوقی محسوب می شود".

شکل بلند در خط پای: از مهارت `mandatsverhaeltnis-hinweis`.

### فرمول نهایی

استاندارد: "به سلام های دوستانه"

انواع زبان:
- انگلیسی: "صداقت شما" / "بچه احترام می گذارد،
- فرانسوی: "به لطف شما، اظهار سلام های متميز را بپذیرید".
- "تخت های سالوتی"

## خروجی

مهارت، ایمیل آماده را به صورت متن فرمت شده می دهد که برای کپی کردن در برنامه ی ایمیل دفترچه آماده است.
- خلاصه داخلی از تصمیمات گرفته شده (چه قسمت ها و بخش هایی که اضافه/ حذف شد)
- اشاره به بازبینی های دستی که در انتظار هستند (به عنوان مثال اگر نام مشخص نشده باشد)

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **الزامِ تمام‌نویسی و استانداردِ قالب.** محصولِ نهایی در **جمله‌های کامل و تمام‌نوشته** تحویل می‌شود — نه اسکلتِ کلیدواژه، نه تنهٔ خالیِ شرط، نه صرفِ فهرست. شرط‌ها به‌صورتِ جمله‌های تمام‌نوشتهٔ بیان‌گرِ اثرِ حقوقی می‌آیند؛ جای‌گیرها مانند `[Name der Mandantin]` روشن علامت می‌خورند و متنِ پیرامون کامل می‌ماند.
>
> **شکلِ نوشتار:** هرگاه لایحه، قرارداد، یادداشت، تصمیم، ومرک یا هر سندِ نهاییِ دیگر به‌صورتِ DOCX، PDF یا متنِ قالب‌بندی‌شده بیرون داده شود، باید **Times New Roman ۱۱ pt** به‌عنوانِ قلمِ پایه به‌کار رود. عنوان‌ها در همان قلم می‌مانند و تنها می‌توانند سیاه (بولد) یا پلکانی باشند. در خروجیِ صرفاً Markdown یا چت، این خواستهٔ قالب به‌عنوانِ یادداشتِ برون‌سپاری درج می‌شود.
>
> **شماره‌گذاری:** ساختاربندی منحصراً اعشاری (`1`، `1.1`، `1.1.1` و به همین ترتیب). بدون اعداد رومی، بدون ساختاربندی حرفی یا آمیخته.
<!-- END ausformulierungspflicht (autogen) -->

## اشاره به مهارت های دیگر

- `anfrage-eingang-parser` - پایه داده ها
- `anrede-uebernehmen` - خط های گفتار
- `telefon-konfiguration` - شماره تلفن
- `transkriptionsdienst-erklaerung` - بخش نقل
- `einwilligung-hinweis-datenschutz` — DSGVO-ازمضای
- `mandatsverhaeltnis-hinweis` - اعلامیه
- `dringlichkeitsmarker` - اطلاع اضطراری
- `spam-und-massen-anfrage-filter` - پیش فیلتر
- `folgekorrespondenz-vorbereiten` - ثبت CRM متوازی
- `mehrsprachige-antwort` - زبان پاسخ
- `muster-erstantwort` - نامه ای برای مرجع
