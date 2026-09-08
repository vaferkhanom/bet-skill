# 02 — Quantitative Models: xG, Poisson/Dixon-Coles, Elo, Context, CLV/Kelly

> Formulas are standard. Thresholds are empirical rules-of-thumb — validate on your league/sample before staking.

## 1. Expected Goals (xG / xGA / xGD / xPTS)

xG assigns each shot 0-1 from thousands of similar shots (distance, angle, GK position/line-of-sight, defenders in cone, pressure, body part, pattern: open/fast-break/corner/FK, previous action). Opta XGBoost uses 20+ features. Providers (Opta, StatsBomb, Understat) are NOT interchangeable.

Reference: penalty ~0.76-0.79, 6-yard cutback ~0.35-0.50, central box ~0.15-0.25, outside box ~0.02-0.05, 30-yarder ~0.01-0.03.

```
Team xG = sum(shot xG)
xGA = sum(opponent shot xG)
xGD/90 = (xGF - xGA) / matches        # strongest single predictor of future points
xPTS = sum over matches of simulated P(win)*3 + P(draw)  # via Poisson from xG scorelines
```

Interpretation:

| Signal | Read |
|---|---|
| Goals >> xG over 8-12 games | hot finishing / weak opp GKs, low persistence → fade candidate |
| Goals << xG | cold finishing / posts / elite opp GK → buy-low candidate |
| xGA low but GA high | GK underperforming, likely to improve |
| xGA low + clean sheets via GK overperformance | less sustainable than structure-driven low xGA |
| xGD > +0.5/90 | title-level dominance |
| xGD ~ 0 | mid-table true talent |
| xGD < -0.5/90 | relegation-level process |
| High shots + low xG/shot | long-shot volume, low-block bait, unsustainable |
| Low shots + high xG/shot | efficient box creation, sustainable |

xG predicts next-match result and next-6 goal ratio better than shots/goals (r≈0.57 vs 0.46/0.47, Mead et al. 2023). Predicted SoT-off-target + corners + SoT add info BEYOND odds-implied prob; predicted goals alone adds little once odds in model (Wheatcroft/LSE) — model shot process, not just goals.

Regression rules: finishing skill G-xG/shot persists only r≈0.15-0.25 (75-85% noise). Overperformer reverts to ~even on FUTURE shots; banked goals stay. Flag only after MW10+, min 8-10 games (ideally 10-15), `|G-xG|/xG > 25-30%`. Backtest: overperformers +35% pre → +8-12% post; fade ≈3-4% ROI, back underperformers ≈1-2% at ~1.92 — small edge, needs CLV discipline. Always split home/away. Adjust for game state (leading team creates less late), red cards, manager change, missing elite finisher/GK.

## 2. Poisson + Dixon-Coles

Goals ≈ independent count events → Poisson:

```
P(X=k; λ) = λ^k * e^-λ / k!
Attack_i = AvgScored_i / LeagueAvgScored
Defense_i = AvgConceded_i / LeagueAvgConceded   # <1 = good
λ_home = Attack_home * Defense_away * LeagueAvgHomeGoals
μ_away = Attack_away * Defense_home * LeagueAvgAwayGoals
```

LeagueAvgHome ~1.4-1.6, Away ~1.0-1.2 (Bundesliga total ~3.0, Serie A/Ligue 1 ~2.5 — calibrate per league). Joint matrix assuming independence:

```
P(i,j) = Poisson(i;λ) * Poisson(j;μ), i,j = 0..8
P(Home) = sum(i>j), P(Draw) = sum(i==j), P(Away) = sum(i<j)
Over N = sum(i+j > N)
BTTS Yes = 1 - P(home shutout) - P(away shutout) + P(0-0)
```

Independent Poisson underestimates 0-0/1-1, overestimates 1-0/0-1. Dixon-Coles (1997) fix:

```
λ_ij = exp(α_i + β_j + γ),  μ_ij = exp(α_j + β_i)
α = attack (avg 0), β = defense (positive = leaky), γ = log home advantage
P = τ(x,y,λ,μ,ρ) * Pois(x;λ) * Pois(y;μ)
τ = 1-λμρ (0-0); 1+λρ (0-1); 1+μρ (1-0); 1-ρ (1-1); 1 otherwise
```

Most code uses ρ<0 (~-0.05..-0.15, typical -0.08..-0.13) to BOOST 0-0/1-1. Renormalize matrix to sum 1. Fit by max likelihood with time weights `w = exp(-ξ·days_ago)`, ξ≈0.0018-0.00325/day. γ gives home multiplier exp(γ)≈1.25-1.36 EPL (~+0.3 goals). Extensions: blend 60% xG + 40% goals, team-specific HFA, separate 1H model.

