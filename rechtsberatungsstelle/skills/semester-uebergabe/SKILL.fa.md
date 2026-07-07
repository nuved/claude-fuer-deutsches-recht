---
name: semester-uebergabe
description: "Wenn es um Semesterübergabe in Plugin für die studentische Rechtsberatungsstelle geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# انتقال سمستر

## مسیر کار

- روشن‌کردن نقش، هدف و محصول کاری خواسته‌شده: چه کسی اقدام می‌کند، چه تصمیمی در پیش است، چه مهلتی در جریان است و چه خروجی‌ای لازم است؟
- نخست علامت‌گذاری مهلت‌ها و خطرهای فوری: تنها از مهلت‌های همان حوزهٔ حقوقی مشخص و همان پرونده استفاده کنید؛ اعتراض (Widerspruch)، دعوا (Klage)، ایراد (Einspruch)، طرق شکایت (Rechtsmittel)، مرور زمان (Verjährung)، سقوط حق (Verwirkung) و مهلت‌های ایراد، اعلام، ثبت و انقضا را به‌دقت جدا کنید و هرگز از حوزهٔ تخصصی دیگری برندارید.
- راستی‌آزماییِ قوانینِ پایه: قوانینِ مرتبط در زمینهٔ افزونه را به‌صورت زنده در gesetze-im-internet.de، dejure.org، eur-lex.europa.eu و درگاه‌های رسمی فدرال/ایالتی بررسی کنید — نشانی مآخذ را در gesetze-im-internet.de، dejure.org، openJur و پایگاه‌های BVerfG/BGH/EuGH به‌صورت زنده وارسی کنید؛ هیچ استنادِ برخاسته از دانش مدل نیاورید.
- تعیین مرجع صالح و انتخاب درست مخاطب: موکل، طرف مقابل، ادارهٔ صالح یا دادگاه، کارشناسان و در صورت لزوم نهاد اتحادیهٔ اروپا/بین‌المللی (به جزئیات اسکیل نگاه کنید).
- گردآوری اسناد و ادلّه و بررسی خلأها: پرونده‌های اداری، اسناد قراردادی، لوایح، تصمیم‌های اداری (Bescheide)، صورت‌جلسه‌ها، نظرهای کارشناسی و ادلّهٔ بیرونیِ همان حوزه — مدارک نبود را از راه دسترسی به پرونده یا پرسش از موکل فراهم کنید، و برای تغییرهای روزِ قوانین و رویهٔ اداری بررسی زنده انجام دهید.

## هدف

هر ترم، این موسسه تمام دانش آموزان خود را از دست می دهد و دوباره آن ها را بازسازی می کند. `/einarbeitung` این مهارت نیمی از مشکل را حل می کند، آنبورد کردن گروه های جدید. و نیمه دیگر را: با تصویب گروهی که در حال خروج هستند، به وسیله ی ایجاد اطلاعیهای انتقال داده شده ای است که تمام اطلاعاتی را برای انجام هر ماموریت جاری شامل خواهد شد.

بدون این انتقال، دانش قضایی از مشاور با نام دانشجویان خارج می شود. گروه های جدید با پرونده و یادداشت کار شروع می کنند - که هرگز کافی نیست. دو هفته برای بازیافت به دست می آید؛ مشتری آن را یک گام عقب تر می بیند: تماس ها جواب نمی دهند، سوالات قبلاً پاسخ داده شده دوباره مطرح می شوند.

**سرنامه ی مأموریت:** اطلاعیه های تحویل حاوی اطلاعات محرمانه مشتری (§ 43a Abs. 2 BRAO, § 203 StGB) آنها فقط در داخل مرکز مشاوره بین دانش آموزان درگیر و سرپرست تبادل می شوند - هرگز از طریق ایمیل خصوصی، سرویس چت یا دیگر ارتباطات غیرقابل اطمینان.

## ورودی‌ها

- **سمنستر** (بعد از معیاری: سمنتر جاری)
- **در مورد فردی** (اختیاری: `--fall=[fall-id]`) برای انتقال به صورت جداگانه (به عنوان مثال در هنگام خروج زودرس)
- ** لیست فعال موارد** - اگر کلینیک پرونده های مرکزی را نگه نمی دارد، باید به عنوان یک ورودی ارائه شود؛ مهارت ایجاد موارد نیست
- **مرتبط:** چه کسی می آید، چه کس می رود - اگر معلوم باشد؛ در غیر این صورت "TBD-Supervisor"

