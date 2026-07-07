---
name: status
description: "Wenn es um Fallstatus: Zielgruppengerechte Fallzusammenfassung in Plugin für die studentische Rechtsberatungsstelle geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# وضعیت موردی: خلاصه ای از موارد مربوط به گروه هدف

## مسیر کار

- روشن‌کردن نقش، هدف و محصول کاری خواسته‌شده: چه کسی اقدام می‌کند، چه تصمیمی در پیش است، چه مهلتی در جریان است و چه خروجی‌ای لازم است؟
- نخست علامت‌گذاری مهلت‌ها و خطرهای فوری: تنها از مهلت‌های همان حوزهٔ حقوقی مشخص و همان پرونده استفاده کنید؛ اعتراض (Widerspruch)، دعوا (Klage)، ایراد (Einspruch)، طرق شکایت (Rechtsmittel)، مرور زمان (Verjährung)، سقوط حق (Verwirkung) و مهلت‌های ایراد، اعلام، ثبت و انقضا را به‌دقت جدا کنید و هرگز از حوزهٔ تخصصی دیگری برندارید.
- راستی‌آزماییِ قوانینِ پایه: قوانینِ مرتبط در زمینهٔ افزونه را به‌صورت زنده در gesetze-im-internet.de، dejure.org، eur-lex.europa.eu و درگاه‌های رسمی فدرال/ایالتی بررسی کنید — نشانی مآخذ را در gesetze-im-internet.de، dejure.org، openJur و پایگاه‌های BVerfG/BGH/EuGH به‌صورت زنده وارسی کنید؛ هیچ استنادِ برخاسته از دانش مدل نیاورید.
- تعیین مرجع صالح و انتخاب درست مخاطب: موکل، طرف مقابل، ادارهٔ صالح یا دادگاه، کارشناسان و در صورت لزوم نهاد اتحادیهٔ اروپا/بین‌المللی (به جزئیات اسکیل نگاه کنید).
- گردآوری اسناد و ادلّه و بررسی خلأها: پرونده‌های اداری، اسناد قراردادی، لوایح، تصمیم‌های اداری (Bescheide)، صورت‌جلسه‌ها، نظرهای کارشناسی و ادلّهٔ بیرونیِ همان حوزه — مدارک نبود را از راه دسترسی به پرونده یا پرسش از موکل فراهم کنید، و برای تغییرهای روزِ قوانین و رویهٔ اداری بررسی زنده انجام دهید.

## ورودی‌ها

- ** گروه هدف:** `mandant`, `intern` یا `gericht`
- **نوشته های موردی** - حقایق و وضعیت پرونده
- **حال حاضر در این پرونده** - کجاست؟

## چارچوب حقوقی

### قوانین هسته ای

- **§ 6 RDG** - واجب اطلاع رسانی: دانش آموزان باید در مورد وضعیت روش های آموزشی آگاه باشند؛ این مسئولیت خود دانشجویان تحت نظارت مدیران است.
- **§ 43a Abs. 2 BRAO** - محرمانه بودن: گزارش های وضعیت شامل اطلاعات حسی از مشتریان هستند؛ بدون رضایت، به اشتراک گذاشته نمی شوند.
- **§ 11a BRAO** - استخدام حقوق دانشجویی: دانشجویان در مراکز مشاوره تحت نظارت عمل می کنند؛ گزارش های وضعیت دادگاه تنها پس از انتشار سرپرست ها منتشر می شوند.
- **§§ 128–142 ZPO** - پرونده های دادگاه: دستورالعمل ها برای شکل و محتوای گزارشات وضعیت قضایی؛ رعایت مقررات محلی.
- **§ 81 VwVfG** - انجام پرونده ها و وظایف اطلاع رسانی اداره؛ تعهدات اطلاعاتی نماینده نسبت به مشتری را نشان می دهد.
- **Art. 13, 14 DSGVO** - اطلاعات مربوط به رفتار با داده های شخصی؛ گزارش هایی که از پردازش ها توضیح می دهند باید مطابق قوانین حفاظت از داده باشند.

### آرای راهنما

- قضیه: هیچ تصمیمی را از دانش نمونه ای نقل نکنید؛ قبل از انتشار با دادگاه، شکل تصمیم گیری و تاریخ آن ها، نشانه های پرونده یا اظهارات قابل اثبات را توسط منبع رسمی یا آزاد تأیید کنید.

### قاعدهٔ منابع

قانون منبع: هیچ جای برای یافتن نظرات، کتابچه یا مقاله از دانش مدل؛ ادبیات فقط با منابع کاربر و یا زیرنویس زنده مجوزff.

## زمان

