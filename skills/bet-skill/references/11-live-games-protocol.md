# 11 — Live Games Protocol (Hermes can't open 1xBet — this is the workaround)

> Live odds are often HIGH — high odds mean LOW probability, not value. The EV
> rule never changes: bet only if `model% > no-vig% + margin of safety`.
> Live margins are WIDER (6-12%) than pre-match, so demand a bigger edge (≥5pp).

## 1. How Hermes gets live data (3 tiers, top first)

**Tier 1 — User paste (always works, preferred for live speed).**
Ask for a live snapshot in this exact shape (`templates/live-snapshot.md`):
`match | minute | score | live 1X2 + O/U + BTTS/Next-Goal odds | red cards? | what happened last 10 min (shots/corners/subs)?`
One message, 30 seconds of their time, zero tooling risk.

**Tier 2 — Hermes fetches from the web (no 1xBet login needed).**
Hermes cannot browse 1xBet's JS-heavy live pages, so use these instead:
- **OddsPortal / BetExplorer / Oddspedia live + dropping odds** — live prices and steam across books; compare vs 1xBet price the user sees.
- **Flashscore / SofaScore / FotMob** — minute, score, cards, subs, momentum/xG (SofaScore live xG where available).
- **FlashScore search API** (no key): `GET https://s.livesport.services/api/v2/search/?q=<team>&lang-id=13&type-ids=1,2,3,4&project-id=202&project-type-id=1`, filter `sport.id=1`. Covers men's, women's and youth fixtures.
- **Free live-score APIs (optional key):** API-Football (100 req/day free — live fixtures/scores/lineups), OpenLigaDB (free, scores only). Set key only if the user provides one; never ask twice.
- **1xBet public live pages** (`1xbet.com/en/live`) may be tried via web fetch, but treat failure as normal (JS wall) and fall back to Tier 1 — never stall the analysis waiting on it.

**Tier 3 — Pre-match model + time decay (always available).**
Even with only minute + score, `scripts/live_fair.py` turns the pre-match
λh/λa into live-fair 1X2 / O-U / BTTS for the REMAINDER of the match.
It is a baseline (constant rates, no game-state effects) — adjust manually for
red cards, all-out attack, or dead rubbers (see §3).

## 2. Live decision pipeline (max 1-2 positions, 0.5-1% each)

1. **Snapshot:** minute, score, cards, live odds (quoted time), last-10-min events.
2. **Baseline:** `python scripts/live_fair.py --lh [pre λh] --la [pre λa] --minute [m] --home-score [h] --away-score [a] --line 2.5 --odds [live odds for your market]`.
3. **Adjust (manual, state it):** red card ≈ −0.6 to −1.0 goals to the 10-man side (more if losing creators/GK); chasing favorite after 70' ≈ +10-20% next-goal share; dead rubber / mutually-convenient draw ≈ downgrade all goal markets.
4. **Momentum check:** box entries + SoT + corners since 60' > possession. Sterile possession (no box touches) = NO BET.
5. **Edge:** live no-vig% vs adjusted model% → need ≥5pp (wider margin regime). High odds (e.g. 9.00 = 11%) need model ≥16%+.
6. **Enter 70-77' only** for late-goal markets (Next Goal / Over 0.5 76-90' / live Asian Over 1.0 — refund if exactly 1). Max 2 live bets per game. Never pre-bet live positions.
7. **Exit:** partial cash-out / manual hedge at another book beats full cash-out (cash-out margin peaks 8-12% at half-time and in losing positions).

## 3. Live 1xBet rules that burn people

- Markets **suspend after goals/reds/penalties** then reopen repriced — a price you saw 10 seconds ago is gone; always re-quote before staking.
- Bets placed **during** the event that caused suspension may be **voided**.
- Cash-out price moves while the dialog is open — must re-accept; manual sale deactivates Auto.
- Live totals/handicaps reference the score **at bet time** for period markets (e.g. "rest of match" vs "full match incl. current score") — read the market name, they price differently.

## 4. What Hermes says when data is thin

"Live price without minute+score+cards is a NO BET — paste the 30-second snapshot and I'll price it." Never invent a scoreline, never price from odds alone.
