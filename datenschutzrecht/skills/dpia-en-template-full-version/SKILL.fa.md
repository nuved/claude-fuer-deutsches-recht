---
name: dpia-en-template-full-version
description: "Wenn es um DPIA Full Template in English in Datenschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# DPIA Full Template در زبان انگلیسی

## هدف

Complete English-language Data Protection Impact Assessment template aligned with Art. 35 GDPR. تمام شش بخش مورد نیاز توسط Art. 35(7) GDPR این قالب از ساختار روش شناسی، ضرورت و تناسب پذیری، ریسک برای افراد داده ها، اقدامات، خطر باقیمانده، تأیید پیروی می کند.

## When to use

- پس از یک ارزیابی مثبت DPIA
- وقتی پردازش شامل انتشارات انگلیسی زبان، کنترل کننده های مشترک در اتحادیه اروپا و خارج از آن است یا الزامات اسناد انگلیسی
- قبل از یک مشاوره قبلی در Art. 36 GDPR با یک فایل انگلیسی زبان
- When the in-house format is missing and a defensible standard template is needed

## چارچوب قانونی

- Art. 35(7) GDPR حداقل محتوای DPIA:
 - lit. یک توصیف سیستماتیک از عملیات و اهداف پردازش
 - lit. ب) ارزیابی ضرورت و تناسب
 - lit. c ارزیابی ریسک به حقوق و آزادی های افراد داده
 - lit. d اقدامات مورد نظر برای رسیدگی به خطر، از جمله حفاظت ها و مکانیسم های امنیتی
- Art. 35(2) GDPR مشاوره DPO
- Art. 35(9) GDPR مشاوره با افراد داده یا نمایندگان آنها در صورت لزوم
- Art. 5(2) GDPR پاسخگویی
- راهنمای EDPB WP 248 rev.01 on DPIA

## روش شش مرحله ای

1. **صفحه پردازش* * Populate بخش 1.
2. ** نیاز و ارزیابی تناسب اندام* * بخش 2.
3. ** خطر به افراد داده* * بخش 3 با ماترکس ریسک
4. ** اقدامات برای کاهش خطر* * بخش 4.
5. ** ریسک باقیمانده* * بخش 5.
6. **موافقیت* * بخش 6 با امضا

## قالب (به انگلیسی: Full DPIA)

