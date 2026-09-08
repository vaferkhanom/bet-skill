# 06 — Prompts, Templates & One-Line Calculators

> Copy-paste starters. Replace brackets. Always attach odds + date/time + book.

## 1. Pre-match request (user → agent)

```
Analyze [Home] vs [Away], [Competition], [Date time UTC], for 1xBet pre-match.
1xBet odds (quoted [time]): 1X2 [1/X/2], Over 2.5 [x] / Under [x], BTTS Yes [x]/No [x].
Bankroll [amount]. Specialist league? [yes/no]. Known news: [injuries/suspensions/congestion or "none yet"].
Return: full bet-skill template (model% vs no-vig% vs edge/EV, stake%, risks + 3 counters, exact 1xBet market + slip type, CLV target + log row).
```

## 2. Live request

```
Live: [Home] [H]-[A] [Away], [minute]', [Competition].
Pre-match 1xBet 1X2 was [1/X/2]. Live odds now: [1X2 + O0.5 late + Next Goal if have].
Live xG (SofaScore/FotMob): [Hx]-[Ax]. Shots since 60': [..]. What is the best 0.5-1% position, if any? Partial hedge plan?
```

## 3. Value-check request

```
Value check: my model says [Home win 55%]. 1xBet offers [2.10] (1X2: [1.95/3.60/4.20]).
Compute: implied, no-vig, edge pp, EV, quarter-Kelly capped 2%, CLV if close is [..]. BET or NO BET?
```

## 4. Bankroll plan request

```
Build staking plan. Bankroll [€1000]. Experience [200 bets, CLV +1.5%]. Markets [O/U + AH]. Max bets/day [5].
Return: unit size, caps, stop-loss, 90/8/2 split, tracker header, quarterly kill rule.
```

## 5. Strategy review request

```
Review my last [50] bets (paste tracker CSV). Break down ROI/CLV by league/market, calibration, tilt flags (>1.5× unit, chasing), and what to cut.
```

## 6. Tracker CSV header (paste into Sheets)

```
Date,League,Match,Market,Pick,Model%,Odds,Book,ClosingNoVig,CLV%,StakeEUR,StakePctBR,Result,ProfitLoss,RunningBR,Reason,CounterArgument
2026-09-01,EPL,Arsenal-Everton,AH -0.75,Arsenal,55%,1.95,1xBet,1.90,+2.6%,20,2%,W,+19,1019,xG 1.8v0.9 XI confirmed,away low-block
```

## 7. One-line calculators (no script needed)

```
Implied: 1 / decimal (2.50 → 40%)
No-vig: implied / sum(implied) (1.90+1.90 → 52.63% each → 50% fair → 2.00)
EV per unit: p*odds - 1 (0.48 @2.20 → +0.056 = +5.6%)
Edge pp: p_model - p_noVig
Kelly: (p*d - 1)/(d - 1) (0.50 @2.20 → 8.33% full → half 4.17% → quarter 2.08%; ≤0 = no bet)
CLV raw: yours/close - 1 (2.05 vs 1.95 → +5.13%); no-vig: yours/fairClose - 1
Acca margin: 1.05^n - 1 (2 legs 10.3%, 5 legs 27.6%, 10 legs 62.9%)
Hedge: OrigStake*OrigOdds / HedgeOdds (100 @3.00 vs 2.50 → 120 locks 80 either way)
BTTS Yes: (1-e^-λh)*(1-e^-λa)
```

## 8. Do / Don't one-liners for the agent

- DO specialize 1 league + 1 market, singles, 1% flat, log every bet, beat closes.
- DON'T promise, parlay comfort legs, double after loss, trust widget/pick sites/tipsters, bet blocked jurisdictions.
- ALWAYS end: *18+ only. EV, not certainty. Never stake more than you can afford to lose.*