### حالت: به مشتری اختصاص داده شده

**خاطب/در:**مطالب. ممکن است تحت استرس باشد. شاید با روش های قانونی آشنا نباشد. سطح خواندن مطابق با استاندارد درک بالینی (استانداردی: درجه ی تحصیلات تکمیلی، جملاتی کوتاه و هیچ مفاهیم تخصصی بدون توضیح).

** شامل:**
- از آخرین تماس چه اتفاقی افتاده؟
- چه اتفاقی می افتد و وقتی
- آنچه که مشتری باید انجام دهد (مخصوص)
- چگونه به مرکز مشاوره برسید

** شامل نمی شود:**
- تحلیل حقوقی (کارنامه IRSE برای مشتری جالب نیست)
- ضعف پرونده (مگر اینکه زمان این گفتگو باشد - که نظارت کننده تصمیم می گیرد، نه یک وضعیت تازه)
- زبان تخصصی

*تقصی برای نام دانش آموز (نه برای مشتری - قبل از ارسال حذف کنید):*
`[KI-GESTÜTZTER ENTWURF — erfordert studentische Prüfung und Supervisionsschritt per Klinik-Konfiguration]`

توجه به قوانین قانونی: برخی از مشاوران (به عنوان مثال در زیر) BRAO- نظارت) برای نامه های تحت نظر دانش آموزان بلوک هایی خاص دارند.

```markdown
Sehr geehrte/r [Mandant/-in],

ich möchte Sie über den aktuellen Stand Ihres Falls informieren.

**Was passiert ist:** [Klares Deutsch. "Wir haben Ihren Widerspruch am [Datum]
beim Amt eingereicht" — nicht "Der fristwahrende Schriftsatz wurde übermittelt."]

**Was als nächstes passiert:** [Was und wann. "Das Amt hat jetzt 3 Monate Zeit,
über Ihren Widerspruch zu entscheiden. Wir erwarten bis spätestens [Datum]
eine Antwort. Falls nichts kommt, melden wir uns."]

**Was Sie tun müssen:** [Konkret und klar. Oder: "Im Moment müssen Sie nichts
tun. Wir melden uns, sobald wir etwas von Ihnen brauchen."]

**So erreichen Sie uns:** [Telefon, Sprechzeiten, Name des Studentenn]

Mit freundlichen Grüßen

[Name des Studentenn]
Studentische/-r Rechtsberater/-in
unter Aufsicht von [Supervisorenname, Rechtsanwalt/-anwältin]
[Name der Beratungsstelle]
```

**پیش از ارسال:** انتقال وضعیت مشتری یک اقدام جدی است.§ 6 Abs. 2 این گزارش از سوی دیگر در مورد بررسی های انجام شده توسط سازمان ملل متحد و همچنین بر روی اطلاعات مربوط به آن ها، می گوید:`[KI-GESTÜTZTER ENTWURF]`, `[PRÜFEN]` و غیره) از نسخه مشتری حذف شده است.

### حالت: کارکن (برای نظارت کننده)

**خودخواهی:** سرپرست همراه. حقوق را می داند، می خواهد که پرونده کجاست و دانش آموزان چه چیزی از او نیاز دارند

** شامل:**
- وضعیت کار (که در این مورد است)
- از آخرین چک ان انجام شده
- چه اتفاقی می افتد (زمان، تاریخ)
- سوالات که نیاز به اطلاعات نظارت دارند
- ارزیابی دانش آموزان (چگونه کار می کند، نگرانی)

```markdown
### Fallstatus: [Mandant] — [Gegenstand] — [Datum]

**Studentenr:** [Name] | **Verfahrensstand:** [Vorberatung / Widerspruch eingereicht /
Klage erhoben / Verhandlung ausstehend / etc.]

## Seit dem letzten Check-in

- [Was wurde getan]

## Kommende Termine und Fristen

| Datum | Was | Handlung erforderlich durch |
|---|---|---|
| [Datum] | [Frist/Termin] | [Studentenr/Supervisor/beide] |

## Supervisoren-Input benötigt

- [Konkrete Frage oder Entscheidungspunkt]

## Einschätzung des Studentenn

[Wie läuft es. Stärken, Bedenken, strategische Fragen. Hier zeigt sich das Denken
des Studentenn.]

---
[KI-GESTÜTZTER ENTWURF — Studentenr sollte insb. den Abschnitt Einschätzung
selbst formulieren; das ist sein/ihr Denken, keine Notizenzusammenfassung]
```

### حالت: در دادگاه/در اداره

