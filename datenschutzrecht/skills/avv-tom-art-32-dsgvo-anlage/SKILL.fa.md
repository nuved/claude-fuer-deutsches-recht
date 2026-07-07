---
name: avv-tom-art-32-dsgvo-anlage
description: "Wenn es um TOM-Anlage Art. 32 DSGVO in Datenschutzrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# دستگاه TOM Art. 32 DSGVO

## هدف / مقصد

سیستم ساختاری AVV با اقدامات فنی و سازمانی پردازنده در برابر Art. 32 DSGVO و Art. 28 Abs. 3 lit. c DSGVO. هدف: زبان آلمانی TOM annex to a DPA under Article 32 GDPR.

## این ماژول کِی کمک می‌کند

- دستگاه TOM برای AVV باید ایجاد، بررسی یا به روز رسانی شود.
- سازمان نظارتی از توم برای اثبات این کار می خواهد.
- از نظر داده ها، سیستم TOM باید به طور مداوم بررسی شود.
- اگر پردازش تغییر کند، دستگاه TOM را باید تنظیم کرد.

## چارچوب حقوقی

- Art. 32 Abs. 1 DSGVO: مناسب برای TOM با توجه به وضعیت تکنولوژی، هزینه های پیاده سازی و نوع، حجم، شرایط و اهداف پردازش و احتمال وقوع مختلف و میزان خطر.
- Art. 32 Abs. 1 lit. a تا d DSGVO: نامگذاری و رمزنگاری، محرمانه بودن، صداقت، دسترسی، قابل تحمل شدن، بازیابی، بررسی منظم.
- Art. 25 DSGVO: حفاظت از داده ها با طراحی فنی و تنظیمات دوستانه به حفظ اطلاعات.
- Art. 28 Abs. 3 lit. c DSGVO: TOM به عنوان یک شرط اجباری در AVV.

## زمان رسانی / چک لیست

1. ** ارزیابی ریسک*
 - نوع داده ها (تاریخ، ترافیک و محتوای آن) Art. 9 DSGVO).
 - اندازه و هدف.
 - احتمال وقوع و میزان خطر برای افراد مبتلا.

2. **کتاب های حداقل (Art. 32 Abs. 1 DSGVO).**

 | دسته بندی | نمونه های اقدامات |
 |---|---|
 | نامگذاری | نامگذاری در محیط های آزمایش و توسعه، جداسازی فنی جدول تخصیص |
 | رمزنگاری | TLS 1.3 در حال عبور AES-256 at rest HSM |
 | محرمانه بودن | کنترل دسترسی، کنترل ورودی، کنترل برقراری ارتباط |
 | صداقت | کنترل انتقال، کنترول ورودی، ثبت نام، عملکرد هاش |
 | در دسترس بودن | پشتیبان گیری، RPO/RTO، برنامه اضطراری، ذخیره سازی جغرافیایی |
 | قابل تحمل | حفاظت از DDoS، توزیع بار و ناکامی |
 | قابلیت بازیابی | آزمایش های پشتیبان، روش های بازپرداخت مستند |
 | بررسی منظم | آڈیتی سالانه TOM، آزمایش نفوذ و اسکن آسیب پذیری |

3. ** اقدامات سازمانی*
 - کارگزار حفاظت از اطلاعات، آموزش های مربوط به محافظت از داده ها (سالانه) ، تعهدات حریم خصوصی, دستورالعمل امنیت فناوری اطلاعات, برنامه پاسخ حادثه، نیاز به دانش اصول، مدیریت مجوزها و فرآیند جاوید کننده.

4. ** گواهینامه ها و استانداردها*
 - در این زمینه، باید از نظر معیارهای مربوط به سیستم های مختلف استفاده شود.
 - BSI IT Basic Protection / BSI C5:2020 (تخصیص ابر)
 - معیار خدمات اعتماد SOC 2 نوع II
 - TISAX (آتوماسیون)
 - PCI-DSS (تدبیرات پرداخت)

5. **بعد از اون، همت AV*
 - فرعی که حداقل همان سطح TOM را داشته باشند.
 - (در حال حاضر، این موضوع در موردArt. 28 Abs. 4 DSGVO).

## متن نمونه / قالب

سیستم TOM (تازه ساخت):

