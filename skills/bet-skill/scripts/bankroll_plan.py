"""Bankroll Card generator: unit, caps, stop-loss, drawdown ladder. Pure stdlib."""
import argparse


PROFILES = {
    "conservative": {"base": 0.01, "max": 0.015, "cap": 0.02, "live": 0.005},
    "standard": {"base": 0.01, "max": 0.02, "cap": 0.03, "live": 0.005},
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bankroll", type=float, required=True)
    ap.add_argument("--profile", default="standard", choices=PROFILES)
    ap.add_argument("--currency", default="EUR")
    a = ap.parse_args()
    p = PROFILES[a.profile]
    u = a.bankroll * 0.01
    print(f"## Bankroll Card — {a.bankroll:.2f} {a.currency} ({a.profile})")
    print(f"- Unit (1%): {u:.2f} | Standard: {a.bankroll*p['base']:.2f} | "
          f"Max conviction: {a.bankroll*p['max']:.2f} | Hard cap: {a.bankroll*p['cap']:.2f}")
    print(f"- Live/prop/HT-FT: {a.bankroll*p['live']:.2f}-{u:.2f} | "
          f"Daily stop-loss: {a.bankroll*0.05:.2f} (5%) | Halt at: {a.bankroll*0.5:.2f} (-50% peak)")
    print("- Split: 90% singles / 8% +EV 2-3-leg / 2% fun. Recalc weekly. "
          "Drawdown: -10% halve max, -20% base 0.5-1%, -50% HALT + paper trade.")


if __name__ == "__main__":
    main()
