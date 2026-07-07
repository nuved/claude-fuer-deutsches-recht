---
name: output-pruefdokument-ki-vo-mit-warnhinweisen
description: "Wenn es um Output: Prüfdokument europäischer Technikregulierungsrahmen mit Warnhinweisen in diesem Spezialbereich geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# محصول: سند آزمایشی AI-VO با اطلاعات هشدار دهنده

## سرنخ های واجب

```text
MECHANISCHES PRÜFDOKUMENT — KI-VO
Verordnung (EU) 2024/1689

Keine Rechtsberatung. Dieses Dokument beruht auf den angegebenen Tatsachen und ersetzt keine anwaltliche Prüfung. Tatsachen, Zweckbestimmung, technische Eigenschaften und tatsächliche Nutzung können die Einordnung ändern.
```

## ساختار حداقل

### ۱. ماموریت و منابع

- مشتری / سازمان
- نام سیستم و نسخه
- بخش کاری که مورد بررسی قرار گرفته است: مدل، API، چتbot، ورک فلو تخصصی، کل محصول
- اسناد: مستندات فنی، دستورالعمل استفاده، دستور کار، دفترچه ی ثبت نام ها، قراردادها، اسکرین شاټها، سیاست های
- وضعیت بررسی و حقایق آشکار

### 2- تنظیم سیستم های هوش مصنوعی

از `liegt-ki-system-vor-art-3-nr-1` در این زمینه:

| عنصر | نتیجه | دلیل |
|---|---|---|
| سیستم مبتنی بر ماشین | بله/نه / غیر واضح | |
| سطح استقلال | بله/نه / غیر واضح | |
| سازگاری | بله/نه/غیر مشخص/ضروری نیست | |
| اهداف صریح/عاطفه | بله/نه / غیر واضح | |
| نتیجه گیری از ورودی | بله/نه / غیر واضح | |
| نوع تولید | پیش بینی/محتویات / توصیه و تصمیم گیری | |
| تاثیرات بر محیط زیست | بله/نه / غیر واضح | |

متن اجباری:
```text
Auf Grundlage der vorliegenden Angaben ist das System [wahrscheinlich / wahrscheinlich nicht / offen] als KI-System im Sinne von Art. 3 Nr. 1 KI-VO einzuordnen. Entscheidend ist insbesondere [Inferenz/Automation/Output/Zweck]. Die bloße Automation wurde [nicht allein / zusammen mit Inferenz] bewertet; Autonomie wurde nicht als Vollautonomie verstanden.
```

### ۳. هدف و استفاده واقعی

اسناد:
- هدف ارائه دهنده
- هدف کاربری
- استفاده واقعی در سازمان
- استفاده های ممنوع یا غیرقابل اجرا
- سوءاستفاده قابل پیش بینی
- انحرافات شناخته شده توسط کارکنان
- محرک های ارزیابی مجدد

### 4- جدایی GPAI/Chatbot

متن لازم در چت های عمومی یا GPAI:
```text
Die allgemeine technische Nutzbarkeit eines GPAI-Systems oder Chatbots in Hochrisiko-Bereichen begründet für sich genommen noch keine Hochrisiko-Einstufung. Maßgeblich ist die konkrete Zweckbestimmung und der verantwortete Einsatz. Eine Hochrisiko-Prüfung nach Art. 6 Abs. 2 i.V.m. Anhang III ist erforderlich, wenn das System in einen entsprechenden Fachprozess integriert oder hierfür tatsächlich verwendet wird.
```

### 5ـ نتیجه کلاس های خطر

| نقطه آزمایش | نتیجه | محل یافت | ادامه |
|---|---|---|---|
| فعالیت های ممنوع | بله/نه / غیر واضح | Art. 5 | |
| قطعه ایمنی با ریسک بالا | بله/نه / غیر واضح | Art. 6 Abs. 1در ضمیمه ی 1 | |
| خطر بالا در آگهی III | بله/نه / غیر واضح | Art. 6 Abs. 2در ضمیمه ی III | |
| حذف بازپسین | دستگیر / نه گرفتگی / غیر واضح | Art. 6 Abs. 3/4 | |
| خطر محدود | بله/نه / غیر واضح | Art. 50 | |
| مدل/سیستم GPAI | بله/نه / غیر واضح | Art. 3 Nr. 63/66, Art. 51 ff. | |

