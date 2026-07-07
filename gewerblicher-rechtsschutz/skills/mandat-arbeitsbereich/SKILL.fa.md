---
name: mandat-arbeitsbereich
description: "Wenn es um Mandatsarbeitsbereich in Plugin: Gewerblicher Rechtsschutz geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# حوزه ی کار در زمینه ماموریت

## مسیر کار

- روشن‌کردن نقش، هدف و محصول کاری خواسته‌شده: چه کسی اقدام می‌کند، چه تصمیمی در پیش است، چه مهلتی در جریان است و چه خروجی‌ای لازم است؟
- نخست علامت‌گذاری مهلت‌ها و خطرهای فوری: تنها از مهلت‌های همان حوزهٔ حقوقی مشخص و همان پرونده استفاده کنید؛ اعتراض (Widerspruch)، دعوا (Klage)، ایراد (Einspruch)، طرق شکایت (Rechtsmittel)، مرور زمان (Verjährung)، سقوط حق (Verwirkung) و مهلت‌های ایراد، اعلام، ثبت و انقضا را به‌دقت جدا کنید و هرگز از حوزهٔ تخصصی دیگری برندارید.
- راستی‌آزماییِ قوانینِ پایه: قوانینِ مرتبط در زمینهٔ افزونه را به‌صورت زنده در gesetze-im-internet.de، dejure.org، eur-lex.europa.eu و درگاه‌های رسمی فدرال/ایالتی بررسی کنید — نشانی مآخذ را در gesetze-im-internet.de، dejure.org، openJur و پایگاه‌های BVerfG/BGH/EuGH به‌صورت زنده وارسی کنید؛ هیچ استنادِ برخاسته از دانش مدل نیاورید.
- تعیین مرجع صالح و انتخاب درست مخاطب: موکل، طرف مقابل، ادارهٔ صالح یا دادگاه، کارشناسان و در صورت لزوم نهاد اتحادیهٔ اروپا/بین‌المللی (به جزئیات اسکیل نگاه کنید).
- گردآوری اسناد و ادلّه و بررسی خلأها: پرونده‌های اداری، اسناد قراردادی، لوایح، تصمیم‌های اداری (Bescheide)، صورت‌جلسه‌ها، نظرهای کارشناسی و ادلّهٔ بیرونیِ همان حوزه — مدارک نبود را از راه دسترسی به پرونده یا پرسش از موکل فراهم کنید، و برای تغییرهای روزِ قوانین و رویهٔ اداری بررسی زنده انجام دهید.

## ورودی‌ها

دلیل فرمان (ترجمه ای اول):

- `neu <kurzzeichen>` - ایجاد حوزه ی جدید کار در زمینه ماموریت
- `liste` - همه دستورات را با وضعیت و فرمان فعال نشان دهید
- `wechseln <kurzzeichen>` - انجام ماموریت فعال
- `schliessen <kurzzeichen>` - پرونده ی دستور
- `kein` - از هر ماموریت جدا شدن، کار کردن در سطح عملی

## چارچوب حقوقی

### شرایط چارچوبی قانونی حرفه ای

- **§ 43a Abs. 2 BRAO** - محرمانه بودن وکیل؛ رازداری از فرمان؛ اساس جداسازی متن دستور
- **§ 43a Abs. 4 BRAO** - ممنوعیت نمایندگی منافع متضاد (مخالفات علاقه) ؛ دستور العمل باید به صورت جداگانه انجام شود
- **§ 203 Abs. 1 Nr. 3 StGB** - نقض راز خصوصی توسط وکلا؛ حفظ محرمانه بودن در زمینه کیفری
- **§ 50 BRAO** - تعهدات حفظ دست نوشته ها (کم از 5 سال) ؛ نگهداری شامل حوزه های کاری نیست؛ حذف مستبعد است
- **§ 2 BORA** - تعهدات قانونی حرفه ای؛ اصل استقلال وکلا

### آرای راهنما

- قضیه: هیچ تصمیمی را از دانش نمونه ای نقل نکنید؛ قبل از انتشار با دادگاه، شکل تصمیم گیری و تاریخ آن ها، نشانه های پرونده یا اظهارات قابل اثبات را توسط منبع رسمی یا آزاد تأیید کنید.

### نظرات

- قانون منبع: ادبیات فقط با منابع کاربر یا دسترسی زنده مجاز؛ هیچ جای برای یافتن نظرات، کتابچه و مقاله از دانش مدل نیست.
- فوئریچ/ویلند/بئونلین BRAO، 10م نسخه 2022 § 50 Rn. 1 ff. (ملاحظه ی دستگیره)

## زمان

### مرحله ی اول: بررسی شرط

در صورت این که `Mandatsarbeitsbereiche: ✗` (تعداد استاندارد تیم های داخلی):

