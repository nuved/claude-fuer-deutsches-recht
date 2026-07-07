---
name: mandantenakte-anlegen-mandantenbrief-vorlagen
description: "Wenn es um Mandantenakte anlegen in Kanzlei-Allgemein geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# ثبت اسناد مشتری

## حوزهٔ کار

در این گزارش، اطلاعات مربوط به قرارداد های کنتینتی را ثبت می کند.§ 43a Abs. 4 BRAO § 3 BORA) اطلاعات مربوط به حفاظت از داده ها (Art. 13 DSGVO) شناسایی پولشویی (§§ 10 11 GwG) توافقنامه ی حقوق یا RVG- اشاره. ساخت پرونده ها را در زیر دستورات/ نشانه های ثبت شده / با فرعی استاندارد تولید می کند فرماندهی طرح اطلاعات محرمانه، اسناد نقدی؛ وارد شدن به کلانت استام; ارتباط با دفتر زمان زمانی اگر مهلتها همراه باشد: کار بر روی این خط معینی بررسی و نقش مشخص ، مدت زمان، صلاحیت، بار اثبات و محصول مورد نظر

## مسیر کار

- روشن‌کردن نقش، هدف و محصول کاری خواسته‌شده: چه کسی اقدام می‌کند، چه تصمیمی در پیش است، چه مهلتی در جریان است و چه خروجی‌ای لازم است؟
- نخست علامت‌گذاری مهلت‌ها و خطرهای فوری: تنها از مهلت‌های همان حوزهٔ حقوقی مشخص و همان پرونده استفاده کنید؛ اعتراض (Widerspruch)، دعوا (Klage)، ایراد (Einspruch)، طرق شکایت (Rechtsmittel)، مرور زمان (Verjährung)، سقوط حق (Verwirkung) و مهلت‌های ایراد، اعلام، ثبت و انقضا را به‌دقت جدا کنید و هرگز از حوزهٔ تخصصی دیگری برندارید.
- بررسی معیارهای مربوط به: BRAO §§ 43، 43a، 43e، 45 49b، 53 59b و 73 BORA §§ 2, 3, 4, 5, 6, 10, 11, 12; RVG §§ 3a, 10; GwG §§ 2, 10, 11, 43; DSGVO Art. 5, 6, 9, 28, 32; BDSG § 26; ZPO § 130d; BRAO § 31aاز اطلاعات اتاق های محلی و بی-ای، بدون مدارک بین المللی
- تعیین مرجع صالح و انتخاب درست مخاطب: موکل، طرف مقابل، ادارهٔ صالح یا دادگاه، کارشناسان و در صورت لزوم نهاد اتحادیهٔ اروپا/بین‌المللی (به جزئیات اسکیل نگاه کنید).
- گردآوری اسناد و ادلّه و بررسی خلأها: پرونده‌های اداری، اسناد قراردادی، لوایح، تصمیم‌های اداری (Bescheide)، صورت‌جلسه‌ها، نظرهای کارشناسی و ادلّهٔ بیرونیِ همان حوزه — مدارک نبود را از راه دسترسی به پرونده یا پرسش از موکل فراهم کنید، و برای تغییرهای روزِ قوانین و رویهٔ اداری بررسی زنده انجام دهید.

## بررسی درگیری (§ 43a Abs. 4 BRAO)

**پیش از هر اقدام به انجام وظیفه**

- بررسی در قبای یک معاون، اینکه آیا به عنوان یکی از معلمان فعلی یا قبلی این شرکت استخدام شده است.
- بررسی اینکه آیا به عنوان یک فرماندار § 3 BORA (به نفع متضاد)
- در صورت اختلاف: عدم پذیرش مجوز یا رضایت نوشته شده از همه افراد درگیر.
- ثبت چک کننده با تاریخ اول

## سیستم شماره گذاری پرونده

توصیه:

`<Jahr>/<lfd. Nr.>` (به عنوان مثال: `2026/0042`)

یا

`<RG>-<Jahr>-<Nr>` (به عنوان مثال: `Z-2026-0042` در قانون مدنی).

## ساختار فهرست

در زیر `~/.claude/plugins/config/claude-fuer-deutsches-recht/kanzlei-allgemein/mandate/<az>/`:

```
01_stammdaten/
 mandatsblatt.md
 vollmacht.docx
 vollmacht-unterschrieben.pdf
 datenschutzhinweis.md
 gwg-identifizierung.pdf
 konfliktprüfung.md
 honorarvereinbarung.docx (falls Vereinbarung)
02_eingaenge/
03_schriftsaetze/
04_anlagen/
05_fristen/
06_honorar/
 rechnungen/
 zahlungseingang.yaml
07_korrespondenz_mandant/
08_korrespondenz_dritte/
09_aktennotizen/
_archiv/
```

## نامه ی فرمانده

