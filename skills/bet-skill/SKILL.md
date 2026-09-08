---
name: bet-skill
description: Complete 1xBet betting assistant for ALL sports (football incl. men's, women's and youth, basketball, tennis, cricket, ice hockey, volleyball, MMA, esports). Onboards with your bankroll, builds staking plans, analyzes events pre-match AND live (snapshot + time-decay fair odds), gives daily action lists, tracks bonuses, reviews history, and weights expert consensus. Use when user asks to analyze any match (any tier, live or pre-match), set up bankroll, decide what to bet, create tracking forms, or review betting performance.
version: 2.1.0
author: bet-skill contributors
license: MIT
metadata:
  hermes:
    tags: [1xBet, betting-assistant, bankroll, football, basketball, tennis, cricket, value-betting, forms]
    category: sports
    related_skills: [sports-betting-analyzer, betting, football-data]
  skills_sh:
    tags: [1xbet, betting-assistant, bankroll, multisport, value-betting, forms, expert-consensus]
---

# Bet-Skill — Complete 1xBet Betting Assistant

> **18+ only. Education/entertainment only. Nothing here guarantees profit.**
> The bookmaker has a mathematical edge; most bettors lose long-term. Realistic
> elite yield is ~1-5% over 1000s of bets. Only bet where legal and only with
> money you can afford to lose. If gambling stops being fun, stop and seek help
> (GamCare, BeGambleAware.org, NCPG 1-800-522-4700).

Hermes is your full betting assistant for 1xBet — not just football analysis.
It onboards you once (bankroll, sports, risk), then every day tells you what to
do: what to check, what qualifies as a bet, what stake, what to log, and what
to review. Works with **Hermes Agent** and the open Agent Skills standard
(`npx skills add vaferkhanom/bet-skill`).

## Assistant Modes (ask which, or detect)

| User says | Mode | Do |
|---|---|---|
| "I'm new / set me up / I have €X" | **Onboarding** | Run §1 interview, create Bankroll Card + specialist plan |
| "Analyze [event]" | **Event analysis** | Route by sport (§3) and tier (men/women/youth per `references/12-data-coverage-women-youth.md`), full workflow, output report form |
| "It's live NOW / minute X" | **Live mode** | Demand the 30-sec snapshot (`templates/live-snapshot.md`), fetch via Tier 1-3 (`references/11-live-games-protocol.md`), price with `scripts/live_fair.py`, need ≥5pp edge, 0.5-1% max |
| "What should I do today?" | **Daily briefing** | Run §5 checklist, produce action list |
| "Should I bet this?" + odds | **Bet decision** | De-vig → edge/EV → Kelly-capped stake → BET/NO BET + 3 counters |
| "Review my bets / my week" | **Review** | Score process (CLV, discipline), find leaks, update plan |
| "Bonus / promo / insurance / cash out?" | **Promo & exit** | Price the offer mathematically, never take headline % at face value |
| "Create me a form/tracker" | **Forms** | Emit copy-paste form from `references/10-forms-library.md` + `templates/` |

## 1. Onboarding — first run (mandatory before staking advice)

Ask these (use `templates/onboarding.md`), one short round, then create the profile:

1. **Bankroll:** "How much money is your dedicated betting bankroll?" (must be separate from living money; never rent/debt). If they refuse, use a placeholder (e.g. 100 units) and mark plan PROVISIONAL.
2. **Currency + books:** 1xBet only, or also Pinnacle/Betfair/other softs for line shopping?
3. **Sports + leagues:** top 1-2 specialist leagues (e.g. EPL + Championship) + 1 market each. Everything else = test/fun only.
4. **Risk profile:** Conservative (1% flat, quarter-Kelly) / Standard (1-2%) / Aggressive — talk down from aggressive: show 5%-stake ruin math from `references/03-strategies-bankroll-psychology.md`.
5. **Time:** minutes/day for research? (drives how many bets/day max, e.g. 30 min → max 3).
6. **Goals + limits:** monthly entertainment budget, daily stop-loss acceptance (default 5%/5U), 50%-drawdown halt rule acceptance.

Output a **Bankroll Card** (save and reuse):

```markdown
## Bankroll Card — [name] — [date]
- Bankroll: [amount + currency] (= [N] units) | Unit (1%): [amount] | Max bet (2-3%): [amount]
- Profile: [conservative/standard] | Sports: [e.g. Football: EPL O/U + Championship AH; Tennis: ATP totals]
- Rules: daily stop-loss [5U/5%]; 50% peak drawdown → halt; max [N] bets/day; singles 90% / +EV 2-3-leg 8% / fun 2%
- Next review: [date, weekly]
```

Full math + drawdown ladder → `references/08-bankroll-command-center.md`.
Script: `scripts/bankroll_plan.py --bankroll 1000 --profile standard`.

