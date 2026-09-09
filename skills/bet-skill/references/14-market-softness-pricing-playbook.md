# 14 — Market Softness Ladder & Pricing Playbook (which of the 1,400+ to actually bet)

> The catalog (`references/13-1xbet-all-markets-catalog.md`) lists EVERYTHING. This file
> tells you which markets carry the smallest margin, which are softest for value, and
> how to price any of them from ONE Poisson matrix (`scripts/poisson.py --full`).
> Rule that never changes: exotic markets have HIGH margins — they exist to farm the
> acca-mentality. Value lives in efficiency, not variety.

## 1. Softness ladder (margin low → high, empirical typical ranges)

| Tier | Markets | Typical margin | Why |
|---|---|---|---|
| 1 — tightest | 1X2 (top leagues), AH, O/U 2.5, DNB | 2-5% | sharpest liquidity, pro money |
| 2 — fair | Double Chance, Team Totals, HT totals, O/U other lines, Asian Total | 4-6% | derivative but efficiently priced off main lines |
| 3 — soft-ish | BTTS, 1X2+Total combos, DC+Total, To Qualify, race markets, half markets | 5-8% | recreational flows; combos = hidden margin stacking |
| 4 — soft | Corners totals/handicap, Cards totals/points, Exact Score, HT/FT, Multi Goal bands, Odd/Even | 6-10% | volatile, data-thin, public-friendly |
| 5 — farm | Intervals (0-15 etc.), Goal Minutes, First To Happen, 1-minute markets, Player vs Team, Multi Corner, Set Piece Goal, Highest Scoring Quarter, time-with-no-goals, VAR/medical/referee-duel, Alternative Matches, Constructor fantasy | 8-15%+ | settlement edge cases + noise; mostly NO BET |
| 6 — never | Alternative double matches, manager/transfer/FIFA specials, "Player has the ball at the final whistle", Who Will Kick Off | entertainment only | pure novelty pricing |

Values are typical — measure YOUR league's actual margins with `scripts/devig_kelly.py` per market family and re-rank locally.

## 2. Where value actually hides (in order of practical hit-rate)

1. **Derivative-vs-mainline arbitrage within 1xBet:** AH +0.5 vs X2, AH 0.0 vs DNB, Team Total vs match Total, DC+Total combo vs two singles — same probability, different prices. Always compare before taking the headline market.
2. **Goal timing asymmetries:** league + team-specific first/last-half goal splits (SoccerSTATS) vs interval markets — but interval margin (Tier 5) eats most of it; only bet when split is extreme.
3. **Cards markets via referee:** refs with ±0.5 cards/game vs league average, 30+ game samples (`references/04` tools) — the only reliable cards edge. Team style (fouls/game) second.
4. **Corners via style:** wing-heavy attacks + blocked-cross defences; use team corner averages (FootyStats H2H corners) vs line. Tier 4 margin — need ≥6pp model edge.
5. **Totals via shot quality:** both PPDA <11 or both >14 + shot distance profile (§02 bore-draw filter) beats the line more often than any exotic.
6. **2UP as insurance, not value:** 1X2 2UP costs ~5% of odds — take it when you'd otherwise hedge late, never as a default.

## 3. Price ANY market from the Poisson matrix (λh, λa)

`python scripts/poisson.py --lh 2.06 --la 0.86 --full` prints every derivable family:

| Market family | Matrix formula |
|---|---|
| 1X2 / DC / DNB | P(i>j), P(i=j), P(i<j) and sums of two |
| O/U line N (incl. .25/.75 Asian) | Σ P(i+j vs N), Asian split across two lines |
| Team Total T1/T2 | Σ P(i vs n), Σ P(j vs n) |
| BTTS | 1 − P(i=0) − P(j=0) + P(0,0) |
| Exact score / Any Other | cell P(i,j); "any other" = 1 − Σ listed |
| Multi Goal band a-b | Σ P(a ≤ i+j ≤ b) |
| Odd/Even | Σ P(i+j odd/even) |
| HT/FT approx | two independent half-Poissons (λ/2 each) × result logic |
| Highest scoring half | 1H total vs 2H total distributions |
| Win both/either halves | P(win 1H)·P(win 2H), union |
| Race to N / Next goal | 1 − P(neither reaches N in remaining goals) via negative-binomial logic |
| Correct Score combos (live chase) | conditional matrix on current score (see `live_fair.py`) |
| Corners/Cards/Stats | NOT derivable from goal matrix — separate Poisson/Negative-Binomial on the stat's own λ (team avg per game, time-scaled); treat as Tier 4-5 |
| Intervals | λ × (15/90) per interval with stoppage conventions (§13 §0) |

## 4. Exotic pre-bet gate (run before ANY Tier 3-5 market)

- [ ] Settlement read in §13 (interval stoppage matrix? OG rules? corner-taken rule?) — if uncertain → NO BET
- [ ] Independent λ estimated for the stat (not gut), sample ≥15 games
- [ ] De-vigged edge ≥6pp (Tier 4) / ≥8pp (Tier 5)
- [ ] Stake 0.5% max, singles only, logged with Tier column
- [ ] Not correlated with a same-game position (Cards + total, Corners + AH)

## 5. Combo-pricing discipline

Book combos (1X2+BTTS, DC+Total, BTTS+O/U) price as P(A)·P(B)·(1+extra margin). Always:
`fair_combo = P(A)·P(B) / P(A∧B)` from the matrix (they're correlated!) — if the book's combo odds are below the correlated fair value, it's a trap; if above, it's rare value. Combos of positively-correlated events (BTTS + Over) pay LESS than independent math suggests — compute the joint from the matrix, never multiply marginals blindly.
