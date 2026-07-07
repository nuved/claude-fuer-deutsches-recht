---
name: anlagen-bauen
description: "Wenn es um Fahrgastrechte — Anlagen bauen in Fahrgastrechte geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# حقوق مسافرتی - ساخت اینترنتی

## ورودی‌ها

```yaml
schriftsatz: <pfad zum Schriftsatz, z.B. widerspruch-2026-05-15.md>
rohbelege_verzeichnis: <fall>/belege/
ausgabeverzeichnis: <fall>/anlagen/
bundle: true                       # erzeugt zusätzlich Schriftsatz_mit_Anlagen.pdf
schriftgrad_stempel: 12
schrift_stempel: Arial-Bold        # Arial 12 FETT oben rechts
bezeichnung: "Anlage K"
```

## روند کار

### ۱. پارس کردن اسناد

گزارش را بخوانید و همه این تجهیزات را با استفاده از نام شناسایی کنید `Anlage K 1`, `Anlage K 2`یا `Anlage K1`, `Anlage K2`. لیست را در ترتیب ذکر شده در متن تهیه کنید.

### ۲. به اسناد خام اختصاص دادن

فهرست `belege/` برای بررسی و تعیین یک فایل به هر ثبت C، اسناد معمول در زمینه حقوق مسافر:

| دستگاه معمولی | الگوهای فایل | توضیحات |
|---|---|---|
| K1 | `buchung-*.pdf` | تایید حسابداری DB / EVU |
| K2 | `e-ticket-*.pdf` یا `fahrkarten-*.pdf` | بلیط های الکترونیکی / بلیط تمام مسافران |
| K3 | `verspaetung-*.png` یا `db-navigator-*.png` | پیام تاخیر DB (آپ / SMS / ایمیل) |
| K4 | `anzeigetafel-*.jpg` | صفحه نمایش عکس ایستگاه مقصد با زمان |
| K5 | `belege-auslagen/*.pdf` | گواهی حمل و نقل جایگزین / غذا خوردن / هتل |
| K6 | `erstantrag-*.pdf` | خود را از مرکز خدمات DB |
| K7 | `ablehnung-*.pdf` | نامه های انکار DB |
| K8 | `widerspruch-*.pdf` | اعتراض خود (در مورد شکایت) |
| K9 | `schlichtungsspruch-*.pdf` | درخواست شفاعت از طرف اداره ی میانجی سفر و حمل |
| K10 ff. | `vollmacht-*.pdf` | اختیارات مسافر |

اگر یک دستگاه ذکر شده را نمی توان به عنوان نامگذاری کرد: ** پرچم بازرسی** با لیست نام های غیر مرتبط.

### ۳. تبدیل و سیتم کردن مدارک

هر کالا را به PDF تبدیل کنید (HEIC / JPG / PNG / DOCX / XLSX → pdf). در بالای راست هر فایل پی دی اف، نامگذاری کننده ای را با **Arial 12 FETT** (Helvetica-Bold 12pt) پرتاب نمایید:

```
                                                                    Anlage K 1
[Inhalt]
```

نام فایل: بدون پوشه و علامت خالی `Anlage_K_1.pdf`, `Anlage_K_2.pdf`... طبق کنوانسیون beA

### چهارمین جمع آوری PDF اختیاری

اگر `bundle: true`: جمع آوری PDF `Schriftsatz_mit_Anlagen.pdf` تولید - نوشته های پیش روی، دستگاه ها به ترتیب شماره گذاری شده با علامت خواندن هر سیستم. برای ثبت پرونده و پشتیبان گیری دیدگاه مفید است

### شماره پنجم

در `ausgabeverzeichnis/`:

- `Anlage_K_1.pdf`, `Anlage_K_2.pdf`، ... (پی دی اف های جداگانه برای اپلود beA)
- `Schriftsatz_mit_Anlagen.pdf` (در صورت جمع آوری PDF، اگر بسته: true)
- `anlagen-uebersicht.md` (جدول ضمیمه K → فایل → توضیحات؛ اطلاعات نادرست)

## کنوانسیون beA

- این برنامه ها به صورت PDF های جداگانه در beA ارسال می شوند.
- هر کدام با یک تمبر در سمت راست بالا، به نام "آریال 12 FETT"
- **نام ثبت نام** بدون چاپ، بدون علامت خالی: `Anlage_K_1.pdf`.
- **در ترتیب** باید به ذکر در اسناد مربوط باشد.
- جمع آوری PDF برای نسخه های پرونده خود (نه برای اپلود beA).

## شواهد تصویری در مورد تاخیر DB - اطلاعات ویژه

