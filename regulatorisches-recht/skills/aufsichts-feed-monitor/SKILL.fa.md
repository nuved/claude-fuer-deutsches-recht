---
name: aufsichts-feed-monitor
description: "Wenn es um Regulatorischer Feed-Watcher in Regulatorisches Recht – Plugin für deutsches geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# نظارت بر تغذیه

## ورودی‌ها

- ** فهرست تماشاگران:** چه مقامات و حوزه های قانونی را باید نظارت کنیم؟
- **محدود اهمیت:** چگونه مادی سازی تنظیم می شود؟
- **مدت امتحان:** از کی؟ (بعد از آخرین دوره، به طور متناوب) `--since DATUM`)
- ** منابع:** فیدرهای تنظیم شده، آدرس های RSS, خدمات.
- **بخاطر:** متن تنظیم کننده برای طبقه بندی تکانه ای که به صورت دستی وارد شده است.

## چارچوب حقوقی

### قوانین هسته ای

- **BGBl* - اعلامیه رسمی؛ برای ورود به قوانین مهم است.
- **بزرگ: اتحادیه اروپا، مجموعه L + C** - قوانین و دستورالعمل های اجباری در این کشور.
- **خطوط گردآوری با فن** (به عنوان مثال MaRisk BA 2023، BAIT, ZAIT) - مشخص کنید
 مقررات نظارت؛ §§ 6، 25b KWG, §§ 6, 23 VAG, §§ 6 ff. WpHG.
- **BSI** - دستورالعمل های فنی و اعلامیهای انتقادی (§§ 8a ff. BSIG).
- **EU-KI-VO (VO (EU) 2024/1689)** - طبقه بندی ریسک بالا، الزامات مطابق با مقررات.
- **CSRD (RL (EU) 2022/2464)** - گزارش غیرمالی، استانداردهای ESRS.
- **Art. 20 Abs. 3 GG** - قانون اساسی، وضوحی در مورد قوانین؛ معیار برای
 ارزیابی اعلامیه های دولتی بدون استاندارد رسمی مجاز.

### تصمیمات اصلی / آرکر های بروزرسانی

حالت 05/2026. قبل از استفاده در اسناد زنده - هیچ نشانه های ثبت شده با دانش مدل.

