# 03 — Strategies, Bankroll, Psychology, Scams, Responsible Play

> 18+ only. Education only. Long-term profit requires +EV at scale + strict staking + beating closes. Everything else is variance management. `EV = p·profit - (1-p)·stake`, `implied = 1/odds`, `edge = p·odds - 1`.

## 1. Frameworks

| Approach | Profit source | Variance / needs | 1xBet fit |
|---|---|---|---|
| **Value (core 80-90%)** | your prob > implied prob, accept losses. ROI 2-6%/bet over 500+ | medium-high, can lose 10+ straight with real edge. €200-500 min, 3-5 soft books + Pinnacle/Betfair ref | HIGHEST. Natural pattern, lasts 200-2,000 bets. Fits low margins + depth |
| **Arbitrage** | cover ALL outcomes where sum implied <100% (e.g. 1.80+3.80+6.50=94.8% = 5.2% arb) | near-zero per arb IF executed; needs €500-1k over 8-15 books, fast execution, 1-3% typical | LOW. Flagged in days-weeks. 2-way (AH/O-U/BTTS) simpler than 1X2 |
| **Matched** | convert bonuses (back book + lay exchange). SNR 70-80%, SR 90%+ | very low per trade; needs exchange. 1xBet welcome 100%→300% but 5× wagering in 3+ accas @1.40+ ≤30d — often -EV | LIMITED. Price the conversion first |
| **Trading** | back high lay low as odds move. Needs exchange/liquidity | medium, needs speed. 1xBet NOT exchange: no lay, live margins 6-8% vs 4-5% pre, cash-out margin 2-9% | HARD. Use 1xBet for positions, hedge elsewhere |

Use value as core; arb only on fresh accounts for cash-flow; matched only for calculated +EV bonus; trading only for hedging.

## 2. Market strategies (1xBet context: EPL 1X2 ~3-5%, O/U ~5.6%, BTTS ~5.5%, AH 2-4%)

### Over/Under 2.5
Total ≥3 (Over) or ≤2 (Under). Use xG not goals. `λ_total = λ_h+λ_a` → Poisson `P(Under)=P0+P1+P2`, `P(Over)=1-P(Under)`. Example λ=2.6 → P(Over)=48.2%; book 1.90 (52.6%) = no Over value; Under 2.05 (48.8%) vs 51.8% model = small edge. Pros: 2-outcome, liquid, modelable, Under often undervalued (public loves Overs). Cons: Over bias shortens Overs; live margins 6-8%. Use: adj xG >2.8 Over, <2.2 Under; defensive derbies/second-leg protects for Under; press vs tired for Over. Avoid: no injury/weather/rotation adjust; blind Overs. Stake 1-2% or ¼ Kelly. Never Over+BTTS same-game acca (corr +0.65).

### BTTS Yes/No
`P(Yes)=(1-e^-λh)(1-e^-λa)`. Only 1-1 is Yes + Under. Pros: binary, soft books misprice vs Pinnacle, good in >60% BTTS leagues. Cons: ~5.5% margin, Yes overbet. Use: both high xGF AND high xGA, press with weak rest-defence. Avoid: clean-sheet machine or opp <1.0 xG/game; 3-0 mismatches (Over but No). Track Yes/No separately.

### Asian Handicap
Draw removed, 2 outcomes, lowest margin. Quarter splits stake. +0.5 ≈ X2 but often 0.02 better (≈5% ROI lift/season); +1.0 refunds narrow loss killing DC. Pros: efficiency + push as stop-loss. Cons: needs precision. Use: compare AH+0.5 vs X2, AH 0.0 vs DNB; underdog +0.75/+1.0 for defensive dogs; fave -0.75 instead of -1 for half-refund on 1-0. Avoid: paying for coverage unneeded. Core Kelly/flat 1-2% market.

### Double Chance (1X/X2/12)
2 of 3, 60-75% hit-rate but short odds. Pros: simple, safe feel; good where home rarely loses but draws often (<2.2 avg, high draw%). Cons: highest margin per € (DNB/AH cheaper 5-8%); frequent wins with no +EV = slow bleed. Use: fade overvalued fave with X2. Avoid: <1.30 no-edge; acca filler "for safety" (compounds margin); when AH+0.5 better. Max 1%.

### DNB = AH 0.0
Win→win, draw→refund, lose→lose. Removes highest-margin outcome (draw), overround 1-3% lower than 1X2. Use: slight lean + genuine 20-25% draw risk; cup ties (draw refunds even if ET later). Avoid: big dog @6.00 → DNB @4.50 kills value. 1-2%.