**خبری:** قاضی، وکیل یا کارگزار اداره. رسمی § 273 ZPO یا برای کنفرانس وضعیت § 278a ZPO در مورد این امر، باید توجه داشته باشید که § 24 VwVfG).

** شامل:**
- تاریخچه ی پرونده ها (مختصر)
- وضعیت فعلی (بررسی شواهد/تعارف ها / توافق خارج از دادگاه)
- نکات باز
- پیشنهادات بعدی (اگر در نظر گرفته شود)

**فورم:** به دستور کار و سنت های محلی. ggf. مدرک تحویل

```
═══════════════════════════════════════════════════════════════════════
 KI-GESTÜTZTER ENTWURF — erfordert studentische Analyse und Supervisoren-Prüfung
 Gerichtliche und behördliche Schriftstücke IMMER vor Einreichung mit Supervisor
 abstimmen (§ 6 Abs. 2 RDG)
═══════════════════════════════════════════════════════════════════════

[Rubrum nach Verfahrensordnung — PRÜFEN gegen aktuelle Gerichts-/Behördenregeln]

SACHSTANDSBERICHT / STATUSMITTEILUNG

[Partei/Antragsteller] zeigt den Verfahrensstand gemäß [Anforderung des Gerichts
vom [Datum] / § [X] ZPO/VwGO/VwVfG / im Hinblick auf den Termin vom [Datum]] an.

1. Verfahrensgeschichte: [kurz]

2. Aktueller Stand: [Beweisaufnahme / Antragsstand / Einigungsgespräche]

3. Offene Punkte: [was ausstehend ist]

4. Vorgeschlagene nächste Schritte: [soweit relevant]

[Unterschriftsblock — Studentenr unter Aufsicht von [Supervisor, Rechtsanwalt/-anwältin]]

[Zustellungsnachweis falls eingereicht]

---

[PRÜFEN: Rubrum, örtliche Formvorgaben für Statusberichte, Zustellungserfordernisse
— nach aktuellen Regeln des zuständigen Gerichts / der zuständigen Behörde]
```

## مسیر نظارت

به ترتیب کلینیک:
- هدفمند → معمولا پرچم (تواصل فرمانده)
- داخلی → هیچ پرچم (به هر حال به سرپرست می رود)
- در صورت فعال کردن صف رسمی برای بررسی (درخواست های دادگاهی/مقامی) همیشه پرچم بردار

## نمونه

** سناریو:** متقاضی زمین، اعتراض به درخواست هزینه های جانبی.04.2026. انتظار تایید از طرف مالکین

- `/status mandant` → "ما اعتراض شما را در مورد محاسبه هزینه های جانبی داریم.04.2026 و حالا، این مالکان دو ماه وقت دارند که جواب بدهند. تا آن زمان شما هیچ کاری نمی کنید".
- `/status intern` → وضعیت کار: اعتراض مطرح شد؛ زمان پاسخ مالک مکان حدود 01.06.2026; اطلاعات نظارت: آیا باید در صورت عدم پاسخ به شکایت مورد نظر قرار گیرد؟
- `/status gericht` → (حتی که هنوز مربوط نیست، چون هیچ قانونی وجود ندارد)

## خطرات و اشتباهات معمول

- ** نامه ی فرمانده با اصطلاحات تخصصی:** عبارت هایی مانند "مبلغ بدهکار در حال تاخیر است" برای مشتریان درک نمی شود.
- **ملاحظات استراتژیک برای مشتریان بدون مصاحبه با سرپرست:** اخبار بد (مانند کمترین شانس موفقیت) یا گزینه های استراتژیکی در مکالمه با سرپرستی قرار دارند، نه یک نامه وضعیت.
- **حوالۀ قضایی بدون انتشار نظارت:** نقض حقوق § 6 Abs. 2 RDG. هر سندی که به خارج می رود توسط نظارت کننده منتشر میشود
- **تضمينات اشتباه در تاریخ:**توضیحات و توضيحات زمان نامه مشتری باید با `deadlines.yaml` با هم مقایسه می شود.
- ** ارزیابی دانشجویی در گزارش داخلی هوش مصنوعی:** بخش "تقدیرات دانش آموزان" تفکر شخصی است.

## تعهد به منبع

گزارش های وضعیت هیچ استاندارد ای را به عنوان شواهد اولیه نمی گیرند که بر اساس این اطلاعات است (`/memo`) ادعاهای حقوقی در گزارش های وضعیت باید توسط نظرات تایید شده که این گزارش به آن اشاره می کند، پشتیبانی شوند. هیچ سندی از حالت شامل ادعاهای قانونی غیرمحقق نشده نیست.

توجه: این مهارت جایگزین مشاوره حقوقی در یک مورد خاص نیست.
