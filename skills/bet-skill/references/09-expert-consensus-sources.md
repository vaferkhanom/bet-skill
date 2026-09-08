# 09 — Expert Consensus & Trustworthy Sources (weighting guide)

> No analyst or site replaces your model vs no-vig price. Consensus upgrades confidence; it never creates edge alone.

## 1. Weight ladder (highest → zero)

1. **Sharp market (weight 3):** Pinnacle no-vig close, Betfair Exchange price, OddsPortal/BetExplorer >70% of books dropping the same way. Treat persistent CLV-beating moves as the strongest "expert" available.
2. **Pinnacle-verified records (weight 2):** tipsters tracked against Pinnacle odds with full timestamped win+loss logs, 400+ bets, ROI + CLV + drawdown published (model: Bet2Invest-style Pinnacle certification; Tipstrr/Pyckio-style verified histories). Require: pre-kick timestamps, losers visible, realistic 52-57% / 1-5% yield — never 90%+.
3. **Reputable editorial (weight 1, context only):** Pinnacle Betting Resources (market mechanics/math), Action Network (projections staff, e.g. long-tenured modelers), Covers (beat writers per sport, transparent tracked records). Use for injury/weather/market-behavior context and methodology explainers — not as picks to copy.
4. **Data platforms (weight 1, inputs):** FBref/Understat (xG), OddsPortal/BetExplorer/Oddspedia (movement), official club/league feeds + RotoWire-style presser digests + Transfermarkt/MissesNextMatch (news), FootyMetrics/Statz.ai (refs), Windy/AccuWeather (totals). See `04-websites-toolstack.md`.
5. **Prediction aggregators (weight 0.5, convergence only):** Forebet/PredictZ/Vitibet/WindrawWin — count agreement as a weak signal, never a stake reason.
6. **Zero weight / block:** "fixed matches", "VIP 95%", paywalled screenshots-only tips, Martingale/recovery sellers, anyone hiding losers or demanding crypto/gift-card payment.

## 2. Verification checklist (before citing any analyst)

- [ ] Timestamped BEFORE kickoff? Full history incl. losses? Sample ≥400?
- [ ] Odds source stated (Pinnacle/Exchange = good; "best odds" cherry-pick = bad)?
- [ ] ROI + CLV + max drawdown shown? Staking consistent (no varying units to fake yield)?
- [ ] Sport/league specialization stated? Line-movement reasoning, not narratives?
- [ ] Independent platform (not their own screenshots)? Traceable payments, no timer pressure?

Fail any → treat as entertainment, stake 0.

## 3. How Hermes cites consensus (template)

```markdown
**Consensus:** Pinnacle [x] → [y] ([n]% books dropping) agrees with model lean [..]. Verified record [name/platform, n bets, ROI x%, CLV +xpp] aligns on [market]. Editorial [outlet] notes [injury/weather context]. Weight: [3/2/1]. Against: [sharp move opposite? model disagreement?].
```

## 4. Red-flag phrases (instant disqualify)

"Fixed / guaranteed / 100% / can't lose / limited slots / pay in crypto now / deleted losing post / opposite picks to different groups / unlock fee". Real edges are small, boring, and fully logged — including losing months.
