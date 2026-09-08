---
name: bet-skill
description: 1xBet football (soccer) betting analyst for pre-match and live. Covers 1xBet markets/rules/settlement, xG/Poisson/Dixon-Coles/Elo modeling, value/CLV/Kelly/bankroll, strategies (O-U/BTTS/AH/DNB/late-goals), odds comparison and stats websites. Use when user asks to analyze a football match, find value bets, explain 1xBet markets, build a staking plan, or review betting strategy.
version: 1.0.0
author: bet-skill contributors
license: MIT
metadata:
  hermes:
    tags: [1xBet, football, soccer, betting, xG, Poisson, value-betting, bankroll, odds]
    category: sports
    related_skills: [sports-betting-analyzer, betting, football-data]
  skills_sh:
    tags: [1xbet, football, soccer, betting, xg, poisson, bankroll, odds-comparison]
---

# Bet-Skill — 1xBet Football Betting Analyst

> **18+ only. Education/entertainment only. No strategy guarantees profit.**
> Betting involves financial risk and the bookmaker has a mathematical edge.
> Only bet where legal and only with money you can afford to lose.
> If gambling stops being fun, stop and seek help (GamCare, BeGambleAware.org, NCPG 1-800-522-4700).

This skill teaches an agent everything needed to analyze football matches for
1xBet accurately: markets + settlement, quantitative models, strategies +
bankroll, and which websites/tools to use at each step.

It works with **Hermes Agent** (`hermes skills install`, tap, slash command)
and with the open Agent Skills standard (`npx skills add <owner>/bet-skill`).

## When to Use / When Not to Use

**Use when the user asks to:**
- analyze a specific football match for 1xBet (pre-match or live)
- explain any 1xBet market, rule, settlement, bet-slip type, cash-out, insurance, bonus
- find value (`model prob vs book prob`), compute EV / CLV / Kelly / stake size
- choose a strategy (Over/Under, BTTS, Asian Handicap, DNB, Double Chance, HT/FT, late goals, contrarian, league specialization)
- pick which stats/odds/news sites to check and what to pull from each
- review a bet history, bankroll plan, or tilt/psychology problem

**Do NOT use as:**
- a guarantee, fixed match, or "sure win" — never promise outcomes
- financial advice — always frame as probabilistic education
- a live-odds fetcher — this skill computes and reasons; fetch odds/lineups from the web or user-provided data, then analyze
- a bypass for legality — if 1xBet is blocked in the user's country, say so and stop

**Language rules (mandatory):**
- Probabilistic only: "suggests", "leans", "signal", "≈55% model vs 48% implied".
- Never: "will win", "fixed", "safe", "guaranteed".
- Always show: model prob, book implied prob (no-vig), edge/EV, and stake as % of bankroll.
- Always end high-stakes answers with the 18+/risk disclaimer in one line.

## Quick Start — 8-Step Match Workflow

For any `Home vs Away` request, follow this order. Load the reference file
shown at each step for full detail.

1. **Identify match + markets available** → `references/01-1xbet-markets-rules.md`
   - Confirm competition, date/time, 1xBet market names present.
   - Default settlement = **90 min + stoppage only**. ET/penalties count ONLY for
     `To Qualify / ET / Shootout` markets. Never confuse 1X2 with To Qualify.
2. **Collect data from toolstack** → `references/04-websites-toolstack.md`
   - Odds: OddsPortal / BetExplorer / Oddspedia (opening vs current, % drop, best price).
   - xG/form: FBref + Understat (last 8-10, home/away split), FootyStats (BTTS/O-U/corners/cards %).
   - News: official club XI 60-75 min before KO → Flashscore predicted XI → Transfermarkt / MissesNextMatch / RotoWire pressers.
   - Cards/props: FootyMetrics refs + Statz.ai. Totals/weather: Windy/AccuWeather 2-3h pre-KO.
   - Never bet on the 1xBet `Probability of Winning` widget alone — it is margin-included implied prob.
