# 1xBet Football — ALL Markets & Bet Types Reference Catalog

**Primary source (primary/trust anchor):** Official 1xBet Betting Rules, 260-page PDF, served from the official rules endpoint
`https://1xbet.cd/web-api/rulespdf` (also exists as `https://bol.1xbet.com/rulespdf`; the same doc underpins `1xbet.com/en/information/rules` — the rules homepage at 1xbet.com geo-blocks non-licensed jurisdictions, so the PDF endpoint on licensed regional domains is the retrievable copy).

**Document structure confirmed from the PDF (2026 edition):**
1. General Terms and Definitions · 2. General Terms · 3. General betting rules (3.1 Bet slip sale [Cash Out], 3.2 Bet slip editing [Edit Bet], 3.3 Powerbet) · 4. Types of bets (4.1 Single … 4.11 Patent) · 5. Self-Exclusion · 6. Dispute Resolution · 7. Accounts, Payouts & Bonuses · 8. Live Betting · 9. Match Results, Dates and Starting Times · 10. Rules on sports (10.25 = Football; 10.62 = Bet Constructor) · 11. Available Markets (Outcomes) · 12. Extra bets · 13. Examples (13.4 Asian handicap, 13.6 Asian total…) · 14–22 TOTO products · 23 Main sources of information.

Secondary sources: 1xbets.bet (mirror reproducing live match-board data: "Total (106 markets), Handicap (18), Popular (313), Players (8), Goals (240)" on a World Cup fixture; 1X2 2UP odds shown), 1xbet.onl football guide (live/abandonment rules), Google-indexed rule text from 1xbet.ng / 1xbet.co.ke / so.1xbet.com / 1xbet.ci.

All quotes below are from the official PDF unless noted.

---

## 0. Global settlement basis (applies to every market unless stated)

