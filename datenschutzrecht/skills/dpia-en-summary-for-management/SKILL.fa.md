---
name: dpia-en-summary-for-management
description: "Wenn es um DPIA Management Summary in English in Datenschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# خلاصه ی مدیریت DPIA در زبان انگلیسی

## هدف

خلاصه مدیریت زبان انگلیسی از یک ارزیابی تاثیر حفاظت داده (DPIA) Art. 35 GDPR. برای اعضای هیئت مدیره، کمیته های اجرایی، افسران ریسک گروهی و سایر ذینفعانی غیر قانونی طراحی شده است که نیاز به یک صفحه دفاعی دارند نه اینکه کامل سند DPIA باشد. خلاصه این مقاله روش شش مرحله ای را دنبال می کند و با توصیه صریح تأیید پایان می یابد.

## When to use

- وقتی یک DPIA در دستور کار هیئت مدیره، کمیته اجرایی یا لیژنۀ هدایت قرار دارد
- برای سرمایه گذار due diligence covering high-risk processing
- برای بررسی داخلی و گزارش دهی ریسک گروهی
- برای تبادل با شرکت های مادر انگلیسی زبان، کنترلرهای مشترک یا پردازنده ها
- برای مشاوره های بین المللی که بعدا به زبان ملی ترجمه می شوند

## چارچوب قانونی

- Art. 35(7) GDPR محتوای اجباری یک DPIA
- Art. 35(2) GDPR مشاوره DPO
- Art. 36 GDPR prior consultation if residual risk remains high (مخاطر باقیمانده همچنان بالا است)
- Art. 5(2) GDPR اصل پاسخگویی
- راهنمای EDPB WP 248 rev.01 on DPIA
- برای پردازش مرتبط با هوش مصنوعی: مقررات (EU) 2024/1689 Art. 26 و Art. 27

## ساختار 6 مرحله ای از خلاصه مدیریت

1. **صفحه پردازش.** یک پاراگراف: هدف، داده ها، موضوعات، تکنولوژی و انتقال.
2. ** نیاز و ارزیابی تناسب.** یک پاراگراف: قانونی، حداقل سازی، جایگزین.
3. ** ریسک به موضوعات داده ها.** جدول کوتاه خطر با سناریوهای برتر.
4. ** اقدامات برای کاهش خطر* * Short list of key measures.
5. ** ریسک باقیمانده* * رتبه بندی خطر قبل و بعد از اقدامات.
6. ** توصیه تایید* * Approve, approve with conditions، prior consultation under Art. 36، نه تایید.

## سانت (مجموعه مدیریت انگلیسی)

```
DPIA MANAGEMENT SUMMARY
Confidential — for internal management use

Reference: [DPIA-YYYY-NN]
Date: [DD-MM-YYYY]
Controller: [Entity, legal representative]
DPO: [Name, contact]

1. PROCESSING IN ONE PARAGRAPH
[What is processed, for what purpose, on which legal basis, for which categories of data subjects, with which key technology, including transfers to third countries.]

2. NECESSITY AND PROPORTIONALITY
- Legal basis: [Art. 6 / Art. 9 GDPR with national law]
- Data minimisation: [Brief assessment]
- Less intrusive alternatives considered: [Yes / No, with note]
- Storage period: [Period, justification]
- Data subject rights: [Implemented mechanisms]

3. TOP RISKS TO DATA SUBJECTS (BEFORE MEASURES)
| Scenario | Likelihood | Severity | Rating |
| Unauthorised access | [h/m/l] | [h/m/l] | [R/O/Y/G] |
| Covert profiling | | | |
| Data leakage / transfer exposure | | | |
| Discrimination of data subjects | | | |
| Identity theft / fraud | | | |

4. KEY MEASURES
- Technical: [encryption, pseudonymisation, access control, logging, key management]
- Organisational: [training, four-eyes principle, authorisation concept, incident response]
- Contractual: [DPA Art. 28, SCC for transfers, TIA]
- AI-specific (if applicable): [human oversight, logging Art. 26(6) AI Act, transparency Art. 50 AI Act]

5. RESIDUAL RISK
| Scenario | Rating after measures |
| Unauthorised access | [R/O/Y/G] |
| Covert profiling | |
| ... | |

Overall residual risk: [HIGH / MEDIUM / LOW]

6. APPROVAL RECOMMENDATION
[ ] Approve — proceed with processing
[ ] Approve with conditions — see action items
[ ] Prior consultation under Art. 36 GDPR required
[ ] Do not approve — redesign processing

Action items
| No | Action | Owner | Deadline |

Next review: [DATE]

Sign-off
Controller representative: ____________________ Date: ____________________
DPO: ____________________ Date: ____________________
```

## اشتباهات معمول

- خلاصه مدیریت از کلمه ی مختلف استفاده می کند - عدم مطابقت ریسک قانونی را ایجاد میکند.
- میز ریسک به یک رتبه بندی بدون سناریو محدود شده است - هیئت مدیره نمی تواند چالش بکند.
- توصیه تایید در روایت پنهان شده است - باید یک انتخاب دوگانه باشد.
- نظر دپوهی مورد توجه نیست - به نظر می رسد یک تصمیم کنترل کننده است.
- مشخصه های عبور مرز یا هوش مصنوعی حتی اگر در خلاصه حذف شده باشند، مهم هستند.
- هیچ چیز عملی با مالک و مهلت - توصیه قابل عمل نیست.
- رازداری طبقه بندی گم - خطر افشای غیرمطلوب.

## مرجع های متقابل

- `datenschutzrecht/skills/dpia-en-template-full-version/SKILL.md` - قالب کامل انگلیسی DPIA
- `datenschutzrecht/skills/dsfa-template-deutsch-vollvorlage/SKILL.md` - توليد کامل زبان آلمانی
- `datenschutzrecht/skills/dsfa-restrisiko-und-art-36-konsultation/SKILL.md` — Art. 36 روش
- `datenschutzrecht/skills/dsfa-für-internationale-datentransfers/SKILL.md` - انتقال
- `datenschutzrecht/skills/dsfa-für-ki-systeme-schnittstelle-art-26-kivo/SKILL.md` - رابط هوش مصنوعی
- `references/zitierweise.md` - قوانین نقل قول

## منابع 06/2026

- Art. 5(2), 35, 36 GDPR
- در این زمینه، باید از نظر ارجاعی و با توجه به شرایط مختلف استفاده شود. Art. 26 و 27
- راهنمای EDPB WP 248 rev.01 on DPIA
- نظر ادبی 28/2024 در مورد مدل های هوش مصنوعی
- قانون قضایی: از دانش مدل استفاده نکنید؛ با منابع رسمی تأیید کنید
- ادبیات: فقط از منبع ارائه شده توسط کاربر یا دسترسی زنده مجوز داده می شود