3. **Build model probability** → `references/02-quant-models-xg-poisson-elo.md`
   - Rolling xGF/xGA (home/away split, opp-adjusted), xGD, SoT/box rates, PPDA, momentum.
   - Poisson / Dixon-Coles `λ/μ` → full 1X2 + O/U matrix. Elo + rest/congestion + motivation + XI adjustment.
   - Scripts: `scripts/poisson.py` (scoreline matrix), `scripts/devig_kelly.py` (devig/EV/Kelly/CLV).
4. **De-vig the book + compute edge** → `references/02-quant-models-xg-poisson-elo.md`
   - `implied = 1 / decimal_odds`, `no_vig_p = implied / sum(implied)`, `fair = 1 / no_vig_p`
   - `EV = p_model * odds - 1`. Bet only if `edge ≥ +3-5pp` AND EV > 0 with margin of safety.
5. **Pick market + strategy fit** → `references/03-strategies-bankroll-psychology.md`
   - Prefer singles in ONE specialist league + ONE market (e.g. Championship O/U or AH).
   - Singles > accas (acca margin = `1.05^n - 1`). Max 2-3 legs only if EVERY leg independently +EV.
   - AH +0.5 vs X2, AH 0.0 vs DNB — take the better price. Check correlation (Over + BTTS ≈ +0.65).
6. **Size the stake** → `references/03-strategies-bankroll-psychology.md`
   - Default: **1% flat** (2% max conviction), 0.5-1% for HT/FT and live.
   - Kelly only if calibrated (300+ bets): `f* = (b*p - q)/b`, use **quarter-Kelly capped at 1-3%**.
   - Daily stop-loss 5 units / 5% bankroll. 50% drawdown from peak → halt and reassess.
7. **Time the bet**
   - Bet early if clear misprice + low rotation risk; else wait for confirmed XI.
   - Live: max 1-2 positions, 0.5-1%. Manual hedge at another book beats Cash-Out (cash-out margin 2-12%).
8. **Log + verify CLV** → `references/05-match-analysis-workflow.md`
   - Log: date, league, match, market, pick, model %, odds taken, closing no-vig, CLV%, stake, result, notes + counter-argument.
   - CLV (devigged) +1-3pp solid, +3pp elite over 300+ bets. Profit is lagging; CLV is leading.

## 1xBet Essentials (memorize)

- **Result markets (1X2, Double Chance, DNB/AH 0.0, Exact Score, HT/FT, BTTS, Totals, Corners, Cards, Scorers):** 90 min only.
- **AH:** whole = push possible (`-1.0` refunds on 1-goal win); half = win/lose; quarter (`-0.75`, `+1.75`) = split stake across two halves.
- **European Handicap:** 3-way, exact margin only, no push.
- **2UP (1X2 2UP):** must select explicitly — 2-goal lead settles early. Standard 1X2 has NO early payout.
- **Corners:** must be TAKEN. **Cards:** Yellow=1/10pts, straight Red or 2nd Yellow→Red=2/25pts, one player max 3 cards/35pts. Bench/manager/post-match cards void.
- **Scorers:** own goals count for score/totals but NOT for scorer markets. DNP = void (1.00).
- **Postponed pre-match >48h = void. Live interrupted + no resume within 5h = void** unless outcome already decided (e.g. Over 0.5 after a goal stands).
- **Acca rule:** all legs must win; void leg = 1.00 and acca continues. Same-match correlated legs get stripped — use Constructor/Bet Builder instead.
- **Slip types:** Single, Accumulator, System, Chain, Patent/Lucky, Multibet, Conditional, Anti-Accumulator, Constructor, Advancebet (credit vs unsettled bets ≤48h), Promo Code, Cash-Out/Bet Slip Sale (full/partial, Singles/Accas/Systems only). Max return €50,000/bet, min ≈ $0.30.
- Full market-by-market table + promo math (Acca of the Day +10%, Insurance, No-Risk Exact Score, TOTO) → `references/01-1xbet-markets-rules.md`.

## Quant Essentials (memorize)

