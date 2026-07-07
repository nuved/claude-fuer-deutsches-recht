---
name: mandat-arbeitsbereich
description: "Wenn es um Produktmandat-Workspace in Produkthaftung und Produktrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# فضای کاری دستورات محصول

## مسیر کار

- روشن‌کردن نقش، هدف و محصول کاری خواسته‌شده: چه کسی اقدام می‌کند، چه تصمیمی در پیش است، چه مهلتی در جریان است و چه خروجی‌ای لازم است؟
- اولین زمان و ریسک های فوری را نشان دهید: GPSR آغاز به کار 13.12.2024، ماشین آلات، 2001.2027. تولیدات و توسعه12.2026، فوراً برگشت، گزارش حادثه جدی در عرض دو روز
- بررسی معیارهای مربوط به: ProdSG, ProdHaftG، نظارت بر بازار اتحادیه اروپاVO 2019/1020، ایمنی محصولات اتحادیه اروپاVO 2023/988 (GPSR از 13.12.2024), محصول مسئولیت:RL 2024/2853 ، ماشین آلات، ووس 2023/1230, GPSGV - یافته های مربوط به gesetze-im-internet.de, dejure.org،آفتاب BVerfG-/BGH-/EuGH-دیتابیس زنده را بررسی کنید، بدون نقل قول دانش مدل
- تعیین و انتخاب صحیح ارجاعی برای سازمان های مربوطه: تولید کنندگان، واردکنندگان، فروشندگان، ارائه دهندگان خدمات تکمیل کننده، اداره نظارت بر بازار (BAuA) ، آژانس نامگذاری شده، مصرف کنندگان نهایی.
- جمع آوری اسناد و شواهد، بررسی شکاف ها: اعلامیه ی مطابق سازی، مستندات فنی، تجزیه و تحلیل ریسک، CE نشان دادن، مفهوم بازپسین، گزارش ایمنی، مقررات بازار آنلاین - دریافت مدارک از طریق مشاهده پرونده یا پرسیدن مشتری ، چک زنده برای تغییرات روزانه در استانداردها و شیوه های مدیریت.

## هدف

وکلا و حقوقی های داخلی در یک زمان روی چندین محصول، دستورات و پروسه کار می کنند.§ 43a Abs. 2 BRAO, § 203 StGB) و همچنین جداسازی واقعی تحلیل های حقوقی محصول. این مهارت، سطح مدیریت فایل نازک است که این جدایی را تضمین می کند.

**بعد از حد معمول غیر فعال شده است.** وکلا داخلی با یک زمینه شرکت واحد به این مهارت نیاز ندارند - آنها فقط در سطح دفتر / سازمان کار می کنند. `## Mandats-Workspaces` در دفتر CLUDE.md `Aktiviert` به `✗` این موضوع را می گوید: `/mandat-workspace`-حکومت را به حالت غیر فعال سفارش بده و `/kaltstart-interview --redo` برای کاربران که واقعا نیاز به انزوا در اختیار دارند.

این مهارت زمانی را می گیرد که کاربر بخواهد دستورات ایجاد کند، تغییر دهد، فهرست بندی نماید یا متن فرمان را غیرفعال سازد.

## ورودی‌ها

- ** فرماندهی زیر:** `neu`, `liste`, `wechsel`, `schließen` یا `keine` - پس از آن، اگر لازم باشد
- **مهم:** حروف کوچک با خط های متصل (به عنوان مثال `mustermann-gmbh-launch-2026`, `klindt-prüfung-q3`)
- **برای `neu`:** اطلاعات مربوط به مشتریان از مصاحبه ثبت نام (به مرحله 2 راه اندازی را ببینید)

** فرمان های زیر در نظرسنجی:**
- `/produktrecht:produktrecht-mandat-arbeitsbereich neu <slug>` - ایجاد فضای کار جدید برای ماموریت، انجام مصاحبه های کوتاه `mandat.md` نوشتن
- `/produktrecht:produktrecht-mandat-arbeitsbereich liste` - فهرست مأموریت های دارای وضعیت و ماموریت فعال
- `/produktrecht:produktrecht-mandat-arbeitsbereich wechsel <slug>` - در حال انجام ماموریت فعال
- `/produktrecht:produktrecht-mandat-arbeitsbereich schließen <slug>` - ثبت دستور (نه حذف)
- `/produktrecht:produktrecht-mandat-arbeitsbereich keine` - غیر فعال کردن زمینه ی ماموریت، کار فقط در سطح دفتر

