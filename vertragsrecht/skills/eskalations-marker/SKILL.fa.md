---
name: eskalations-marker
description: "Wenn es um Eskalationsregeln in Vertragsrecht geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# قوانین بالا رفتن

## مسیر کار

- روشن‌کردن نقش، هدف و محصول کاری خواسته‌شده: چه کسی اقدام می‌کند، چه تصمیمی در پیش است، چه مهلتی در جریان است و چه خروجی‌ای لازم است؟
- نخست علامت‌گذاری مهلت‌ها و خطرهای فوری: تنها از مهلت‌های همان حوزهٔ حقوقی مشخص و همان پرونده استفاده کنید؛ اعتراض (Widerspruch)، دعوا (Klage)، ایراد (Einspruch)، طرق شکایت (Rechtsmittel)، مرور زمان (Verjährung)، سقوط حق (Verwirkung) و مهلت‌های ایراد، اعلام، ثبت و انقضا را به‌دقت جدا کنید و هرگز از حوزهٔ تخصصی دیگری برندارید.
- بررسی معیارهای مربوط به: BGB §§ 305-310, AGBG (سابق) EuGH در مورد شفافیت شقایق (مثل C-26/13, C-186/16), VerbrG §§ 305 ff. BGBاین در حالی است که از طریق آن، NDA و SaaS gesetze-im-internet.de, dejure.org،آفتاب BVerfG-/BGH-/EuGH-دیتابیس زنده را بررسی کنید، بدون نقل قول دانش مدل
- تعیین مرجع صالح و انتخاب درست مخاطب: موکل، طرف مقابل، ادارهٔ صالح یا دادگاه، کارشناسان و در صورت لزوم نهاد اتحادیهٔ اروپا/بین‌المللی (به جزئیات اسکیل نگاه کنید).
- گردآوری اسناد و ادلّه و بررسی خلأها: پرونده‌های اداری، اسناد قراردادی، لوایح، تصمیم‌های اداری (Bescheide)، صورت‌جلسه‌ها، نظرهای کارشناسی و ادلّهٔ بیرونیِ همان حوزه — مدارک نبود را از راه دسترسی به پرونده یا پرسش از موکل فراهم کنید، و برای تغییرهای روزِ قوانین و رویهٔ اداری بررسی زنده انجام دهید.

## سه بعدی در آغاز

1. کدام یک از محرکات افزایش وجود دارد؟ حد مبلغ، انحراف قاعده یا محرک های خودکار.
2. شرکت در چه طرفی قرار دارد (خریدگر یا فروشنده) - کدام کتاب بازی قابل اجرا است؟
3. چه کسی به طور مشخص از طریق ماتریس اسکالاسیون (CLAUDE.md) مجوز می دهد؟
4. تا چه زمانی باید یک تصمیم در دست باشد (مدت مذاکرات) ؟

## رویهٔ قضایی روز

- قضیه: هیچ تصمیمی را از دانش نمونه ای نقل نکنید؛ قبل از انتشار با دادگاه، شکل تصمیم گیری و تاریخ آن ها، نشانه های پرونده یا اظهارات قابل اثبات را توسط منبع رسمی یا آزاد تأیید کنید.

## قوانین محوری

- § 164 ff. BGB - نمایندگی؛ اختیارات
- § 177 BGB - اجازه دادن به فعالیت های بی اختیار
- § 311 Abs. 2 BGB - گناه در قرارداد
- §§ 5-8 LkSG - واجبات مراقبت (تغییرات در موارد نقض زنجیره تامین)
- Art. 33, 34 DSGVO - گزارش در مورد کلاهک های داده (تغییرات افزایش)
- § 43a Abs. 2 BRAO - محرمانه بودن حقوقی

## ورودی‌ها

- توضیحات مشکل (به طور مستقیم یا با اشاره به یک یادداشت آزمایش)
- پروفایل عملی `~/.claude/plugins/config/claude-fuer-deutsches-recht/vertragsrecht/CLAUDE.md` → `## Eskalation`
- ارزش سالیانه/ACV قرارداد (برای حد رقم)

## متن پرونده ها

اگر قسمت های کاری پرونده فعال شده است، فایل های فعال را بررسی کنید.

## زمان

### مرحله اول: بارگذاری ماتریکس

`~/.claude/plugins/config/claude-fuer-deutsches-recht/vertragsrecht/CLAUDE.md` → `## Eskalation` در صورت عدم وجود یا مبهم بودن، اشاره به اینکه باید پروفایل عملی را تکمیل کنید.

** کدام صفحه؟** کتاب بازی خریدار یا فروشنده تعیین می کند که آیا یک مفهوم در موقعیت های سقوط قرار دارد و یا به طور خودکار افزایش پیدا میکند.

### مرحله دوم: حل مسئله

چه چیزی در حال افزایش است؟