```yaml
mandat-az: 2026/0042
mandat-eroeffnet: 2026-05-20
zuständiger-anwalt: RA Mueller
sekretariat: Frau Schmidt

mandant:
 typ: juristische-person # juristische-person / natürliche-person / ehepaare-vergleichsweise
 name: Mueller GmbH
 anschrift: ...
 rechtsform: GmbH
 vertretungsberechtigte: Hans Mueller (Geschäftsführer)
 registergericht: HRB ... AG München
 ust-id: DE...
 steuernummer: ...

ansprechpartner:
 name: Hans Mueller
 funktion: Geschäftsführer
 telefon: ...
 e-mail: ...

mandatsumfang:
 beschreibung: Verteidigung in Zivilrechtsstreit gegen ABC GmbH (Klage)
 rechtsgebiet: Zivilrecht / Vertragsrecht
 instanz: 1. Instanz LG München
 streitwert: 35.000 EUR

honorar:
 basis: rvg # rvg / vereinbarung
 stundensatz: 320 # bei Vereinbarung
 pkh-pruefung: nein

konfliktpruefung:
 erfolgt-am: 2026-05-20
 ergebnis: kein-konflikt
 geprueft-von: RA Mueller
```

## فرماندهی

متن فرماندهی با:

- به عنوان وکیل شرکت.
- در این زمینه، محدوده صلاحیت مشخص شده است (در حال حاضر از طریق دادگاه های مقدماتی نیز می توان به آن ها رسیدگی کرد).
- دست کم و جایگزین شدن
- فرمان دریافتی برای تحویل.
- -آره .
- تاریخ و امضا مشتری.

## اطلاعات مربوط به حفاظت از داده (Art. 13 DSGVO)

نماد استاندارد:

- هویت مسئول (کتابخانه)
- هدف پردازش (منتظره اجرا)
- (در مورد این موضوع،Art. 6 Abs. 1 lit. ب DSGVO + § 50 BRAO پرونده ها
- دریافت کنندگان (در دادگاه اداره مالیاتی مشاوران طرف دیگر - به عنوان مورد نیاز).
- مدت زمان نگهداری (کم از 6 سال پس از پایان دوره) § 50 Abs. 1 BRAO).
- حقوق مربوطه (تغییر اطلاعات، اصلاح حذف اعتراض).

## شناسایی پولشویی (§§ 10 11 GwG)

در مورد دستورات زیر GwG در این بخش، موارد زیر شامل می شوند (به عنوان مثال معاملات املاک و مستغلات تجارت نقدی از حد پایین):

- شناسایی شخص طبیعی با کپی از کارت عکاسی
- در مورد یک شخص حقوقی، HRB و همچنین افراد دارای حقوق اقتصادی به صورت شفافیت ثبت شده است.
- بررسی فهرست تحریم های اتحادیه اروپا و ملی.
- ثبت چک کننده با تاریخ اول

## ثبت قبیله معاون

در `~/.claude/plugins/config/claude-fuer-deutsches-recht/kanzlei-allgemein/mandantenstamm.yaml`:

```yaml
- mandant-id: M-00874
 name: Mueller GmbH
 typ: juristische-person
 mandate:
 - 2026/0042
 konfliktstatus: kein-konflikt
 letzte-pruefung: 2026-05-20
```

## آدیتی

- پرونده های ثبت شده با آدرس (دستگاه وکیل تاریخ).
- تغییرات با آدیت ترایل.

## خروجی

- ساختار کامل پرونده ها
- نامه و اسناد اجباری.
- ثبت نام در قبیله مشتری
- در صورت لزوم، به دفترچه ی مهلت اشاره کنید.

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **الزامِ تمام‌نویسی و استانداردِ قالب.** محصولِ نهایی در **جمله‌های کامل و تمام‌نوشته** تحویل می‌شود — نه اسکلتِ کلیدواژه، نه تنهٔ خالیِ شرط، نه صرفِ فهرست. شرط‌ها به‌صورتِ جمله‌های تمام‌نوشتهٔ بیان‌گرِ اثرِ حقوقی می‌آیند؛ جای‌گیرها مانند `[Name der Mandantin]` روشن علامت می‌خورند و متنِ پیرامون کامل می‌ماند.
>
> **شکلِ نوشتار:** هرگاه لایحه، قرارداد، یادداشت، تصمیم، ومرک یا هر سندِ نهاییِ دیگر به‌صورتِ DOCX، PDF یا متنِ قالب‌بندی‌شده بیرون داده شود، باید **Times New Roman ۱۱ pt** به‌عنوانِ قلمِ پایه به‌کار رود. عنوان‌ها در همان قلم می‌مانند و تنها می‌توانند سیاه (بولد) یا پلکانی باشند. در خروجیِ صرفاً Markdown یا چت، این خواستهٔ قالب به‌عنوانِ یادداشتِ برون‌سپاری درج می‌شود.
>
> **شماره‌گذاری:** ساختاربندی منحصراً اعشاری (`1`، `1.1`، `1.1.1` و به همین ترتیب). بدون اعداد رومی، بدون ساختاربندی حرفی یا آمیخته.
<!-- END ausformulierungspflicht (autogen) -->