- EuGH، ساعت 1302.2025 - C-383/23 (ILVA) DSGVO-دفعات می تواند به کل درآمد گروه مربوط شود؛ "شركات" در مفهوم قانون رقابت، برای نظارت بر شیوه های قومی مجازات مناسب است.
- EuGHساعت 02:12.2025 - C-492/23 (روسی رسانه) DSGVO در این مورد، DSA پیش می رود؛ هیچ امتیاز ارائه دهنده ای برای DSGVO- نقض، برای نظارت بر انطباق سیستم عامل ها مهم است.
- EuGH، ساعت 1903.2026 - C-526/24 (چشمی روتلر) DSGVO-برخواست اطلاعات ممکن است خلاف قانون باشد .
- BVerfG-خط های اساسی و شفافیت استاندارد (BVerfGE 33, 125; 49, 89- Kalkar) در فرمان [bundesverfassungsgericht.de](https://www.bundesverfassungsgericht.de) زنده تایید کنید.
- در این زمینه، به گزارش شرکت های بین المللی اطلاعات و ارتباطات (Bafin) ، "مجموعه ی خدمات جدید" از طریق برنامه های کاربردی با هدف ارائه داده شده توسط سازمان DORA برای سال 2025/2026: لیست ESA از سرویس دهندگان مهم ICT سوم (نومبر 2025)؛ تاریخ 09.30 - BaFin.03.2026.
- این گزارش در سال ۲۰۱۴ به عنوان "مجموعه ای از برنامه های کاربردی" منتشر شد.07.2027; اداره AMLA که از سال 01 در فرانکفورت واقع شده است.07.2025 عمل جراحی.
- این امر در مورد "مجموعه ای از افراد" به نظر می رسد که با توجه به شرایط مختلف، باید بر اساس قوانین و مقررات مربوط به کشور های دیگر نیز اقدام کند.02.2025؛ GPAI از 02.08.2025استفاده اصلی از هوش مصنوعی با ریسک بالا در سال ۲۰۰۲08.2026; قطعات امنیتی از 02.08.2027.

### نظرات

- `Sachs (Hrsg.), GG, 10. Aufl. 2021, Art. 20 Rn. 78 ff.` - قانون اساسی
 و وضوح استاندارد به عنوان یک معیار ارزیابی برای اعلامیه های دولتی.
- قانون منبع: ادبیات فقط با منابع کاربر یا دسترسی زنده مجاز؛ هیچ جای برای یافتن نظرات، کتابچه و مقاله از دانش مدل نیست.
 مهارت های قانونی؛ مربوط به میزان تعهد نامه ی دایره ای با فن.
- `Schwennicke/Auerbach (Hrsg.), KWG/CRR, 4. Aufl. 2022, § 6 KWG Rn. 5 ff.`
 - شیوه و تاثیر قانونی اعلامیه های BaFin.

## زمان

### مرحله 0: بررسی شکاف

بررسی فهرست و تنظیمات منبع در مقابل کتالوگ داخلی.
شکاف آشکار (به عنوان مثال "BaFin" در فهرست تماشاچی، اما نه یک نمایشگر فدرال و یا
بافین ژورنال تنظیم شده) را یک بار نشان می دهد - تکرار نمی شود اگر شکاف
این موضوع شناخته شده و پذیرفته می شود.

### مرحله اول: تماس بگیرید

| منبع | محتوای آن |
|---|---|
| (در این زمینه،bgbl.de) | قوانین و مقررات |
| AB EU / EUR-Lex | قوانین اتحادیه اروپا، موجودیت یکپارچه |
| بافن (bafin.de(در مورد: | نامه های گردآوری، ورق تجاری و ضوابط عمومی |
| BSI (bsi.bund.de) | دستورالعمل های فنی، هشدارهای انتقادی |
| بررسی قانونی زنده | تایید زنده لازم است |
| BMJ | طرح های سخنرانان، اعلامیهای مطبوعاتی |
| شورای فدرال | چاپ و نظرات |
| آگهی دهنده های فدرال | اطلاعیه های مقامات |

خدمات قابل استفاده (سرچشمه های رسمی/آزاد یا پایگاه داده هایی که دارای مجوز هستند، با دسترسی Premium و Wolters Kluwer)
اگر تنظیم شده باشد، دوگونی ها را در سطح دیگر حذف کنید.

**هیچ افزونه ای خاموش نیست.** در چند مورد، هیچ تحقیق وب مستقل -
گزینه هایی را برای کاربر ارائه دهید (چشمه های زمانی، منابع دیگر، جستجو با اشاره ی آزمون
تصمیم گیری در اختیار کاربر است.

**آگاهی به منبع** (هیچ وقت حذف نکنید): `[BGBl.]`, `[ABl. EU]`, `[BaFin-RSS]`, `[BSI]`,
`[Websuche — prüfen]`, `[Modell-Wissen — prüfen]`, `[manuell eingegeben]`.
منابع ثانویه (برنامه های شرکت، پورتال تخصصی) `[Sekundärquelle]`
نشان دادن؛ کاهش سطح مواد تا زمانی که منبع اولیه تایید شود.

### مرحله دوم: طبقه بندی

| نوع ثبت | طبقه بندی |
|---|---|
| قانون / مقررات (نهایت) | همیشه مهم |
| طرح مرجع / سند مشورت | ارزش بررسی - زمان تعبیر |
| اجرای قانون / حکم مجازات | بخش ارائه → مهم؛ نزدیک بودن به موضوع |
| دستورالعمل ها / صفحات مشخص | ارزش امتحان |
| خبرگزاری ها / بیانیه های مطبوعاتی | به اطلاع رسانی / پر شدن |

هیچ وقت طرح های سخنران و مشاوره را "هميشه مهم" نمی دانند - هنوز هم
واجب رعایت: در این مطلب به وضوح یادآوری کنید که "درسته اول.
[Datum]هنوز شکاف در تعمیل وجود ندارد".

### مرحله سوم: غنی سازی

برای هر مطلب فوق "به خاطر داشته باشید": خلاصه یکبار + توجه به اهمیت
+ لینک + ورود به بازار و یا زمان نظر دادن.

## بررسی های نظارتی در مورد تغذیه [Datum]
 زمان: [letzter Lauf] – [jetzt] | منابع: [...] | نوشته ها: [N] 

### خلاصه
[N Einträge erfordern Handlung bis [Datum] - سه تا: X، Y، Z]

### همیشه مهم
**[Behörde] — [Titel]**
[Zusammenfassung]. [Relevanz]. در حال اجرا: [Datum]. [Link] [Quellenkennung]
→ توصیه: [nächster Schritt]

### ارزش امتحان
**[Behörde] — [Titel]**
[Zusammenfassung]. زمان برای نظر: [Datum]. [Link] [Quellenkennung]

### برای اطلاع
[N] - واردات [Titelliste mit Links]

---
آخرین زمان امتحان: [Zeitstempel]
قبل از استفاده، محل های موجود را تأیید کنید.
```

Zusätzlich Dateiausgabe (Markdown) unter konfiguriertem Pfad oder
`~/regulatorisches-digests/reg-digest-YYYY-MM-DD.md`; bei mehreren Tagesläufen
anhängen statt überschreiben.

## Beispiel

**Watchlist:** "BaFin — Zahlungsdienste", "EU — KI-Verordnung". Letzter Lauf: 01.07.2024.

BaFin-RSS liefert Merkblatt zu § 25b KWG-Auslagerungen → "Prüfenswert" (Leitlinie).
EUR-Lex liefert delegierte Verordnung zur KI-VO → "Immer wesentlich" (EU-Rechtsakt).

```
### همیشه مهم
**EU - مقررات مرجعیت (EU) 2024/XXX در مورد AI**
ارزیابی های مشخصی برای هوش مصنوعی با ریسک بالا (Art. 43 آایس و آی، اِنکس ۳ Nr. 5).
01.08.2024. [ABl. EU L 2024/XXX] [ABl. EU]
→ بررسی فهرست های موجودی هوش مصنوعی در برابر لیست ریسک بالا ggf. شروع ارزیابی سازگاری
```

## Risiken und typische Fehler

- **Sekundärquelle als Primärquelle verwenden:** Kanzlei-Newsletter berichten über
 Entscheidungen, sind aber nicht die Entscheidung. Immer auf BGBl., ABl. oder
 Behördenwebsite verweisen.
- **Referentenentwurf als geltendes Recht einstufen:** Klare Kennzeichnung als Vorstufe.
- **Kommentierungsfristen übergehen:** Fristen sind real und oft kurz — immer im Tracker.
- **Verbindlichkeitsgrad verwischen:** BaFin-Rundschreiben sind keine Gesetze.
 Unterschied Gesetz / VO / Leitlinie / Merkblatt in der Ausgabe erkennbar halten.
- **Stille Ergänzung durch Websuche:** Ohne Rückfrage unzulässig.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

## Quellenpflicht

Jeder Eintrag muss enthalten: Behörde, Dokumenttyp, Datum, Direktlink zur Primärquelle,
Quellenkennung und ggf. Kommentierungsfrist. Zitierweise Rechtsprechung:
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Zitierweise Kommentare:
`Sachs/Sachs, GG, 10. Aufl. 2021, Art. 20 Rn. 78`

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 18 UStG
- § 25a KWG
- § 4 RDGEG
- § 13d RDG
- § 203 StGB
- Art. 288 AEUV
- § 25b KWG
- § 1 ZAG
- § 13 RDG
- § 10 ZAG
- Art. 80 AEUV
- § 17 UStG

### Leitentscheidungen

- EuGH C-6/64
- EuGH C-117/20
