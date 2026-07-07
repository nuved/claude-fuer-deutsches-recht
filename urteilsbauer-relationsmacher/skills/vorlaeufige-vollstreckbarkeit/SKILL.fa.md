---
name: vorlaeufige-vollstreckbarkeit
description: "Wenn es um Vorläufige Vollstreckbarkeit in Urteilsbauer und Relationsmacher geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# امکان اجراء موقت

## سه بعدی در آغاز

1. چه نوع تصمیم گیری وجود دارد؟ حکم بازپسین، قضاوت از دست دادن، تشخیص و تصمیمه.
2. چقدر باید مجازات شود؟§ 708 Nr. 11 ZPO) یا بیشتر از آن (§ 709 ZPO)?
3. آیا این درخواست قابل تجدید است (مبلغ شکایت > 600 یورو) - در غیر این صورت: § 713 ZPO (بدون امنیت) ؟
4. آیا طرف زیرمایه درخواست حمایت را دنبال می کند؟ § 711 ZPO قرار داده شده؟

## رویهٔ قضایی روز

- قضیه: هیچ تصمیمی را از دانش نمونه ای نقل نکنید؛ قبل از انتشار با دادگاه، شکل تصمیم گیری و تاریخ آن ها، نشانه های پرونده یا اظهارات قابل اثبات را توسط منبع رسمی یا آزاد تأیید کنید.

## قوانین محوری

- § 708 ZPO - قابل اجرا بدون تضمین (Nr. 1-11 تعداد)
 - Nr. دوم: حکم عدم اجرا
 - Nr. ۴: حکم شناخت
 - Nr. 11: حكمات نهایی تا 1500 یورو
- § 709 ZPO - قابل اجرا در برابر 110 درصد تضمین (قاعده)
- § 711 ZPO - درخواست حمایت از طرف زیر
- § 713 ZPO - عدم تضمین در صورت نبود وکالت (مبلغ شکایت ≤ 600 یورو)
- § 719 ZPO - توقف اجرای درخواست

## درخت تصمیم گیری قدم به گام

```
Entscheidungstyp?
├── Versäumnisurteil → § 708 Nr. 2 ZPO (ohne Sicherheit)
├── Anerkenntnisurteil → § 708 Nr. 4 ZPO (ohne Sicherheit)
├── Endurteil bis 1.500 EUR → § 708 Nr. 11 ZPO (ohne Sicherheit)
└── Endurteil über 1.500 EUR:
 ├── Berufung statthaft (Beschwer > 600 EUR)? → § 709 ZPO (110 Prozent Sicherheit)
 │ └── Schutzantrag § 711 ZPO gestellt? → § 711 ZPO Formulierung ergänzen
 └── Berufung nicht statthaft (Beschwer ≤ 600 EUR, keine Zulassung)? → § 713 ZPO (ohne Sicherheit)
```

## قالب محصول

** آدرس:** حکمff. 3) - صورت: رسمی

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **الزامِ تمام‌نویسی و استانداردِ قالب.** محصولِ نهایی در **جمله‌های کامل و تمام‌نوشته** تحویل می‌شود — نه اسکلتِ کلیدواژه، نه تنهٔ خالیِ شرط، نه صرفِ فهرست. شرط‌ها به‌صورتِ جمله‌های تمام‌نوشتهٔ بیان‌گرِ اثرِ حقوقی می‌آیند؛ جای‌گیرها مانند `[Name der Mandantin]` روشن علامت می‌خورند و متنِ پیرامون کامل می‌ماند.
>
> **شکلِ نوشتار:** هرگاه لایحه، قرارداد، یادداشت، تصمیم، ومرک یا هر سندِ نهاییِ دیگر به‌صورتِ DOCX، PDF یا متنِ قالب‌بندی‌شده بیرون داده شود، باید **Times New Roman ۱۱ pt** به‌عنوانِ قلمِ پایه به‌کار رود. عنوان‌ها در همان قلم می‌مانند و تنها می‌توانند سیاه (بولد) یا پلکانی باشند. در خروجیِ صرفاً Markdown یا چت، این خواستهٔ قالب به‌عنوانِ یادداشتِ برون‌سپاری درج می‌شود.
>
> **شماره‌گذاری:** ساختاربندی منحصراً اعشاری (`1`، `1.1`، `1.1.1` و به همین ترتیب). بدون اعداد رومی، بدون ساختاربندی حرفی یا آمیخته.
<!-- END ausformulierungspflicht (autogen) -->

```
## Vorläufige Vollstreckbarkeit

**Standardfall § 709 ZPO:**
"Das Urteil ist vorläufig vollstreckbar gegen Sicherheitsleistung in Höhe von einhundertzehn
Prozent des jeweils zu vollstreckenden Betrages."

**Bei § 713 ZPO (keine Berufung):**
"Das Urteil ist ohne Sicherheitsleistung vorläufig vollstreckbar."

**Bei Schutzantrag § 711 ZPO:**
"Der Beklagten wird nachgelassen, die Vollstreckung gegen Sicherheitsleistung in Höhe von
einhundertzehn Prozent des jeweils zu vollstreckenden Betrages abzuwenden, wenn nicht die
Klägerin vor der Vollstreckung Sicherheit in gleicher Höhe leistet."
```

## سیستم استاندارد

ماده 709 ZPO - امکان اجراء موقت در مقابل 110 درصد (110%) از مبلغ مورد اجرا.

## وقتی که روش دیگر

- ماده 708 Nr. 1 ZPO - یادآوری های مستند
- ماده 708 Nr. 2 ZPO - قضاوت های غفلت بدون اطمینان
- ماده 708 Nr. 4 ZPO - قضاوت های تایید
- ماده 708 Nr. 11 ZPO - برخی از قضاوت های نهایی تا 1500 یورو (پروژه ریپو)
- ماده 711 ZPO - درخواست حمایت از طرف متعهد (بخش دادن ضمانت به خاطر خسارت نامتناسبی)
- ماده 713 ZPO - شکایت کمتر از 600 یورو و هیچ درخواست ای نیست
- ماده 719 ZPO - از درخواست دادخواست رد

## عبارت

- "این حکم به صورت موقت قابل اجرا است تا از یک مقدار ۱۰۰ درصد ضمانت شده در هر مورد.
- "حکمت مقدماتی قابل اجرا است".
- در مورد درخواست حمایت: "مدافع به دفع ضمانت 110 درصد از مقدار لازم برای اجرای آن، اجازه داده می شود تا شرط آنکه متقاضیان تضمین برابر با میزان لازم را ارائه دهند".

---

آډیت ۲۷05.2026 -->

## ۲۷.05.2026)

این مهارت در Bundle 046 به دلیل شواهد قضایی توهم یافته مورد بررسی و اصلاح قرار گرفت.