### HT/FT (9 outcomes)
Need half + full. HT Draw ~45-50%; most common Draw/Home 15-18%. Pros: 9 outcomes → mispricing; boosts short fave (1X2 1.60 → Home/Home ~2.00 if fast starter). Cons: two calls, turnarounds 15-30 rarely hit. Use: data-backed scripts from last 10-15 HT/FT splits (fast→Home/Home; slow + strong bench→Draw/Home). Avoid: slow starters needing HT lead; derbies. 0.5-1% singles only.

### Late goals (75'+, incl. added)
~25-30% goals 75'+, ~50%+ matches score after 70', ~42.6% after 80'. Drivers: fatigue (9-10km), fresh subs vs tired backs, chasing 3-4-3, stretched state, 7-10' VAR time. Pros: live less efficient; Over 0.5 late 1.80-2.10 often value in close high-stakes. Cons: stress, fast moves. Use: draw/1-goal where both need result; press fading; 3+ corners/shots since 75', 70%+ last-15' possession, strong bench used. Wait 70-77', use Next Goal / Over 0.5 76-90' / live Asian Over 1.0 (refund if exactly 1). Avoid: dead rubbers suiting draw; double low-blocks. 0.5-1% live, max 2/game.

### Favourite vs underdog / fading public
Public overbets faves/Overs/TV names; books shade to manage liability. Blind fave loses to vig; blind dog also loses. Plus-money needs low win% (3.00 needs 33.3%+). Contrarian filter (not blind opposite): 80%+ tickets one side but line moves opposite (reverse move), tickets% >> handle% (public fave, sharp dog). Example NFL <20% side won 55.5% ATS (+8.2% ROI); football-Data UK 15k contrarian small + at Pinnacle close. Use: high-visibility lopsided + reverse + xG agrees; home dog low xGA vs overrated giant; newly promoted underrated / relegated overrated. Avoid: low-volume small leagues (no shade to exploit); sharp+public aligned. 1% flat, large sample.

### Specialize in 1-2 leagues
Most reproducible manual edge. Learn rotation/refs/travel/weather/xG baselines/close habits; spot news first; lower leagues (Championship, La Liga 2) less efficient than EPL. Cons: fewer bets, force-play temptation. Allocate 80%+ bankroll to specialists.

## 3. Live / cash-out / hedging

Eye test lies: 70% possession + 0.2 xG ≠ dominating. Use live shots/SoT/box touches/corners since 60', fresh legs. Books faster than you + data delayed.

Cash-Out ("Bet Slip Sale", full+partial, no auto): `Fair = LiveProb × Potential Return`, offer 2-9% less (10-18% on losing longshots). Example €10 @3.00 now 50% → fair €15, offer €14-14.50. Use partial never full by default: lock 80%+ when 2-0 up 70' on big stake, high-variance dog now 56%, genuine funds/stress need. Avoid: cashing every green (pays margin repeatedly), cashing 30% when fair 35-40% (widest margin), HT banner (8-12% peak). Checklist: estimate live prob → offer/fair >97%? → certainty change behaviour? → partial? → manual hedge cheaper?

Hedging beats cash-out: `HedgeStake = OrigStake·OrigOdds / HedgeOdds`. Example €100 @3.00 vs hedge @2.50 → €120 locks €80 either way, often €5-15 better than cash-out. Hedge pays 4-5% vs cash-out 4-12%. Use cash-out only if opposite side inaccessible.

## 4. Accumulators — math + when (rarely) OK

Single = 3-5% majors (2-3% Pinnacle). Acca multiplies margin: `1.05^n - 1` → 2 legs 10.3%, 3:15.8%, 4:21.6%, 5:27.6%, 10:62.9%. At -110 each: single 4.55%, 2-leg 8.88%, 4-leg 16.9%, 10-leg 37.1%. ~97% accas lose. 53% singles (+0.55% ROI) but losing 2-leg parlays (-1.63%). Singles Sharpe ≈3.3× better than 4-leg. Systems (Yankee/Lucky-15/Trixie) less terrible (Lucky-15 ~-8% vs -19% 4-fold) but still worse than singles.

When acca OK: (1) EVERY leg independently +EV (two +5% → ~+0.25% double — thin, max 2-3 legs), (2) truly correlated SGP mispriced by book, (3) bonus/boost priced via calculator (headline % ≠ keep-rate), (4) small fun ticket 2% bankroll as fixed entertainment cost. Pro split if forced: 90% singles / 8% 2-3-leg value / 2% fun. 1xBet welcome forcing 5× in 3+ accas @1.40+ — calculate keep-rate first.