### 6- ماتریس III-پذیری

حتی اگر نتیجه منفی باشد، به طور خلاصه:

| Nr. | منطقه | نتیجه | توضیحات کوتاه |
|---|---|---|---|
| 1 | بیومتری | بله/نه / غیر واضح | |
| 2 | زیرساخت های حیاتی | بله/نه / غیر واضح | |
| 3 | آموزش و پرورش | بله/نه / غیر واضح | |
| 4 | اشتغال/کار | بله/نه / غیر واضح | |
| 5 | خدمات خصوصی/عام ضروری | بله/نه / غیر واضح | |
| 6 | تعقیب | بله/نه / غیر واضح | |
| 7 | مهاجرت/ پناهندگی/ مرز | بله/نه / غیر واضح | |
| 8 | مراقبت های حقوقی/دستورهای دموکراتیک | بله/نه / غیر واضح | |

### 7- اشاره به کاربری و حاکمیت

در مورد Chatbot/GPAI عمومی یا استفاده از هدف باز:
- آیا دستورالعمل های هوش مصنوعی وجود دارد؟
- آموزش پس از Art. 4?
- حقوق نقش و محدودیت های فنی؟
- ثبت و حسابرسی؟
- پروسه تخفیف برای موارد حساس استفاده؟
- با سوءاستفاده های جداگانه؟
- ارائه دهنده Art. 25 از این رو؟

### 8 برنامه ی واجبات

با توجه به نتیجه، تفاوت:

**پرویداران با ریسک بالا:** Art. 9 تا 15 Art. 17, Art. 43 49، پایگاه داده اتحادیه اروپا ، نظارت بازار پست

**پردازنده های خطر بالا:** Art. 26, ggf. Art. 27، نظارت انسانی، دفترچه ها، اطلاعات ورودی، وظایف اطلاعاتی، فرآیند حادثه

**غیر خطر بالا:** Art. 50، GPAI Art. 4 مهارت های هوش مصنوعی، مدیریت داخلی، حفاظت از داده ها، حقوق حرفه ای، ارزیابی مجدد.

**GPAI:** Art. 51 55، قانون عمل، خطر سیستماتیک، اسناد فنی، سیاست حقوق چاپی، خلاصه اطلاعات آموزشی.

### ۹. استانداردها

به طور خلاصه:
- آیا معیارهای هماهنگ با دفتر رسالت وجود دارد؟
- آیا از استاندارد های ISO/IEC 42001, 23894, 22989, 23053 یا امنیت برای هدایت استفاده می شود؟
- چه معیارهای دیگری که تاثیر گمان را برطرف نمی کند؟

### 10 - فرمول نتیجه

```text
Ergebnis:
Nach den vorliegenden Angaben handelt es sich bei [System] [wahrscheinlich / wahrscheinlich nicht / offen] um ein KI-System nach Art. 3 Nr. 1 KI-VO. [Begründung in 3-5 Sätzen.]

Die Hochrisiko-Einstufung nach Art. 6 Abs. 2 i.V.m. Anhang III ist [wahrscheinlich / nicht ersichtlich / offen], weil [konkreter Zweck und Bereich]. Ein allgemeiner Chatbot/GPAI-Einsatz allein genügt hierfür nicht; entscheidend ist [konkrete Zweckbestimmung/tatsächliche Nutzung].

Die Rückausnahme nach Art. 6 Abs. 3 ist [zu prüfen / greift wahrscheinlich / greift nicht], weil [Profiling/Risiko/Fallgruppe].

Empfohlene nächste Schritte:
1. [Maßnahme]
2. [Maßnahme]
3. [Maßnahme]
```

## منبع و اطلاعیه ی به روز

حالت: 05/2026. وضعیت منبع و شرایط دستورالعمل قبل از استفاده خارجی باید به روز شود.
