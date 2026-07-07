---
name: legw-bmwe-aussenwirtschaft-und-investitionspruefung
description: "Wenn es um Aussenwirtschaft und Investitionspruefung (BMWE) in Legistik-Werkstatt geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Berechnungstabelle mit Schwellen, Annahmen und Kontrollfragen."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# بررسی امور خارجه و سرمایه گذاری (BMWE)

> چهارم و عمیق ترین مهارت در زنجیره ریسورت: کامپاس حوزه های تخصصی برای بررسی امور خارجه و سرمایه گذاری بخش BMWE. به معیارهای استاندارد، بازیگران، ارتباط اتحادیه اروپا و نقاط آزمون مربوط به این زمینه را می دهد.

## ورودی‌ها

- ورق سفارش `legistik-auftragsaufnahme`
- کامپوس ريسورت `legw-ressort-bmwe`
- ماتریس کار از `legw-ressortaufgaben-bmwe`
- یک سوال یا پروژه استاندارد خاص در این زمینه

## سوابق استاندارد

این بخش اصلی: AWG؛ AWV (قسم 5) ؛ FDI-Screening-VO (EU); KrWaffKG.

در نظر گرفتن قانون اساسی قبل از قوانین فدرال، مقررات قانونی پیش از نظم و ضبط. برای اتحادیه اروپا اول به حقوق (پیش فرض و دستور استفاده) ، سپس استاندارد های ملی اجرا و همراهی می شود.

## بازیگران و نظارت

BMWE؛ BMI; AA ؛ BMF: دفتر بنظامی فدرال

نقشه بازیگران: واحد رهبری در مجلس؛ دفتر های امضا کننده، مقامات فرعی که به اجرا می رسند؛ سازمانهای کشور مورد توجه؛ شرکت کنندگان و مشاوران علمی؛ قضایی اختصاصی.

## ارتباط اتحادیه اروپا و قانون بین المللی

غربالگری از FDI؛ محدوده های قطعی اتحادیه اروپا، گزارشات بررسی به اتحادیه اروپا.

آیا این امر می تواند به دلیل اینکه در مورد یک قانون یا دستورالعمل مربوطه، زمان اجرا آن، لزوم اطلاع رسانی، پیشگیری از قوانین کمک های مالی و امکان تصمیم گیری مقدماتی باشد انجام شود؟

## وظایف عادی لجستیک

تعیین بخش ها؛ روش های آزمایشی، تخفیف یا محدودیتها؛ مشاوره در شورای امنیت فدرال.

برای معیارهای ارائه دهنده:

1. بررسی شرایط و اهداف قانونی در این زمینه
2. نقشه برداری از استانداردهای موجود؛ تحلیل جای
3. شدت مداخله و دایره مخاطب را تعیین کنید
4. بررسی مطابق بودن قانون اساسی و قوانین اروپا
5. بررسی دقیق و شفاف بودن پرونده ها و قانونی؛
6. کنترل ساختار اجرای و نظارت
7. برنامه ریزی کردن قوانین همراه و دنباله دار (نظم، مقررات اداری)

## سنگ های تصادفی و نقاط آزمایش

زمان کمی؛ محرمانه بودن، ارتباط متقابل با کنترل صادرات BVerwG.

نکات آزمایشی گسترده: تعیین کننده بودن؛ متناسب شدن، ممنوعیت بازخورد; قانون مساومیت؛ مقررات اساسی در زمینه حفاظت از داده ها؛ تعامل با سایر منابع؛ زمان بندی و ارزیابی.

## خروجی

کامپاس ساکفیلد:

```
Sachfeld:           Aussenwirtschaft und Investitionspruefung
Ressort:            BMWE
Kernnormen:         AWG; AWV (Abschnitt 5); FDI-Screening-VO (EU); KrWaffKG.
Akteure/Aufsicht:   BMWE; BMI; AA; BMF; Bundeskanzleramt.
EU/Voelkerrecht:    FDI-Screening-VO; sektorale EU-Schwellen; Pruefberichte an EU.
Pruefpunkte:        <verfassungs-/europarechtlich; bestimmt; verhaeltnismaessig>
Stolpersteine:      <Sachfeld-spezifisch>
Naechste Skills:    legw-ressortaufgaben-bmwe; normhierarchie-routing;
                    normenkartierung; verfassungsmaessigkeit-quercheck;
                    europarechtskonformitaet; rechtsfolgenabschaetzung
```

## اتصال به زنجیره لوازم

- `legistik-auftragsaufnahme` -> `legw-ressort-router` -> `legw-ressort-bmwe` -> `legw-ressortaufgaben-bmwe` -> `legw-bmwe-aussenwirtschaft-und-investitionspruefung` (در اینجا) -> `normhierarchie-routing` و بازجویی.

## جداسازی

این مهارت به عنوان یک کامپاس ساحه ای عمل می کند و از بررسی استاندارد استفاده نمی شود بلکه دانش را برای معیارهای ارائه دهنده فراهم می سازد.

## قاعدهٔ منابع

تمام منابع موجود: gesetze-im-internet.de; bundestag.de; bundesrat.de; bundesregierung.de; bmj.de; bundesverfassungsgericht.de; bundesgerichtshof.de; bverwg.de; eur-lex.europa.eu; dejure.org; openjur.de; normenkontrollrat.bund.de.نه وبلاگ های ثانویه و نه پورتالهای وب. هر استاندارد با نقطه ی پیدا کردن کامل و تاریخ
