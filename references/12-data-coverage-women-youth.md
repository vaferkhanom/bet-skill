# 12 — Full Football Coverage: Men's, Women's & Youth/Age-Group

> In scope: ALL football on 1xBet — men's leagues/cups, women's leagues/cups
> (WSL, NWSL, UWCL, internationals), youth/reserve/U17-U23, lower divisions.
> Settlement is IDENTICAL (90 min + stoppage; corners must be taken; cards/scorer
> rules per `references/01-1xbet-markets-rules.md`). What changes is DATA
> SPARSITY and VARIANCE — so the process tightens, not loosens.

## 1. Coverage per source (what to use when)

| Need | Men's top 5 | Women's top (WSL/NWSL/D1/UWCL) | Youth / lower / obscure |
|---|---|---|---|
| Odds + movement | OddsPortal, BetExplorer, Oddspedia | SAME three (coverage good for top women's) | OddsPortal/BetExplorer (thinner, slower) |
| xG / advanced | FBref, Understat, SofaScore | FBref (women's comps), SofaScore/FotMob (basic xG majors) — NO Understat | SofaScore/FotMob basics only; often no xG at all |
| Scores/H2H/fixtures | Flashscore, Soccerway | SAME (Flashscore + Soccerway cover women's + youth well) | SAME — your primary sources here |
| Tables/form | FootyStats (hit-rates), SoccerSTATS | FootyStats (women's leagues included), Soccerway | Soccerway + Flashscore; FootyStats where listed |
| Lineups/news | Official clubs, RotoWire, Transfermarkt | Official club sites + league sites (WSL/NWSL), Transfermarkt women, club socials | Official academy/league pages + club socials; expect late/thin news |
| Refs/cards | FootyMetrics, Statz.ai | Soccerway ref data + league sites (small samples — see §3) | Skip ref modeling below national youth cups |

Rule: women's top-flight ≈ men's second tier for data richness. Youth/obscure ≈ model with goals + H/A splits only.

## 2. Modeling adjustments (sparser data → humbler model)

- **Minimum sample:** men 8-10 games; women top-flight 8-10 (shorter seasons — use last season + current, decayed); youth 6+ with SAME squad (lineups rotate heavily — check team sheets, squads change weekly).
- **No xG available?** Fall back to: goals scored/conceded (H/A split) → simple Poisson λ (§02 method) + league-average totals for that competition. State "no-xG model" in the report and raise the edge bar.
- **Higher variance competitions** (youth cups, early women's cup rounds, mismatches): scorelines spread wider — prefer TOTALS and AH over 1X2/Exact Score; never HT/FT turnarounds here.
- **Squad volatility (youth):** first-team call-ups, rotation, trialists. If XI unknown and competition is developmental → WAIT for XI or PASS. Friendly/u-friendly tournaments with nothing at stake = PASS by default.
- **Motivation reads differ:** youth = development over result (late subs, experiments); women's cups early rounds = heavy rotation vs minnows (favorites -3.5+ handicaps are efficient — don't lay blind chalk).

## 3. Staking + edge bars by coverage tier

| Tier | Edge required | Stake | Notes |
|---|---|---|---|
| Men's specialist league (your 1-2) | ≥3-5pp | 1-2% | full process |
| Women's top-flight | ≥4-6pp | 0.5-1% | thinner xG, faster limits |
| Youth / lower / obscure | ≥6-8pp | 0.5% max, singles only | no-xG model, XI risk |
| Friendlies / exhibitions | NO BET | 0 | watch only |

1xBet limits women's/youth markets FASTER when you win — spread volume, use them as secondary edges, keep the bankroll core in specialist men's leagues. Log coverage tier in the tracker (add column `Tier`) and review ROI per tier monthly — cut any tier with negative CLV after 100 bets.

## 4. What Hermes always states for women's/youth analyses

Competition + tier, data available vs missing ([N/A] where absent — never fill gaps with men's-team priors), squad-news confidence, edge bar applied, and the smaller stake. Same report template (SKILL.md §7), same probabilistic language, same 18+ line.
