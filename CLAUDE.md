# Agents — Ustoz Shodiyevning plugin manbasi

Bu repo Claude Code plugin marketplace'i. Undagi `ustoz-agentlar` plugin'i istalgan loyihaga o'rnatiladi.

## Tuzilma
- `.claude-plugin/marketplace.json` — marketplace tavsifi
- `plugins/ustoz-agentlar/.claude-plugin/plugin.json` — plugin nomi va versiyasi
- `plugins/ustoz-agentlar/agents/` — 7 ta subagent
- `plugins/ustoz-agentlar/commands/` — /dars, /kontent, /loyiha
- `plugins/ustoz-agentlar/skills/ustoz-qoidalari/SKILL.md` — umumiy qoidalar (alifbo, reja, fayllar, brend)
- `brend/brend.md` — shu repo ichida ishlaganda ishlatiladigan brend (boshqa loyihalarga ham nusxa qilish mumkin)

## Plugin'ni o'zgartirganda
1. Kerakli faylni tahrirla.
2. `plugins/ustoz-agentlar/.claude-plugin/plugin.json` va `.claude-plugin/marketplace.json` dagi `version` ni bir xil oshir (1.0.0 → 1.0.1).
3. Tekshir: `claude plugin validate .` va `claude plugin validate plugins/ustoz-agentlar`.
4. Agent frontmatter'idagi `description` qo'shtirnoq bilan boshlanmasin (YAML xatosi beradi).
5. Commit va push. Foydalanuvchi `/plugin update ustoz-agentlar` bilan yangilaydi.

Umumiy ish qoidalari `ustoz-qoidalari` skill'ida — shu repoda ham ular amal qiladi.
