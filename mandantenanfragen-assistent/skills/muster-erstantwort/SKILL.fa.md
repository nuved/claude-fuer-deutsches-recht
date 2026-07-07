---
name: muster-erstantwort
description: "Wenn es um Muster-Erstantwort in mandantenanfragen-assistent geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# نمونه کلمه اول

## مسیر کار

- روشن‌کردن نقش، هدف و محصول کاری خواسته‌شده: چه کسی اقدام می‌کند، چه تصمیمی در پیش است، چه مهلتی در جریان است و چه خروجی‌ای لازم است؟
- اول، مهلت ها و خطرات فوری را مشخص کنید: BRAO § 44 پذیرش/پذیرفتن فوری، RVG § 34 مشاوره اولیه حداکثر 190 یورو (مصرف کنندگان) DSGVO Art. 13 اطلاعات در هنگام جمع آوری.
- بررسی معیارهای مربوط به: BRAO §§ 43a، 44، 49b BORA §§ 2, 11, BGB §§ 145 ff., 280, 627, 675, GwG §§ 10, 11, RVG §§ 1، 4، 34 (مجلس اول) DSGVO Art. 613 - یافته های مربوط به gesetze-im-internet.de, dejure.org،آفتاب BVerfG-/BGH-/EuGH-دیتابیس زنده را بررسی کنید، بدون نقل قول دانش مدل
- اداره ی صلاحیت را تعیین کنید و به درستی مخاطب ها را انتخاب نمایید: درخواست کننده (مهم) ، وکیل، دفترچه، مأموریت رعایت مقررات، مدیر مشتری.
- جمع آوری اسناد و شواهد، بررسی شکاف ها: فرم تماس اول، غربالگری درگیری، قرارداد اجاره ای، فرماندهی، توافق نامه حقوق، پرونده ی متقاضی، اطلاعیه حریم خصوصی - دریافت مدارک از طریق بازرسی یا درخواست به متقاضیان ، چک زنده برای تغییرات روزانه استاندارد و شیوه های مدیریت.

## دانش ویژه

اولین نامه از یک نمونه ی نامزدی برای دفتر اداری است که می تواند فوراً ارسال شود: این نامه دریافت را تایید کرده، به صورت تصادفی در اختیار قرار نمی گیرد و نشان دهنده قرارداد مشاوره ای باقی مانده است.

همه نگهدارندگان در چسب های گوشه ای `[...]` به وسیله مهارت `telefon-konfiguration` و `anrede-uebernehmen` به صورت خودکار پر می شود یا باید دستکاری کند.

## سه بعدی در آغاز
1. چه نوع نمونه ای از نماد نوشتن مورد نیاز است: حالت استاندارد، فقط نام اول یا سرویس نقل؟
2. آیا همه ی نگهبانان جای (نام دفتر، تلفن سکرتاریات و آدرس امضا کننده) در kanzlei.json تنظیم شده اند؟
3. آیا گفتار از مهارت های پذیرفتن سخنرانی تحویل داده شده است و می تواند مورد استفاده قرار گیرد؟
4. آیا این نمونه باید به زبان آلمانی یا یک زبان خارجی منتشر شود؟

## رویهٔ قضایی روز
- قضیه: هیچ تصمیمی را از دانش نمونه ای نقل نکنید؛ قبل از انتشار با دادگاه، شکل تصمیم گیری و تاریخ آن ها، نشانه های پرونده یا اظهارات قابل اثبات را توسط منبع رسمی یا آزاد تأیید کنید.

## قوانین محوری
- § 49b Abs. 5 BRAO - واجب آموزش هزینه: در قالب کلمه اول باید ذکر شود
- Art. 13 DSGVO - نیاز به اطلاع رسانی: در قالب کلمه اول باید ذکر شود
- § 43 BRAO - وظیفه دقت: تضمین استاندارد کیفیت از طریق قالب
- § 43a Abs. 2 BRAO - محرمانه بودن: نماد نباید حاوی اطلاعات حریم خصوصی باشد

## فهرست نگهدارندگان

| نگهدارنده ی مکان | توضیحات | منبع |
|---|---|---|
| `[KANZLEI-NAME]` | نام کامل دفتر | `kanzlei.json` |
| `[SEKRETARIATS-TELEFON]` | شماره تلفن دفتر اداری | `kanzlei.json` |
| `[TRANSKRIPTIONS-TELEFON]` | شماره تلفن سرویس نقل | `kanzlei.json` |
| `[UNTERZEICHNENDE-RA]` | نام و عنوان وکیل/کارگری که امضا می کند | `kanzlei.json` |
| `[ANREDE]` | خط های رسمی | مهارت `anrede-uebernehmen` |
| `[KANZLEI-ADRESSE]` | آدرس پست | `kanzlei.json` |
| `[KANZLEI-E-MAIL]` | آدرس ایمیل | `kanzlei.json` |
| `[ERREICHBARKEITSZEITEN]` | ساعت های کاری | `kanzlei.json` |
| `[DATUM]` | تاریخ امروز | خودکار |

---

## گزینه ی ۱: استاندارد (مطابق کامل، واقعیت به صورت ایمیل)

