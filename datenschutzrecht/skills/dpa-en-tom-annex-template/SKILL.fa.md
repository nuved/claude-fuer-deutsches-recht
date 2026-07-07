---
name: dpa-en-tom-annex-template
description: "Wenn es um TOM Annex – English Template (Article 32 GDPR) in Datenschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# TOM Annex - English Template (ماده 32 GDPR)

## هدف / مقصد

سانتایل ضمیمه زبان انگلیسی که اقدامات فنی و سازمانی (TOM) مورد نیاز را در ماده 32 مشخص می کند GDPR و توسط reference into the DPA به کار گرفته شده است. Art. 32 DSGVO.

## این ماژول کِی کمک می‌کند

- DPA به زبان انگلیسی یا Cross-border needs a TOM annex.
- پروسسور ارائه می دهد ISO 27001 / SOC 2 / BSI C5 خط بندی و ضمیمه باید این را منعکس کند.
- به عنوان مثال، این امر قابل توجه است که از طریق برنامه های کاربردی و یا خدمات عمومی برای تولید محصولات مختلف استفاده شود.

## چارچوب حقوقی

- ماده 32 (1) (a) GDPR -اسرار نامگذاری و رمزنگاری
- ماده 32 (1) (ب) GDPR - محرمانه بودن، سالمیت، دسترسی و انعطاف پذیری
- ماده 32 (1) (ج) GDPR - توانایی بازگرداندن دسترسی و دستیابی به زمان
- ماده 32 (1) (د) GDPR - فرآیند تست، ارزیابی و بررسی موثر بودن به صورت منظم.
- ماده 25 GDPR - حفاظت از داده ها به صورت طراحی و پیش فرض

## زمان رسانی / چک لیست

1. پروفایل ریسک پردازش را تایید کنید.
2. نقشه های اقدامات علیه ماده 32 (1) (a) تا (d) GDPR.
3. گواهینامه های مرجع (ISO 27001، SOC 2 و BSI C5)
4. تعریف آزمایش cadence (تجربه نفوذ، اسکن آسیب پذیری).
5. اطمینان از اینکه اقدامات زیر پردازشگر سازگار است (ماده 28 (4) GDPR).
6. این نامه با مهر تاریخ، سالانه یا به صورت تغییر قابل تجدید است.

## متن نمونه / قالب

```
ANNEX II TO THE DATA PROCESSING AGREEMENT
TECHNICAL AND ORGANISATIONAL MEASURES (Article 32 GDPR)

Effective date: [DATE]
Processor: [NAME]
Review cycle: annually and upon material change

1. PSEUDONYMISATION (Art. 32 (1) (a) GDPR)
 1.1 Personal data shall be pseudonymised in development and test environments.
 1.2 The mapping table shall be stored separately, with access limited to the
 Data Protection Officer.

2. ENCRYPTION (Art. 32 (1) (a) GDPR)
 2.1 In transit: TLS 1.3 with forward secrecy, configured in accordance with
 industry guidance (e.g. BSI TR-02102 or NIST SP 800-52 Rev. 2).
 2.2 At rest: AES-256 (CBC or GCM) for all databases and backups.
 2.3 Key management: hardware security module (HSM) or equivalent; keys rotated
 at least annually.

3. CONFIDENTIALITY (Art. 32 (1) (b) GDPR)
 3.1 Physical access controls: 24/7 guarded data centres with multi-factor
 physical access.
 3.2 Logical access: multi-factor authentication for all privileged accounts.
 3.3 Authorisation: role-based access control on a least-privilege basis;
 periodic recertification.
 3.4 Segregation: multi-tenant logical separation with tenant-scoped access
 control.

4. INTEGRITY (Art. 32 (1) (b) GDPR)
 4.1 Transfer controls: documented interfaces; audit logging of all data
 exports.
 4.2 Input controls: write-operation logging with attribution to authenticated
 identities.
 4.3 Hashing: SHA-256 or stronger for integrity verification.

5. AVAILABILITY AND RESILIENCE (Art. 32 (1) (b) GDPR)
 5.1 Backups: daily incremental, weekly full; retention thirty (30) days.
 5.2 Recovery Point Objective (RPO): twenty-four (24) hours or less.
 5.3 Recovery Time Objective (RTO): eight (8) hours or less for critical
 processing.
 5.4 Geographic redundancy: synchronous replication across at least two EEA
 data centres.
 5.5 DDoS protection: upstream filtering with provider SLA.

6. RECOVERABILITY (Art. 32 (1) (c) GDPR)
 6.1 Incident response runbook; tabletop exercises at least annually.
 6.2 Documented restoration procedures.
 6.3 Restoration drills with actual data restoration tests at least semi-annually.

7. REGULAR TESTING (Art. 32 (1) (d) GDPR)
 7.1 Independent third-party penetration testing at least annually.
 7.2 Vulnerability scanning monthly.
 7.3 Internal ISMS audits annually; external ISO 27001 audits annually.
 7.4 TOM annex review at least annually.

8. ORGANISATIONAL MEASURES
 8.1 Data Protection Officer designated; contact details in Annex IV.
 8.2 Confidentiality undertakings from all personnel processing personal data
 (Article 28 (3) (b) GDPR).
 8.3 Annual data protection training with attendance records.
 8.4 Joiner-mover-leaver process; immediate revocation of access on exit.
 8.5 Incident response procedure with notification to the Controller within
 forty-eight (48) hours of becoming aware of a personal data breach
 (Article 33 GDPR).

9. CERTIFICATIONS AND STANDARDS
 9.1 ISO/IEC 27001:2022 – certified on [DATE] by [BODY].
 9.2 BSI C5:2020 Type 2 – report dated [DATE].
 9.3 SOC 2 Type II – report period [PERIOD].

10. SUB-PROCESSORS
 10.1 Sub-processors are required to implement measures at least equivalent
 to those set out in this Annex II (Article 28 (4) GDPR).
 10.2 Sub-processor audit reports shall be provided to the Controller on
 request.

Signed by: Date:
________________________________ ____________________________
[Processor representative]
```

## اشتباهات معمول در طراحی

- نسخه بازاریابی به جای اقدامات عملی.
- "حکومت هنر" بدون جزئیات
- از زمان امضا اول تا حالا خبر نداري
- نامگذاری غیرقابل شناخت حذف شده است، حتی اگر ماده 32 (1) (a) GDPR ازش استفاده کرد.
- نه RPO/RTO
- هیچ تست cadence.
- زیر پردازنده استحکام نمی رسید.

## وضعیت منابع 06/2026

- GDPR ماده 25، ماده 28 (3) (ج) ، مقاله 32 و ۳۳
- BSI TR-02102 (ملاحظه رمزنگاری)
- NIST SP 800-52 Rev. 2
- در این زمینه، باید از نظر معیارهای مربوط به سیستم های مختلف استفاده شود.
- BSI C5:2020.
- این موضوع در مورد شرایط و مقررات مربوط به خدمات اعتباری است.
- قوانین نقل قول: `../../../references/zitierweise.md`.
```
