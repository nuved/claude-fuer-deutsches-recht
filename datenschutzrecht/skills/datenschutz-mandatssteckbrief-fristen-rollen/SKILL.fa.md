---
name: datenschutz-mandatssteckbrief-fristen-rollen
description: "Wenn es um Datenschutzmandat: Steckbrief, Fristen, Rollen und Kontexttrennung in Datenschutzrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# در این زمینه، باید به نظر برسد که آیا یک سازمان یا شرکت از طریق آن ها می تواند اطلاعات مربوطه را ارائه دهد.

## هدف

جداسازی دستورات حفاظت از اطلاعات در دفاتر چندمندت: هر کس به یک حوزه کاری خاص با پرونده های خود اختصاص داده می شود (`mandat.md`مهارت ها در مطالعه پروفایل عملاً کل دفتر (`CLAUDE.md`) برای قوانین کل دفتر و پرونده اختصاصی در مورد حقایق خاص به وظایف.

**فقط برای شرکت های چندمندت مرتبط است.** در صورت کار داخلی (یک مسئول) این مهارت غیرفعال می شود؛ مهارت ها از پروفایل عملی به طور مستقیم استفاده می کنند.

توجه: اطلاعات مربوط به مشتری § 43a Abs. 2 BRAO, § 203 StGB.ازادگی در اختیار افراد، یک تعهد مربوط به حفاظت از اطلاعات و حقوق حرفه ای است.

## ورودی‌ها

 - شکل فرمان: `new | لیست | تغییر کنید [Mandat-ID] | بسته شدن [Mandat-ID] | هیچکدوم 
- در `neu`: نام کاربری، خلاصه از فرمان حفاظت از اطلاعات, هویت ماموریت (مختصر)
- در `wechsle`: هویت ماموریت در مورد مأموریت هدف

## زمان

### `neu` - شروع به کار جدید

1. مجوز شناسایی (مختصر، z.B. `mand-2024-04-mueller-dsfa`).
2. فهرست را ایجاد کنید: `~/.claude/plugins/config/claude-fuer-deutsches-recht/datenschutzrecht/mandate/[mandat-id]/`
3. خالی `mandat.md` با زمینه های لازم (ببینید ساختار زیر)
4. در پروفایل عملی، قرار دادن یک مجوز فعال به نام شناسه جدید.
5. تایید: "منتظره" [ID] تمام فراخوان های مهارت زیر در این زمینه کار می کنند".

### `liste` - برآورد ماموریت

تمام فهرست ها در زیر `mandate/` این موارد را ذکر کنید:
| هویت ماموریت | مشتری | توضیحات | وضعیت | آخرین فعالیت |
|---|---|---|---|---|
| … | … | … | باز / بسته | تاریخ |

### `wechsle [Mandat-ID]` - تغییر ماموریت

1. تایید هویت مأموریت از لیست.
2. در پروفایل عملی، قرار دادن یک مجوز فعال به نام شناسه جدید.
3. تاییدیه را صادر کنید؛ اگر وجود داشته باشد، وظایف باز در زمان ماندگاری قبلی را ذکر نمایید.

### `schließe [Mandat-ID]` - پایان دادن به ماموریت

1. وضعیت در `mandat.md` "ختم شده" و تاریخ پایان را انتخاب کنید.
2. تعویض ماموریت فعال (به "هیچ)
3. فایل های صادر شده از دستور کار هنوز قابل دسترسی هستند اما دیگر توسط مهارت ها فعالانه خوانده نمی شوند.

### `keins` - زمینه دفتر (هیچ مأموریت فعال)

مهارت ها در سطح کل دفتر عمل می کنند بدون زمینه خاص به مأموریت. برای تنظیمات عمومی اداره یا مهارت های مربوط به تمام شرکت (z.B. نظارت بر سیاست های داخلی شرکت).

## ساختار Matter.md

```markdown
# Mandat: [Mandat-ID]

## Mandant
- **Name:** [Mandantenname]
- **Rechtsform:** [GmbH / AG / Einzelperson / öffentliche Stelle]
- **Branche:** [Branche]
- **Hauptniederlassung:** [Bundesland]
- **Rolle Mandant:** [Verantwortlicher / Auftragsverarbeiter / beides]

## Mandatsbeschreibung
[Kurzbeschreibung: Was ist der Auftrag? Welches datenschutzrechtliche Vorhaben?]

## Zuständige Aufsichtsbehörde (Mandant)
[BfDI / LfDI [Bundesland]]

## Ansprechpartner
- **Mandant:** [Name, E-Mail]
- **DSB Mandant:** [Name oder "nicht bestellt"]
- **Kanzlei intern:** [zuständige·r Anwalt/Anwältin]

## Abweichungen vom Kanzlei-Praxisprofil
[Nur aufführen, was beim Mandanten anders ist als im kanzlei-weiten Profil]
- Rechtsgrundlage: [...]
- AVV-Positionen: [...]
- DSFA-Auslöser: [...]

## Systemliste Mandant (für Betroffenenanfragen Art. 15 DSGVO)
- [System 1]
- [System 2]

## Verarbeitungsverzeichnis
[Pfad oder "noch nicht bereitgestellt"]

## Ausgaben dieses Mandats
[Ordnerpfad oder Auflistung erstellter Dokumente]
## Status
offen / abgeschlossen
**Abgeschlossen am:** [Datum]

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

```

## منابع و نقل قول

واجب است `../../references/zitierweise.md`.

- § 43a Abs. 2 BRAO (مکلف وکیل محرمانه)
- § 203 StGB (تخلف از راز خصوصی، محرومیت در حفظ اطلاعات حرفه ای)
- Art. 28, 29 DSGVO (مصرفی از طریق سیستم های خارجی)
- Art. 25 DSGVO (حمايت اطلاعات از طریق طراحی - جداسازی به عنوان TOMs)
- زاک، در: زک/لانس, حقوق وکلا, نسخه دوم 2018, § 43a BRAO Rn. 15 ff. (سرآهنگی حرفه ای)

## قالب خروجی

- تاییدات کوتاه (بدل، تغییر و بسته) به عنوان یک خط پیام وضعیت
- جدول بر اساس دستور العمل
- `mandat.md` به صورت کامل تکمیل شده

## خطرات / اشتباهات معمول

- **ازاد شدن در ماموریت تضمین نشده:** اگر مهارت های بدون مجوز فعال به داده های اختصاصی دسترسی داشته باشند یا از طریق یک مجموعه بین دوره ها جمع آوری شوند، این امر خلاف است § 43a Abs. 2 BRAO و Art. 5 Abs. 1 lit. f DSGVO (امنیت و محرمانه بودن)
- **حذف نهاده های انجام شده:** پوشه ها را حذف نکنید - احتفاظ با پرونده § 50 Abs. 1 BRAO (۶ سال پس از پایان یکسال تقویم که در آن دوره به پایان رسید)
- **منتظرم خود AV است:** اگر متقاضی خودش پردازنده ی شخص ثالث باشد، این فرمان محافظت از داده ها می تواند به سوالات عمودی Sub-AV (Art. 28 Abs. 2 فرض دوم DSGVO) در `mandat.md` به طور واضح اشاره کنید.
- **منتظره فعال به تعویض نرفته:** همیشه پس از تغییر ماموریت، بررسی کنید که هیچ زمینه ای غیرعمدتی برای مأموریت در حال کار نیست. `keins` پس از اتمام مهلت توصیه می شود.

## منابع / بروزرسانی

حالت: 05/2026. در صورت تغییر به نظر می رسد که BRAO (مجبوری برای نگهداری آکتهای § 50 BRAO), StGB § 203 یا DSGVO-تعزیرات فنی

**ملاحظات:**
- `datenschutzrecht/skills/mandantendaten-ki/SKILL.md` - انزوا ماموریت در خدمات هوش مصنوعی
- `datenschutzrecht/skills/avv-pruefung/SKILL.md` - بررسی ویژه ای از AVV

## در حال حاضر (v14.2)

- قضیه: هیچ تصمیمی را از دانش نمونه ای نقل نکنید؛ قبل از انتشار با دادگاه، شکل تصمیم گیری و تاریخ آن ها، نشانه های پرونده یا اظهارات قابل اثبات را توسط منبع رسمی یا آزاد تأیید کنید.

## سه بعدی در آغاز

1. چند نفر در یک زمان فعال هستند؟
2. آیا وظایف مربوط به حقوق حفاظت از داده ها باید در نظر گرفته شود (مقاولین مختلف) ؟
3. آیا در میان مأموریت ها تضاد منافع وجود دارد؟
4. آیا باید از پروفایل های عملی مخصوص ماموریت (مختلف کتابهای بازی AVV) استفاده شود؟

## نماد محصول - وضعیت حوزه کاری ماموریت

** آدرس:** دفتر اداری داخلی - صورت صوتی: ساختار واقعی

```
Mandatsarbeitsbereich-Übersicht [DATUM]
Aktive Arbeitsbereich-IDs:
- [ID_1]: [MANDANT/PROJEKT] | Status: aktiv/geschlossen | Kontext: isoliert
- [ID_2]: [MANDANT/PROJEKT] | Status: aktiv | Kontext: isoliert

Aktuell aktiver Kontext: [ID_X]
Sicherheitshinweis: Kontextleak zwischen Mandaten wurde verhindert.
Letzter Wechsel: [DATUM, UHRZEIT]
```
