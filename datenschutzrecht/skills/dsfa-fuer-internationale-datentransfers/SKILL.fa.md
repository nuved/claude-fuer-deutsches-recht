---
name: dsfa-fuer-internationale-datentransfers
description: "Wenn es um DSFA bei internationalen Datentransfers in Datenschutzrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# DSFA در انتقال بین المللی داده ها

## این ماژول کِی کمک می‌کند

- در مورد پردازنده های غیرمستقیم یا فرعی
- در صورت ایجاد یک دفتر رسمی در کشور ثالث
- در مورد خدمات ابر ایالات متحده (همچنین برای میزبانی اتحادیه اروپا به دلیل دسترسی مقامات آمریکا)
- در مورد انتقال بین المللی از طریق مرزهای کشور
- در مورد ارائه دهندگان هوش مصنوعی با آموزش یا تأکید در کشور ثالث
- در مورد قوانین امنیتی ملی کشور ثالث (مانند قانون CLOUD، FISA 702 و China DSL)

## چارچوب حقوقی

- Art. 44 DSGVO اصل: هر انتقال باید به صورت قانونی در فصل V باشد.
- Art. 45 DSGVO تصمیم کافی از سوی کمیسیون
- Art. 46 DSGVO تضمین های مناسب (SCC، BCR، قوانین رفتاری و گواهینامه)
- Art. 47 DSGVO قوانین شرکت های متعهد.
- Art. 49 DSGVO استثنا در مورد فايل خاص (موافقت، اجرای قرارداد و منافع عمومی)
- شرمز II EuGH ساعت 1607.2020C-311/18 - نیاز به بررسی انتقال؛ TIA لازم است.
- دستورالعمل های EDSA 04/2022 در مورد انتقال داده های شخصی (استفاده کننده باید به دقت بررسی کند).
- تصمیم کافی برای چارچوب داده های خصوصی ایالات متحده و اتحادیه اروپا (DPF) 10.07.2023، تصمیم اجرایی (EU) 2023/1795
- در این باره، از نظر ارجاعی و با توجه به شرایط مربوطه، باید تصمیم گیری های لازم را انجام دهیم.06.2021 با ماژول های 1 تا 4

## روش 6 مرحله

1. **صفحه پردازش* * چه داده هایی به کجا، به کی، در کدام شکل، چقدر و تا چه حد می روند؟
2. **آیا انتقال به کشور خارج برای این هدف ضروری است یا گزینه های اتحادیه اروپا وجود دارد؟
3. **تحليل خطر*
 - حقوق کشورهای دیگر: اختیارات دسترسی مقامات، درخواست های حقوقی افراد.
 - ریسک ارائه دهنده: صنعت، نوع داده ها و فرعی.
 - ریسک داده ها: حساسیت، جمع آوری و شناسایی.
4. ** اقدامات*
 - پایه قانونی: تصمیم کافی، SCC با ماژول مناسب، BCR، استثنا Art. 49.
 - اقدامات معاوضه ای که طبق توصیه های EDSA انجام می شود 01/2020 (مطالب به تأیید): فنی (تشفیه، کلید) ، قراردادی (تعمیر اطلاعات در مورد درخواست های مقامات دولتی) و سازمانی (آudit، آموزش).
5. **خطر بازپسین.** بررسی اینکه آیا اقدامات در این زمینه سطح حفاظت را به سطح اتحادیه اروپا می رساند یا خطر بازپسين بالا است.
6. **معاونیت / مجوز* *حاکمت های DSB؛ در صورت باقی مانده خطر بالا Art. 36 DSGVO پیش از این، مشاوره و بررسی DPF توسط ارائه دهندگان آمریکایی.

## متن نمونه / قالب (قسم انتقال DSFA)

