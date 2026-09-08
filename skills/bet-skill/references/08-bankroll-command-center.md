# 08 — Bankroll Command Center (user states bankroll → plan)

> The user telling you "I have €X" triggers this file. Never answer with a bare stake — always regenerate/refresh the Bankroll Card.

## 1. Intake (use `templates/onboarding.md`)

Required: bankroll amount + currency (separate from living money). Optional but asked: books, sports/leagues, risk profile, minutes/day, monthly budget, stop-loss acceptance. No bankroll → PROVISIONAL 100-unit plan, clearly labeled.

## 2. Profiles → numbers

| Profile | Base | Max conviction | Cap | Kelly | Min bankroll |
|---|---|---|---|---|---|
| Conservative (default) | 1% flat | 1.5% | 2% | eighth–quarter | 50 units |
| Standard | 1% flat | 2% | 3% | quarter (if +CLV 300+ bets) | 50-100 units |
| Aggressive (discouraged) | show ruin math first | 2% | 3% | quarter max | 100 units |

- **Unit = 1% of CURRENT bankroll, recalculated weekly** (not per bet).
- Props / HT-FT / live / esports / MMA: 0.5-1% regardless of profile.
- Simultaneous/correlated exposure: cap 20-30% total pending.
- Script: `python scripts/bankroll_plan.py --bankroll 1000 --profile standard [--currency EUR]`.

## 3. Drawdown ladder (automatic)

| Drawdown from peak | Action |
|---|---|
| -10% | halve max conviction to 1%, cut fun bets |
| -20% | base 0.5-1%, max 2 bets/day, mandatory weekly review |
| -50% | HALT all staking, paper trade only, full leak audit before resume |

Daily stop-loss 5U/5% → done for the day, log off, no "one more". Never reload to chase.

## 4. Stake table example (€1,000 standard)

| Bet class | % | € | When |
|---|---|---|---|
| Standard single | 1% | €10 | edge 3-5pp, XI known |
| Max conviction | 2% | €20 | edge >5% + sharp agrees + XI confirmed |
| Live / prop / HT-FT | 0.5-1% | €5-10 | momentum + stakes, max 2/game |
| Fun ticket | ≤2% total | ≤€20 | fixed entertainment cost, logged separately |

## 5. Monthly review (update the card)

Recompute unit from current roll, check ROI/CLV by league/market, calibration (said 60% → won ~60%?), tilt flags, kill rule (negative CLV + negative yield after 300 bets → abandon system, not double it). Profits are withdrawn on schedule, never "let it ride" without a rule.

## 6. What Hermes says when bankroll changes

- "My bankroll is now €X" → new card + new table + confirm stop-loss.
- "How much on this?" → needs model% + odds first; no prob → no stake, offer landmarks (1% = €Y).
- "I'm down 30%" → ladder step + fewer bets + review, never bigger stakes.