> بخش های کار مأموریت غیر فعال شده اند - شما به عنوان یک عمل داخلی با مشتری تنظیم می شوید؛ افزونه خود بخود در سطح عملیات انجام خواهد شد. اگر واقعاً از طریق چندین دستور خارج از سازمان، دوباره مکالمه اولیه را اجرا کنید و گزینه دفتر را انتخاب نمایید. `/gewerblicher-rechtsschutz:gewerblicher-rechtsschutz-mandat-arbeitsbereich` نه، نمی تونم.

هیچ خطا ای نیست، حالت غیر فعال شده همان چیزی است که برای کاربران داخلی انتظار می رود.

### مرحله دوم: پردازش دستورات

به اولین نمره استدلال ارسال کنید.

---

#### فرمان `neu <kurzzeichen>`

1. بررسی کنید که آیا این علامت کوتاه در حال حاضر `mandate/<kurzzeichen>/` یا `mandate/_archiv/<kurzzeichen>/` در صورت برخورد، نام های دیگری را انتخاب کنید.
2. مصاحبه های ثبت شده را انجام دهید (در یک دوره):
 - **منتظرم** - طرف نمایندگی یا واحد تجاری داخلی
 - **طرف مقابل** - طرف دیگر (می تواند شامل چند نفر باشد؛ ممکن است "تجاوز کننده ثالث ناشناخته" در مورد ملاقات کنندگان Watch باشد)
 - **منتظرهای کاری** - برای حفاظت از حقوق تجاری: محافظت در مورد علامت گذاری / نقض مارک ها / انتقال حق های امنیتی / نقص ثبت اختراع / گزارشات FTO / بررسی شقایق IP / مطابقت با OSS / مدیریت کیف پول / مسئولیت اختلال
 - ** سطح اطمینان** | افزایش | تیم پاک (در شرایط حساسیت ویژه، گروه پاک در موارد FTO و خرید حق ثبت اختراع بیشتر است) 
 - **حقیقت های مهم** - 2-5 جمله: درباره چه چیزی، افراد در این زمینه و آنچه که به خطر می افتد
 - **مختلفات مربوط به ماموریت از موقعیت استاندارد** (به عنوان مثال "تدارک کننده فقط می خواهد ارتباطات نوشته شده را داشته باشد"، "دفاع دهنده شرکای تجاری است - صدای قابل توجه")
 - **منتظرات مرتبط** - اختصار متناوب
3. `mandate/<kurzzeichen>/mandat.md` با این طرح که در زیر ذکر شده است، بنویسید.
4. `mandate/<kurzzeichen>/verlauf.md` با یک صفحه باز کردن
5. خالی `mandate/<kurzzeichen>/notizen.md` -بذارید .
6. ** نه** به طور خودکار برای تغییر ماموریت جدید. `<kurzzeichen>` تغییر می کنند؟"

---

#### فرمان `liste`

`mandate/*/mandat.md` از هر فایل وضعیت و شارژ می گیرید. جدول را به صورت زیر بزنید:

| علامت های کوتاه | مشتری | نوع فرمان | وضعیت | باز شده | فعال |
|---|---|---|---|---|---|

مأموریت فعال `*` نشان دادن `_archiv/*` این مطلب را تحت عنوان "منتظرات محفوظ شده" ذکر کنید.

---

#### فرمان `wechseln <kurzzeichen>`

1. بررسی اینکه آیا `mandate/<kurzzeichen>/mandat.md` در صورت وجود ندارد: `neu <kurzzeichen>` پیشنهاد می کنم.
2. `Aktives Mandat:`-در فایل پیکربندی عملی، خطی را در نظر بگیرید `<kurzzeichen>` به روز رسانی
3. به کاربر خلاصه mandat.md را نشان دهید تا بتواند دستور کار صحیح را تایید کند

---

#### فرمان `schliessen <kurzzeichen>`

1. `mandate/<kurzzeichen>/` و اگر وجود داشته باشد.
2. "ملاحظ" با تاریخ فعلی `mandate/<kurzzeichen>/verlauf.md` و از آن استفاده کنید.
3. `mandate/<kurzzeichen>/` بعد از `mandate/_archiv/<kurzzeichen>/` پس از آن، حرکت کنید.
4. آیا این فرمان بسته، آن فرمان فعال بود؟ `Aktives Mandat:` به `kein — nur Praxisebene` می دانی؟

---

#### فرمان `kein`

`Aktives Mandat:` در فایل پیکربندی عملی `kein — nur Praxisebene` قرار دادن. تایید به کاربر

## طرف ها

** فرمانده:** [Name]
**طرف مقابل:** [Name(n)]

## نوع فرمان

[Markenschutz / Markenverletzung / FTO-Gutachten / Patentverletzung / IP-Klauselprüfung / OSS-Compliance / Portfolioverwaltung / Störerhaftung / Sonstiges — mit einzeiliger Begründung]

## حقایق اساسی