```
Anlage 2 zum Auftragsverarbeitungsvertrag
Technische und organisatorische Massnahmen (Art. 32 DSGVO)

Stand: [DATUM]
Auftragsverarbeiter: [NAME]
Pruefturnus: jaehrlich, unverzueglich bei wesentlicher Aenderung

1. Pseudonymisierung (Art. 32 Abs. 1 lit. a DSGVO)
 1.1 In Entwicklungs- und Testumgebungen werden personenbezogene Daten ausschliesslich in pseudonymisierter Form verarbeitet.
 1.2 Die Zuordnungstabelle wird getrennt gespeichert; Zugriff nur für den Datenschutzbeauftragten.

2. Verschluesselung (Art. 32 Abs. 1 lit. a DSGVO)
 2.1 In Transit: TLS 1.3 mit Forward Secrecy; SSL/TLS-Konfiguration gemaess BSI TR-02102.
 2.2 At Rest: AES-256 (CBC oder GCM) für alle Datenbanken und Backups.
 2.3 Schluesselverwaltung: HSM oder gleichwertige Loesung; jaehrliche Rotation.

3. Vertraulichkeit (Art. 32 Abs. 1 lit. b DSGVO)
 3.1 Zutrittskontrolle: physische Sicherung der Rechenzentren (24/7-Bewachung, Mehrfaktor-Zutritt).
 3.2 Zugangskontrolle: Multi-Faktor-Authentifizierung für alle priviligierten Konten.
 3.3 Zugriffskontrolle: rollenbasiertes Berechtigungsmodell, Least Privilege, periodische Rezertifizierung.
 3.4 Trennungskontrolle: mandantenfaehige Trennung; logische Trennung mit eigener Zugriffskontrolle.

4. Integritaet (Art. 32 Abs. 1 lit. b DSGVO)
 4.1 Weitergabekontrolle: dokumentierte Schnittstellen, Audit-Log für alle Datenexporte.
 4.2 Eingabekontrolle: nachvollziehbare Protokollierung aller Schreibvorgaenge auf personenbezogene Daten.
 4.3 Hash-Funktionen: SHA-256 oder besser für Integritaetspruefungen.

5. Verfuegbarkeit und Belastbarkeit (Art. 32 Abs. 1 lit. b DSGVO)
 5.1 Backup: taegliche inkrementelle Backups, woechentliche Vollbackups, Aufbewahrung 30 Tage.
 5.2 RPO (Recovery Point Objective): hoechstens 24 Stunden.
 5.3 RTO (Recovery Time Objective): hoechstens 8 Stunden für kritische Verarbeitungen.
 5.4 Geo-Redundanz: synchrone Replikation in mindestens zwei EU-Rechenzentren.
 5.5 DDoS-Schutz: vorgeschalteter Filter; SLA mit Provider.

6. Wiederherstellbarkeit (Art. 32 Abs. 1 lit. c DSGVO)
 6.1 Notfallhandbuch; Notfalluebungen mindestens jaehrlich.
 6.2 Dokumentierte Wiederherstellungsverfahren.
 6.3 Verifikation der Wiederherstellbarkeit durch tatsaechlichen Wiederherstellungstest mindestens halbjaehrlich.

7. Regelmäßige Pruefung (Art. 32 Abs. 1 lit. d DSGVO)
 7.1 Penetrationstest durch unabhaengige Dritte mindestens jaehrlich.
 7.2 Vulnerability Scan monatlich.
 7.3 ISMS-internes Audit jaehrlich; externes Audit nach ISO 27001 jaehrlich.
 7.4 TOM-Anlage wird mindestens jaehrlich auf Aktualitaet geprueft.

8. Organisatorische Massnahmen
 8.1 Datenschutzbeauftragter benannt; Kontaktangabe in Anlage 4.
 8.2 Verschwiegenheitsverpflichtung aller Mitarbeitern (Art. 28 Abs. 3 lit. b DSGVO).
 8.3 Jaehrliche Datenschutzschulung; Schulungsnachweise vorhanden.
 8.4 Joiner-Mover-Leaver-Prozess; sofortiger Entzug der Zugriffsrechte bei Austritt.
 8.5 Incident-Response-Plan mit Meldewegen an den Verantwortlichen binnen 48 Stunden nach Kenntnis einer Datenpanne (Art. 33 DSGVO).

9. Zertifikate und Standards
 9.1 ISO/IEC 27001:2022 – Zertifizierungsdatum [DATUM], Zertifizierer [STELLE].
 9.2 BSI C5:2020 Typ 2 – Stand [DATUM].
 9.3 SOC 2 Type II – Berichtszeitraum [ZEITRAUM].

10. Sub-Auftragsverarbeiter
 10.1 Sub-AV unterliegen denselben oder gleichwertigen TOM gemaess Art. 28 Abs. 4 DSGVO.
 10.2 Sub-AV-Audits werden auf Verlangen vorgelegt.
```

## اشتباهات معمول در طراحی

- توم کمپانی به عنوان یک کتابچه بازاریابی در عوض از اقدامات عملی.
- شکل های بسته ای (به صورت تکنولوژی) بدون توصیف مشخصی.
- از زمان قرارداد، هیچ گونه بروز رسانی نشده است.
- نامگذاری به عنوان یک وظیفه، اما Art. 32 Abs. 1 lit. a DSGVO او به طور واضح نام می دهد.
- هیچ آر پی او و RTO
- اطلاعات مربوط به بازرسی وجود ندارد.
- -آنها به دنبال همبستگی زیر آب هستند

## وضعیت منابع 06/2026

- Art. 25, Art. 28 Abs. 3 lit. ج) Art. 32 DSGVO.
- BSI TR-02102 (مطالعات رمزنگاری)
- در این زمینه، باید از نظر معیارهای مربوط به سیستم های مختلف استفاده شود.
- BSI C5:2020.
- معیار خدمات اعتباری SOC 2
- به عبارت دیگر: `../../../references/zitierweise.md`.
