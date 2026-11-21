# Agents — Ustoz Shodiyevning AI agentlari

Claude Code uchun plugin: 7 ta agent va 3 ta tezkor buyruq.
Dars materiallari, Telegram/Instagram kontenti va vibe coding loyihalari uchun.

## Istalgan loyihaga o'rnatish

Claude Code chatiga yozing:

```
/plugin marketplace add Asadbek-749/Agents
/plugin install ustoz-agentlar@ustoz-shodiyev
```

Keyin yangi sessiya oching (yoki `/reload-plugins`). Bir marta o'rnatsangiz, shu kompyuterdagi barcha loyihalarda ishlaydi.

**Bulutli sessiya (claude.ai/code) uchun:** har bir yangi sessiyada yuqoridagi 2 qatorni yozing.
Yoki loyihangizga `.claude/settings.json` faylini qo'shing (shu repodagi namunadan nusxa oling) —
shunda plugin o'sha loyihada avtomatik yoqiladi.

## Agentlar

| Agent | Vazifasi |
|---|---|
| `dars-rejachi` | Dars rejasi, topshiriq varaqasi, uyga vazifa (Word + HTML) |
| `taqdimot-ustasi` | Sinf uchun taqdimot (PowerPoint + HTML slaydlar) |
| `excel-mashq` | Excel mashq, javob kaliti, baholash jadvali |
| `test-tuzuvchi` | Test va javob kaliti (PDF + Word) |
| `kontent-muallif` | Telegram post, Reels ssenariy, karusel, haftalik reja |
| `vibe-koder` | Telegram bot, sayt, Office avtomatlashtirish, AI agentlar |
| `tekshiruvchi` | Yakuniy sifat nazorati |

## Buyruqlar

| Buyruq | Misol |
|---|---|
| `/dars` | `/dars Excel VLOOKUP` |
| `/kontent` | `/kontent hafta` yoki `/kontent ChatGPT bilan Excel formulasi` |
| `/loyiha` | `/loyiha o'quvchilar test topshiradigan Telegram bot` |

Agar `/dars` boshqa plugin bilan to'qnashsa, to'liq nomini yozing: `/ustoz-agentlar:dars`.

## Brend
Loyihangizda `brend/brend.md` bo'lsa, agentlar ranglar va shriftni undan oladi. Bo'lmasa, standart brend ishlatiladi.
Namuna: shu repodagi `brend/brend.md`.

## Yangilash
Agentlar o'zgartirilgach: `/plugin update ustoz-agentlar`.