- **xG:** sum of shot probs. `xGD/90` best single predictor. Flag `|G - xG|/xG > 25-30%` over 8-12 games (min MW10) for regression. Finishing skill persists only r≈0.15-0.25.
- **Poisson:** `P(k;λ) = λ^k·e^-λ/k!`, `λ_home = Att_home·Def_away·LgAvgHome`. Matrix `P(i,j)=Pois(i;λ)·Pois(j;μ)` → 1X2 / O-U / BTTS. Dixon-Coles `ρ≈-0.08..-0.13` boosts 0-0/1-1.
- **Elo:** `We = 1/(1+10^(-dr/400))`, `Rn = Ro + K·G·(W-We)`. Home +65-100pts. K≈20 clubs.
- **CLV:** `raw = YourOdds/CloseOdds - 1`, always devig close first.
- **Kelly:** `f* = (p·d - 1)/(d - 1)`. If ≤0 → no bet. Use quarter, cap 1-3%.
- Full formulas, worked example (Arsenal λ=2.06/μ=0.86), bore-draw filter, referee/weather adjustments → `references/02-quant-models-xg-poisson-elo.md`.

## Strategy Essentials (memorize)

- **Core:** value betting (80-90% volume) > arbitrage > matched > trading-on-1xBet. Trading on 1xBet alone pays double vig — no lay button.
- **O/U 2.5 & AH:** lowest margin (2-5%), most modelable. **BTTS:** ~5.5% margin, public overbets Yes. **DC:** high hit-rate, highest margin per € — check AH +0.5 first. **HT/FT:** 9 outcomes, 0.5-1% max. **Late goals (75'+):** ~25-30% of goals; enter 70-77' only with momentum + stakes.
- **Accas:** 2 legs ≈10.3% margin, 5 legs ≈27.6%, 10 legs ≈62.9%. Singles Sharpe ≈3.3× better than 4-leg.
- **Bankroll:** 50-100 units, 1U = 1-2%. 90/8/2 split (singles / +EV 2-3-leg / fun).
- **Biases:** recency, chasing (loss hurts 2×), confirmation (write 3 reasons bet is WRONG first), sunk cost (kill rule: negative CLV + negative yield after 300 bets → abandon).
- **Scams:** "fixed matches", "95% VIP tips", Martingale — 100% fraud/fallacy. Doubling changes distribution, not EV.
- Full pros/cons/timing/staking per strategy + tilt protocol → `references/03-strategies-bankroll-psychology.md`.

## Toolstack Essentials (memorize)

| Job | Primary | What to pull |
|---|---|---|
| Odds + movement | OddsPortal, BetExplorer, Oddspedia | opening vs current, % drop, >70% books dropping = sharp |
| Deep stats | FBref (StatsBomb xG), Understat (shot maps, xPts) | xG/xGA per 90, xPts gap, home/away split |
| Live + mobile | SofaScore (momentum, live xG), FotMob, Flashscore (fastest scores) | live xG surge after sub, predicted XI, H2H |
| Betting hit-rates | FootyStats (1500+ leagues), SoccerSTATS (goal timing) | BTTS/O-U/corners/cards %, late-goal teams |
| History/H2H | Soccerway, StatBunker, Football-Data.co.uk CSV | last 10 H2H, fixtures, CSV for backtests |
| Squad/news | Official club sites, RotoWire pressers, Transfermarkt, MissesNextMatch | confirmed XI, same-unit absences (2 CBs out compounds) |
| Refs/cards | FootyMetrics refs, Statz.ai, WorldReferee | Y/90, pens/match, n≥15 (ideally 30+) |
| Weather/totals | Windy, AccuWeather, Yr.no | wind >15mph, rain >5mm/h, snow, heat WBGT>28°C |
| Predictions | Forebet/PredictZ/Vitibet — convergence only | never blind-follow; require your prob > implied + margin |

Full URL table + free/paid + limitations → `references/04-websites-toolstack.md`.

## Output Template (use for every match analysis)

```markdown
# [Home] vs [Away] — [Competition] — [Date UTC]

**Status:** pre-match | live [minute + score if live]
**1xBet snapshot:** 1X2 [1/X/2] | O2.5 [over/under] | BTTS [yes/no] (quote time)
**Model:** Home [x]% | Draw [x]% | Away [x]% | O2.5 [x]% | BTTS [x]%
**No-vig book:** Home [x]% | Draw [x]% | Away [x]% (overround [x]%)
**Edge:** [market]: model [x]% vs book [x]% = [+x.xpp / EV +x.x%] → BET / NO BET
**Stake:** [x]% bankroll ([fractional Kelly + cap applied]) | BR: [amount]

## Why (evidence, tagged)
- [API]/[ODDS]/[IND] facts only; mark [N/A] when missing
- Form (last 8, H/A split), xG/xGA/xGD, shots/box/SoT, PPDA/tilt
- Rest/congestion/Europe ±4d, travel, motivation matrix, XI vs best XI
- Ref (cards/pens, n), weather/pitch at venue-time, tactical matchup

## Risks / What would invalidate
- 3 reasons this bet is WRONG + bore-draw check + rotation risk

## 1xBet execution
- Exact market name + slip type (Single preferred) + cash-out/hedge plan
- If acca/system: show compounded margin math

*18+ only. EV, not certainty. Never stake more than you can afford to lose.*
```

Detailed checklist + bore-draw filter + live protocol → `references/05-match-analysis-workflow.md`.
Copy-paste prompts + tracker header → `references/06-prompts-templates.md`.

## Scripts

- `scripts/poisson.py` — Poisson + Dixon-Coles τ matrix → 1X2 / O-U / BTTS from λ/μ.
  `python scripts/poisson.py --home 2.06 --away 0.86 --rho -0.08`
- `scripts/devig_kelly.py` — implied/devig/EV/edge/Kelly/CLV + acca-margin.
  `python scripts/devig_kelly.py --odds 1.95,3.60,4.20 --model 0.55 --stake-method quarter`
- No API keys. Pure computation. Verify with `python -m py_compile`.

## Verification (before answering)

- [ ] Competition/date/time + 1xBet exact market names confirmed?
- [ ] Settlement basis stated (90 min vs ET/pens)?
- [ ] Model % vs no-vig % vs edge/EV shown with margin-of-safety (≥3-5pp)?
- [ ] Home/away splits (not season avg), last 8+ sample, opp-adjusted?
- [ ] XI/news, motivation, rest, ref (n≥15 for cards), weather checked or marked [N/A]?
- [ ] Stake = 1-2% (cap 3%), no Martingale, no acca-stacking without per-leg +EV?
- [ ] 3 counter-reasons + invalidation conditions listed?
- [ ] CLV target + log row provided?
- [ ] 18+/risk line included, no "guaranteed/fixed" language?

## Pitfalls

- Confusing 1X2 with To Qualify; playing standard 1X2 expecting 2UP protection.
- Betting widget % as true prob (it includes margin).
- Using season averages instead of H/A splits; sample <8 games.
- Over + BTTS same-game acca (correlation double-exposure).
- Cashing out every green (pays margin repeatedly); full cash-out by default (prefer partial/manual hedge).
- Chasing, doubling stakes, forcing plays outside specialist leagues.
- Trusting Forebet/PredictZ picks, "fixed match" sellers, Martingale recovery.
- Ignoring same-unit absences (CB+DM+GK), Thursday→Sunday congestion, derby card inflation.

## Install

```bash
# skills.sh standard (any agent: Claude Code, Codex, Cursor, Copilot, Hermes)
npx skills add vaferkhanom/bet-skill
npx skills add vaferkhanom/bet-skill --skill bet-skill
npx skills add vaferkhanom/bet-skill --list

# Hermes Agent
hermes skills install vaferkhanom/bet-skill/skills/bet-skill
hermes skills tap add vaferkhanom/bet-skill
/skills install vaferkhanom/bet-skill/skills/bet-skill
```

Local test: `npx skills add ./bet-skill --skill bet-skill` then `npx skills list`.
