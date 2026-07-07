# شروع سریع (Schnellstart)

> **یادداشت ترجمه:** این سند ترجمهٔ فارسی «QUICKSTART.md» است و صرفاً جنبهٔ راهنمایی دارد. **نسخهٔ آلمانی معتبر و ملاک است.** اصطلاحات حقوقی آلمانی در پرانتز حفظ شده‌اند. تمام محتوای این مجموعه اطلاعات عمومی و ابزار کار است، نه مشاورهٔ حقوقی (keine Rechtsberatung) — برای پروندهٔ مشخص خود همیشه به وکیل دادگستری (Rechtsanwalt) مراجعه کنید.

این راهنما در ۵ دقیقه شما را به نخستین استفادهٔ عملی از افزونه‌ها در Claude Code یا Claude Desktop می‌رساند.

## ۱. پیش‌نیازها

- Claude Code نسخهٔ ‎≥ 1.0 یا Claude Desktop نسخهٔ ‎≥ 0.7.
- اختیاری: یک پوشهٔ محلی برای پرونده‌ها و موکل‌ها (Mandats-/Aktenordner).
- اختیاری: دسترسی به منابع رسمی یا آزاد؛ پایگاه‌های دادهٔ دارای مجوز فقط در صورت داشتن اشتراک، برای یافتن مآخذ به‌روز.

## ۲. نصب

### گزینهٔ الف — مارکت‌پلیس مستقیم از GitHub

```text
/plugin marketplace add Klotzkette/claude-fuer-deutsches-recht
/plugin install arbeitsrecht@klotzkette-german-legal-skills
/plugin install vertragsrecht@klotzkette-german-legal-skills
/plugin install datenschutzrecht@klotzkette-german-legal-skills
```

### گزینهٔ ب — نصب محلی از کلون

```bash
git clone https://github.com/Klotzkette/claude-fuer-deutsches-recht.git
cd claude-fuer-deutsches-recht
claude
```

سپس در خط فرمان Claude Code:

```text
/plugin marketplace add .
/plugin install arbeitsrecht@klotzkette-german-legal-skills
```

### گزینهٔ پ — نصب مستقیم یک افزونهٔ منفرد

```text
/plugin install ./prozessrecht
```

## ۳. ساخت پوشهٔ پرونده (Mandatsordner)

ساختار پیشنهادی (نگاه کنید به اسکیل `mandats-arbeitsbereich` در هر افزونه):

```
~/Mandate/
└── 2026-0142_Mueller_Kuendigung/
    ├── 01_korrespondenz/      ← مکاتبات
    ├── 02_schriftsaetze/      ← لوایح
    ├── 03_urkunden/           ← اسناد
    ├── 04_recherche/          ← تحقیق و پژوهش
    ├── 05_fristen/            ← مهلت‌ها
    └── mandat.yaml
```

## ۴. نخستین آزمایش‌ها

### حقوق کار (Arbeitsrecht) — دعوای حمایت در برابر اخراج (Kündigungsschutzklage)

```
Lade Skill kuendigungsschutzklage. Mandant: Müller, Arbeitnehmer seit 2018,
ordentliche Kündigung erhalten am 10.05.2026, Zugang 12.05.2026,
Begründung "betriebsbedingt". Entwirf Klageschrift und prüfe 3-Wochen-Frist.
```

*(ترجمهٔ فرمان: اسکیل «دعوای حمایت از اخراج» را بارگذاری کن. موکل: مولر، کارمند از ۲۰۱۸، اخراج عادی دریافت‌شده در ۱۰.۰۵.۲۰۲۶، ابلاغ در ۱۲.۰۵.۲۰۲۶، با توجیه «دلایل ساختاری بنگاه». پیش‌نویس دادخواست را تهیه و مهلت سه‌هفته‌ای را بررسی کن.)*

### حقوق آیین دادرسی (Prozessrecht) — فرایند اخطار پرداخت (Mahnverfahren)

```
Lade Skill mahnbescheid. Gläubiger: GmbH X, Schuldner: Y, Forderung 12.430,50 €
aus Rechnung 2026-0017, fällig 14.04.2026. Erstelle Antrag.
```

### حفاظت از داده‌ها (Datenschutz) — درخواست دسترسی بر پایهٔ DSGVO

```
Lade Skill dsgvo-auskunft. Mandant hat Auskunftsersuchen erhalten,
Verantwortlicher ist Plattformbetreiber, Frist Art. 12 III DSGVO. Erstelle Antwortentwurf
mit Hinweis auf §§ 29 BDSG, 5 GeschGehG.
```

## ۵. قواعد الزام‌آور در هر اسکیل

- هر گزارهٔ حقوقی باید مستند شود — طبق [`references/zitierweise.md`](./references/zitierweise.md) (شیوه‌نامهٔ استناد).
- در مسائل اختلافی، نظر غالب (h. M.) و نظر مخالف جداگانه استناد می‌شوند.
- در نبود رویهٔ قضایی، این نکته صریحاً ذکر می‌شود («تا جایی که پیداست هنوز رأیی صادر نشده است»).
- **رازداری وکالت (Mandantengeheimnis):** هیچ دادهٔ مرتبط با پرونده بدون قرارداد پردازش داده (AVV) به ابزارها منتقل نمی‌شود.

## ۶. نکته‌ها

- **اول مهلت را بررسی کن (Frist zuerst prüfen).** هر اسکیلی که به دعوا/ابطال/تجدیدنظر مربوط است، با بررسی مهلت آغاز می‌شود.
- **محاسبهٔ ارزش موضوع دعوا (Streitwert).** اسکیل `streitwert` (در `prozessrecht`) جدول‌های RVG/GKG را ارائه می‌دهد.
- **قالب‌ها را شخصی‌سازی کنید.** فایل‌های SKILL.md مارک‌داون هستند و آزادانه قابل ویرایش‌اند. منطق دفتر خودتان را می‌توانید در `kanzlei-builder-hub` اضافه کنید.
- **منابع را راستی‌آزمایی کنید.** حتی بهترین اسکیل ممکن است شمارهٔ پرونده را «توهم» کند — همیشه با منابع رسمی یا آزاد کنترل کنید؛ پایگاه‌های دارای مجوز فقط در صورت داشتن دسترسی.

## ۷. رفع اشکال

| مشکل | راه‌حل |
| --- | --- |
| اسکیل پیدا نمی‌شود | آیا `plugin.json` مسیر را دارد؟ `‎/plugin reload` را اجرا کنید. |
| ابزار MCP پاسخ نمی‌دهد | `‎.mcp.json` را بررسی و سرور را دوباره راه‌اندازی کنید. |
| مأخذ نادرست | به‌صورت دستی در Beck-Online بررسی و اسکیل را اصلاح کنید — PR خوش‌آمد است. |
| پرسش حفاظت از داده‌ها | اسکیل `datenschutzrecht/mandantendaten-ki` را فراخوانی کنید. |