## چارچوب حقوقی

### قوانین هسته ای

- **§ 43a Abs. 2 BRAO** - محامّت صراحت؛ به طور کلی برای دانشجویان مشاوران اعمال می شود. اطلاعیه ی انتقال تنها اطلاعاتی را شامل خواهد شد که ضروری است تا پرونده ادامه یابد.
- **§ 203 Abs. 1, Abs. 3 StGB** - نقض راز خصوصی: انتقال اطلاعات مشتری به اشخاص غیر مجاز، مجازات است. S. د. § 203 Abs. 3 S. 2 StGB.
- **§ 6 Abs. 2 RDG** - وظیفه نظارت: انتقال پرونده ها یک حوزه ای است که نیاز به کنترل از سوی ناظران دارد؛ وکیل همراه/دستور دستیار، تحویل را می نویسد.
- **§ 50 BRAO** - نیاز به نگهداری دستاوردها: نظارتگر باید اسناد را پس از پایان کار حداقل 5 سال نگه دارد؛ اطلاعیه های انتقال بخشی از سندورها در مفهوم قانونی هستند.
- **DSGVO Art. 5 Abs. 1 lit. f** (امنیت و محرمانه بودن) **Art. 32 DSGVO** - اقدامات فنی و سازمانی برای امنیت داده ها؛ راه های امن انتقال اطلاعات ارسال.

### آرای راهنما

- قضیه: هیچ تصمیمی را از دانش نمونه ای نقل نکنید؛ قبل از انتشار با دادگاه، شکل تصمیم گیری و تاریخ آن ها، نشانه های پرونده یا اظهارات قابل اثبات را توسط منبع رسمی یا آزاد تأیید کنید.

### قاعدهٔ منابع

قانون منبع: هیچ جای برای یافتن نظرات، کتابچه یا مقاله از دانش مدل؛ ادبیات فقط با منابع کاربر و یا زیرنویس زنده مجوزff.

## زمان

### مرحله ی ۱: شناسایی موارد و صلاحیت ها

- همه موارد فعال را ثبت کنید (از پرونده های موردی + `deadlines.yaml` شناسه های موردی + ثبت اطلاعات)
- در هر صورت، چه کسی کارمند فعلی است؟ آیا این فرد باقی می ماند یا از آن خارج می شود؟
- اختصاص: خارج شده → جانشین (اگر معلوم باشد؛ در غیر این صورت "TBD - سرپرست را تعیین می کند")

اگر پرونده های مرکزی وجود نداشته باشند، لازم است که یک لیست موردی را وارد کنید.

### مرحله دوم: انتقال موردی

در هر صورت:

```markdown
### Fallübergabe — [Fallbezeichnung] — [Semester-Ende]

**Fall-ID:** [fall-id]
**Rechtsgebiet:** [Gebiet]
**Ausscheidende/-r Studenten/-r:** [Name]
**Nachfolger/-in:** [Name oder "TBD"]
**Begleitender Supervisor:** [Name]
**Mandant:** [Name oder Mandanten-ID — kein Klarname in unsicheren Systemen]

---

## Aktueller Stand

[Ein Absatz: Verfahrensstand. Was ist getan, was steht aus, wo geht der Fall hin.
Falls der Fall an einem natürlichen Haltepunkt steht (zwischen Einreichungen, wartend
auf Behördenantwort), dies benennen.]

## Offene Fristen

*Aus `deadlines.yaml`. Erste Aufgabe der/des Nachfolger/-in: Fristen bestätigen und übernehmen.*

| Fällig | Typ | Beschreibung | Hinweise |
|---|---|---|---|
| [Datum] | [Typ] | [Einzeiler] | [bei Dringlichkeit: "DRINGEND — fällig innerhalb von [N] Tagen nach Semesterbeginn"] |

## Was getan wurde

- [Wichtige Schritte dieses Semesters: Erstberatung, Einreichungen, Termine, wesentliche Schriftstücke]
- [Erstellte Dokumente — mit Verweis auf Ablageort]

## Was noch offen ist

- [Ausstehende Entscheidungen: z. B. "Mandantin hat noch nicht über das Vergleichsangebot entschieden"]
- [Recherche-Lücken: z. B. "§ 556g BGB Mietpreisbremse — Ausnahmen noch nicht abschließend geprüft"]
- [Offene Kommunikation: z. B. "Antwort der Behörde auf Widerspruch ausstehend"]

## Mandantenbeziehung

- [Wie oft Kontakt? Telefon, E-Mail, persönlich?]
- [Relevanter Beziehungskontext für Nachfolger/-in: Sprache, besondere Lebensumstände, Kommunikationspräferenzen]
- [Nächster geplanter Kontakt oder Termine]

## Erstellte und eingereichte Schriftstücke

*Verweise, kein Inhalt.*

- [Datum] [Schriftstücktyp] — [Ablagepfad] — [Status: eingereicht / Entwurf / in Supervisor-Prüfung]

## Kommunikationshistorie-Zusammenfassung

*Aus dem Kommunikationslog. Dreizeilige Zusammenfassung hier; Nachfolger/-in liest den vollständigen Log.*

[Kurze Zusammenfassung des jüngsten Kommunikationsmusters — z. B. "3 Telefonate seit Erstberatung, alle auf Russisch, Mandantin bevorzugt abends. Letzter Kontakt: 15.04.2026, Adresse für Schriftstück bestätigt."]

## Hinweise des Supervisors an Nachfolger/-in

*Vom Supervisor vor Weiterleitung der Übergabenotiz ergänzt. Kann enthalten: "Dieser Fall hat eine sensible Familiensituation — Akte vor dem ersten Kontakt genau lesen"; "Mandant hat gebeten, alle Post an Postfach, nicht Hausadresse"; "Es gibt noch eine offene Scoping-Frage — erste Woche mit mir besprechen."*

[Hinweise, oder "keine"]

## Erste-Woche-Prioritäten für Nachfolger/-in

1. [Konkret — z. B. "Mandantin innerhalb von 48 Stunden nach Fallübernahme anrufen. Sich vorstellen, Fallübernahme bestätigen."]
2. [Fristenbezogen — z. B. "Widerspruchsfrist endet am [Datum]. Entwurf des abgehenden Studentenn prüfen, überarbeiten, einreichen."]
3. [Wissenslücke — z. B. "Gutachten des abgehenden Studentenn zur Mietpreisbremse lesen, bevor am [Datum] die Verhandlung stattfindet."]

---

**Übergabe erstellt von:** [Ausscheidende/-r Studenten/-r]
**Datum:** [JJJJ-MM-TT]
**Geprüft von:** [Supervisor, sofern Supervisionsmodell dies vorsieht]
```

### مرحله سوم: برآورد کل گروه ها

پس از همه ی یادداشت های مربوط به این مورد، `handoffs/[semester]/_zusammenfassung.md` ایجاد:

```markdown
### Kohortenübergabe-Zusammenfassung — [Semester-Ende]

**Ausscheidende Studenten:** [N]
**Eintretende Studenten:** [N]
**Laufende, zu übergebende Fälle:** [N]
**Fälle, die zum Semesterende abgeschlossen werden (keine Übergabe):** [N]

---

## Übergaben

| Fall | Ausscheidend | Nachfolge | Rechtsgebiet | Dringlichkeit |
|---|---|---|---|---|
| [fall-id] | [Name] | [Name oder TBD] | [Gebiet] | [normal / Frist innerhalb 2 Wochen / dringend] |

## Nicht zugewiesen

[Fälle, für die "TBD" als Nachfolger/-in eingetragen ist — Supervisor weist vor Semesterstart zu]

## Fristen innerhalb von 30 Tagen nach Semesterbeginn

[Aus deadlines.yaml — das sind die Fälle, in die die neue Kohorte sofort einarbeiten muss]

## Hinweise für den Supervisor

- [Falls in diesem Semester besondere Leistungsprobleme bei Studentenn aufgefallen sind — für engere Begleitung im Folgesemester notieren]
- [Falls ausscheidende Studenten bereit sind, für den Nachfolger/die Nachfolgerin zur Verfügung zu stehen — z. B. Absolvent/-in, der/die die Übergabe begleiten möchte]
- [Muster über Fälle hinweg — z. B. "Drei von sechs Fällen haben Fristen in den ersten 14 Tagen des neuen Semesters; ggf. Onboarding-Übungen auf diese Rechtsgebiete fokussieren"]
```