- **مطابق نمایش عکس:** زمان باید قابل تشخیص باشد. در چند صفحه فقط مهم (ستانسیون مقصد) است. تاریخ یک روز مقایسه ggf. از طریق اطلاعات EXIF تکمیل شود.
- **DB Navigator Screenshot:** تا جایی که ممکن است با صفحه جزئیات اتصال، زمان برنامه ریزی شده و واقعی ورود را نشان می دهد.
- ** نامه های انکار:** همه صفحات در یک PDF (به عنوان مثال، پشت صفحه / ورق نوشته)
- ** کامل:** اسکن های اصلی با کیفیت بالا.

## منابع خطا

- نوشته شده است `Anlage K5`در فهرست اسناد فایل مربوط به آن وجود ندارد → اسکریپت شکسته می شود؛ پرچم بازرسان.
- دوگانه ضمیمه K شماره گذاری در فایل → گزارش خطا؛ دستکاریff.
- فایل های HEIC iOS → تبدیل خودکار؛ در صورت نیاز OCR اشاره کنید.
- چند صفحه ای در چندین فایل (z.B. نامه های انکار S. 1 جدا) → پیش از ادغام به یک فایل قبل از تمپ کردن.

## نمونه ی انتشار

```
anlagen-uebersicht.md
============================
Fall: FGR-2026-0042
Schriftsatz: widerspruch-2026-05-15.md
Erzeugte Anlagen:

| Anlage   | Datei                       | Beschreibung                          | Status |
|----------|-----------------------------|----------------------------------------|--------|
| Anlage K 1 | Anlage_K_1.pdf             | Buchungsbestätigung PNR ABC123          | ok      |
| Anlage K 2 | Anlage_K_2.pdf             | E-Tickets Mueller (3 Personen)          | ok      |
| Anlage K 3 | Anlage_K_3.pdf             | DB-Navigator Verspätungsmitteilung       | ok      |
| Anlage K 4 | Anlage_K_4.pdf             | Foto Anzeigetafel Muenchen Hbf 15:05   | ok      |
| Anlage K 5 | Anlage_K_5.pdf             | Kassenbon Bahnhofs-Imbiss 12,50 EUR    | ok      |
| Anlage K 6 | Anlage_K_6.pdf             | Erstantrag an DB Servicecenter           | ok      |
| Anlage K 7 | Anlage_K_7.pdf             | Ablehnungsschreiben DB vom 12.05.2026    | ok      |

Sammel-PDF: Schriftsatz_mit_Anlagen.pdf erzeugt (28 Seiten, 4.2 MB).
```

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **الزامِ تمام‌نویسی و استانداردِ قالب.** محصولِ نهایی در **جمله‌های کامل و تمام‌نوشته** تحویل می‌شود — نه اسکلتِ کلیدواژه، نه تنهٔ خالیِ شرط، نه صرفِ فهرست. شرط‌ها به‌صورتِ جمله‌های تمام‌نوشتهٔ بیان‌گرِ اثرِ حقوقی می‌آیند؛ جای‌گیرها مانند `[Name der Mandantin]` روشن علامت می‌خورند و متنِ پیرامون کامل می‌ماند.
>
> **شکلِ نوشتار:** هرگاه لایحه، قرارداد، یادداشت، تصمیم، ومرک یا هر سندِ نهاییِ دیگر به‌صورتِ DOCX، PDF یا متنِ قالب‌بندی‌شده بیرون داده شود، باید **Times New Roman ۱۱ pt** به‌عنوانِ قلمِ پایه به‌کار رود. عنوان‌ها در همان قلم می‌مانند و تنها می‌توانند سیاه (بولد) یا پلکانی باشند. در خروجیِ صرفاً Markdown یا چت، این خواستهٔ قالب به‌عنوانِ یادداشتِ برون‌سپاری درج می‌شود.
>
> **شماره‌گذاری:** ساختاربندی منحصراً اعشاری (`1`، `1.1`، `1.1.1` و به همین ترتیب). بدون اعداد رومی، بدون ساختاربندی حرفی یا آمیخته.
<!-- END ausformulierungspflicht (autogen) -->

## قوانین و رویهٔ قضایی

### کتابخانهٔ گزیدهٔ قوانین

- Art. 13 DSGVO
- § 71 GVG
- § 32 VSBG
- § 23 VSBG

### آرای راهنما

- BVerfGE جلد 6 Rn 32 (تثبیت، اثر ثالث حقوق اساسی)
- BVerwG 6 C 12.21 (مستقیم تصمیمات مدیریتی)
- BGH GSZ 1/14 (تدریس و آموزش حقوقی)
