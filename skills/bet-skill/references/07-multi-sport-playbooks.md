# 07 — Multi-Sport Playbooks (1xBet settlement + what to model)

> Football bible stays in `01`/`02`. This file routes every OTHER sport. Always confirm the `i` tooltip — never guess settlement.

## 1. Basketball (NBA / FIBA / NCAA / 3x3)

- **1xBet:** match-winner markets **INCLUDE overtime** unless market says quarter/half. Quarter/half handicaps/totals = that period only, OT excluded. 48-min games need **40 min** played, 40-min games **35 min**, else void unless decided. Specials (highest-scoring quarter, most points in a half, first rebound, player stats) per official stats; ties in quarter markets exclude OT.
- **Model:** pace (possessions/48), ORtg/DRtg last 8 (H/A split), eFG% + TOV% + OREB%, rest (B2B, 3-in-4, travel/time zones), injuries to primary creators (usage% + on/off), motivation (playoff race vs tanking/resting starters).
- **Markets:** spread (lowest margin), totals (pace-driven), 1H/quarter splits, player points/rebounds/assists vs usage + matchup.
- **Websites:** official NBA injury report + team beat writers → Flashscore → OddsPortal movement; pace/ratings from reputable stats hubs; referee crew for foul/total leans (sample 20+).

## 2. Tennis (ATP / WTA / Slams / Davis Cup)

- **1xBet:** retirement/walkover = void unless the market's outcome already decided (e.g. first set winner stands if set completed). Check exact market: match-winner voids on retirement; set/game handicaps and totals void unless unconditionally decided. Live "next point/game" mirrors pre-match plus in-play only props.
- **Model:** surface-specific Elo (clay/hard/grass split, min 10 matches), hold% + break% last 12 months per surface, recent form (last 8, retirements/injury flags), fatigue (5-set history, matches last 7 days, travel), outdoor wind/heat, lefty vs 1HBH matchup, motivation (Slam vs 250, Davis Cup home).
- **Markets:** match-winner (2-way, low margin), game handicap, set betting, total games, live break markets (0.5-1% max).
- **Websites:** official draws/order of play + press → head-to-head per surface → OddsPortal steam; weather for outdoor totals.

## 3. Cricket (Test / ODI / T20 + IPL / BBL / CPL)

- **1xBet:** format defines everything. Match-winner, top batsman/bowler, total runs/wickets, innings scores, session markets. Rain/DLS can void or settle per official result — check market tooltip. Live adds "next wicket/method".
- **Model:** format split (never mix Test with T20), venue par score + toss bias, pitch (green/dry/dew) + weather/DLS risk, team news (XI, bowling attack fit), recent scoring rates + powerplay/death economy, motivation (series state, NRR scenarios).
- **Markets:** match-winner (2-way + draw in Tests), totals (runs), top batsman (high variance — 0.5% max), innings bands.
- **Websites:** official boards (BCCI/ECB/ICC) + toss news → pitch reports → OddsPortal; Bet Builder for correlated cricket combos only if priced.

## 4. Ice Hockey (NHL / KHL / internationals)

- **1xBet:** match-winner usually **includes OT + shootout**; "regular time" (60-min) markets exclude them — read the label. TOTO Ice Hockey exists as pool. Abandoned/postponed per general 48h/5h rules.
- **Model:** 5v5 xG share last 10, goalie CONFIRMED (starter vs backup swings totals ~0.5 goal), rest/B2B + travel, special teams (PP%/PK%), motivation (playoff clinch/elimination).
- **Markets:** moneyline (OT-incl vs 60-min — pick deliberately), puck line (-1.5), totals (goalie-driven), period markets.
- **Websites:** official starting-goalie announcements (highest weight) → line combos → OddsPortal.

## 5. Volleyball (indoor / beach)

- **1xBet:** sets-based; retirement rules per market (completed sets stand, rest void). Beach (best-of-3) vs indoor (best-of-5) differ.
- **Model:** serve/receive efficiency, attack% + block/set quality, rotation/injury news, travel + back-to-back tournaments, motivation (qualification vs dead rubber).
- **Markets:** match-winner, set handicap, total sets/points, live set-winner (momentum real — 0.5-1%).

## 6. MMA / UFC / Boxing

- **1xBet:** method (KO/Sub/Decision) + round markets; late card changes → void affected. Draw rare but priced.
- **Model:** styles (wrestler vs striker, takedown D% vs accuracy), weight-cut news (missed weight = red flag), camp/coach changes, age + damage absorbed, 5-round cardio.
- **Markets:** moneyline (2-way), method, round bands, goes-distance Yes/No. Small sample — 0.5-1% max, specialists only.
- **Sources:** official weigh-ins + reputable MMA media (e.g. Covers UFC team) for context; Pinnacle/Exchange move = sharp.

## 7. Esports (CS2 / Dota 2 / LoL / FIFA / NBA2K)

- **1xBet:** patch/version dependent; map markets (winner/handicap/totals). Roster subs can void player props. Huge menu (Dota, CS, LoL ARAM, FIFA, etc.) — each with own rules §10.40+.
- **Model:** current patch meta (last 30 days only), map pool win% (min 8 maps), roster stability, LAN vs online, motivation (Major qualifier vs showmatch).
- **Markets:** match-winner, map handicap, map totals. High variance — 0.5% max until 200+ tracked bets in ONE title.
- **Sources:** official tournament pages + patch notes + team announcements; Exchange liquidity thin — demand bigger edge (≥6-8pp).

## 8. Universal cross-sport rules

- 2-way markets (no draw) almost always cheaper margin than 3-way equivalents.
- Confirm OT/retirement/DLS handling BEFORE staking — three most common void disputes.
- Specialize: ONE title/league + ONE market for 80%+ volume; everything else fun-sized.
- Live: max 1-2 slots, 0.5-1%; hedge at another book beats cash-out.
