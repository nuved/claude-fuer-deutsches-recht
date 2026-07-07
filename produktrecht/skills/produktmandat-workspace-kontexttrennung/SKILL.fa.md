---
name: produktmandat-workspace-kontexttrennung
description: "Wenn es um Produktmandat-Workspace und Kontexttrennung in Produkthaftung und Produktrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# فضای کاری و جداسازی زمینه

## هدف

وکلا و حقوقی های داخلی در یک زمان روی چندین محصول، دستورات و پروسه کار می کنند.§ 43a Abs. 2 BRAO, § 203 StGB) و همچنین جداسازی واقعی تحلیل های حقوقی محصول. این مهارت، سطح مدیریت فایل نازک است که این جدایی را تضمین می کند.

**بعد از حد معمول غیر فعال شده است.** وکلا داخلی با یک زمینه شرکت واحد به این مهارت نیاز ندارند - آنها فقط در سطح دفتر / سازمان کار می کنند. `## Gesellschaftsrechtlicher Mandatsworkspace und Kontexttrennungs` در دفتر CLUDE.md `Aktiviert` به `✗` این موضوع را می گوید: `/mandat-workspace`-حکومت را به حالت غیر فعال سفارش بده و `/kaltstart-interview --redo` برای کاربران که واقعا نیاز به انزوا در اختیار دارند.

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

## قالب خروجی

### `mandat.md`-تازه

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **الزامِ تمام‌نویسی و استانداردِ قالب.** محصولِ نهایی در **جمله‌های کامل و تمام‌نوشته** تحویل می‌شود — نه اسکلتِ کلیدواژه، نه تنهٔ خالیِ شرط، نه صرفِ فهرست. شرط‌ها به‌صورتِ جمله‌های تمام‌نوشتهٔ بیان‌گرِ اثرِ حقوقی می‌آیند؛ جای‌گیرها مانند `[Name der Mandantin]` روشن علامت می‌خورند و متنِ پیرامون کامل می‌ماند.
>
> **شکلِ نوشتار:** هرگاه لایحه، قرارداد، یادداشت، تصمیم، ومرک یا هر سندِ نهاییِ دیگر به‌صورتِ DOCX، PDF یا متنِ قالب‌بندی‌شده بیرون داده شود، باید **Times New Roman ۱۱ pt** به‌عنوانِ قلمِ پایه به‌کار رود. عنوان‌ها در همان قلم می‌مانند و تنها می‌توانند سیاه (بولد) یا پلکانی باشند. در خروجیِ صرفاً Markdown یا چت، این خواستهٔ قالب به‌عنوانِ یادداشتِ برون‌سپاری درج می‌شود.
>
> **شماره‌گذاری:** ساختاربندی منحصراً اعشاری (`1`، `1.1`، `1.1.1` و به همین ترتیب). بدون اعداد رومی، بدون ساختاربندی حرفی یا آمیخته.
<!-- END ausformulierungspflicht (autogen) -->

```markdown
# Mandat: [Mandant] — [Kurzbeschreibung]

**Slug:** [slug]
**Eröffnet:** [JJJJ-MM-TT]
**Status:** aktiv
**Vertraulichkeit:** [standard / erhöht / Clean-Team]

---
## Parteien

**Mandant:** [Name]
**Gegenseite / Beteiligte:** [Name(n)]

## Mandatstyp

[Produkt-Launch | Feature-Review | Marketingaussagen-Prüfung | Risikoanalyse | Produktbereich dauerhaft | Sonstiges — mit einzeiliger Begründung]

## Kernsachverhalt

[2–5 Sätze. Worum geht es? Wer sind die Beteiligten? Was steht auf dem Spiel? Was unterscheidet dieses Mandat vom Standardfall?]

## Mandatsspezifische Abweichungen

*Jede Abweichung vom kanzleiweiten Standard, die nur für dieses Mandat gilt.*

- [z. B. "Haftungsbeschränkung: Mandant besteht auf 24 Monaten statt Kanzleistandard 12 Monate."]
- [z. B. "Ton: partnerschaftlich — Gegenseite ist strategischer Partner."]
- [z. B. "Rechtsstand: österreichisches Recht statt deutschem."]

## Zusammenhängende Mandate

- [Slug — einzeilige Begründung der Verbindung]

## Vertraulichkeitshinweise

[Bei erhöhter Vertraulichkeit oder Clean-Team: Begründung. Wer darf Mandatsdateien einsehen? Ist mandatsübergreifender Kontext auch bei globaler Aktivierung zulässig?]
```

### `verlauf.md`-دستخونه شروع

