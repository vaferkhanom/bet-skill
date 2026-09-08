"""Poisson + Dixon-Coles scoreline matrix -> 1X2 / O-U / BTTS. Pure stdlib."""
import argparse, math


def pois(k, lam):
    return (lam ** k) * math.exp(-lam) / math.factorial(k)


def tau(x, y, lh, la, rho):
    if x == 0 and y == 0:
        return 1 - lh * la * rho
    if x == 0 and y == 1:
        return 1 + lh * rho
    if x == 1 and y == 0:
        return 1 + la * rho
    if x == 1 and y == 1:
        return 1 - rho
    return 1.0


def matrix(lh, la, rho=0.0, max_g=8):
    m = [[pois(i, lh) * pois(j, la) * tau(i, j, lh, la, rho)
          for j in range(max_g + 1)] for i in range(max_g + 1)]
    s = sum(sum(r) for r in m)
    return [[v / s for v in r] for r in m]


def summarize(m):
    n = len(m)
    ph = sum(m[i][j] for i in range(n) for j in range(n) if i > j)
    pd = sum(m[i][j] for i in range(n) for j in range(n) if i == j)
    pa = sum(m[i][j] for i in range(n) for j in range(n) if i < j)
    over = {}
    for line in (0.5, 1.5, 2.5, 3.5):
        over[line] = sum(m[i][j] for i in range(n) for j in range(n) if i + j > line)
    btts = 1 - sum(m[0]) - sum(r[0] for r in m) + m[0][0]
    top = sorted(((m[i][j], i, j) for i in range(n) for j in range(n)), reverse=True)[:5]
    return ph, pd, pa, over, btts, [(i, j, p) for p, i, j in top]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--home", type=float, required=True, help="lambda home xG")
    ap.add_argument("--away", type=float, required=True, help="lambda away xG")
    ap.add_argument("--rho", type=float, default=-0.08)
    ap.add_argument("--max-goals", type=int, default=8)
    a = ap.parse_args()
    m = matrix(a.home, a.away, a.rho, a.max_goals)
    ph, pd, pa, over, btts, top = summarize(m)
    print(f"lambda H={a.home} A={a.away} rho={a.rho}")
    print(f"Home {ph:.1%} | Draw {pd:.1%} | Away {pa:.1%}")
    for line, p in over.items():
        print(f"Over {line}: {p:.1%} | Under {line}: {1 - p:.1%}")
    print(f"BTTS Yes {btts:.1%} | No {1 - btts:.1%}")
    print("Top scores:", ", ".join(f"{i}-{j} {p:.1%}" for i, j, p in top))


if __name__ == "__main__":
    main()
