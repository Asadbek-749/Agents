---
name: ustoz-qoidalari
description: Ustoz Shodiyevning umumiy ish qoidalari — dars materiali, ijtimoiy tarmoq kontenti, Office fayllar yoki vibe coding loyihasi ustida ishlaganda, ayniqsa ustoz-agentlar plugin agentlari (dars-rejachi, taqdimot-ustasi, excel-mashq, test-tuzuvchi, kontent-muallif, vibe-koder, tekshiruvchi) yoki /dars, /kontent, /loyiha buyruqlari ishlatilganda yukla. 2021-yilgi o'zbek lotin alifbosi, avval reja keyin ish tartibi, fayllar joylashuvi va brend qoidalari.
---

# Ustoz Shodiyev — umumiy qoidalar

Bu repo egasi: Asadbek (Ustoz Shodiyev), kompyuter savodxonligi va sun'iy intellekt o'qituvchisi.
Darslar: Word, Excel, PowerPoint, Google vositalari, Canva, AI vositalari.
Auditoriya: o'quvchilar va kattalar (tadbirkorlar, davlat xodimlari), IT bilimi yo'q odamlar.
Agentlardan faqat egasining o'zi foydalanadi.

## Asosiy qoidalar (barcha agentlar uchun)

### 1. Avval reja, keyin ish
Har qanday katta vazifada (dars paketi, kontent, loyiha):
1. Qisqa reja ko'rsat: nima tayyorlanadi, qaysi fayllar, qaysi agentlar ishlaydi.
2. Egasining tasdig'ini kut ("ha", "boshla", yoki tuzatish).
3. Tasdiqdan keyin vazifani tegishli agentlarga bo'lib ber, imkon bo'lsa parallel.
4. Oxirida `tekshiruvchi` agentidan o'tkaz va natijani qisqa hisobot bilan ber.

Kichik savol yoki bitta tuzatish uchun reja shart emas — darhol bajar.

### 2. Til va alifbo
- Barcha materiallar va kontent **2021-yilgi yangi o'zbek lotin alifbosi loyihasida** yoziladi.
  - oʻ → **ó** (Ó), gʻ → **ǵ** (Ǵ), sh → **ş** (Ş), ch → **ç** (Ç)
  - ng o'zgarmaydi, tutuq belgisi ʼ qoladi (maʼlumot, taʼlim)
  - Misollar: Ózbekiston, ǵoya, şahar, çiroyli, óqituvçi, kóçirish, jadvaldaǵi
- Rus tilidagi variant **faqat egasi so'raganda** tayyorlanadi.
- Atamalar (Excel, VLOOKUP, ChatGPT, Canva) asl nomida qoladi.
- Murakkab narsani sodda so'z va hayotiy misol bilan tushuntir.

### 3. Dizayn
- Ranglar va shriftlar: joriy loyihada `brend/brend.md` bo'lsa undan, bo'lmasa standart brend: asosiy #1E3A8A, urg'u #F59E0B, matn #1F2937, och fon #F3F4F6; Montserrat Bold (sarlavha), Inter (matn), zaxira Arial.
- Shrift ó, ǵ, ş, ç harflarini qo'llashi shart (tekshiruvchi buni tekshiradi).

### 4. Fayllar qayerga saqlanadi
- Dars materiallari: `materiallar/<kurs>/<NN-mavzu>/` (masalan `materiallar/excel/05-vlookup/`)
- Ijtimoiy tarmoq: `kontent/<YYYY-MM-DD>-<mavzu>/`
- Kod loyihalari: `loyihalar/<loyiha-nomi>/`
- Fayl nomlari lotin harflarida, bo'sh joysiz: `dars-rejasi.docx`, `taqdimot.pptx`

### 5. Texnologiyalar
- Word: Python `python-docx`
- Excel: Python `openpyxl`
- PowerPoint: Node.js `pptxgenjs`
- PDF: avval HTML yasaladi, keyin Chromium/Playwright orqali PDF ga o'giriladi
- HTML: bitta mustaqil fayl (CSS ichida), telefonda ham chiroyli ko'rinadi
- Yaratish skriptlari fayl yonida `_skript/` papkasida saqlanadi, keyin qayta ishlatish uchun

### 6. Kod qoidalari
Egasi kodni o'zi yozmaydi. Shuning uchun:
- Kod doim to'liq va ishga tayyor bo'lsin, "qolganini o'zing to'ldir" bo'lmasin.
- Qayerga qo'yish va qanday ishga tushirish qadamma-qadam yozilsin.
- Xato bo'lsa, sababi oddiy tilda tushuntirilsin va tuzatilgan to'liq variant berilsin.
- API kalit va tokenlar hech qachon kodga yozilmaydi, faqat `.env` faylga (`.gitignore` da).

## Agentlar jamoasi

| Agent | Vazifasi |
|---|---|
| `dars-rejachi` | Dars rejasi, amaliy topshiriq, uyga vazifa (Word + HTML) |
| `taqdimot-ustasi` | Sinf uchun taqdimot (PowerPoint + HTML slaydlar) |
| `excel-mashq` | Amaliy Excel fayllar, javob kaliti, baholash jadvali |
| `test-tuzuvchi` | Test va tekshirish savollari, javob kaliti (PDF + Word) |
| `kontent-muallif` | Telegram post, Reels ssenariy, karusel, haftalik kontent-reja |
| `vibe-koder` | Telegram bot, sayt, Office avtomatlashtirish, AI agentlar |
| `tekshiruvchi` | Yakuniy sifat nazorati: alifbo, tuzilma, fayllar ochilishi |
| Nargis (`nargis` skill) | Jamoa direktori: agent yaratish, tahrirlash, arxivlash, ishni taqsimlash |

## Tezkor buyruqlar
- `/dars <mavzu>` — to'liq dars paketi
- `/kontent <mavzu yoki hafta>` — ijtimoiy tarmoq kontenti
- `/loyiha <g'oya>` — yangi vibe coding loyiha
- `/nargis <buyruq>` yoki "Nargis, ..." — jamoa direktori (agentlar tarkibi va ishni taqsimlash)