```markdown
# Verlauf: [Mandant] — [Kurzbeschreibung]

Anhängendes Ereignisprotokoll. Neuestes oben.

---

## [JJJJ-MM-TT] — Mandat eröffnet

Aufnahme abgeschlossen. Slug: `[slug]`. Status: aktiv.
[Anfangskontext, der über mandat.md hinausgeht — z. B. "Eröffnet auf Basis des eingehenden PRD-Entwurfs von [Gegenseite]."]
```

## نمونه

**آقای:** این شرکت در یک زمان سه فرماندهی حقوقی محصول را اداره می کند: تولید کننده A (ملاحظه کار ماشین) ، سازنده B (صحت و ادعاهای بررسی مواد غذایی مکمل) و شرکت C (مشاورهای قانونی دائمی محصولات).

```
/produktrecht:produktrecht-mandat-arbeitsbereich neu hersteller-a-maschinen-2026
/produktrecht:produktrecht-mandat-arbeitsbereich neu hersteller-b-health-claims
/produktrecht:produktrecht-mandat-arbeitsbereich neu unternehmen-c-dauerberatung
/produktrecht:produktrecht-mandat-arbeitsbereich liste
/produktrecht:produktrecht-mandat-arbeitsbereich wechsel hersteller-a-maschinen-2026
```

پس از تغییر به `hersteller-a-maschinen-2026` هر مهارت فقط به زبان می آید `mandat.md` این دستور العمل و هزینه ها را در فولدرهای مربوطه می نویسد. `hersteller-b-health-claims` از این رو، نمی توان گفت.

## خطرات و اشتباهات معمول

- **مطالعه متن ماموریت:** اگر اطلاعات مربوط به مأموریت B را در یادداشت های آزمون برای معین A گنجانید، ممکن است خلاف قانون باشد § 43a Abs. 2 BRAO و § 203 StGB پرچم متن مرجع عبور فقط باید در صورت درخواست صریح کاربر فعال شود.
- ** استفاده مجدد از سلوگ:** یک سلوغ جدید `acme-launch` پس از ثبت `_archiviert/acme-launch` این باعث می شود که ما در مورد نسخه ای از آن ها دچار سردرگمی شویم. مهارت هر دو مسیر را بررسی میکند.
- **برای پایان دادن به دوره های اولیه:** § 50 BRAO (۵ سال) نباید با بسته شدن زودرس حذف شود.
- ** تغییر ماندگار فراموش شده:** اگر بعد از کار در مهد A هیچ تغییری صریحی رخ ندهد، مهارت بعدی همچنان به فعالیت خود ادامه می دهد. `/mandat-workspace liste` تماس بگیرید تا ببینید چه ماموریت هایی فعال است.
- **هیچ بررسی خودکار در مورد تضاد منافع:** این مهارت نمی تواند هیچ تضاد علاقه ای را ایجاد کند. S. د. § 43a Abs. 4 BRAO این وظیفه وکیل است. مصاحبه ضبط شده چیزی را که کاربر می گوید، ثبت کرده و نه آنچه واقعاً درست است.
- **منتظرات تیم پاک:** در مورد اطمینان از یک گروه پاک، زمینه های بین المللی نیز برای جهانی است `Ein` اجازه نمی دهد. `mandat.md` در زیر این مطلب، اطلاعات محرمانه را ذکر کنید.

## تعهد به منبع

- ** حقوق حرفه ای:** BRAOمتن کامل (gesetze-im-internet.de), BORA, FAO
- **حفاظتی:** § 50 BRAO, ggf. §§ 257 HGB, 147 AO
- **اقضیه:** منابع رسمی یا آزاد؛ پایگاه های اطلاعاتی که تنها در دسترس هستند، BGH-قرارهای سرپشتی و تضاد منافع در قالب `BGH, Urt. v. TT.MM.JJJJ – Az., Fundstelle Rn. X`

منابع که فقط از دانش مدللی هستند، به عنوان منبع قابل اقتباس استفاده نمی شوند. تنها زمانی که یک شماره ی پیش فرض یا صفحه ای و یا دستورالعمل رسمی را از این منبع مشخص بررسی کرده اند، از آن ها نقل قول می کنند.

توجه: این مهارت به حفظ جداسازی از دستورات محصول کمک می کند تا سازمان کاری وکلا را تقویت نماید؛ درگیری های منافع همچنان توسط وکیل مسئول ارزیابی می شود.

آډیت ۲۷05.2026 bundle_040
قضیه: هیچ تصمیمی را از دانش نمونه ای نقل نکنید؛ قبل از انتشار با دادگاه، شکل تصمیم گیری و تاریخ آن ها، نشانه های پرونده یا اظهارات قابل اثبات را توسط منبع رسمی یا آزاد تأیید کنید.
-->