```
DATA PROTECTION IMPACT ASSESSMENT (DPIA)
pursuant to Article 35 GDPR

Internal reference: [...]
Version: [1.0] | Date: [DD-MM-YYYY]
Controller: [Legal entity, address, legal representative]
DPO: [Name, e-mail, phone]
Lead department: [...]
Classification: [confidential / internal]

COVER PAGE
Processing activity: [Designation]
Legal basis: [Art. 6 / Art. 9 GDPR, plus national law if applicable]
Competent supervisory authority: [BfDI / state DPA / lead authority Art. 56]
Version history: [...]

EXECUTIVE SUMMARY (one page)
Purpose: [...]
Categories of data: [...]
Data subjects: [...]
Overall risk before measures: [HIGH / MEDIUM / LOW]
Overall risk after measures: [HIGH / MEDIUM / LOW]
Approval recommendation: [Approved / Prior consultation Art. 36 / Not approved]

1. DESCRIPTION OF PROCESSING
 (Art. 35(7)(a) GDPR)
1.1 Purpose and nature of processing
[...]
1.2 Categories of personal data
- Identification data: [...]
- Content data: [...]
- Usage data: [...]
- Special categories Art. 9 GDPR: [...]
- Criminal data Art. 10 GDPR: [...]
1.3 Categories of data subjects
[Customers / Employees / Patients / Citizens]
1.4 Recipients and transfers
- Internal recipients: [...]
- External processors: [...]
- Third country transfers: [Country, safeguards under Chapter V]
1.5 Retention periods
[Period, deletion concept]
1.6 Technical environment
[Hosting, sub-processors, encryption baseline]
1.7 Data flow
[Diagram reference or short narrative]

2. NECESSITY AND PROPORTIONALITY ASSESSMENT
 (Art. 35(7)(b) GDPR)
2.1 Necessity of processing for purpose
[Suitable, necessary, no less intrusive means]
2.2 Data minimisation Art. 5(1)(c) GDPR
[...]
2.3 Purpose limitation Art. 5(1)(b) GDPR
[...]
2.4 Storage limitation Art. 5(1)(e) GDPR
[...]
2.5 Lawfulness Art. 6 / Art. 9 GDPR
[Legal basis per category of data and category of data subject]
2.6 Rights of data subjects
[How are access, rectification, erasure, restriction, portability, objection ensured?]
2.7 Transparency Art. 12 et seq. GDPR
[...]

3. RISK TO DATA SUBJECTS
 (Art. 35(7)(c) GDPR)
3.1 Risk matrix before measures
| No | Scenario | Likelihood | Severity | Risk |
|----|-----------------------------------|------------|----------|------|
| 1 | Unauthorised access (confid.) | [h/m/l] | [h/m/l] | [R/O/Y/G] |
| 2 | Data leakage to outside | | | |
| 3 | Covert profiling | | | |
| 4 | Data loss / availability | | | |
| 5 | Manipulation / integrity | | | |
| 6 | Discrimination of data subjects | | | |
| 7 | Identity theft | | | |
3.2 Protection goals touched
[Confidentiality / Integrity / Availability / Transparency / Intervenability / Unlinkability / Data minimisation]
3.3 Vulnerable data subjects
[Children / Patients / Employees / Consumers]

4. MEASURES TO MITIGATE RISK
 (Art. 35(7)(d) GDPR)
4.1 Technical measures (Art. 32 GDPR)
- Encryption: [type, key length]
- Pseudonymisation: [...]
- Access control: [role / rights concept]
- Logging: [...]
- Backup and restore: [...]
- State of the art: [...]
4.2 Organisational measures
- Training: [target group, frequency]
- Four-eyes principle: [...]
- Authorisation concept: [...]
- Incident response plan: [...]
4.3 Contractual measures
- Data processing agreement (Art. 28 GDPR): [Processor, date, version]
- Standard Contractual Clauses for transfers: [Module, date]
- Transfer impact assessment (TIA): [Reference]
4.4 Measures table
| No | Risk | Measure | Owner | Deadline | Residual risk |

5. RESIDUAL RISK
5.1 Risk matrix after measures
[Table as 3.1 with values after measures]
5.2 Assessment of residual risk
[Remaining risk per scenario, overall rating]
5.3 Need for prior consultation Art. 36 GDPR
[ ] No consultation required (residual risk medium or low)
[ ] Prior consultation required (residual risk high)

6. CONSULTATION AND APPROVAL
6.1 DPO opinion (Art. 35(2) GDPR)
[Wording or reference to annex]
DPO signature: ____________________ Date: ____________________

6.2 Consultation of data subjects (Art. 35(9) GDPR)
[Performed / not performed with justification]

6.3 Approval by controller
Name: ____________________
Role: ____________________
Signature: ____________________ Date: ____________________

6.4 Inclusion in records of processing Art. 30 GDPR
Reference: [...]

6.5 Review plan Art. 35(11) GDPR
Next review: [DATE]
Triggers for ad-hoc review: [change of data categories / recipients / technology / law]
```

## اشتباهات معمول

- بخش 1 بدون توصیف جریان داده های واقعی عمومی باقی می ماند.
- نیاز به ارزیابی محدود شده است تا قانونی؛ کاهش داده ها و محدودیت ذخیره سازی نادیده گرفته می شود.
- سناریوهای خطر فقط شامل محرمانه بودن هستند؛ اهداف دیگر حفاظت خالی باقی مانده است.
- جدول اندازه گیری بدون مالک و مهلت - نه استرایبل.
- DPO signs late or not at all - شکاف شواهد
- هیچ کنترل نسخه ای وجود ندارد - تغییرات قابل ردیابی نیست.

## مرجع های متقابل

- `datenschutzrecht/skills/dsfa-template-deutsch-vollvorlage/SKILL.md` - توليد کامل زبان آلمانی
- `datenschutzrecht/skills/dsfa-risikoanalyse-eintrittswahrscheinlichkeit-schaden/SKILL.md` - روش ریسک
- `datenschutzrecht/skills/dpia-en-summary-for-management/SKILL.md` - English management summary
- `datenschutzrecht/skills/dsfa-für-internationale-datentransfers/SKILL.md` - انتقال بین المللی
- `references/zitierweise.md` - قوانین نقل قول

## منابع 06/2026

- Art. 35(2), (7), (9), (11) GDPR
- Art. 5(2), 30, 32 GDPR
- راهنمای EDPB WP 248 rev.01
- SDM V3.0 (نموذج استاندارد حفاظت از داده های آلمانی) - اهداف محافظت
- قانون قضایی: از دانش مدل استفاده نکنید؛ با منابع رسمی تأیید کنید
- ادبیات: فقط از منبع ارائه شده توسط کاربر یا دسترسی زنده مجوز داده می شود