## چارچوب حقوقی

### رازداری از وظیفه و اصول قانونی حرفه ای

- § 43a Abs. 2 BRAO: محترم وکیل باید در خصوص قانون حرفه ای، به عنوان یک وظیفه اصلی از خود محافظت کند؛ بدون محدودیت زمانی برای تمام اطلاعات مربوط به مأموریت ها اعمال می شود
- § 2 BORA: مشخص کردن عدم شناخت، وظیفه استخدام کارکنان
- § 203 StGB: نقض راز خصوصی - مجازات کیفری در مورد انتقال اطلاعات غیر مجاز
- § 43a Abs. 4 BRAO: ممنوعیت برخورد منافع - جدایی از محل کار و ماموریت، بررسی اختلافات را پشتیبانی می کند اما جایگزین آن نمی شود
- قضیه: هیچ تصمیمی را از دانش نمونه ای نقل نکنید؛ قبل از انتشار با دادگاه، شکل تصمیم گیری و تاریخ آن ها، نشانه های پرونده یا اظهارات قابل اثبات را توسط منبع رسمی یا آزاد تأیید کنید.

### قاعدهٔ منابع

قانون منبع: هیچ جای برای یافتن نظرات، کتابچه یا مقاله از دانش مدل؛ ادبیات فقط با منابع کاربر و یا زیرنویس زنده مجوزff.
### تعهدات نگهداری

- § 50 BRAO: نیاز به نگهداری دستاوردها - در اصل 5 سال از پایان دوره؛ ثبت نام حذف نیست
- §§ 257 HGB, 147 AO: مهلت های عمومی برای نگهداری اسناد تجاری و مالیاتی (6-10 سال)

## زمان

### مرحله 0: بررسی وضعیت فعال سازی

`CLAUDE.md` این کتاب را برای شرکت مطالعه کنید و `## Mandats-Workspaces` بررسی کنید.

- اگر `Aktiviert: ✗` → به کاربر اطلاع دهید: "منتظرات ورک اسپیس غیر فعال شده اند - آنها را در یک عمل داخلی با تنها مشتری تنظیم کرده اید؛ افزونه خود بخود بر اساس زمینه دفتر کار می کند. اگر شما واقعاً بین مشتریان فعالیت دارید، `/produktrecht:produktrecht-kaltstart-interview --redo` در صورت انتخاب یک تنظیمات دفتر خارجی، شما باید `/mandat-workspace` نه".
- اگر `Aktiviert: ✓` → ادامه به فرمان زیر

### مرحله اول: شناسایی و اجرای فرمان فرعی

به دلیل اول (کمتر) پاسخ دهید:
- `neu` → مصاحبه های ثبت نام `mandat.md` راه اندازی
- `liste` → همه `mandate/*/mandat.md` شمارش و انتشار جدول
- `wechsel` → به روز رسانی ماموریت فعال در CLAUDE.md
- `schließen` → فرمانده در `_archiviert/` تعویض
- `keine` → `Aktives Mandat:` به `keine — nur Kanzleikontext` قرار دادن

### مرحله دوم: مصاحبه ثبت نام (تنها در `neu`)