[2–5 Sätze. Worum geht es. Wer sind die Beteiligten. Was steht auf dem Spiel. Was macht dieses Mandat vom Standard abweichend.]

## تفاوت های اختصاصی

*هر انحراف از موضع عملی که فقط برای این ماموریت است.

- [z. B. "Durchsetzungsstrategie: hier maßvoll, obwohl Hausstandard aggressiv — Gegenpartei ist wichtiger Handelspartner."]
- [z. B. "Genehmigung für Abmahnungen: zusätzliche Freigabe durch Mandant erforderlich."]
- [z. B. "Clean-Team: Mandatsakten auch bei aktiviertem mandatsübergreifendem Kontext nicht lesbar."]

## مأموریت های مرتبط

- [kurzzeichen — einzeilige Begründung]

## اطلاعات محرمانه

[Bei erhöhter oder Clean-Team-Stufe: warum. Wer darf die Mandatsakten einsehen. Ob mandatsübergreifender Kontext zulässig ist.]
```

### Vorlage `verlauf.md`

```markdown
### دوره: [Mandant] — [Kurzbeschreibung]

فقط گزارش مربوط به اتفاقات اخیر بالا

---

## [JJJJ-MM-TT] - اجاره باز شده

ضبط تمام شد. `[kurzzeichen]`حالت: فعال
[Ggf. initialer Kontext — z. B. "Eröffnet nach Watch-Treffer auf `APEXLEAF` in Klasse 25."]
```

## Beispiel

**Eingabe:** `/gewerblicher-rechtsschutz:gewerblicher-rechtsschutz-mandat-arbeitsbereich neu bmw-marke-2026`

**Verarbeitung:**
Kurzzeichen prüfen → Aufnahmeinterview starten → `mandat.md` erstellen → `verlauf.md` mit Eröffnungseintrag anlegen → Nutzer fragen, ob zum neuen Mandat gewechselt werden soll.

**Ausgabe (Auszug):**

> Mandatsarbeitsbereich `bmw-marke-2026` angelegt.
>
> | Kurzzeichen | Mandant | Mandatstyp | Status | Eröffnet |
> |---|---|---|---|---|
> | bmw-marke-2026 | BMW AG | Markenschutz | aktiv | 2025-07-15 |
>
> Möchten Sie jetzt zu `bmw-marke-2026` wechseln?

## Risiken und typische Fehler

- **Interessenkonflikte nicht erkennen:** Diese Skill führt keine Interessenkonfliktprüfung durch — das ist Aufgabe des Anwalts und der Kanzlei. Die Aufnahme erfasst nur, was der Nutzer angibt.
- **Archivierung ist keine Löschung:** Geschlossene Mandate bleiben lesbar (§ 50 BRAO — Aufbewahrungspflicht mindestens 5 Jahre). Retention-Policy ist außerhalb des Skill-Umfangs.
- **Mandatsübergreifender Kontext standardmäßig aus:** Die Praxiskonfiguration hat ein `Mandatsübergreifender Kontext:`-Flag. Standardmäßig `aus` — Skill A im Mandat X liest niemals Dateien aus Mandat Y. Das ist die Vertraulichkeitsgarantie.
- **Kurzzeichen-Kollision mit Archiv:** Wird ein Kurzzeichen wiederverwendet, das im Archiv liegt, wird das archivierte Mandat unter `_archiv/<kurzzeichen>/` bewahrt; das neue erhält einen anderen Namen.

## Quellenpflicht

Alle Aussagen zu Vertraulichkeit, Aufbewahrung und Interessenkonflikten müssen auf konkreten Normen beruhen:

- **§ 43a BRAO** (Verschwiegenheit), **§ 43a Abs. 4 BRAO** (widerstreitende Interessen), **§ 203 StGB** (Verletzung von Privatgeheimnissen), **§ 50 BRAO** (Handaktenaufbewahrung)
- Modellannahmen als `[Modellwissen — verifizieren]` kennzeichnen.

## Triage-Fragen bei Mandatseröffnung

Bevor das Mandat angelegt wird, klaere:
1. Ist ein Interessenkonflikt-Check (§ 43a IV BRAO) durchgefuehrt worden?
2. Sind die wesentlichen Mandatsdaten vollstaendig (Mandant, Gegner, Rechtsgebiet, Streitgegenstand)?
3. Wurde der Mandant über Honorar und Kostenrisiko aufgeklaert (§ 49b BRAO, § 34 RVG)?
4. Laeuft bereits eine Frist (z.B. Widerspruchsfrist Marke, Abmahnungsfrist), die sofort ins Fristenbuch muss?

## Aktuelle Rechtsprechung

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

<!-- AUDIT 27.05.2026
Task: Bundle 031 / Halluzinations-Reparatur
Korrektur: Zitat aus "Aktuelle Rechtsprechung"-Block entfernt (bei Zweifel loeschen).
-->
