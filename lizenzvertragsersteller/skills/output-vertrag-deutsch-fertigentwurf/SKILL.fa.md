---
name: output-vertrag-deutsch-fertigentwurf
description: "Wenn es um Output: Lizenzvertrag in deutscher Sprache in Lizenzvertragsersteller geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten."
---

> <div dir="rtl">
>
> **ترجمهٔ فارسی (لایهٔ افزوده) — نسخهٔ آلمانی معتبر و ملاک است.**
> این متن ترجمهٔ ماشینیِ کمکی و صرفاً برای **جهت‌یابی** است، نه ترجمهٔ رسمی و نه مشاورهٔ حقوقی. اصطلاح‌های حقوقی، شمارهٔ مادّه‌ها (مثل «§ 305 BGB»)، نام دادگاه‌ها و شمارهٔ پرونده‌ها **عیناً به آلمانی** نگه داشته شده‌اند؛ بخش‌هایی که مطمئن ترجمه نشده‌اند به آلمانی می‌مانند. **خروجیِ کارِ این اسکیل باید به زبان آلمانی تولید شود.** متن اصلی و معتبر: [`SKILL.md`](./SKILL.md).
>
> </div>

# محصول: قرارداد مجوز در زبان آلمانی

## روند کار

1. جمع آوری اطلاعات درآمدی (حزب ها، IP، مدل مزد و انتخاب حقوق) - Skills A-D را ببینید.
2. هر فصل مهارت ساختمانی مناسب را انتخاب کنید.
3. قرارداد را از زیر جمع آوری کنید.
4. از مهارت های مربوطه به سیستم A-E استفاده کنید.
5. با خود تست (در پایین)

## در حال انجام کار

```
[Briefkopf Lizenzgeber / Lizenznehmer]

LIZENZVERTRAG ueber [IP-Typ]

zwischen

[Lizenzgeber], [Anschrift], vertreten durch [Vertreter]
- "Lizenzgeber" -

und

[Lizenznehmer], [Anschrift], vertreten durch [Vertreter]
- "Lizenznehmer" -

- gemeinsam "Parteien" -

PRAEAMBEL

(1) Der Lizenzgeber ist [allein/Mit-]inhaber der in Anlage A bezeichneten
    [Patente, Marken, Designs, Software, Know-how].
(2) Der Lizenznehmer beabsichtigt, [Beschreibung Geschaeftsmodell] und
    sucht hierfuer eine [Patent-, Marken-, Software-, Know-how-]Lizenz.
(3) Die Parteien haben am [Datum] eine Vertraulichkeitsvereinbarung
    geschlossen und Due Diligence durchgefuehrt.

Dies vorausgeschickt vereinbaren die Parteien:

$ 1 Definitionen
$ 2 Lizenzgegenstand                  -> Baustein 12
$ 3 Lizenzumfang                       -> Baustein 13
$ 4 Exklusivitaet                      -> Baustein 14
$ 5 Verguetung                         -> Baustein 15
$ 6 Sublizenzen                        -> Baustein 17
$ 7 Verbesserungen / Grant-Back        -> Baustein 18
$ 8 Garantien                          -> Baustein 19
$ 9 Haftungsbeschraenkungen            -> Baustein 19
$ 10 Mindestlizenz, Meldungen, Audit  -> Baustein 16
$ 11 Vertragsdauer                     -> Baustein 21
$ 12 Folgen der Vertragsbeendigung    -> Baustein 21
$ 13 Vertraulichkeit                   -> Baustein NDA
$ 14 Source-Code-Escrow (bei SW)       -> Baustein 22
$ 15 Rechtswahl und Streitbeilegung   -> Baustein 20
$ 16 Insolvenzfestigkeit               -> Baustein 23
$ 17 Exportkontrolle                   -> Baustein Compliance
$ 18 Datenschutz                       -> Baustein Compliance
$ 19 Steuern                           -> Baustein Compliance
$ 20 Schlussbestimmungen
    (1) Salvatorische Klausel
    (2) Schriftformerfordernis fuer Aenderungen (Textform mit ausdruecklichem
        Bezug)
    (3) Abtretungsverbot
    (4) Aufrechnungsverbot ausser unstreitiger oder rechtskraeftig festgestellter
        Gegenforderungen
    (5) Gesamtvertragsabrede ("Entire Agreement")
    (6) Anwendbares Recht / Schiedsklausel siehe $ 15

[Ort], den [Datum]

___________________________      ___________________________
Lizenzgeber                       Lizenznehmer

ANLAGEN
- Anlage A: IP-Liste (Lizenzgegenstand) -> Baustein 12
- Anlage B: Anwendungsfelder              -> Baustein 13
- Anlage C: Verguetungsmodell + Reporting -> Baustein 15+16
- Anlage D: AVV (DSGVO)                    -> Baustein DSGVO
- Anlage E: Sub-Lizenznehmer-Liste (falls)
```

## روال چک قبل از امضا

| نقطه آزمایش | بررسی |
|---|---|
| طرف ها | اطلاعات مربوط به منابع انسانی در حال حاضر؟ |
| آگهی A | تمام قوانین IPNr. زنده تایید شده؟ |
| پاداش | آیا میزان پرداخت مالیات تعریف شده است؟ |
| انتخاب حقوق | شق قضایی رو درک میکنی؟ |
| ورشکستگی | پس، گروگانگري؟ |
| تعمیل | DSGVO-آفوا امضا شده؟ |
| آگهی های A تا E | همه همراهی؟ |

## اتصال

- نسخه انگلیسی: `output-vertrag-englisch-fertigentwurf`
- دو زبان: `output-zweisprachig-bilingual-deutsch-englisch`
