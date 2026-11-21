# Agent-001

Ustoz Shodiyevning shaxsiy AI agentlar jamoasi (Claude Code subagentlari).
Dars materiallari, ijtimoiy tarmoq kontenti va vibe coding loyihalari uchun.

## Ichida nima bor

```
Agent-001/
├── CLAUDE.md                  ← umumiy qoidalar (barcha agentlar o'qiydi)
├── brend/brend.md             ← ranglar, shriftlar, logotip
├── .claude/
│   ├── agents/                ← 7 ta agent
│   │   ├── dars-rejachi.md
│   │   ├── taqdimot-ustasi.md
│   │   ├── excel-mashq.md
│   │   ├── test-tuzuvchi.md
│   │   ├── kontent-muallif.md
│   │   ├── vibe-koder.md
│   │   └── tekshiruvchi.md
│   └── commands/              ← tezkor buyruqlar
│       ├── dars.md            → /dars
│       ├── kontent.md         → /kontent
│       └── loyiha.md          → /loyiha
├── materiallar/               ← tayyor dars materiallari shu yerga tushadi
├── kontent/                   ← postlar va ssenariylar
└── loyihalar/                 ← kod loyihalari
```

## O'rnatish (bir marta)

1. GitHub'da `Agent-001` repo oching (README bilan).
2. Shu papkadagi barcha fayllarni repoga yuklang:
   - GitHub sahifasida **Add file → Upload files** ni bosing va papkalarni sudrab tashlang.
   - `.claude` papkasi nuqta bilan boshlanadi va ba'zan yashirin turadi. Yuklanganini tekshiring: repoda `.claude/agents/` ko'rinishi kerak.
3. `brend/brend.md` faylini oching va o'z ranglaringizni yozing.
4. Claude Code'da `Agent-001` tanlangan holda yangi sessiya oching.
5. Tekshirish uchun `/agents` deb yozing: 7 ta agent ro'yxatda ko'rinishi kerak.

## Ishlatish

| Nima kerak | Nima yozasiz |
|---|---|
| To'liq dars paketi | `/dars Excel VLOOKUP` |
| Ijtimoiy tarmoq posti | `/kontent ChatGPT bilan Excel formulasi yozish` |
| Haftalik kontent-reja | `/kontent hafta` |
| Yangi bot yoki sayt | `/loyiha o'quvchilar test topshiradigan Telegram bot` |
| Bitta agentni chaqirish | `test-tuzuvchi agenti bilan Word bo'yicha 20 ta savol tuz` |

Har bir katta ishda Claude avval qisqa reja ko'rsatadi. "Ha" yoki "boshla" deb yozsangiz, ishni boshlaydi. Rejani o'zgartirmoqchi bo'lsangiz, oddiy so'z bilan yozing.

## Agentni o'zgartirish
Agent fayli oddiy matn. Masalan, testlar 15 emas, 20 ta savoldan iborat bo'lishini xohlasangiz, `.claude/agents/test-tuzuvchi.md` ni oching va raqamni o'zgartiring. Yoki Claude'ga ayting: "test-tuzuvchi agentida standart savollar sonini 20 qil".
