# bet-skill

> 18+ only. Education/entertainment only. No strategy guarantees profit. Betting involves risk — only bet where legal and only with money you can afford to lose.

A FULL 1xBet football (soccer) betting skill for AI agents: markets + settlement rules, xG / Poisson / Dixon-Coles / Elo models, value + CLV + Kelly + bankroll, strategies, and the exact websites/tools to use for faster, more accurate match analysis.

## Install

```bash
# skills.sh standard (Claude Code, Codex, Cursor, Copilot, Hermes, …)
npx skills add <owner>/bet-skill
npx skills add <owner>/bet-skill --skill bet-skill
npx skills add <owner>/bet-skill --list

# Hermes Agent
hermes skills install <owner>/bet-skill/skills/bet-skill
hermes skills tap add <owner>/bet-skill
/skills install <owner>/bet-skill/skills/bet-skill
```

Replace `<owner>` with the GitHub owner. Local test: `npx skills add ./bet-skill --skill bet-skill`.

## Layout

- `SKILL.md` — root skill (Agent Skills standard).
- `skills/bet-skill/SKILL.md` — same skill for taps / `--skill` selection.
- `skills/bet-skill/references/` — the FULL guides:
  - `01-1xbet-markets-rules.md`
  - `02-quant-models-xg-poisson-elo.md`
  - `03-strategies-bankroll-psychology.md`
  - `04-websites-toolstack.md`
  - `05-match-analysis-workflow.md`
  - `06-prompts-templates.md`
- `skills/bet-skill/scripts/` — `poisson.py`, `devig_kelly.py` (stdlib only).

## Verify

```bash
python -m py_compile skills/bet-skill/scripts/poisson.py skills/bet-skill/scripts/devig_kelly.py
python skills/bet-skill/scripts/poisson.py --home 2.06 --away 0.86 --rho -0.08
python skills/bet-skill/scripts/devig_kelly.py --odds 1.95,3.60,4.20 --model 0.55
```

## Responsible play

18+. Set deposit/loss/session limits before depositing. Self-exclusion: GAMSTOP (UK), GamCare/BeGambleAware, NCPG 1-800-522-4700 (US). Stop signals: chasing, hiding, borrowing, drunk/stressed betting → stop + seek support.

## License

MIT
