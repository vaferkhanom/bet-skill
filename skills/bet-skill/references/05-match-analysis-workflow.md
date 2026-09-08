# 05 — Match Analysis Workflow, Checklists & Output Format

> Use for EVERY match. Tag facts [API] direct, [ODDS] from odds, [IND] computed, [N/A] missing — never invent.

## 1. Pre-match pipeline (30-15 min before KO, re-check XI 60-75' pre-KO)

```
1. Parse request → home, away, competition, date/time UTC, pre-match vs live.
2. Confirm 1xBet exact market names present + settlement basis (90 min vs ET/pens).
3. Odds snapshot (quote time): 1X2, O2.5, BTTS from 1xBet + best on OddsPortal/BetExplorer/Oddspedia (opening vs current, % drop, >70% dropping = sharp).
4. Stats: FBref + Understat last 8-10 H/A split (xGF/xGA/xGD, shots/box/SoT%, big chances, PPDA, tilt) + FootyStats hit-rates + Soccerway H2H last 3-5.
5. News: RotoWire/presser → Transfermarkt/MissesNextMatch → Flashscore predicted XI → official XI. Note same-unit absences, GK/CB/DM, suspensions.
6. Context: standings + stakes both sides (title/Europe/relegation/dead-rubber/derby/cup rotation), rest≤3? 3-in-8? Europe±4d? travel/zones? NEXT match rotation?
7. Ref (cards/pens only, n≥15 ideally 30+): Y/90, pens/match, H/A delta. Weather at venue-time (wind>15mph, rain>5mm/h, snow, WBGT>28°C, altitude) for totals.
8. Model: Poisson/DC λ/μ (+Elo) → 1X2/O-U/BTTS. Adjust λ/μ for XI, congestion, motivation, weather, tactical matchup (press vs low-block = bore risk; wing vs slow FB = corners).
9. De-vig book → edge/EV. Require ≥+3-5pp + EV>0. Write 3 reasons bet is WRONG + bore-draw check.
10. Stake: 1% flat (2% max, 0.5-1% HT/FT/live), or ¼ Kelly capped 1-3%. Daily stop 5U/5%. Log row + CLV target.
```

## 2. Live pipeline (max 1-2 positions, 0.5-1%)

```
Score + minute → xG live (SofaScore/FotMob) + momentum (shots/SoT/box/corners since 60', possession last 15', subs/fresh legs) + 1xBet tracker.
Ask: does score reflect xG? Is surge structural (box entries) or sterile (long shots)? Do stakes demand a goal (both need result) or suit draw (dead rubber)?
Enter 70-77' only with momentum + stakes. Prefer Next Goal / Over 0.5 76-90' / Asian live Over 1.0 (refund if exactly 1).
Partial cash-out / manual hedge only for variance (2-0 up 70' big stake; high-variance dog now 56%). Manual hedge at another book beats cash-out (4-5% vs 4-12%).
```

## 3. Bore-draw Under filter (pass on Over if 4×Yes)

- Both PPDA >14? Avg shot distance >19y? 2+ 0-0/1-0 in last5? Safety-first managers / second-leg protect / derby cage? If Yes×4 → NO Over, consider Under/cards or skip side.

## 4. Motivation matrix (both sides)

Title/UCL raise; relegation 6-pointers volatile (Unders+cards > side); mid-table nothing vs motivated = fade coasters away; confirmed champions/safe/relegated = sharp drop; derbies compress + cards up; cup/Europe priority = league rotation. Must-win ≠ will-win.

## 5. Output template (copy-paste)

```markdown
# [Home] vs [Away] — [Competition] — [Date UTC]

**Status:** pre-match | live [minute + score]
**1xBet snapshot:** 1X2 [1/X/2] | O2.5 [over/under] | BTTS [yes/no] (quoted [time])
**Model:** Home [x]% | Draw [x]% | Away [x]% | O2.5 [x]% | BTTS [x]%
**No-vig book:** Home [x]% | Draw [x]% | Away [x]% (overround [x]%)
**Edge:** [market]: model [x]% vs book [x]% = [+x.xpp / EV +x.x%] → BET / NO BET
**Stake:** [x]% bankroll ([method + cap]) | BR: [amount]

## Why (tagged)
- Form last 8 H/A split, xG/xGA/xGD, shots/box/SoT, PPDA/tilt [IND]
- Rest/congestion/Europe±4d/travel, motivation both sides, XI vs best XI [API]/[IND]
- Ref Y/90 + pens (n) [API], weather/pitch venue-time [API], tactical matchup [IND]
- Odds movement: opening→current, % drop, sharp? [ODDS]

## Risks / invalidation
- 3 reasons WRONG + bore check + rotation risk + what score/lineup would void edge

## 1xBet execution
- Exact market + slip type (Single preferred) + hedge/cash-out plan
- If acca/system: compounded margin math shown

*18+ only. EV not certainty. Never stake more than you can afford to lose.*
```

## 6. Tracker header (Google Sheets/Excel, log immediately, every bet)

| Date | League | Match | Market | Pick | Model% | Odds (book) | Closing no-vig | CLV% | Stake (€+%) | Result | P/L | Running BR | Reason + counter |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

Dashboard: bets, win%, ROI, profit by league/market/book, CLV+%, streak, calibration (said 60% → won 60%?). Review weekly CLV, monthly cuts, quarterly kill rule (neg CLV + neg yield after 300 → abandon).

## 7. Verification before answering

- [ ] Competition/date/time + exact 1xBet markets confirmed?
- [ ] 90-min vs ET/pens stated? AH push behavior? Cards/corners/scorer rules?
- [ ] Model% vs no-vig% vs edge/EV + safety margin?
- [ ] H/A splits, 8+ sample, opp-adjusted?
- [ ] XI/news, motivation, rest, ref n≥15, weather checked or [N/A]?
- [ ] Stake 1-2% cap 3%, no Martingale, no acca without per-leg +EV?
- [ ] 3 counters + invalidation listed? CLV target + log row? 18+/risk line, no guaranteed/fixed?
