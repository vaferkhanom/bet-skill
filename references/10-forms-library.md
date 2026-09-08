# 10 — Forms Library (copy-paste, fill-in)

> Emit the requested form pre-filled with what you know. Forms live here AND in `templates/` as separate files.

## F1. Onboarding (`templates/onboarding.md`)

Bankroll, currency, books, sports/leagues + markets, risk profile, minutes/day, monthly budget, stop-loss + drawdown acceptance → output Bankroll Card.

## F2. Pre-Bet Intake (REQUIRED before any BET verdict)

```markdown
## Pre-Bet Intake — [event + date]
- Sport/league/market: [..] | 1xBet exact market: [..] | Slip: [Single]
- Odds taken (book + time): [..] | Best elsewhere: [..] | Closing target: [..]
- Model%: [..] | No-vig%: [..] | Edge: [..]pp | EV: [..]%
- Bankroll%: [..]% ([method + cap]) | Reason (3 bullets, tagged): [..]
- 3 reasons WRONG: 1.[..] 2.[..] 3.[..] | Invalidation: [..]
- Sharp: Pinnacle/Exchange/dropping? [..] | Expert weight: [..]
- Stop status: bets today [n/max], daily P/L [..] → PROCEED / WAIT-XI / PASS
```

No model% → NO BET (offer to build one or pass).

## F3. Event Report

See SKILL.md §7. One report per event, probabilistic language only.

## F4. Post-Bet Review (within 24h, win OR lose)

```markdown
## Post-Bet — [event] — [W/L/P] [+/- units]
- Result vs process: won because [edge real]/[luck]? lost because [variance]/[missed XI/weather/ref]? 
- CLV: took [x] vs close [y] = [+/-x%]. Process score (1-5): [..]
- Lesson (1 line) + rule change? [..]
```

Score process, not outcome. Good bets lose; bad bets win.

## F5. Weekly Review (`templates/weekly-review.md`)

Bets, win%, ROI, CLV+% by league/market/book, calibration, tilt flags (>1.5× unit, >max/day, chased?), leak list (cut/add), Bankroll Card refresh, next week's max bets + focus leagues.

## F6. Bonus / Promo Pricer

```markdown
## Promo — [name]
- Offer: [..] | Wagering: [e.g. 5× in 3+ accas @1.40+ ≤30d] | Funds: [real/bonus? crypto excluded?]
- Keep-rate math: acca margin [1.05^n-1] × rollover = expected cost [..] vs bonus value [..] → TAKE / SKIP
- Hedge/insurance cost: [..] | Expiry: [..] | Decision + log row
```

Headline % means nothing without keep-rate. 1xBet acca wagering is usually -EV — price it first.

## F7. Bankroll Card

See SKILL.md §1. Re-issue on every bankroll change + weekly.
