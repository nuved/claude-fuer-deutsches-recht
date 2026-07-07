---
name: legw-bmi-auslaender-und-staatsangehoerigkeitsrecht
description: "Wenn es um Auslaender- und Staatsangehoerigkeitsrecht (BMI) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# حقوق خارجی و شهروندی (BMI)

> چهارم و عمیق ترین مهارت در زنجیره ریسورت: کامپاس موضوعی برای قانون خارجی و تابعیت در بخش کسب وکار BMI. به معیارهای استاندارد، بازیگران، ارتباط اتحادیه اروپا و نقاط امتحان را برای این یک رشته می دهد.

## ورودی‌ها

- ورق سفارش `legistik-auftragsaufnahme`
- کامپوس ريسورت `legw-ressort-bmi`
- ماتریس کار از `legw-ressortaufgaben-bmi`
- یک سوال یا پروژه استاندارد خاص در این زمینه

## سوابق استاندارد

در این زمینه، موجودیت اصلی: AufenthG؛ AsylG؛ StAG؛ FreizuegG/EU؛ AZRG؛ AzilbLG (با BMAS).

در نظر گرفتن قانون اساسی قبل از قوانین فدرال، مقررات قانونی پیش از نظم و ضبط. برای اتحادیه اروپا اول به حقوق (پیش فرض و دستور استفاده) ، سپس استاندارد های ملی اجرا و همراهی می شود.

## بازیگران و نظارت

BAMF؛ مقامات خارجی، پلیس فدرال

نقشه بازیگران: واحد رهبری در مجلس؛ دفتر های امضا کننده، مقامات فرعی که به اجرا می رسند؛ سازمانهای کشور مورد توجه؛ شرکت کنندگان و مشاوران علمی؛ قضایی اختصاصی.

## ارتباط اتحادیه اروپا و قانون بین المللی

این کشور در حال حاضر با یک قانون اساسی است.

آیا این امر می تواند به دلیل اینکه در مورد یک قانون یا دستورالعمل مربوطه، زمان اجرا آن، لزوم اطلاع رسانی، پیشگیری از قوانین کمک های مالی و امکان تصمیم گیری مقدماتی باشد انجام شود؟

## وظایف عادی لجستیک

سازماندهی اهداف اقامت؛ وضعیت محافظت، ورود خانواده؛ شهروندی؛ اخراج؛ انتقال اطلاعات بین مقامات.

برای معیارهای ارائه دهنده:

1. بررسی شرایط و اهداف قانونی در این زمینه
2. نقشه برداری از استانداردهای موجود؛ تحلیل جای
3. شدت مداخله و دایره مخاطب را تعیین کنید
4. بررسی مطابق بودن قانون اساسی و قوانین اروپا
5. بررسی دقیق و شفاف بودن پرونده ها و قانونی؛
6. کنترل ساختار اجرای و نظارت
7. برنامه ریزی کردن قوانین همراه و دنباله دار (نظم، مقررات اداری)

## سنگ های تصادفی و نقاط آزمایش

حداقل استانداردهای قانونی اتحادیه اروپا؛ قرضه های زنجیره ای Art. 6 GG; حقوق پرندگان; کشورهای امن

نکات آزمایشی گسترده: تعیین کننده بودن؛ متناسب شدن، ممنوعیت بازخورد; قانون مساومیت؛ مقررات اساسی در زمینه حفاظت از داده ها؛ تعامل با سایر منابع؛ زمان بندی و ارزیابی.

## خروجی

کامپاس ساکفیلد:

```
Sachfeld:           Auslaender- und Staatsangehoerigkeitsrecht
Ressort:            BMI
Kernnormen:         AufenthG; AsylG; StAG; FreizuegG/EU; AZRG; AsylbLG (mit BMAS).
Akteure/Aufsicht:   BAMF; Auslaenderbehoerden; Bundespolizei.
EU/Voelkerrecht:    GEAS; Dublin-VO; Rueckfuehrungs-RL; Visa-Kodex; Schengen.
Pruefpunkte:        <verfassungs-/europarechtlich; bestimmt; verhaeltnismaessig>
Stolpersteine:      <Sachfeld-spezifisch>
Naechste Skills:    legw-ressortaufgaben-bmi; normhierarchie-routing;
                    normenkartierung; verfassungsmaessigkeit-quercheck;
                    europarechtskonformitaet; rechtsfolgenabschaetzung
```

## اتصال به زنجیره لوازم

- `legistik-auftragsaufnahme` -> `legw-ressort-router` -> `legw-ressort-bmi` -> `legw-ressortaufgaben-bmi` -> `legw-bmi-auslaender-und-staatsangehoerigkeitsrecht` (در اینجا) -> `normhierarchie-routing` و بازجویی.

## جداسازی

این مهارت به عنوان یک کامپاس ساحه ای عمل می کند و از بررسی استاندارد استفاده نمی شود بلکه دانش را برای معیارهای ارائه دهنده فراهم می سازد.

## قاعدهٔ منابع

تمام منابع موجود: gesetze-im-internet.de; bundestag.de; bundesrat.de; bundesregierung.de; bmj.de; bundesverfassungsgericht.de; bundesgerichtshof.de; bverwg.de; eur-lex.europa.eu; dejure.org; openjur.de; normenkontrollrat.bund.de.نه وبلاگ های ثانویه و نه پورتالهای وب. هر استاندارد با نقطه ی پیدا کردن کامل و تاریخ