```
Betreff: Ihre Anfrage bei [KANZLEI-NAME] — Eingangsbestätigung

[ANREDE],

vielen Dank für Ihre Anfrage, die uns heute zugegangen ist.

Bitte beachten Sie, dass diese Eingangsbestätigung kein Mandatsverhältnis
begründet und keine Rechtsberatung darstellt.

Für ein erstes Beratungsgespräch vergeben wir Termine ausschließlich
telefonisch. Unser Sekretariat erreichen Sie unter:

 [SEKRETARIATS-TELEFON]
 [ERREICHBARKEITSZEITEN]

Um Ihr Anliegen bestmöglich vorzubereiten, bitten wir Sie herzlich,
uns Ihren Sachverhalt vorab kurz per E-Mail zu schildern. Folgende
Angaben helfen uns dabei:

 — Worum geht es in Ihrem Fall (in einigen Sätzen)?
 — Wann hat das zugrunde liegende Ereignis stattgefunden?
 — Gibt es Fristen, Termine oder behördliche Bescheide?
 — Wer ist die Gegenseite (Person, Unternehmen, Behörde)?

Mit freundlichen Grüßen

[UNTERZEICHNENDE-RA]
[KANZLEI-NAME]
[KANZLEI-ADRESSE]
[KANZLEI-E-MAIL]
[SEKRETARIATS-TELEFON]

---
Diese Nachricht begründet kein Mandatsverhältnis und stellt keine Rechtsberatung dar.
```

---

## گزینه دوم: فقط نام اول (هیچ گفتاری، شکل صدا غیر جانبدار)

```
Betreff: Ihre Anfrage bei [KANZLEI-NAME] — Eingangsbestätigung

Sehr geehrte[r] [VORNAME] [NACHNAME],

vielen Dank für Ihre Anfrage, die uns heute zugegangen ist.

[Identischer Textblock wie Variante 1 ab "Bitte beachten Sie ..."]
```

اگر نام خانوادگی مشخص نباشد:
گفتار: "شخصی بسیار محترم که از ما سوال می کند،

---

## گزینه 3: حالت سرویس نقل (نمی تواند/ نمیتواند بنویسد)

```
Betreff: Ihre Anfrage bei [KANZLEI-NAME] — Eingangsbestätigung

[ANREDE],

vielen Dank für Ihre Anfrage, die uns heute zugegangen ist.

Bitte beachten Sie, dass diese Eingangsbestätigung kein Mandatsverhältnis
begründet und keine Rechtsberatung darstellt.

Für ein erstes Beratungsgespräch vergeben wir Termine ausschließlich
telefonisch. Unser Sekretariat erreichen Sie unter:

 [SEKRETARIATS-TELEFON]
 [ERREICHBARKEITSZEITEN]

Da Ihnen eine schriftliche Schilderung schwerfällt, bieten wir Ihnen
einen automatisierten Transkriptionsservice an. Sie rufen unter der
folgenden Nummer an und schildern Ihr Anliegen mündlich — es wird
automatisch verschriftlicht und uns vertraulich übermittelt:

 Transkriptionsservice: [TRANSKRIPTIONS-TELEFON]

Ablauf des Anrufs:
 1. Automatische Ansage mit Datenschutzhinweis
 2. Bestätigung Ihres Einverständnisses (Tastendruck oder "Ja")
 — Ohne Bestätigung keine Aufnahme.
 3. Freie Schilderung Ihres Anliegens
 4. Automatische Verschriftung und vertrauliche Weiterleitung an uns

Wichtiger Datenschutzhinweis: Da zwischen uns noch kein Mandatsverhältnis
besteht, erfolgt die Verarbeitung Ihrer Sprachdaten ausschließlich auf
Basis Ihrer ausdrücklichen Einwilligung nach Art. 6 Abs. 1 lit. a DSGVO.
Sie können diese Einwilligung jederzeit widerrufen. Die vollständige
Datenschutzinformation senden wir Ihnen auf Anfrage gerne zu.

Mit freundlichen Grüßen

[UNTERZEICHNENDE-RA]
[KANZLEI-NAME]
[KANZLEI-ADRESSE]
[KANZLEI-E-MAIL]
[SEKRETARIATS-TELEFON]

---
Diese Nachricht begründet kein Mandatsverhältnis und stellt keine Rechtsberatung dar.
Datenschutzhinweis gemäß Art. 13 DSGVO auf Anfrage erhältlich unter [KANZLEI-E-MAIL].
```

---

## استفاده از دفتر ریاست

1. با توجه به ورودی، گزینه ای را انتخاب کنید.
2. همه `[...]`-موقع داران رو با اطلاعات دفتر عوض ميکنيم
3. `[ANREDE]` از مهارت `anrede-uebernehmen` و به عنوان یک شرکت
4. قبل از ارسال: بررسی اصلاحات، به ویژه شماره تماس و تلفن.
5. کپی اصلی ایمیل درخواست کننده را در اختیار داشته باشید.
6. ثبت CRM از طریق مهارت `folgekorrespondenz-vorbereiten` -بذارید .

## اشاره به مهارت های دیگر

- `anrede-uebernehmen` - خط های گفتار
- `telefon-konfiguration` - تمام شماره تلفن و اطلاعات دفتر
- `erstantwort-generator` - مهارت اصلی که به طور خودکار گزینه را انتخاب می کند
- `einwilligung-hinweis-datenschutz` - شکل بلند در صورت درخواست
- `mandatsverhaeltnis-hinweis` - اعلامیه (در صورت لزوم شکل بلند)
