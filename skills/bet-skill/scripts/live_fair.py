"""Live fair-odds baseline from pre-match lambdas + time decay. Pure stdlib.

Assumes constant scoring rates over remaining minutes (NO game-state,
momentum, or fatigue effects) except an optional crude red-card adjustment.
Always a baseline: combine with the momentum check in
references/11-live-games-protocol.md before staking.
"""
import argparse, math


def pois(k, lam):
    return (lam ** k) * math.exp(-lam) / math.factorial(k)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lh", type=float, required=True, help="pre-match home xG")
    ap.add_argument("--la", type=float, required=True, help="pre-match away xG")
    ap.add_argument("--minute", type=float, required=True)
    ap.add_argument("--home-score", type=int, required=True)
    ap.add_argument("--away-score", type=int, required=True)
    ap.add_argument("--line", type=float, default=2.5)
    ap.add_argument("--stoppage-left", type=float, default=None,
                    help="default 8 if min<=45 else 5")
    ap.add_argument("--red", choices=["home", "away", "none"], default="none",
                    help="crude: 10-man attack x0.45, opponent x1.15")
    ap.add_argument("--market", choices=["home", "draw", "away", "over", "under", "btts"],
                    default=None)
    ap.add_argument("--odds", type=float, default=None, help="live price for --market")
    a = ap.parse_args()

    stop = a.stoppage_left if a.stoppage_left is not None else (8.0 if a.minute <= 45 else 5.0)
    f = max(0.0, (90.0 - a.minute + stop) / 90.0)
    rh, ra = a.lh * f, a.la * f
    if a.red == "home":
        rh, ra = rh * 0.45, ra * 1.15
    elif a.red == "away":
        ra, rh = ra * 0.45, rh * 1.15

    N = 9
    ph = pd = pa = over = 0.0
    btts_num = 0.0
    hs, aws = a.home_score, a.away_score
    for i in range(N):
        pi = pois(i, rh)
        for j in range(N):
            p = pi * pois(j, ra)
            fh, fa = hs + i, aws + j
            if fh > fa:
                ph += p
            elif fh == fa:
                pd += p
            else:
                pa += p
            if fh + fa > a.line:
                over += p
            if fh > 0 and fa > 0:
                btts_num += p
    under = 1 - over
    probs = {"home": ph, "draw": pd, "away": pa, "over": over, "under": under, "btts": btts_num}
    print(f"remaining ~{(90 - a.minute + stop):.0f} min (f={f:.2f}) | rem xG H={rh:.2f} A={ra:.2f}"
          + (f" | RED {a.red} adjusted" if a.red != "none" else ""))
    print(f"Live fair: Home {ph:.1%} | Draw {pd:.1%} | Away {pa:.1%}")
    print(f"Total {a.line}: Over {over:.1%} (fair {1/over:.2f}) | Under {under:.1%} (fair {1/under:.2f})"
          if over > 0 else "Total: n/a")
    print(f"BTTS Yes {btts_num:.1%}")
    if a.market and a.odds:
        p = probs[a.market]
        ev = p * a.odds - 1
        print(f"{a.market} @ {a.odds}: model {p:.1%} vs implied {1/a.odds:.1%} "
              f"= {p - 1/a.odds:+.1%}pp | EV {ev:+.1%} -> "
              + ("BET (needs momentum confirm + 0.5-1%)" if ev > 0.05 else "NO BET"))
    print("Note: constant-rate baseline only; red-card factor is crude; "
          "live margins 6-12% — demand >=5pp edge.")


if __name__ == "__main__":
    main()