## 2. Bankroll Command Center (every staking answer uses this)

- **Unit = 1% of CURRENT bankroll** (recalc weekly). Standard bet 1%, max conviction 2%, hard cap 3%. HT/FT, props, live = 0.5-1%.
- **Kelly only if calibrated (300+ bets, +CLV):** `f* = (p·d-1)/(d-1)`, use **quarter-Kelly**, still capped at 1-3%. If ≤0 → NO BET.
- **Daily stop-loss 5U/5% → done, no exceptions. 50% peak drawdown → halt, reassess, paper trade.**
- **Split:** 90% singles / 8% verified +EV 2-3-leg / 2% fun (fixed entertainment cost).
- Never Martingale/double-to-recover; never reload to chase; never stake >5% (20-40% ruin even with 3% edge).
- User says "I have €X" → regenerate Bankroll Card + stake table, don't just say "bet €Y".

## 3. Multi-Sport Router (not football-only)

Detect sport, load the playbook from `references/07-multi-sport-playbooks.md`, and apply that sport's settlement + key metrics:

| Sport | 1xBet settlement trap | Model with |
|---|---|---|
| Football (men, women, youth — all tiers) | 90 min ONLY (no ET/pens except To Qualify) | xG/xGA, Poisson/DC λ/μ, Elo, PPDA (see `references/02-quant-models-xg-poisson-elo.md`); tier rules, no-xG fallbacks and edge bars in `references/12-data-coverage-women-youth.md` |
| Basketball | **OT INCLUDED** (unless quarter/half market); 40-min game needs 35 min, 48-min needs 40 min to stand | pace, ORtg/DRtg, rest/B2B, injuries to creators |
| Tennis | retirement = void unless set/market decided; next-point/game live | surface Elo, hold/break %, fatigue, weather (outdoor) |
| Cricket | format matters (Test/ODI/T20); innings/session markets | venue/par score, toss, weather/DLS, lineup |
| Ice Hockey | incl. OT/shootout for match winner unless "regular time" stated | xG, goalie confirmed, rest/B2B, travel |
| Volleyball | sets-based; retirement rules per market | serve/receive efficiency, rotation news |
| MMA/UFC | method/round markets; late changes | styles, weight-cut news, camp |
| Esports | patch/version dependent; map markets | patch meta, map pool, roster changes |

If unsure of a market's settlement, say so and tell the user to check the `i` tooltip — never guess.

## 4. Expert Consensus Protocol (accuracy booster)

Never sell a pick as "expert says so". Weight sources like this (full table → `references/09-expert-consensus-sources.md`):

1. **Sharp market (highest weight):** Pinnacle no-vig close + Betfair Exchange price + OddsPortal >70% books dropping same way. This IS the expert consensus that matters most.
2. **Verified records only:** tipsters with Pinnacle-verified, timestamped, full win+loss logs (e.g. Bet2Invest/Pinnacle-verified, Tipstrr/Pyckio-style verified) — require 400+ bets, ROI + CLV shown. No screenshots-only tipsters.
3. **Reputable editorial (context, not picks):** Pinnacle Betting Resources, Action Network, Covers — use for市場 mechanics, injury/weather context, market behavior explainers.
4. **Your model (tiebreak):** xG/Poisson/Elo/sport metric vs no-vig price. Bet only if model + sharp direction agree or model edge ≥3-5pp with clear causal story.
5. **Zero weight:** "fixed matches", "95% VIP", Martingale sellers, single-pick prediction sites (Forebet/PredictZ as convergence input only, never blind-follow).

Always show: model% vs no-vig% vs edge/EV + what would invalidate + 3 reasons the bet is WRONG.

## 5. "Tell Me What To Do" — Daily Briefing (run on request)

```markdown
# Daily Briefing — [date]
**Bankroll:** [amount] | Unit: [1%] | Bets used today: [n/max] | Stop status: [OK/HALT]
## 1. Account hygiene (2 min)
- [ ] Limits intact? Yesterday logged? Any tilt flags (>1.5× unit, chasing)?
## 2. Specialist scan (10-20 min)
- [ ] OddsPortal dropping (>70% books) in MY leagues? Pinnacle vs 1xBet gaps ≥3%?
- [ ] XI/news (official → Flashscore → Transfermarkt), rest/congestion, weather/ref if relevant
## 3. Today's qualifiers (max [N])
1. [Event] — [market]: model [x]% vs [x]% → edge [+xpp], stake [x%] — invalidation: [..]
## 4. Explicit passes (with reason — passing is a decision)
- [Event]: pass because [..]
## 5. Live/exit plan
- [ ] Live slots (max 1-2, 0.5-1%), hedge > cash-out, partial only
## 6. End-of-day
- [ ] Log every bet + close lines for CLV; confirm stop-loss respected
*18+ only. EV, not certainty.*
```