| Rule | Detail (source: Rules §10.25, §3, §9) |
|---|---|
| Regular time | 90 min (2×45 + referee's added time). ET and shootouts count **only** for markets labeled "extra time" or: "To Qualify (For The Next Round)", "League Promotion/Relegation", "Winner Of The Tournament" and similar (§10.25.1) |
| Validity of match | At least **80 minutes** must elapse for bets to stand — except markets already unconditionally decided at the time of stoppage (§10.25.2) |
| Bets after KO (pre-match) | Settled at odds 1 (void) unless live; in accas the leg becomes 1.00 (§9.6) |
| Postponement (prematch) | Postponed/rescheduled **>48 h** → void (odds 1), at bookmaker's discretion may keep standing (§9.8) |
| Live interruption | If match continues **within 5 hours** of start → all bets stand; otherwise void unless already determined (§9.9) |
| Abandonment | Outcomes already determined (e.g., 1st half markets, first goal & its time) count; everything else void (§9.10) |
| Team withdrawal / no-show | All bets void (odds 1); forfeit = refund (§9, §3) |
| Player DNP | Player markets void at 1.00 unless the player appears (multiple clauses: §10.25.24–27, §10.25.55, §10.25.67; §9.13) |
| Card cutoff | No YC/RC shown to outfield players/GK **after the final whistle** counts; deferred cards count for the half in which the offence occurred (§10.25.13) |
| 2nd yellow | Does **not** count as a second YC; counts as one red (RC = 2 YC in YRC markets; max 3 "cards" per player in YRC markets; max 2 in Total Cards markets) (§10.25.11, §10.25.14, §10.25.47) |
| Corners | Only **taken** corners count; retaken corner = 1 corner; Russian Premier League corner counts settled 3 days after the match from official sources (§10.25.4, §10.25.15) |
| Posts/crossbar | Count only if ball stays in play after hitting woodwork; excluded if ball goes out or a goal is scored; shots blocked or hitting woodwork are NOT "shots on target" (§10.25.16–17) |
| Related outcomes | Not combinable in one acca; if included, lowest-odds legs excluded (§4.2.2–3) |
| Wrong settlement | Recalculated; bets placed in the window stay valid (§3) |
| Odds/limit circumvention | Correctly-predicted multiple bets on same outcome exceeding max stake → excess settled at 1.00 (§3.5) |
| Limits | Min stake $0.30/€0.20; max return €50,000 per bet; lowest per-leg max applies in accas/systems (§3.1–3) |
| Timed/interval markets | Live YC-in-interval bets ignore added time (85:00–88:59 example, 90+1 = loss); QUICK-EVENT interval conventions: 40:00–44:59 excl. stoppage, 40:00–49:59 incl., 85:00–89:59 excl., goal in 20th min counts for 10:00–19:59; "First To Happen"/1-minute markets: throw-ins/corners/goal-kicks/cards/free-kicks use time **awarded**, fouls/offsides/goals use time it **happened** (§10.25.12, 20–23) |

Abbreviations used across the line: CK (corners), ACE (aces), SO (sendings-off), PT (penalty time), YC (yellow cards), YRC (yellow+red cards), MS (misses), SOT (shots on target), OFF (offsides), F (fouls), S (series) (§3.19).

---

## 1. Match-page MARKET GROUPS (UI tabs on a football event page)

Confirmed from live match-board documentation (1xbets.bet match-board walkthrough of a WC 2026 fixture, 1,461 markets) and 1xBet NG/line pages:

| Group (tab) | Confirmed evidence | Typical contents |
|---|---|---|
| **Popular** | 313 markets on WC fixture (1xbets.bet) | 1X2, Double Chance, Handicap, Total, BTTS, next-goal, HT/FT, combos, team totals, DNB, 2UP, To Qualify |
| **1X2** | tab named on board; "1X2" + "1X2 (2UP)" shown with separate odds (W1 1.631/X 4.18/W2 6.14 vs 2UP 1.556/4.18/5.85) | 1X2; 1X2 2UP (early payout on 2-goal lead) |
| **Total** | 106 markets | Over/Under goals, Asian totals, 3-way totals, team/individual totals, exact totals, intervals, goal-minute totals |
| **Handicap** | 18 markets | Asian/whole/half/quarter handicaps, European (3-way) handicap, 2-way handicap (−1.5 style), 2UP variants |
| **Goals** | 240 markets | BTTS, exact score, goal timing, scorers, goal methods, races, intervals, combos |
| **Players** | 8 markets on that fixture | Player goalscorer props, player match-ups, cards/shots props |
| **1st Half / 2nd Half (Halves)** | present on event pages ("1st/2nd Half" per user spec; half markets documented in §11.15, §12.1, 10.25.32) | HT result/total/handicap/DC/CS, 2nd-half markets |
| **Corners** | group documented (CK abbreviation; 10.25.8–10, 33) | total, team, handicap, race, first/last/next, per-half, multi-corner |
| **Cards** | group documented (YC/YRC; 10.25.11–14, 47) | totals, team, player, first/last, interval, points |
| **Specials** | group documented (§10.25.38–50, §11.41 Special-Bets combos) | win to nil, win both halves, clean sheet, missed penalties, manager/transfer/FIFA specials |
| **Statistics** | group documented (SOT, offsides, fouls, woodwork, substitutions, distance covered, goalkeeper touches, VAR — 10.25.15–19, 58–61, 77–80) | SOT, saves implied via SOT, fouls, offsides, throw-ins, dribbles, aerial duels, tackles (whoscored.com), distance, medical-team entries, referee-duel points |
| **Intervals / Intervals group** | time-interval conventions (§10.25.20–23); "Total In The Interval", "Outcome In The Interval", "Goal In Time Interval", "First Goal Time" | 0–15, 16–30, 31–HT, HT–60, 61–75, 76–FT-style interval result/total/BTTS/next-goal |
| Others seen on boards | — | "Team to Qualify for the Next Stage" (knockouts), Cup/tournament outrights, "Alternative matches" (live), QUICK EVENTS, Post-Match vs Live, Bet Generator (auto-acca) |

---

## 2. THE MARKETS — exhaustive enumeration with 1xBet notation & settlement notes

### 2.1 Result / match-winner family
| Market (1xBet naming) | Notation | Settlement / notes |
|---|---|---|
| Match Result (1X2) | `1` = Team 1 win, `X` = draw, `2` = Team 2 win (§11.1–3) | Regular time incl. stoppage |
| 1X2 2UP | Same 3 outcomes, "2UP" suffix | Early settlement if backed team leads by 2 at any point; priced differently (odds example W1 1.556 vs 1.631 standard — 1xbets.bet board). Payout-on-2-goal-lead accumulator protection promo (site feature) |
| Double Chance | `1X` (T1 win or draw), `12` (no draw), `X2` (T2 win or draw) (§11.4–6) | 90 min |
| Draw No Bet / "Win Or Draw (refund)" style | e.g. `X Or 2 (Home Win - Refund) – 2` (§11.38) | If T1 wins → refund (odds 1) |
| Handicap Result (European handicap, 3-way) | `Handicap [0:1] W2 / X / W1` (§12.16) | Score adjusted by stated goal start; three outcomes, no push: 2:1 final → [0:1] W2 loses (2:2), X wins, [1:0] W1 wins (3:1). "Whole-number" lines can void: handicap draw → odds 1 (§11.7) |
| 2-way handicap | e.g. `F1(-1.5)` / Handicap −1.5, +1.5 | Win/lose only |
| Asian Handicap | quarter lines split into two bets: `HANDICAP (+1.25)` = `(+1)` + `(+1.5)`, half stake each, equal odds (§13.4) | Push → stake refund. Acca containing AH doubles the number of combinations (§13.5: 3.25-total acca at 3-0 → four €25 sub-bets, one refunded) |
| Asian Handicap (whole) | `HANDICAP (−1)` etc. | Exact margin = handicap → refund |
| Next goal, handicap | "predict which team will score the next goal [with handicap]; if there is no next goal, settled at odds 1" (§10.25.75) | Live |
| To Qualify (For The Next Round) | incl. group-stage "To Qualify For The Next Round (group stage)" (§10.62 nearby §10.25; rule §10.25.1) | ET and shootouts **count** |
| Team to Qualify for the Next Stage | "Team 1 1.30 / Team 2 3.45" (1xbets.bet WC fixture) | Reflects progression incl. ET/pens |
| Winner Of The Tournament / Promotion / Relegation / League | outright futures | ET+shootouts count |
| Higher At The End Of The Tournament (teams) | "Team 1/Team 2" pair market | Both eliminated in groups → settled by group place; same place → 1.00; team plays no match → 1.00; both out at same playoff stage → 1.00 (§10.25.5, §11.17, §10.25.64) |
| Which Team Will Score More Goals / Score (Concede) Most (Least) | tournament-long | Includes ET, excludes shootouts (§10.25.6) |
| 1st and 2nd Place In The Group | named teams in exact order (§11.33) | — |
| Home – Away (round-based cross-matches) | e.g. `Home - Away, Draw 2:2 - Yes`; `Home - Away, First Match Goal From 1 To 5 Minute - Yes`; `Home - Away, Half Time-Full Time W2W1 Or W1W2 - Yes`; `Home - Away, Team Will Score First Goal The Earliest` (§11.18) | Settled on that matchday/round; simultaneous first goals all settled as wins; canceled match in round → 1.00 for undecided parts |
| To Be Higher At The End Of The Championship (players) | player pair market | Official tournament site stats; no shootouts; 1.00 if player misses all matches (§11.16) |

### 2.2 Totals family
| Market | Notation | Notes |
|---|---|---|
| Total Over/Under | `Total Over 2.5`, `Total Under 2.5` (§11.8) | Exact hit → odds 1 (push). Playing time per sport rules |
| 3-way Total | `Total Under 123 (3way)`, `Total Exactly 123 (3way)`, `Total 123 Over (3way)` (§11.9) | No refund on exact hit; only "Exactly" wins |
| Asian Total | multiple of 0.25 (not 0.5): `TOTAL (1.75) UNDER` = (1.5)+(2), half stake each (§13.6) | Push on the integer half |
| Team Total / Individual Total | "Team 1 Total Over 1.5" etc. | **No own goal counts** toward individual/team totals (§11.8) |
| Both Teams' Totals combo | "Team 1 Total + Team 2 Total" O/U combos (Goals group) | Same own-goal exclusion |
| Total (3way "odd/even") | Total Even/Odd (site line) | — |
| Total Goals bands | `Multi goal 2-4` — wins if 2, 3 or 4 goals (§10.25.74) | "Exact Goals" / Exact Total = precise number |
| Total In Interval (QUICK EVENTS) | `Total In The Interval From () To () Minute`, e.g. 0–15, 16–30… (§10.25.21; §11.10) | Interval stoppage conventions per §0 |
| Total Interval (score-band style) | `Total From 0 to 1` — combined score 0 or 1 wins; `No Goals` wins if 0:0 (§11.10) | — |
| Total Goal Minutes | Sum of minutes of all goals; 13+25+47 = 85 (§10.25.20-nn; §11.19; §10.25.20) | Regular time; Over/Under e.g. 140.5 |
| Official Added Time Total | Over/Under minutes added to each half (§12.23) | — |
| Highest/Lowest Scoring Quarter | `Highest Scoring Quarter – Total Under ()` (§11.26–27) | Ties: no refunds, settle on the total |
| Highest Scoring Period | 1st Half / 2nd Half / Draw (§10.25.35; §11.28) | Indeterminate → 1.00 on tied periods, others lose |
| Team With Most Corners-style Points analogs | "Points" team performance markets — see 2.7 | — |

### 2.3 Handicap family — extra entries
| Market | Notes |
|---|---|
| Handicap (2-way & 3-way, all lines) | see 2.1 |
| Handicap In The Interval (QUICK EVENTS) | e.g. "Handicap In The Interval 40:00–49:59" (§10.25.21) |
| Winner with Handicap (season-long) | Season win with cumulative handicap points; favorite at 0 (§11.40) |
| Players, Match-Ups, Handicaps | players' goal totals with handicap; own goals excluded; non-starters → 1.00 (§11.31) |
| Player vs Team | player goals vs team goals; refund if player not in starting XI; dismissal/substitution during match doesn't void (§10.25.67) |
| Team Match-Ups (Teams, Match-Ups) | which named team scores more (§12.17) |

### 2.4 Goals group (timing, scorers, methods, BTTS, score)
| Market | Notation / example | Settlement |
|---|---|---|
| Both Teams To Score | BTTS Yes/No (§12.5) | Yes wins if each team scores ≥1 |
| BTTS + Total combo | e.g. "Both Teams To Score – Yes + Over 2.5" (Goals group combos; §11.41 mechanics) | All legs must win; partial correct = loss, no refund |
| 1X2 + BTTS combo | "W1 and Both Teams to Score – Yes @ 3.0" (1xbets.bet fixture) | — |
| 1X2 + Total combo | `Result + Total Goals` — predict winner AND total (§11.13) | — |
| DC + Total combos | "1X + Total Over 2.5" etc. (combos per §11.41) | — |
| Correct Score | exact score in regular time (§11.11) | Includes live "next score" boards; `Any Other Score` = any score not listed (§11.37, §12.35) |
| Correct Score — live "Any Other Score" group | 3 outcome groups set by current score, e.g. at 0-1: [2-1/3-1/3-2], [1-2/1-3/2-3], Any Other (§11.37) | — |
| HT/FT | `W1W2` = Team 1 wins 1st half, Team 2 wins match; all 9 combos W1W1…X2X2 (§11.12) | Regular time |
| 1st Half–Match | result of 1st half + result of match (§12.1) | — |
| First/Last Goalscorer (player) | "To Score A Goal (David Villa)" (§10.25.24); `() To Score A Goal At Any Time` (§10.25.26) | Own goals don't count; non-participant → 1.00; **live** scorer bets on entered subs settle normally; pre-match on subs → 1.00 |
| First Goalscorer — own-goal rule | If first goal is an OG, first-goalscorer settles on the scorer of the 2nd goal; all-OG match → "No Goals" wins (§11.24) | — |
| Last Goalscorer — own-goal rule | last OG → penultimate goal counts; all OG → No Goals (§11.25) | — |
| First Goal And Win With Score | "Player To Score First Goal And Team To Win With The Score" — e.g. "Adam Lallana To Score First Goal And Team 1 To Win 1-0 – Yes" (§10.25.42) | Player OG after first goal → 1.00 on that player; non-participant → 1.00 |
| Player To Score First Goal | "To Score First Goal (David Villa)" (§10.25.25) | If player enters after 1st goal or DNP → 1.00 |
| Player Will Score Over/Under 0.5 | player goals O/U (§10.25.27) | Starting XI only; sub → 1.00 |
| Brace / Hat-Trick / Poker | "A Player To Score Two Goals (Brace)", "Hat-Trick", "A Player Scores Four Goals (Poker)" (§10.25.29; §12.21) | Exactly-N; own goals excluded; hat-trick scored → "Brace – Yes" loses |
| Players, Special, Total | combined goals of named players (§11.32) | OGs excluded |
| Multi-Scorer combos | "X. Messi to score and Y. Mbappe to score" style (§11.41 Special-Bets combos) | All must win |
| Goalkeeper To Score | GK anytime/first scorer (site specials; OGs excluded per goalscorer rules) | — |
| Goal methods — How The Goal Will Be Scored | Own Goal; From A Direct Free Kick (incl. direct-from-corner); Penalty; With A Header (OG excluded); By Kicking (excl. FK/penalty/OG; any body part except head counts); No Goal (§10.25.53) | First (or next) goal; non-scored goal number → loss (§12.40) |
| Goal 1 Scored With A Header | Yes/No; 0:0 or OG first → "No" wins (§12.26) | — |
| Left/right-footed & headed goal counts | season/player props; no OGs (§10.25.71) | — |
| Free Kick (goal markets) | direct AND indirect FKs count, incl. FK after offside (§10.25.72) | — |
| Set Piece Goal | ball touched ≤2 times (incl. restart kick) by either team from restart to goal; GK touch excluded; restarts: kick-off, throw-in, DFK, IFK, corner, goal kick, penalty, dropped ball (§10.25.69) | — |
| Goal From Outside The Penalty Area | open play only (§10.25.70) | — |
| First Team To Score | "To Score First Goal" (§12.3); OG counts for the team benefiting (§12.3) | 0:0 → all lose |
| To Score First And Win The Match | team to score 1st and win (§12.27; §10.25-nn) | 0:0 → Yes loses |
| Time Of First Goal | `First Match Goal From () To () Minute`; added time included (§12.33; §11.21) | — |
| Goal In Time Interval | team-total in interval; stoppage included unless stated (§10.25.20) | — |
| Last Goal From () To () Minute | added time included (§11.22) | — |
| No Last Goal | wins only on 0:0 (§11.23) | — |
| Next Goal | team/`No Goal` | No further goal → 1.00 (§10.25.75) |
| Race To N Goals | `Team 1 To Win Race To 15 Points`-style; `Neither Team To Win Race To N` (§11.29) | Refund if a side refuses to continue before reaching N |
| Goal () Up To 78 Min – Yes | team scores by 78th minute (§11.14) | — |
| Team to Score First/Last Goal Up To () Minute | e.g. "Team to Score First Goal Up To 30 Min" (§10.25.20) | — |
| Time With No Goals / Duration of Tied Score / Time In Lead | `Draw For Under 19.5 Mins.`, `Team 1 To Lead Over 13.5 Minutes` (§12.34; §10.25.78) | Regular time only (no added time); completed minutes; goal at 90+ = scored in 90th |
| Remaining Time Outcome | `1X After Score 3-2` — outcome of the rest of match from quoted score (§11.35) | — |
| Run Of Play | `Lead – Win / Lead – Draw / Lead – Lose` — first team to lead + final result (§12.32) | — |
| Come From Behind And Win | Yes/No; draw → Yes loses (§12.24) | — |
| Either Team Not To Take The Lead and Avoid Defeat / …and Win | (§12.25) | — |
| Either/Both Goalkeepers To Touch Ball In First N Minutes | any GK touch counts even off-stream moments (§12.36) | — |
| Scores In Each Half / Halves Match-Ups | equal or higher half score (§11.15; §12.6) | — |
| Draw In At Least One Half | `(1-0; 0-1)` → "No" wins (§12.8) | — |
| Leader After Total Points Scored | `Team 1 To Win After 10 Points` (§12.37) | — |
| Team 1/2 Player Has The Ball At The Final Whistle | possession at FT (§10.25.36) | — |
| Who Will Kick Off The Match? | (§12.9) | — |
| First To Happen | "Yellow Card Or Goal", "First To Happen: throw-in/corner/goal-kick/foul/offside/card/substitution/goal" sets; (Costa D.) Will Not Score A Penalty / Get Red-Yellow Card / Be Substituted / Score (§12.20; §10.25.22, 37) | DNP of named player → 1.00 |
| Team 1/2 Player Has… (possession) | see above | — |
| Position Of Goalscorer | scorer's position per transfermarkt; national teams: official starting list (§10.25.54) | — |

### 2.5 Halves family (1st/2nd Half group)
| Market | Notes |
|---|---|
| Half: 1X2 — "Team 2 To Win First Half - Yes" (§10.25.32) | per-half result |
| 1st Half–Match (§12.1) | combo |
| HT/FT (§11.12) | 9 outcomes |
| First Half Total / 2nd Half Total O/U | half totals (UI) |
| First Half Asian Total / Handicap | push rules as §13 |
| First Half Double Chance | — |
| First Half Correct Score | — |
| 2nd Half Result/Total/Handicap | — |
| Highest Scoring Half (§10.25.35) | 1H/2H/Equal |
| Win Both Halves / Win Either Half ("Team 1 To Win At Least One Half – Yes", "Both Halves") (specials; §10.25/PAA) | — |
| Team To Score In Both Halves | — |
| Both Halves Over 0.5 ("both halves to have goals") | — |
| Multi Corner | 1H corners × 2H corners (e.g. 5×7=35) (§10.25.33) |

### 2.6 Corners group
| Market | Source |
|---|---|
| First Corner – Team | §10.25.8 |
| More Corners – Team | §10.25.9 |
| Total Corners Over/Under | §10.25.10; retaken = 1; only taken corners count (§10.25.15) |
| Team Total Corners O/U | UI/§10.25.9 |
| Handicap Corners | UI |
| Race To N Corners / Race markets | UI ("Race To… Points" mechanics §11.29) |
| Next Corner Team | refund if not occurring (§11.30) |
| First/Last Corner Team | UI |
| Corners O/U per half | UI |
| Interval Corners (0–15 etc.) | §10.25.21 conventions |
| Multi Corner | §10.25.33 |
| Corner-related Points markets | "3 points per corner" in Points markets (§10.25.44–46) |

### 2.7 Cards group
| Market | Source |
|---|---|
| Total Yellow Cards O/U (YC) — only outfield+GK cautions; 2nd yellow ≠ 2nd YC | §10.25.11 |
| Total Yellow/Red Cards (YRC): YC=1, RC=2, 2nd-yellow+RC = 25-point max / max 3 cards; Total Cards: 2Y→R = one card only (max 2/player) | §10.25.14, §10.25.47 |
| Cards Handicap (YC with handicap) | §10.25.11 |
| First Card (team/player) — card must be **shown** in interval; prior infraction shown later doesn't count | §10.25.47 |
| Last Card — no cards → "No Cards" wins; multi-player incident → last card shown | §10.25.47 |
| First/Last Booking – Team; simultaneous bookings → 1.00; second booking ≠ count | §12.14–15 |
| YC In Interval (live) — added time excluded (85:00–88:59 bet, 90+1 card = loss) | §10.25.12 |
| Red Card – Yes/No (Sending Off) — outfield+GK only | §12.13 |
| Booking/Total Points For Cards: YC=10 pts, RC=25 pts, 2Y→RC max 25; shown-to-player-on-pitch only | §10.25.43 |
| Player To Get Yellow/Red Card; non-starter → 1.00 | §12.22 |
| Penalty Awarded And Sending Off – Yes (both must occur) | §10.25.31 |
| Duel of Sending Off (player vs player / player vs team) — stoppage included, ET excluded | §10.25.77 |
| Team Performance "Points": −10 per red | §10.25.44 |

### 2.8 Statistics group
| Market | Source |
|---|---|
| Shots On Target (blocked/woodwork shots excluded) | §10.25.17 |
| Shots On Goal (all toward goal + blocked shots count — distinct "wide" book) | §10.25.18 |
| Fouls (F), Offsides (OFF), Throw-ins, Goal kicks | §3.19; §10.25.22 |
| Saves (derived from SOT vs goals; site line) | UI |
| Woodwork/Posts & Crossbars (ball must remain in play) | §10.25.16 |
| Misses (MS) | §3.19 |
| First To Happen (stat events) | §10.25.22 |
| 1-Minute Markets (event awarded-time basis) | §10.25.23 |
| Distance Covered By Player/Team (km, to 0.01; excl. ET/pens) | §10.25.57 |
| Tackles — whoscored.com data | §10.25.79 |
| Dribbling / Aerial Duels — successful only, whoscored.com | §10.25.80 |
| Best Player Of The Match (starter or not; DNP→1.00; whoscored fallback) | §10.25.58 |
| Medical Team Entries (referee permission + actual assistance; two teams = one entry) | §10.25.60 |
| Main Referee To Watch Video Footage – Yes/No; VAR To Be Used – Yes/No (rectangle sign or screen consult; stream-based) | §10.25.61 |
| Duel Of The Referees (referee-team points: YC 1, RC 2 [2Y→RC=2 total], offside 0.5, penalty 3) | §10.25.81 |
| Substitutions — First Substitution (team; simultaneous → 1.00), First Substitution Timing (1H/HT/2H; none → 1.00); 46th-min sub counts as half-time | §12.10–11; §10.25.15 |
| Penalty Awarded – Yes/No | §10.25.30; §12.12 |
| To Score Penalty – Yes/No (team) — no penalty awarded → both lose; "Team 2 To Score Penalty – No" wins if awarded & missed | §12.29–30, §12.38–39 |
| Team To Score Their 1st Penalty – Yes/No (no pen → lose) | §12.31 |
| Penalty Shootout markets — "Penalty Shoot-Out Win 2 – Yes"; 5th-penalty not taken → "Team 2 To Score Their 5th Penalty" refunded | §10.25.34, §10.25.41 |
| Penalty Awarded And Sending Off – Yes | §10.25.31 |
| Goalkeeper touches (§12.36) | see 2.4 |

### 2.9 Specials group (incl. futures & long-term)
| Market | Source |
|---|---|
| To Win To Nil (Team 1/2, Yes/No): "Team 2 To Win To Nil – Yes" wins on 0:1, 0:2… | §12.28–29 |
| Clean Sheet (Shutout) — at least one team concedes none | §12.28 |
| Next Manager Retirement (earliest official-site declaration wins; post-declaration bets 1.00) | §10.25.38 |
| Managers (caretakers excluded; unlisted appointee → bets lose; director ≠ manager) | §10.25.39 |
| Players (transfers) — loans excluded unless stated; unlisted price/no transfer in window → bets lose | §10.25.40 |
| FIFA. Next President (incumbent excluded) | §10.25.50 |
| To Be Sent To The Stands (manager) | §10.25.66 |
| Alternative matches (from LIVE-streamed fixtures; forfeit in real match → 1.00 unless decided) | §10.25.49 |
| Alternative double matches (two simultaneous matches merged, e.g. Eintracht Braunschweig/Borussia Dortmund vs Schalke/Hoffenheim — combined scores) | §10.25.49 |
| Post-Match vs Live (known result + live result; forfeit/abandonment/postponement → void) | §11.39 |
| Accumulator Outcomes. Special Bets ("Fewer Than 2.5 Goals And Fewer Than 4 Cards"; "Juventus, Dortmund & Man United all to score in first 20 mins"; "Fewer Than 10 Corners And Fewer Than 4 Cards") — all outcomes must win; one leg undetermined → settle on determined ones; "9 corners & 4 cards" example loses | §11.41 |
| Football with 8 players (30-min halves variant settlement) | §10.25.48 |
| Indoor soccer/showball (2×20 or 4×15; regular time) | §10.25.73 |
| Statistics of first/second leg (two-leg aggregate settlement after 2nd leg) | §10.25.52 |
| National-team group-stage stats; tournament stats incl. ET, excl. pens & OGs; player match stats incl. ET | §10.25.56, 59 |
| Season/series/tournament player stats — full withdrawal → 1.00 | §10.25.63 |
| Player to score more goals (tournament) — incl. ET, excl. pens | §10.25.65 |
| Which group will have most goals (equal → 1.00) | §10.25.68 |
| Weather specials | §10.100 |
| Outrights (Winner/Top-4/Relegation/Top scorer) | §10.25.1/6, §11.16–17 |

### 2.10 Interval-group conventions (0–15, 16–30, …)
- Interval totals, outcome-in-interval, handicap-in-interval, goal-in-time-interval, YC-in-interval — all defined with the explicit stoppage-time matrix in §10.25.20–23 (reproduced in §0 table).

---

## 3. BET SLIP TYPES — exact rules (Rules §3.1–3.3, §4, §13)

| Type | Official rule summary |
|---|---|
| **Single** (4.1) | One outcome; return = stake × odds |
| **Accumulator (Express)** (4.2) | ≥2 unrelated outcomes; all must win; related outcomes forbidden — if included, lowest-odds legs are excluded |
| **System** (4.3) | All same-size accas from N selections; max 20 outcomes; max 184,756 combinations; full combination table published (2/3 up to 19/20); payout = sum of winning combos |
| **Chain** (4.4) | Ordered singles from a rolling "chain account" (starts = first stake); stake rolls over on wins; balance < stake → remaining balance staked; settles in slip order (not chronological); zero balance → chain lost |
| **Advancebet** (4.5) | Bet funded from potential returns of unsettled bets (≤48 h); repayments from earlier bets settled within 48 h; deposits can't repay; shortfall → advancebet voided; worked example €260 balance, €100 advance |
| **Promo code bet** (4.6) | Free bet at bookmaker's discretion; one-time, non-refundable, not counted in future promos, no partial use; enter code in bet slip, no stake |
| **Multibet** (4.7) | Set of accas+singles with optional **Lobby** (mandatory outcome): ≥3 selections besides Lobby; Lobby loses → whole bet loses; system loses → bet loses; payout = Lobby odds × winning-system odds × per-leg stake; without Lobby = system; all-singles Multibet = system. Worked example: Lobby 1.8, blocks 1.39/1.78/2.44, €300 → all-win = 18.36 × €100 = €1,836 |
| **Conditional bet (If-bet)** (4.8) | Ordered blocks (singles/accas); stake of each block ≤ return of previous (or fixed); 1st loses → all lose; settlement stops when funds run out |
| **Anti-Accumulator** (4.9) | Wins if the equivalent acca **loses** (≥2 unrelated legs; wins if at least one leg loses); odds derived as inverse probability (3 legs 1.25/1.65/1.85 → acca 3.81 → anti-acca 1.17); void legs at 1.00 raise anti-acca odds; all legs 1.00 → stake refund |
| **Lucky** (4.10) | All singles + all accas (2–8 selections): 4 selections = 15 bets (4 singles, 6 doubles, 4 trebles, 1 fourfold); stake split equally; ≥1 correct selection pays |
| **Patent** (4.11) | All accas only (3–8 selections): 4 selections = 11 bets (6 doubles, 4 trebles, 1 fourfold); ≥2 correct selections needed |
| **Bet slip sale = Cash Out / Sell Bet** (3.1) | Full or partial sale of stake while unsettled; min/max amounts case-by-case; blocked if settled, outcomes blocked, unsellable legs, already sold, or price changed; "Auto sell" target-price auto cash-out; not guaranteed; price may change while dialog open |
| **Bet slip editing = Edit Bet** (3.2) | Replace/add/delete legs in singles & accas (prematch+live) while sale available; replace/delete charge sale-equivalent commission; replace only within same market (W1→X or W2); add = free, original odds kept; stake unchangeable; type change → commission (except single→acca); not allowed after partial sale or when in bonus/promo |
| **Powerbet** (3.3) | Boost odds of an already-placed single (live or prematch) on the same market while Cash Out available; no extra stake |
| **Bet Insurance** | Paid service; price depends on current odds; e.g. 100% insurance: if bet loses, full stake refunded (documented in the prior 1xBet rules edition, "Rules-PDF" on Scribd; not present in current .cd PDF — feature availability varies by domain) |
| **Constructor (bet slip)** | Combine two outcomes of different markets on the same event into one bet ("Constructor" in Sports menu & slip; historical rules TOC "Constructor") |
| **Bet Constructor (virtual teams)** (10.62) | Draft 1–5 real players/teams into two virtual teams (1 per player; opponents can't share a team; doubles allowed; tennis/football/ice-hockey eligible); markets: Match Result, Match Result incl. Handicap, Match Total; singles only; settle on summed goals/sets of members; interrupted real match → 1.00 unless decided |
| **One-click bet** (howbet page) | Pre-set stake, single click places bet without confirmation |
| **Bet Generator** (site) | Auto-generated accumulator |
| **TOTO products** (§14–22) | 15-TOTO (14 outcomes, prize-pool distribution table, jackpot), TOTO Correct Score, TOTO-Football, TOTO Ice Hockey/Basketball/FIFA/Esports/Free/Cricket; Batch bet |
| **Accumulator Of The Day / Live Accumulator Of The Day** | site promo accas (bonus on odds) |

---

## 4. Settlement nuances — quick-reference matrix

| Situation | Handling |
|---|---|
| Own goal | Counts as goal for opponent & for match totals; **excluded** from: individual/team totals (§11.8), all goalscorer markets (§10.25.24–26, 29; §11.24–25, 31), headed-goal counts (§10.25.71), left/right-foot counts (§10.25.71), Player Match-Ups (§11.31); "First Goal To Be An Own Goal" market exists; 0:0 → "No First Goal" wins (§11.34); first-goalscorer after OG shifts to 2nd goal scorer |
| Rebounds | Second goal after rebound is a new goal; goalkeeper touch doesn't break set-piece chain (§10.25.69) |
| Corner awarded not taken | Not counted (§10.25.15) |
| Retaken corner / retaken penalty | One corner/penalty (§10.25.15; §10.25.45–46) |
| Cards after FT | Don't count (§10.25.13); deferred HT/FT cards count for the half of the offence |
| DNP player | 1.00 refund on player markets (§10.25.24, 27, 55, 67; §12.22; §11.16, 31–32) |
| 90 min vs ET | Regular time everywhere except ET-labeled & qualify/winner/promotion markets (§10.25.1, 6, 7) |
| Abandoned match | Decided parts stand, rest void (§9.10; ≥80-min rule §10.25.2) |
| Void-in-acca | Canceled leg = odds 1.00, acca continues (§3.10) |
| Postponement >48h (prematch) / <5h resumption (live) | Void vs stand (§9.8–9) |
| Forfeits / known-result bets / match-fixing suspicion | Void at odds 1 (§3, §9.7) |
| Simultaneous finish | 2 winners → stake halved; 3+ → odds 1.00 (except "To Be Higher"/Match-up markets) (§3.15) |
| Mercy rule | Ends game early; thresholds set by organizer (§3.16) |
| Statistics markets | May settle up to 1 hour after FT (§10.25.19); video first, then official sources (§10.25.15) |
| RPL corners | Settled on 3rd day from official sources (§10.25.4) |

---

## 5. Source URLs

**Primary (official):**
- Rules PDF (260 pp., 2026 edition): `https://1xbet.cd/web-api/rulespdf` (alternate: `https://bol.1xbet.com/rulespdf`)
- Rules homepage (geo-blocked outside licensed regions; same text): `https://1xbet.com/en/information/rules`
- How-to-bet: `https://1xbet.com/en/information/howbet` (Wayback capture 2024-05-11 used; regional: `https://1xbet.com.zm/en/information/howbet`, `https://eg1xbet.com/en/information/howbet`)
- Historical rules TOC (2016, Wayback): `https://web.archive.org/web/20160802033718/https://1xbet.com/en/information/rules/`
- Regional official rules pages (indexed, geo-blocked): `https://1xbet.ng/en/information/rules`, `https://1xbet.co.ke/information/rules`, `https://1xbet.ci/information/rules`, `https://so.1xbet.com/information/rules`, `https://indian.1xbet.com/information/rules`

**Secondary (mirrors/reviews reproducing board & rules):**
- `https://1xbets.bet/rules/` (plain-language rules: 80-minute rule, first-caution rule, cards after FT, 90-min settlement)
- `https://1xbets.bet/football/` (live match-board market-group counts: Total 106 / Handicap 18 / Popular 313 / Players 8 / Goals 240; 1X2 vs 1X2-2UP odds; BTTS; combos; Team to Qualify)
- `https://1xbet.onl/1xbet-football-betting/` (settlement framework: ET/pens excluded; AH push; EH 3-way; props on official protocol; void-in-acca at 1.00; abandonment)
- Scribd reproductions of official rulebooks: "1xBet Betting Rules and Regulations" (242 pp.), "Full Doc Rules en GB" (194 pp.), "Rules PDF" (233 pp., includes **Bet Insurance** clause)
- Wayback CDX endpoints used: `web.archive.org/cdx/search/cdx?url=1xbet.com/en/information/rules…`, `…url=1xbet.ng/en/information/rules…` (full 54 KB capture 2023-09-20)

*Caveats: the live site menu rotates groups per match/league; counts above are from one documented fixture. Bet Insurance and some slip features are jurisdiction-dependent (present on 1xbet.com-lineage editions, absent from the .cd PDF). The English rules text is the legal version (§9.26).*