Worked example: Arsenal attack 1.35/def 0.82 vs Brighton att 1.05/def 1.12, home adv 1.36 → λ=2.06, μ=0.86 → P(1-0)=11.1%, P(0-0)=5.4%, P(1-1)=9.5%, P(2-0)=11.4% → Home≈58%, Draw≈21%, Away≈21% before τ. With ρ=-0.08: 0-0 6.1→7.0%, 1-1 11.4→12.3% in λ=1.7/μ=1.1 demo.

## 3. Elo, form, home/away, rest/congestion

```
We = 1 / (1 + 10^(-dr/400)),  dr = (R_home - R_away) + H   # H ≈ 65-100
Rn = Ro + K*G*(W - We),  W = 1/0.5/0 (pens = 0.5)
G = 1 (1-goal), 1.5 (2-goal), 1.75 (3-goal), 1.75+(N-3)/8 (N≥4)
```

K: 20 friendlies, 30 minor, 40 qualifiers/majors, 50 continental finals, 60 WC finals; clubs often single K=20. Converges ~30 games. New season: regress to 1500 by ~25%. Gap guide: +0=0.50, +100=0.64, +200=0.76, +400=0.91 expected score. We is expected SCORE not win prob — need separate draw model (~30% baseline shrinking as |dr| grows).

Form: window 6-8 for xG (5 standard, 10+ stable; <5 noise, >15 stale). Never raw W-D-L: check opp strength, H/A split, xG vs results, margins/reds/game-state. Weight exponential or last5×0.5 + season×0.5.

Home/away: big-5 Home ~44-46%, Draw ~24-26%, Away ~27-30%. Home ≈ +0.3-0.4 xG, larger in lower leagues/hostile grounds (crowd→ref bias, travel, familiarity). Always model H/A xG separately. Post-Covid HFA shrank — refit per league/season.

Rest/congestion flags: `RestDays ≤3`, 3rd game in 7-8 days, Europe ±3-4d, travel miles/zones, NEXT match rotation risk. <72h = red flag; Thursday Europa→Sunday worst; ~15% pressing drop midweek→weekend; 6+ games/30d ≈ -15% away. Congested leans Under (low tempo) but tired legs concede late — split full-game Under vs live late-goal angles. Rested underdog vs tired favourite = classic value.

## 4. Shots / SoT / big chances / PPDA / possession / territory

Hierarchy: combined xG trend (very high) > shots in box / SoT% 35-45% elite (very high) > big chances >0.30 (high) > PPDA (high) > dangerous attacks/final-third/tilt (high) > possession (LOW alone) > raw shots (low alone) > corners/cards (specialist).

- PPDA = opp passes allowed / defensive actions in opp half. Elite press <9, high 9-12, avg 12-15, passive >15. Both <11 = stretched → Overs/cards. Both >14 + deep block = bore-draw (~72% Under 2.5 in one 3k Championship sample).
- Possession alone ≈ zero correlation once quality controlled. Ask: does it become penetration? Use possession-adjusted (xG/possession, shots/sequence).
- Shot texture: 5 box shots > 15 long shots. Avg distance >19y + both PPDA >14 = Under filter.
- SoT most informative observed stat. Minimum 10 games (15-20 stable); first 5 volatile.

## 5. Team news / rotation / motivation

Confirmed linchpin absence swings win prob 10-20% (Haaland/Dortmund 64→41%, De Bruyne xG -0.34/win -8%, Piqué clean-sheet halved, Fabinho opp xG +0.27). Market adjusts in 12-24h; edge biggest first 1-4 games/hours. Public overweights flashy attacker, underweights CB/DM/GK + same-unit multiples (2 CBs out compounds). Suspensions certain; injuries need replacement rating + role check. Sometimes backup ≈ equal — re-simulate xG/xGA with projected XI.

Rotation risk: midweek Europe + weekend, cup/Euro tie in 3-4d, dead rubber, already champion/relegated. Early bet = price but XI uncertainty; late = accurate but efficient. If high rotation risk, wait or size down/skip.

Motivation matrix: must-win ≠ will-win. Title/UCL = raise performance. Relegation 6-pointers = volatile (Unders + cards often better than side). Mid-table nothing-to-play-for vs motivated = fade coasters, esp. away. Champions/safe/relegated confirmed = sharp drop. Derbies compress gap, cards up. Cup/Europe priority = league rotation. Always ask what BOTH sides need.

## 6. Weather / referee / pitch / travel / altitude

