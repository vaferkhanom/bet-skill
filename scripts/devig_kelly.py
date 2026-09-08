"""De-vig, EV/edge, Kelly, CLV, acca-margin. Pure stdlib. Decimal odds."""
import argparse, math


def implied(odds):
    return [1 / o for o in odds]


def devig(odds):
    imp = implied(odds)
    s = sum(imp)
    novig = [p / s for p in imp]
    return imp, novig, s - 1, [1 / p for p in novig]


def kelly(p, d, frac=0.25):
    b = d - 1
    f = (b * p - (1 - p)) / b if b > 0 else 0.0
    return max(f, 0.0), max(f * frac, 0.0) if f > 0 else 0.0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--odds", required=True, help="comma odds, e.g. 1.95,3.60,4.20")
    ap.add_argument("--model", type=float, default=None, help="model prob for leg 1 (0-1)")
    ap.add_argument("--close", default=None, help="comma closing odds for CLV")
    ap.add_argument("--frac", type=float, default=0.25, help="kelly fraction")
    ap.add_argument("--cap", type=float, default=0.03, help="max stake fraction")
    a = ap.parse_args()
    odds = [float(x) for x in a.odds.split(",")]
    imp, novig, margin, fair = devig(odds)
    print(f"Implied: {[f'{p:.1%}' for p in imp]} | margin {margin:.2%}")
    print(f"No-vig: {[f'{p:.1%}' for p in novig]} | fair {[f'{o:.3f}' for o in fair]}")
    if a.model is not None:
        d = odds[0]
        ev = a.model * d - 1
        edge = a.model - novig[0]
        full, fracd = kelly(a.model, d, a.frac)
        print(f"Leg1: model {a.model:.1%} vs book {novig[0]:.1%} = {edge:+.1%}pp | EV {ev:+.1%}")
        print(f"Kelly full {full:.2%} | x{a.frac} {fracd:.2%} | capped {min(fracd, a.cap):.2%}" +
              (" -> NO BET" if ev <= 0 or edge < 0.03 else ""))
    if a.close is not None:
        close = [float(x) for x in a.close.split(",")]
        _, c_novig, _, c_fair = devig(close)
        raw = odds[0] / close[0] - 1
        nvc = odds[0] / c_fair[0] - 1
        print(f"CLV leg1: raw {raw:+.2%} | no-vig {nvc:+.2%} | "
              f"{(c_novig[0] - novig[0]):+.1%}pp move")
    n = len(odds)
    print(f"Acca-margin if {n} legs ~5% each: {1.05 ** n - 1:.1%}")


if __name__ == "__main__":
    main()