1. بررسی کنید که آیا سلوگ در حال حاضر `mandate/<slug>/` یا `mandate/_archiviert/<slug>/` در صورت استفاده مجدد، اجازه دهید که یک سلوگ دیگر را انتخاب کنید.
2. مصاحبه:
 - **منتظرم** (طرفی یا بخش داخلی شرکت در محل)
 - **طرف مقابل / شرکت کنندگان** (دقیقه دیگر - ممکن است چند نفر باشد)
 - **منتظرهای دستور* (از پروفایل دفترچه؛ برای حقوق محصول: راه اندازی محصولات) | بررسی ویژگی | بررسی اظهارات بازاریابی | تجزیه و تحلیل ریسک | دامنه محصول دائمی | (مختلف) 
 - ** سطح اطمینان** (استانداردی) | افزایش | تیم پاک - سطح بالا نیاز به احتیاط در استخدام های مختلف دارد) 
 - **حرف اصلی** (2-5 جمله: این چیست؟ چه کسانی در آن شرکت می کنند؟
 - **مختلفات اختصاصی به ماموریت** از فرآیند استاندارد (به عنوان مثال "مانت 24 ماه محدود مسئولیت است و نه 12" ، "نرد: شرکتی - طرف مقابل شریک استراتژیک")
 - **منتظرات مرتبط** (تدابیر مربوطه)
3. `mandate/<slug>/mandat.md` با این طرح که در زیر توضیح داده شده است، راه اندازی کنید.
4. `mandate/<slug>/verlauf.md` با یک نوشته "آفتاد" ایجاد کنید.
5. خالی `mandate/<slug>/notizen.md` -بذارید .
6. **حتی به طور خودکار تغییر نمی کند.** سوال: "آیا باید الان `<slug>` تغییر می کنند؟`/produktrecht:produktrecht-mandat-arbeitsbereich wechsel <slug>`)"

### مرحله 3: فهرست را منتشر کنید (تنها در `liste`)

همه `mandate/*/mandat.md` در این بخش، می توان به عنوان یک صفحه و یا چند قسمت از آن را حذف کرد.

| خروجی | مشتری | نوع فرمان | وضعیت | باز شده | فعال |
|---|---|---|---|---|---|

مأموریت فعال `*` این امر را باید در یک عنوان جداگانه "آرشیو شده" ذکر کرد.

### مرحله 4: تغییر دستور (تنها در زمان `wechsel`)

1. بررسی اینکه آیا `mandate/<slug>/mandat.md` اگر وجود نداشته باشد، `/produktrecht:produktrecht-mandat-arbeitsbereich neu <slug>` پیشنهاد می کنم.
2. خط `Aktives Mandat:` در کلاهبرداری `Aktives Mandat: <slug>` به روز رسانی
3. خلاصه از `mandat.md` این برنامه ها برای تایید دستور کار مناسب، به صورت تبلیغاتی نمایش داده می شوند.

### مرحله 5: به پایان رساندن فرمان (تنها در صورت `schließen`)

1. بررسی اینکه آیا `mandate/<slug>/` وجود دارد.
2. یک مطلب "مختصر" با تاریخ امروز `mandate/<slug>/verlauf.md` و از آن استفاده کنید.
3. `mandate/<slug>/` بعد از `mandate/_archiviert/<slug>/` (§ 50 BRAO: حفظ و نگهداری را رعایت کنید - هرگز حذف نکنید).
4. اگر فرمان بسته، دستور فعال بود: `Aktives Mandat:` به `keine — nur Kanzleikontext` می دانی؟

### مرحله 6: متن دستور العمل را غیر فعال کنید (تنها در `keine`)

`Aktives Mandat:` در کلاهبرداری `keine — nur Kanzleikontext` قرار دادن. تایید کردن به کاربر

## قضیه فعلی و اصول

- قضیه: هیچ تصمیمی را از دانش نمونه ای نقل نکنید؛ قبل از انتشار با دادگاه، شکل تصمیم گیری و تاریخ آن ها، نشانه های پرونده یا اظهارات قابل اثبات را توسط منبع رسمی یا آزاد تأیید کنید.

**نوردهای اصلی:** §§ 611-630 BGB (عقد خدمات، قانون فرماندهی) §§ 1-4 ProdHaftG — §§ 3، 3a UWG

- قانون منبع: ادبیات فقط با منابع کاربر یا دسترسی زنده مجاز؛ هیچ جای برای یافتن نظرات، کتابچه و مقاله از دانش مدل نیست.

## طرف ها

** فرمانده:** [Name]
**طرف مقابل / شرکت کنندگان:** [Name(n)]

## نوع فرمان

 [بازار محصول] | بررسی ویژگی | بررسی اظهارات بازاریابی | تجزیه و تحلیل ریسک | دامنه محصول دائمی | [در مورد دیگر، با یک دلیل] 

## مواد هسته ای

[2–5 Sätze. Worum geht es? Wer sind die Beteiligten? Was steht auf dem Spiel? Was unterscheidet dieses Mandat vom Standardfall?]

## تفاوت های اختصاصی

*هر انحراف از استاندارد کل دفتر که فقط برای این ماموریت اعمال می شود.*

- [z. B. "Haftungsbeschränkung: Mandant besteht auf 24 Monaten statt Kanzleistandard 12 Monate."]
- [z. B. "Ton: partnerschaftlich — Gegenseite ist strategischer Partner."]
- [z. B. "Rechtsstand: österreichisches Recht statt deutschem."]

## مأموریت های مرتبط

- [Slug — einzeilige Begründung der Verbindung]

## اطلاعات محرمانه

[Bei erhöhter Vertraulichkeit oder Clean-Team: Begründung. Wer darf Mandatsdateien einsehen? Ist mandatsübergreifender Kontext auch bei globaler Aktivierung zulässig?]
```

### `verlauf.md`-Starteintrag

```markdown
### دوره: [Mandant] — [Kurzbeschreibung]

گزارش مربوط به اتفاقات اخیر بالا

---

## [JJJJ-MM-TT] - اجاره باز شده

ضبط تمام شد `[slug]`حالت: فعال
[Anfangskontext, der über mandat.md hinausgeht — z. B. "Eröffnet auf Basis des eingehenden PRD-Entwurfs von [Gegenseite]."]
```

## Beispiel

**Sachverhalt:** Kanzlei betreut drei Produktrechtsmandate gleichzeitig: Hersteller A (Maschinenlauf-Review), Hersteller B (Health-Claims-Prüfung Nahrungsergänzung), Unternehmen C (dauerhafter Produktrechtsberater).

```
/حق محصول:قانون محصولات -منتظره کار زمینه جدید تولید کننده ماشین آلات-2026
/حق محصول:قانون محصولات - کار و وظیفه
/حق محصول:قانون محصولات - کارنامه
/حق محصول:قانون محصولات -منتظره
/حق محصول:قانون محصولات -منتظره- حوزه کاری تغییر تولید کنندگان و ماشین آلات-2026
```

Nach dem Wechsel zu `hersteller-a-maschinen-2026` liest jede Skill ausschließlich die `mandat.md` dieses Mandats und schreibt Ausgaben in den zugehörigen Ordner. Kontextüberlauf auf `hersteller-b-health-claims` ist ausgeschlossen.

## Risiken und typische Fehler

- **Mandatskontext-Überlauf:** Werden Prüfvermerke für Mandant A mit Informationen aus Mandat B angereichert, liegt ein potenziellerVerstoß gegen § 43a Abs. 2 BRAO und § 203 StGB vor. Der Cross-Mandats-Kontext-Flag darf nur auf explizite Nutzeranfrage aktiviert werden.
- **Slug-Wiederverwendung:** Ein neuer Slug `acme-launch` nach Archivierung von `_archiviert/acme-launch` erzeugt Verwirrung über welche Version aktiv ist. Die Skill prüft beide Pfade.
- **Zu frühe Mandatsschließung:** Fristen nach § 50 BRAO (5 Jahre) dürfen nicht durch frühzeitiges Schließen ausgehebelt werden. Schließen archiviert; es löscht nie.
- **Vergessener Mandatswechsel:** Wenn nach der Arbeit an Mandat A kein expliziter Wechsel erfolgt, arbeitet die nächste Skill weiter im Kontext von Mandat A. Regelmäßig `/mandat-workspace liste` aufrufen, um zu prüfen, welches Mandat aktiv ist.
- **Keine automatische Interessenkonfliktprüfung:** Diese Skill kann keine Interessenkonflikte i. S. d. § 43a Abs. 4 BRAO feststellen. Das ist Aufgabe des Anwalts. Das Aufnahmeinterview erfasst, was der Nutzer erklärt — nicht was wirklich zutrifft.
- **Clean-Team-Mandate:** Bei Clean-Team-Vertraulichkeit ist mandatsübergreifender Kontext auch bei globalem `Ein` nicht zulässig. Explizit in der `mandat.md` unter Vertraulichkeitshinweise vermerken.

## Quellenpflicht

- **Berufsrecht:** BRAO-Volltext (gesetze-im-internet.de), BORA, FAO
- **Aufbewahrung:** § 50 BRAO, ggf. §§ 257 HGB, 147 AO
- **Rechtsprechung:** amtliche oder frei zugängliche Quellen; lizenzierte Datenbanken nur bei vorhandenem Zugang — BGH-Entscheidungen zum Mandatsgeheimnis und Interessenkonflikt in der Form `BGH, Urt. v. TT.MM.JJJJ – Az., Fundstelle Rn. X`

Quellen, die nur aus Modellwissen stammen, nicht als zitierfähige Fundstelle ausgeben. Pinpoint-Zitate nur verwenden, wenn Randnummer, Seite oder amtlicher Leitsatz aus der konkreten Quelle geprüft wurde.

Hinweis: Dieser Skill hält Produktmandate sauber getrennt und stärkt damit die anwaltliche Arbeitsorganisation; Interessenkonflikte bewertet weiterhin der verantwortliche Rechtsanwalt.

<!-- AUDIT 27.05.2026 bundle_040
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
-->