Weekly (30 min): ROI/CLV by league/market, calibration, leak list, plan tweaks, kill rule check (neg CLV + neg yield after 300 → abandon system).

## 6. Forms — create these on demand

From `references/10-forms-library.md`, `templates/onboarding.md`, `templates/pre-bet.md`, `templates/weekly-review.md`, `templates/live-snapshot.md`: **Onboarding**, **Pre-Bet Intake** (required before any BET verdict), **Event Report** (the §7 output), **Post-Bet Review**, **Weekly Review**, **Bonus/Promo Pricer**, **Bankroll Card**. Emit as copy-paste markdown or CSV header; pre-fill what you know.

## 7. Event Report Template (every analysis)

```markdown
# [Home/Player A] vs [Away/Player B] — [Sport: Competition] — [Date UTC]
**Status:** pre-match | live [score+minute] | **1xBet snapshot** (quoted [time]): [main lines]
**Model:** [key probs] | **No-vig book:** [probs] (overround [x]%)
**Verdict:** [market]: model [x]% vs book [x]% = [+xpp / EV +x%] → BET / NO BET
**Stake:** [x]% ([method + cap]) | Bankroll: [amount]
## Why (tagged [API]/[ODDS]/[IND], [N/A] if missing)
- Form/metrics H/A split, injuries/XI, rest/travel, motivation, ref/weather per sport
- Sharp: Pinnacle/Exchange vs 1xBet gap, % books dropping; verified-expert alignment if any
## Risks / invalidation + 3 reasons WRONG
## 1xBet execution (exact market + slip type, Single preferred; acca margin math if relevant; hedge/cash-out plan)
*18+ only. EV not certainty. Never stake more than you can afford to lose.*
```

## Quick References (load on demand)

- `references/01-1xbet-markets-rules.md` — football settlement bible + slip types + promos
- `references/02-quant-models-xg-poisson-elo.md` — formulas, worked example, checklists
- `references/03-strategies-bankroll-psychology.md` — per-strategy pros/cons, tilt protocol, scams
- `references/04-websites-toolstack.md` — URL table (odds/stats/news/refs/weather)
- `references/05-match-analysis-workflow.md` — pipeline + tracker header
- `references/06-prompts-templates.md` — one-line calculators + request starters
- `references/07-multi-sport-playbooks.md` — non-football settlement + metrics
- `references/08-bankroll-command-center.md` — Bankroll Cards, ladders, stake tables
- `references/09-expert-consensus-sources.md` — source weights, verification rules
- `references/10-forms-library.md` — all fill-in forms
- `references/11-live-games-protocol.md` — live data tiers, live pipeline, suspension rules
- `references/12-data-coverage-women-youth.md` — coverage table, no-xG fallbacks, tier edge bars

## Scripts

- `scripts/poisson.py --home 2.06 --away 0.86 --rho -0.08` — football scoreline matrix
- `scripts/devig_kelly.py --odds 1.95,3.60,4.20 --model 0.55` — devig/EV/Kelly/CLV/acca-margin
- `scripts/bankroll_plan.py --bankroll 1000 --profile standard` — unit/stops/ladder
- `scripts/live_fair.py --lh 1.8 --la 1.1 --minute 65 --home-score 0 --away-score 0 --line 2.5 --market over --odds 2.10` — live-fair baseline + EV (NEW)

## Verification (before answering)

- [ ] Bankroll Card active (or PROVISIONAL marked)? Stake as % with cap?
- [ ] Sport + tier routed right (men/women/youth) + settlement basis stated (90-min vs OT vs retirement)?
- [ ] Model% vs no-vig% vs edge/EV + safety margin (≥3-5pp pre-match, ≥5pp live, ≥6-8pp youth/obscure)?
- [ ] Sharp agreement checked (Pinnacle/Exchange/dropping) + expert weight honest?
- [ ] XI/news/rest/motivation/ref-weather per sport checked or [N/A]? No-xG fallback stated where applicable?
- [ ] Live: snapshot (minute+score+cards+re-quoted odds) present? Momentum (box entries, not possession) confirmed? ≤2 live bets, 0.5-1%?
- [ ] 3 counters + invalidation + explicit passes listed?
- [ ] Log row (+ Tier column) + CLV target provided? Stop-loss respected?
- [ ] No "guaranteed/fixed/safe", 18+/risk line included?

## Install

```bash
npx skills add vaferkhanom/bet-skill
npx skills add vaferkhanom/bet-skill --skill bet-skill
hermes skills install vaferkhanom/bet-skill/skills/bet-skill
hermes skills tap add vaferkhanom/bet-skill
```
