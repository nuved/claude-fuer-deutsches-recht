---
name: vertragsverlaengerungs-monitor
description: "Wenn es um Verlängerungstracker in Vertragsrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# کششگر تمدید

## سه بعدی در آغاز

1. آیا این دفتر ثبت زمان کامل است (همه قراردادهای فعال با پایان و مدت انقضا) ؟
2. آیا پپرهای پستال به درستی ثبت شده اند (در صورت نامه: 3 روز؛ بصورت الکترونیکی: 0 روز) ؟
3. آیا قراردادها که به شقۀ تمدید آن ها بستگی دارد § 309 Nr. 9 BGB (B2C) یا § 307 BGB (B2B) ممکن است غیرفعال باشد؟
4. کدام تعطیلات فدرال برای محاسبه زمان مناسب هستند؟

## رویهٔ قضایی روز

- قضیه: هیچ تصمیمی را از دانش نمونه ای نقل نکنید؛ قبل از انتشار با دادگاه، شکل تصمیم گیری و تاریخ آن ها، نشانه های پرونده یا اظهارات قابل اثبات را توسط منبع رسمی یا آزاد تأیید کنید.

## قوانین محوری

- § 309 Nr. 9 BGB - بند های زمان B2C: مدت شروع تا 2 سال؛ تمدید تا 1 سال، پایان نامه تا 3 ماه
- § 307 BGB - کنترل محتوا B2B: روابط طولانی
- § 130 BGB - دسترسی به وصایات ارضی (زمان شروع از درخواست تخفیف)
- § 126 BGB - شکل نامه (توقيع اصلی لازم است؛ ایمیل کافی نیست)
- § 126b BGB - شکل متن (میل، PDF)

## ورودی‌ها

- ثبت `~/.claude/plugins/config/claude-fuer-deutsches-recht/vertragsrecht/renewal-register.yaml`
- اختیاری: `--tage N` تغییر در پنجره مشاهده (بعد از 90 روز)
- اختیاری: `--verpasst` برای زمان های گذشته بدون اطلاع رسانی

## زمان

### مرحله ی اول: خواندن فهرست

`~/.claude/plugins/config/claude-fuer-deutsches-recht/vertragsrecht/renewal-register.yaml` در صورت خالی و CLM متصل، حالت سوم (اولین واردات از CLM) را ارائه دهید.

### مرحله دوم: حالت استاندارد - چه چیزی در 90 روز اجرا می شود؟

فاصله های نیمه باز (هر روز رادای مدّی به یک دسته خاص تعلق دارد):

| وپیک | دوره | اهمیت |
|---|---|---|
| 🔴 | 0 تا 13 روز | نیاز به اقدام فوری |
| 🟠 | 14 تا 44 روز | فوری - برنامه ریزی این هفته |
| 🟡 | 45 تا 89 روز | در اون پرده |

** توجه - تاریخ ارسال، نه زمان دریافت:** اگر اعلام نامه به صورت نوشتاری یا ثبت نام نیاز داشته باشد ، باید از طریق پست حساب شود. `sende_bis_effektiv` برای هشدارها، نه `kündigen_bis_effektiv`.

### مرحله سوم: `--verpasst`-مود

نوشته های مربوط به `status: aktiv` این گزارش ها در مورد `kündigen_bis_effektiv` در گذشته است و هیچ `status: gekündigt` این گزارش در مورد پیامدهای زمان غفلت توضیح می دهد:
- در B2C: § 309 Nr. 9 BGB در مورد این موضوع، آیا برآورد می شود که شروط تمدید به طور کلی موثر بوده است؟
- در B2B: § 307 BGB بررسی
- قضیه: هیچ تصمیمی را از دانش نمونه ای نقل نکنید؛ قبل از انتشار با دادگاه، شکل تصمیم گیری و تاریخ آن ها، نشانه های پرونده یا اظهارات قابل اثبات را توسط منبع رسمی یا آزاد تأیید کنید.

## دفترچه

زیر `~/.claude/plugins/config/claude-fuer-deutsches-recht/vertragsrecht/renewal-register.yaml`هر بار:

```yaml
- vertragspartner: "Acme Software GmbH"
 vertrag: "Acme Plattform-Abonnementvertrag"
 unterzeichnungsdatum: 2025-06-15
 erstlaufzeit_ende: 2026-06-15
 aktuelle_laufzeit_ende: 2026-06-15 # rollt nach jeder Verlängerung vor
 verlaengerungsmechanismus: "automatisch jährlich"
 kuendigungsfrist_tage: 90
 kuendigungsform: "schriftlich" # e-mail / schriftlich / einschreiben / portal / § X Vertrag
 postlauf_puffer_tage: 3 # 0 für elektronisch; 3 für Einschreiben; 10 für internationalen Post
 kuendigen_bis_kalender: 2026-03-17
 kuendigen_bis_effektiv: 2026-03-17 # ggf. auf letzten Werktag vorgezogen
 sende_bis_effektiv: 2026-03-14 # kündigen_bis_effektiv minus postlauf_puffer_tage
 vorzieh_hinweis: "" # z. B. "vorgezogen von Sonntag 2026-03-15; Werktags-Definition im Vertrag prüfen"
 kuendigen_bis_provenienz: "[Modellberechnung – gegen Kündigungsklausel prüfen]"
 preis_bei_verlaengerung: "jeweils aktueller Listenpreis (unbegrenzt)"
 jahreswert: 48000
 verantwortlich: "max.mustermann@firma.de"
 clm_id: "IC-12345"
 docusign_umschlag: "abc-123"
 status: "aktiv" # aktiv | gekündigt | verlängert | versäumt
 notizen: "Preis unbegrenzt – vor Verlängerung Alternativen prüfen: X, Y."
 bgb_309_9_pruefung: "B2B – § 307 BGB prüfen; nicht direkt anwendbar"
```

## 🔴 نیاز به اقدام فوری (0-13 روز تا زمان ارسال)

| شرکای قرارداد | قرارداد | ارسال به | از این کار تا | قیمت در صورت تمدید | مسئول |
|---|---|---|---|---|---|
| [Name] | [Vertrag] | **[Datum]** | [Datum] | [Mechanismus] | [E-Mail] |

> ️ شکل استعفا را یاد بگیرید: [schriftlich/einschreiben/e-mail] - پستگوشی [N] روزها بشمار.

---

## فوری (14 تا 44 روز)

[gleiche Tabelle]

---

## روی صفحه نمایش (۴۵ تا ۸۹ روز)

[gleiche Tabelle]

---

## یادداشت‌ها

[Einträge mit unbegrenztem Preis, Einträge ohne Verantwortlichen, verpasste Fristen im Beobachtungsfenster]

---

## § 309 Nr. 9 BGB / § 307 BGB اشاره

[Einträge, bei denen die Verlängerungsklausel auf Wirksamkeit zu prüfen ist]
```

## Fristenberechnung

**Beispiel:** Kündigungsfrist 90 Tage, Schriftform + Einschreiben (3 Tage Postlauf), Laufzeitende 15.06.2026:
- `kündigen_bis_kalender` = 17.03.2026
- `kündigen_bis_effektiv` = 17.03.2026 (kein Wochenende)
- `sende_bis_effektiv` = 14.03.2026

**Werktags-Regel:** Fällt `kündigen_bis` auf Samstag/Sonntag oder gesetzlichen Feiertag, auf den letzten Werktag davor vorziehen. Feiertage sind bundeslandabhängig – Bundesland des zuständigen Büros oder des Vertragsgerichtsstandsorts prüfen.

## Quellen und Zitierweise

Zitierweise nach `../references/zitierweise.md`.

Normen und Rspr.:
- § 309 Nr. 9 BGB – Laufzeit B2C; automatische Verlängerung max. 1 Jahr; Kündigungsfrist max. 3 Monate
- § 307 BGB – Inhaltskontrolle B2B; unangemessen lange Bindungen
- § 308 Nr. 3 BGB – Vorauszahlungsklauseln
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Kommentare:
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Risiken / typische Fehler

- **Postlauf nicht eingerechnet:** Eine Kündigung, die am letzten Fristtag abgeschickt wird, aber per Einschreiben zugestellt werden muss, kommt zu spät.
- **§ 309 Nr. 9 BGB-Unwirksamkeit nicht geprüft:** Wenn der Vertrag B2C ist und die Verlängerungsklausel gegen § 309 Nr. 9 BGB verstößt, kann die Verlängerung unwirksam sein – aber man muss es wissen.
- **Bundesland-Feiertage:** Feiertage variieren zwischen Bundesländern; pauschal "Montag bis Freitag" reicht nicht.
- **Register-Lücken:** Verträge, die vor Plugin-Einrichtung unterzeichnet wurden, sind nicht im Register – einmaliger Erst-Import erforderlich.