- **حده ی مبلغ:** ارزش قرارداد بیش از صلاحیت مجوز
- ** انحراف از بند:** یک مفهوم خارج از موقعیت های فال بیک کتاب بازی است؛ فردی با تجربه تر باید تصمیم بگیرد که آیا پذیرش توجیه شده
- **تغییرات خودکار:** لیست همیشه افزایش (به عنوان مثال، مسئولیت نامحدود، اعطای IP، نقض حفاظت از اطلاعات بدون اصلاح، LkSG)
- ** تصمیم کسب و کار:** یک سوال حقوقی نیست بلکه موضوعی برای صاحب تجارت است

چیزی که واقعاً درست است، بالا نمی رود. اگر مفهوم در موقعیت های عقب نشینی قرار دارد، نیازی به افزایش ندارد.

### مرحله سوم: مجوز را تعیین کنید

خط های ماترکس مناسب را انتخاب کنید. یک شخص یا نقش مشخصی نام ببرید - نه "مستفادۀ رهبری" انتزاعیه ای

### مرحله 4: طراحی درخواست

نمونه (هميشه استفاده ميكنيم):

```markdown
Betreff: Genehmigung erforderlich – [Vertrag] mit [Vertragspartner] – [Problembezeichnung]

[Name],

ich bitte um Genehmigung zu folgendem Vertragspunkt:

**Vertrag:** [Bezeichnung und Vertragspartner]
**ACV:** [Jahreswert]
**Klausel / Problem:** [§ X – Kurzbezeichnung]

**Was der Vertrag sagt:**
> "[wörtliches Zitat der betroffenen Klausel]"

**Was unser Playbook sagt:**
[Standard-Position aus CLAUDE.md] / [Fallback-Position aus CLAUDE.md]

**Warum das eskaliert:**
[Ein Satz: Betrags-Schwelle / Abweichung außerhalb Fallback / automatischer Auslöser / Geschäftsentscheidung]

**Risiko bei Akzeptanz ohne Änderung:**
🔴/🟠/🟡 [Rechtliches Risiko] | 🔴/🟠/🟡 [Geschäftliche Reibung]
[Konkrete Folge: z. B. "Unbegrenzte Haftung für Datenpannen; typischer Schaden bei mittelgroßem Verstoß XXX EUR"]

**Optionen:**

1. **Akzeptieren** – [Bedingung oder unkonditioniert]
 Konsequenz: [was das bedeutet, z. B. "unbegrenzte Haftung bleibt bestehen; kein Deckungsschutz D&O"]

2. **Verhandeln** – Redline: [konkrete Formulierung]
 Verhandlungsspielraum: [einschätzen, ob Markt-Standard / Gegenseite wird wahrscheinlich...]

3. **Ablehnen** – [Begründung gegenüber Gegenseite]

**Empfehlung:** Option [N] – [ein Satz Begründung]

**Entscheidung bis:** [Datum] (Verhandlungsdeadline oder Vertragsabschluss-Termin)

Bei Rückfragen stehe ich gerne zur Verfügung.

[Absender]
```

### مرحله پنجم: ارسال نمی شود

طرحی را اعلام کنید، وکیل شما ارسال می کند. هرگز بدون تایید صریح نمی فرستید

## افزایش: [Vertrag] با [Vertragspartner] – [Klausel]

** علت افزایش:** [Betrags-Schwelle / Klausel-Abweichung / Automatischer Auslöser / Geschäftsentscheidung]
**مطمئن تر:** [Person/Rolle aus CLAUDE.md]
** راه تماس:** [Slack / E-Mail / Meeting]
** صفحه:** [Käufer/Verkäufer – welches Playbook wurde angewendet]

---

[Entwurf der Genehmigungsanfrage gemäß Vorlage oben]

---

️ نکته ی معاینه کننده: قبل از ارسال، بررسی کنید که آیا طرح وضعیت را درست نشان می دهد و اطلاعات محرمانه ای را به طور ناخواسته منتشر نمی کند.
```

## Quellen und Zitierweise

Zitierweise nach `../references/zitierweise.md`.

Relevante Normen:
- § 164 ff. BGB – Vertretungsmacht; Vollmacht
- § 177 BGB – Genehmigung vollmachtlosen Handelns
- § 43a Abs. 2 BRAO – anwaltliche Verschwiegenheitspflicht
- Bei LkSG-Eskalation: §§ 5–8 LkSG – Sorgfaltspflichten, Risikoanalyse, Präventionsmaßnahmen
- Bei DSGVO-Eskalation: Art. 33, 34 DSGVO – Melde- und Benachrichtigungspflichten

## Risiken / typische Fehler

- **Zu viel eskalieren:** Wenn alles eskaliert wird, verliert die Matrix ihre Wirkung. Nur wirkliche Überschreitungen eskalieren.
- **Entscheidung vorwegnehmen:** Der Entwurf bietet Optionen – er trifft keine Entscheidung. Der Genehmiger entscheidet.
- **Frist vergessen:** Ohne Entscheidungs-Datum läuft die Verhandlung. Immer ein Datum nennen.
- **Privilegierter Inhalt außerhalb des Kreises:** Genehmigungsanfragen intern halten; § 43a Abs. 2 BRAO, § 203 StGB beachten.
