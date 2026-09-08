# bet-skill

> 18+ only. Education/entertainment only. No strategy guarantees profit. Betting involves risk — only bet where legal and only with money you can afford to lose.

A complete 1xBet betting assistant for AI agents (Hermes + any Agent Skills agent): ALL sports (football, basketball, tennis, cricket, ice hockey, volleyball, MMA, esports), onboarding with YOUR bankroll, staking plans, pre-match/live analysis, daily action lists, bonus pricing, tracking forms, weekly reviews, and weighted expert consensus.

## Install

```bash
# skills.sh standard (Claude Code, Codex, Cursor, Copilot, Hermes, …)
npx skills add vaferkhanom/bet-skill
npx skills add vaferkhanom/bet-skill --skill bet-skill
npx skills add vaferkhanom/bet-skill --list

# Hermes Agent
hermes skills install vaferkhanom/bet-skill/skills/bet-skill
hermes skills tap add vaferkhanom/bet-skill
/skills install vaferkhanom/bet-skill/skills/bet-skill
```

Local test: `npx skills add ./bet-skill --skill bet-skill`.

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
  - `07-multi-sport-playbooks.md` (basketball/tennis/cricket/hockey/volleyball/MMA/esports)
  - `08-bankroll-command-center.md` (Bankroll Cards, drawdown ladder)
  - `09-expert-consensus-sources.md` (source weights, verification rules)
  - `10-forms-library.md` (onboarding, pre-bet, reviews, bonus pricer)
- `skills/bet-skill/templates/` — `onboarding.md`, `pre-bet.md`, `weekly-review.md`
- `skills/bet-skill/scripts/` — `poisson.py`, `devig_kelly.py`, `bankroll_plan.py` (stdlib only).

## Try it

```bash
python -m py_compile skills/bet-skill/scripts/poisson.py skills/bet-skill/scripts/devig_kelly.py skills/bet-skill/scripts/bankroll_plan.py
python skills/bet-skill/scripts/bankroll_plan.py --bankroll 1000 --profile standard
```

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