No universal "rain = Under" — test per league/venue/style. Link by stadium coords + kickoff time; keep forecast-issue vs observed separate.
- Wind >15mph: crosses/long shots degrade, GK parries↑ → chaotic low scoring. >20mph live = Under value before books adjust.
- Heavy rain >5mm/h: pass -4-6%, volume↓ → Under lean but handling errors↑. Light rain -1-2%.
- Snow: expectancy -15-20%. Heat WBGT>28°C: tempo↓, favours acclimatized late. Fog: GK errors↑.
- La Liga ML study: +weather raised 1X2 to 65.9%, draw-vs-decisive 79.3% (AUC 0.85).

Referee = most underweighted for cards/pens. Range 3.8→5.6 Y/game same season; ~0.8-1.2 attributable; 14% card variance = ref. Track per ref min 15 (ideally 30+) same comp: Y/90, R/match, fouls, pens/match (avg ~0.25 EPL, some 0.4+ vs 0.15), home-away delta, foul-to-card, added time when home trailing, Over%. Buckets: let-play <2.8, avg 3.0-3.8, strict 4.0+, card-happy 4.5+. ±0.5 cards or ±0.1 pens vs avg = soft at recreational books. Biases: home 15% fewer yellows + pens + stoppage when trailing; big teams ~110% deserved pens. Weight 70% current + 30% prior.

Pitch/travel/altitude: poor/heavy favours direct/physical, hurts press; long midweek away + Sat lunch = real disadvantage; altitude fades unacclimatized final 20'.

## 7. Implied / overround removal / CLV / value / Kelly / staking

```
Implied = 1 / decimal_odds
Overround = sum(Implied) - 1          # e.g. 2.10+3.40+3.60 = 104.8% → 4.8%
NoVig_p = Implied_i / sum(Implied)    # proportional baseline
FairOdds = 1 / NoVig_p                # 1.90+1.90 → 50% fair → 2.00
```

Advanced: additive, Shin (longshot correction), power. Differ >1pp on lopsided prices — pick one consistently, anchor to Pinnacle close.

CLV (most efficient estimate): `raw = YourOdds/CloseOdds - 1`, `no-vig = YourOdds/FairClose - 1`, `pp = CloseNoVigProb - YourNoVigProb`. Example take 2.05 close 1.95 both sides → raw +5.13%, fair 2.00 → no-vig +2.5%. Devigged: +3pp elite, +1-3 solid, 0-1 marginal, negative = leak. Track n≥300. Good bets lose, bad bets win — CLV separates skill from variance.

Value: `EV = p_model·odds - 1`, `Edge_pp = p_model - p_market_noVig`, `Fair = 1/p_model`. Bet if Fair > Available AND EV>0 with 3-5% min edge (estimation error). Value ≠ likely winner: 75% at 1.25 can be -EV.

Kelly (one outcome): `f* = (b·p - q)/b = (p·d - 1)/(d - 1)`, b=d-1, fraction of CURRENT bankroll. Example p=0.48 at 2.30 → 8% full; p=0.50 at 2.20 → 8.33% full → half 4.17%, quarter 2.08%. If ≤0 → NO BET. Full = max growth iff p perfect (never) with 40-60% drawdowns. Practice: quarter standard, half if 300+ calibrated, eighth/flat if new. Cap 1-3%/bet + 20-30% total exposure for simultaneous/correlated. Recalc from current bankroll, use accepted price, never chase (Kelly shrinks in drawdown — follow it).

Alternatives: flat $ (simple), flat 1-2% (best default, auto-scales), units 1-5 (1U=1%, max 3U unless CLV-proven). Hybrid: flat 1% + quarter-Kelly capped 3% only when edge>5% + XI known.

## 8. Pre-bet quant checklist

1. Model probs (DC λ/μ + Elo + xG rolling) → fair odds?
2. Market no-vig + overround + Pinnacle vs soft gap?
3. Edge ≥3-5%? EV>0?
4. H/A xG splits, not season avg? Last 6-8 xGD opp-adjusted?
5. Shots/box/SoT/big/PPDA/tilt align with totals pick?
6. Rest≤3? 3-in-8? Europe ±4d? Travel?
7. Projected XI vs best XI? Same-unit absences? GK/CB/DM?
8. Motivation both sides? Derby/cup rotation?
9. Ref Y/90 + pens (n≥15) for cards/pens?
10. Weather/pitch at venue-time (wind>15, rain>5mm/h, snow, heat, altitude)?
11. Tactical: press vs low block = bore risk? Wing vs slow FB = corners?
12. Bet now or wait XI? Market moving toward you?
13. Stake: quarter-Kelly + 1-3% cap + correlation cap?
14. Log model p, price, close target for CLV; stop rules set?

Bore-draw Under filter: both PPDA>14? avg shot >19y? 2+ 0-0/1-0 last5? safety-first managers? 4×Yes = pass on Over.