### مرحله چهارم: بررسی نظارت

بسته شدن یا انتقال یک پرونده، اقدام جدی است.§ 6 Abs. 2 RDG) اطلاعیه های نهایی پرونده همیشه قبل از اینکه در سند انتقال، هر چه مدل نظارت مورد نظر را انتخاب کنید ، به عنوان بسته نشان داده شود توسط ناظری امضا می شوند.

- **خطای رسمی انتظار:** هر خط انتقال به صف قبل از اینکه برای جانشین ارسال شود.
- **پناه های قابل تنظیم:** یادداشت ها برای ارسال [SUPERVISOR] "آزمایش" ، نظارت کننده به صورت غیر رسمی انجام می دهد.
- **رودبندی ساده تر:** برچسب استاندارد هوش مصنوعی؛ سرپرست از ساختار مراقبت های موجود بررسی می کند. با این حال، نتیجه گیری قبل از اینکه به عنوان بسته شده برای سرپرستی مشخص شود، پیش بینی ها را انجام میدهد.

### مرحله پنجم: انتقال

پس از بررسی نظارت، نوتیسه های انتقال زیر است: `handoffs/[semester]/[fall-id].md`.آفریننده آن را در `/einarbeitung`-در ابتدا از هر فصل `/einarbeitung` باید یادداشت های موردی را که به آنها اختصاص داده شده است، در صفحه نمایش قرار دهد.

## نمونه

** سناریو:** دانش آموز Müller پایان می دهد و پرونده `erdem-mietrecht-2026` در ادامه، دانش آموزان تحصیلات خود را به سمت دانشگاه های دیگر منتقل می کنند.06.2026.

این گزارش شامل: وضعیت فعلی (تعدیل آماده است، منتظر انتشار نظارت) ، جدول مهلت ها (08.06.2026 - درنگ) چه کاری انجام شده است (مجلس اول 15.03.2026، طرح 104.2026), توجه به سرپرست: "ماندانت فقط زبان ترک می گوید - مدرسه باید مترجم را سازمان دهد".

## خطرات و اشتباهات معمول

- **برنامه های بدون سرایت:** ارسال اطلاعات ارسالی به صورت ایمیل از طریق حساب ها یا خدمات چت § 203 StGB و DSGVO Art. 5فقط سیستم های کنترل سفارشات و تضمین شده
- ** فراموش کردن زمان:** خطرناک ترین شکاف. تمام زمان های فعال باید در یادداشت ظاهر شوند؛ جانشین باید آن را به صورت `/fristen` به عنوان مهلت های خود را دوباره ثبت کنید.
- **برنامه ی ناظرین بدون علامت:** § 6 Abs. 2 RDG از نظارت موثر می خواهد. همچنین انتقال های "غیر رسمی" باید به ناظران گزارش شود.
- ** نوتیسم انتقال خیلی نازک:** "دقیقه خوب پیش می رود" تحویل نیست. یادداشت باید به اندازه کافی کامل باشد که کسی بدون علم قبلی بتواند پرونده را بر عهده بگیرد.
- ** تماس با مأمور در مرحله انتقال تضمین نشده:** بین خروج دانش آموزان قدیمی و پذیرش توسط دانشجویان جدید، نظارت کننده باید اطمینان حاصل کند که مشتری قابل پاسخ است.

## تعهد به منبع

اطلاعات انتقال، اسناد کاری داخلی هستند نه نظرات قانونی که به آن ها اشاره می شود.`/memo`, `/recherche-start`) با ذکر منابع، گزارش انتقال به نظر می رسد که این اطلاعات را ارائه کرده است اما بدون تایید هیچ استاندارد دیگری را از خود نقل نمی کند.

توجه: این مهارت جایگزین مشاوره حقوقی در یک مورد خاص نیست.