## 5. Bankroll

Separate from living money. 50-100 units min (e.g. €500-1000 for €10 units). 1U = 1-2% CURRENT bankroll (1% conservative, 2% standard, never >5% unproven — >5% → 20-40% ruin even with 3% edge; at 2% RoR <1%). Recalc weekly/monthly.

Kelly: `f = (b·p - q)/b`. Example 2.10 @55% → 14.1% full → half 7.05% → quarter 3.5%. Full = max growth + 50-60% drawdowns. Never full. Half ≈75% growth/half vol (pro standard). Quarter ≈44% growth/75% less drawdown (recommended until 500+ prove calibration). If ≤0 → no bet. Cap 5% regardless. Scale down correlated simultaneous.

Stop-loss/win: daily loss 5U/5% → done, no exceptions. 50% peak drawdown → halt, reassess, drop to 1% or paper. Max 3U/single, max ~5 bets/day. Never reload to chase, never double to recover.

Track: ROI/Yield = profit/staked×100 (win% alone lies: 55% @1.70 loses, @2.00 wins). CLV = yours vs close; +CLV = skill (leading), profit = lagging. Need 200-300 for signal, 1000s for confidence. Pro yield 1-5%/1000s; 25-50%/yr at half-Kelly = upper end. Log EVERY bet immediately (see 05 template). Dashboard by league/market/book + calibration (when you said 60%, did 60% win?).

## 6. Biases — fixes (process, not willpower)

| Bias | Fix |
|---|---|
| Gambler's fallacy ("due" after 5 losses; 6-loss in 200 bets ~84% likely) | every bet independent; ask causal link? if none ignore; flat stake |
| Recency (last 4-0 = crisis/greatness) | 10-game xG avg not last score; review 100-bet blocks |
| Chasing/loss aversion (loss hurts 2×, hold losers 2.7× longer) | pre-commit unit + daily limit; log off at limit; flag >1.5× unit weekly |
| Confirmation (fan bets, only supporting stats) | write 3 reasons WRONG first; record prob BEFORE seeing odds (avoid anchoring) |
| Sunk cost (defend broken model 200 bets) | quarterly kill rule (neg CLV + neg yield after 300 → abandon) |
| Overconfidence/hot-hand (5 wins = 1/32 at 50%) | demand 50+ sample, calibration, ¼ Kelly, journal + max bets/day |

Tilt protocol: bad beat → 15-min break, no live 30 min, 3 losses straight → stop. Spreadsheet doesn't tilt — let rules decide.

## 7. Scams

Fixed/VIP tipsters (Telegram/WhatsApp/Discord/TikTok "guaranteed, limited slots, crypto/gift/mobile"): 100% fraud. Tactics: fake slips (Photoshop/devtools), only winners posted, opposite picks to groups, second unlock fee, deleted negatives, fake contacts. Real fixes criminal, never sold €50 to strangers. Guarantee = instant disqualify. Legit: timestamped pre-kick log WITH losses, 52-57% realistic not 95%, reasoning, traceable payment. Red flags: screenshots only, paywall upfront, timer pressure, anonymous, 90-100% claims, steer to mirror book.

Martingale/Fibonacci (double after loss): fails — independent outcomes, EV stays negative, finite bankroll, book limits cap. 10 losses = 1,023× base; 10-loss in 200 bets 11% likely; 15-loss in 5,000 still 5.5% ruin; sims avg loss 4.2× worse than flat. Changes distribution (many small wins, rare catastrophe), not EV. Never use.

## 8. Responsible play + 1xBet hygiene

18+ only. Entertainment cost, never income/rent. Set BEFORE deposit: deposit/loss/session/stake limits (1xBet tools basic vs UKGC — add bank block + BetBlocker/GamBan). Self-exclusion: 1xBet + GAMSTOP (UK online), MOSES, SENSE, GamCare/GambleAware; US NCPG 1-800-522-4700. Stop signals: chasing, hiding, borrowing, drunk/stressed betting, can't stick to limits → stop + support immediately.

1xBet hygiene: KYC early (ID + address + selfie, 24-72h); screenshots of bets/deposits/chats; withdraw modest via same method (e-wallet/crypto 15m-24h, cards/bank 3-7d); use as ONE price point not sole bankroll; expect limits if systematically winning; check legality (blocked US/UK/many EU, Curaçao 1668/JAZ + local e.g. NLRC Nigeria); verify early, Curaçao recourse weak.