```
TRANSFER IMPACT ASSESSMENT [DATUM]
(Erweiterung der DSFA Sektion 4 / Anlage zur DSFA)

Verantwortlicher: [NAME]
Empfaenger im Drittland: [Name, Land, Konzernverbund]
Sub-AVs: [Liste mit Land]

1. Transferbeschreibung
- Datenkategorien: [...]
- Datenmenge: [...]
- Betroffenenkreise: [...]
- Uebermittlungsweg: [API / SFTP / DB-Replikation]
- Verschluesselung: [Transport / Ruhe / Ende-zu-Ende]
- Schluesselhoheit: [EU / Drittland / Hybrid]

2. Rechtsgrundlage des Transfers
[ ] Angemessenheitsbeschluss Art. 45 DSGVO: [Land, Beschlussdatum]
[ ] SCC Modul: [1 C-C / 2 C-P / 3 P-P / 4 P-C], Datum [...]
[ ] BCR: [Genehmigung, Datum]
[ ] Ausnahme Art. 49 Abs. 1 lit. [a/b/c/...] mit Begruendung
[ ] DPF-Zertifizierung Empfaenger: ja / nein, Stand [Datum]

3. Drittlandrechtspruefung
- Zugriffsbefugnisse Behörden: [CLOUD Act / FISA 702 / Section 702 / China DSL / Russland TK-Gesetz]
- Rechtsbehelfe Betroffener: [vorhanden / nicht aequivalent]
- Aufsichtsstruktur: [unabhaengig / nicht unabhaengig]
- Pruefung Schrems-II-Standard erfuellt: ja / nein
- Quelle: [EDSA-Länderbericht, Anbietererklaerung, Stand]

4. Ergaenzende Massnahmen
- Technisch:
 [ ] Ende-zu-Ende-Verschluesselung mit EU-Schluesselhoheit
 [ ] Pseudonymisierung vor Transfer
 [ ] Tokenisierung
 [ ] Split-Processing (sensitive Felder in EU)
- Vertraglich:
 [ ] Transparenz-Pflicht ueber Behördenanfragen
 [ ] Audit-Recht
 [ ] Loeschpflicht nach Vertragsende
- Organisatorisch:
 [ ] Anbieterschulung Datenschutz
 [ ] Notfallplan bei Behördenzugriff

5. Restrisikobewertung
[GRUEN / GELB / ORANGE / ROT]
Begruendung: [...]

6. Entscheidung
[ ] Transfer zulaessig — Massnahmen umgesetzt
[ ] Transfer zulaessig mit Auflagen
[ ] Vorabkonsultation Art. 36 DSGVO erforderlich
[ ] Transfer nicht zulaessig — Alternative pruefen

7. Ueberwachung
- Naechste Re-Pruefung: [Datum]
- Trigger: [Schrems-III-Folgeurteil / DPF-Status-Aenderung / Anbieterwechsel]

Unterschrift Verantwortlicher: ____________________
Unterschrift DSB: ____________________
```

## خطاهای رایج

- TIA به طور جداگانه از فرآیند DSFA اداره می شود - رابط ها گم شده اند.
- ابر ایالات متحده با میزبانی اتحادیه اروپا به عنوان پردازش خالص اروپایی مورد استفاده قرار می گیرد - اختیار دسترسی توسط مقامات آمریکا نادیده گرفته شده است.
- ماژول SCC اشتباه انتخاب شده (C-P به جای C-C یا برعکس).
- اقدامات معاوضه ای فقط قانونی است و نه فنی.
- استثنا Art. 49 به عنوان یک گزینه دائمی استفاده می شود، اگرچه فقط برای فرد مورد نظر است.
- بازتجربه پس از نتیجه گیری شرمز، باقی مانده است.
- گواهینامه DPF ارائه دهنده سالیانه بررسی نمی شود.

## وضعیت منابع 06/2026

- Art. 44 تا 49 DSGVO
- EuGH ساعت 1607.2020در این زمینه، ما باید به نظر بگیریم که آیا می توانیم از آن ها استفاده کنیم.
- در این باره، از نظر رسمی و با توجه به شرایط مربوطه تصمیم گیری می شود.06.2021 (SCC)
- در این باره، به عنوان مثال:07.2023 (DPF)
- دستورالعمل های EDSA 04/2022 (مطابقات را بررسی کنید)
- توصیه های EDSA 01/2020 اقدامات لازم برای بررسی (مطابق فعلی)
- قضیه: اقتباسات دیگر را از دانش مدل استفاده نکنید؛ قبل از انتشار تایید کنید
- ادبیات: مکان های نظرات و مقالات فقط با منبع خود
