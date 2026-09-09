"""Poisson + Dixon-Coles matrix -> price EVERY derivable 1xBet football market.

Default prints the core board. --full prices the full derivable catalog
(see references/13 + 14). Pure stdlib.
"""
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


def matrix(lh, la, rho=0.0, max_g=9):
    m = [[pois(i, lh) * pois(j, la) * tau(i, j, lh, la, rho)
          for j in range(max_g + 1)] for i in range(max_g + 1)]
    s = sum(sum(r) for r in m)
    return [[v / s for v in r] for r in m]


def core(m):
    n = len(m)
    ph = sum(m[i][j] for i in range(n) for j in range(n) if i > j)
    pd = sum(m[i][j] for i in range(n) for j in range(n) if i == j)
    pa = sum(m[i][j] for i in range(n) for j in range(n) if i < j)
    btts = 1 - sum(m[0]) - sum(r[0] for r in m) + m[0][0]
    top = sorted(((m[i][j], i, j) for i in range(n) for j in range(n)), reverse=True)[:5]
    return ph, pd, pa, btts, [(i, j, p) for p, i, j in top]


def total_gt(m, t):
    n = len(m)
    return sum(m[i][j] for i in range(n) for j in range(n) if i + j > t)


def team_gt(m, t, side):
    n = len(m)
    if side == "h":
        return sum(m[i][j] for i in range(n) for j in range(n) if i > t)
    return sum(m[i][j] for i in range(n) for j in range(n) if j > t)


def asian_total(m, line):
    """e.g. 2.25 -> (2.0, 2.5) half stakes; returns (p_over_eff, fair_over, fair_under)."""
    lo = math.floor(line - 0.25) if line % 0.5 == 0.25 else None
    half = line % 0.5 == 0.25
    if half:
        l1, l2 = line - 0.25, line + 0.25
        po = 0.5 * total_gt(m, l1) + 0.5 * total_gt(m, l2)
        return po, None, None
    o = total_gt(m, line)
    return o, 1 / o, 1 / (1 - o)


def ah_probs(m, line):
    """Asian handicap from team-1 perspective. line in {-2..+2 step .25}."""
    n = len(m)
    if line % 0.5 == 0.25:
        res = [ah_probs(m, line - 0.25), ah_probs(m, line + 0.25)]
        keys = ("fw", "hw", "push", "hl", "l")
        return {k: 0.5 * res[0][k] + 0.5 * res[1][k] for k in keys}
    fw = hl = push = l = 0.0
    for i in range(n):
        for j in range(n):
            adj = i - j + line
            p = m[i][j]
            if adj > 0.4:
                fw += p
            elif adj > -0.4:
                push += p
            else:
                l += p
    return {"fw": fw, "hw": 0.0, "push": push, "hl": 0.0, "l": l}


def ah_fair(p):
    return (1 - p["push"] - p["hw"] / 2 - p["hl"] / 2) / (p["fw"] + p["hw"] / 2)


def gamma_pdf(x, shape, rate):
    if x <= 0:
        return 0.0
    return rate ** shape * x ** (shape - 1) * math.exp(-rate * x) / math.factorial(shape - 1)


def gamma_sf(x, shape, rate):
    if x <= 0:
        return 1.0
    return math.exp(-rate * x) * sum((rate * x) ** k / math.factorial(k)
                                     for k in range(shape))


def race_probs(lh, la, nn=3, minutes=90.0):
    """P(team1 reaches N goals before team2 within 90'); returns (p1, p2, neither)."""
    r1, r2 = lh / minutes, la / minutes
    step, t, p1 = 0.25, 0.0, 0.0
    while t < minutes:
        p1 += gamma_pdf(t + step / 2, nn, r1) * gamma_sf(t + step / 2, nn, r2) * step
        t += step
    p2_total = 1 - gamma_sf(minutes, nn, r2)  # P(t2 reaches N by 90)
    # P2 wins race = P(T2 < min(T1,90)) — symmetric integral
    p2w, t = 0.0, 0.0
    while t < minutes:
        p2w += gamma_pdf(t + step / 2, nn, r2) * gamma_sf(t + step / 2, nn, r1) * step
        t += step
    return p1, p2w, max(0.0, 1 - p1 - p2w)


def full_report(lh, la, rho, max_g):
    m = matrix(lh, la, rho, max_g)
    n = len(m)
    ph, pd, pa, btts, top = core(m)
    o25 = total_gt(m, 2.5)
    # half-split (constant-rate approx, 1H = 45% of goals)
    f1 = 0.45
    mh = matrix(lh * f1, la * f1, 0.0, max_g)
    h1h = sum(mh[i][j] for i in range(n) for j in range(n) if i > j)
    d1h = sum(mh[i][j] for i in range(n) for j in range(n) if i == j)
    a1h = 1 - h1h - d1h
    f2 = 0.55
    m2 = matrix(lh * f2, la * f2, 0.0, max_g)
    h2h = sum(m2[i][j] for i in range(n) for j in range(n) if i > j)
    d2h = sum(m2[i][j] for i in range(n) for j in range(n) if i == j)
    a2h = 1 - h2h - d2h
    p_goal = 1 - m[0][0]
    first_h = lh / (lh + la) * p_goal if lh + la else 0.0

    print("== RESULT ==")
    print(f"1X2: H {ph:.1%} (fair {1/ph:.2f}) | X {pd:.1%} ({1/pd:.2f}) | A {pa:.1%} ({1/pa:.2f})")
    print(f"DC: 1X {ph+pd:.1%} ({1/(ph+pd):.2f}) | 12 {ph+pa:.1%} ({1/(ph+pa):.2f}) | X2 {pd+pa:.1%} ({1/(pd+pa):.2f})")
    print(f"DNB: H {ph/(ph+pa):.1%} ({(ph+pa)/ph:.2f}) | A {pa/(ph+pa):.1%}")
    print(f"2UP-equivalent H (win or 2-goal-lead-early): use 1X2 minus ~5% pricing; matrix H {ph:.1%}")
    print(f"Win to nil: T1 {sum(m[i][0] for i in range(1, n)):.1%} ({1/sum(m[i][0] for i in range(1, n)):.2f}) | "
          f"T2 {sum(m[0][j] for j in range(1, n)):.1%}")
    print(f"Clean sheet: T1 {sum(r[0] for r in m):.1%} | T2 {sum(m[0]):.1%} | either {sum(r[0] for r in m)+sum(m[0])-m[0][0]:.1%}")
    print("== TOTALS ==")
    for t in ("0.5", "1.5", "2.5", "3.5", "4.5"):
        tv = float(t)
        o = total_gt(m, tv)
        print(f"O/U {t}: Over {o:.1%} ({1/o:.2f}) | Under {1-o:.1%} ({1/(1-o):.2f})")
    for at in (1.75, 2.25, 2.75, 3.25):
        if at % 1 == 0.75 or at % 1 == 0.25:
            lo, hi = at - 0.25, at + 0.25
            po = 0.5 * total_gt(m, lo) + 0.5 * total_gt(m, hi)
            print(f"Asian Total {at}: Over-eff {po:.1%} | Under-eff {1-po:.1%}")
    for t in (2, 3):
        e = sum(m[i][j] for i in range(n) for j in range(n) if i + j == t)
        print(f"3-way Total {t}: Over {total_gt(m, t):.1%} | Exactly {e:.1%} | Under {1-total_gt(m, t):.1%}")
    print("== TEAM TOTALS ==")
    for side in ("T1", "T2"):
        side_key = "h" if side == "T1" else "a"
        for t in (0.5, 1.5, 2.5):
            p = team_gt(m, t, side_key)
            print(f"{side} O/U {t}: Over {p:.1%} ({1/p:.2f}) | Under {1-p:.1%}")
    print("== GOALS GROUP ==")
    print(f"BTTS: Yes {btts:.1%} ({1/btts:.2f}) | No {1-btts:.1%}")
    print(f"BTTS+O2.5 joint {sum(m[i][j] for i in range(n) for j in range(n) if i>0 and j>0 and i+j>2.5):.1%}"
          f" | BTTS+U2.5 joint {m[1][1]:.1%}")
    print(f"Combo W1&O2.5 {sum(m[i][j] for i in range(n) for j in range(n) if i>j and i+j>2.5):.1%} | "
          f"W1&BTTS {sum(m[i][j] for i in range(n) for j in range(n) if i>j and i>0 and j>0):.1%}")
    print(f"Multi Goal 0-1 {sum(m[i][j] for i in range(n) for j in range(n) if i+j<=1):.1%} | "
          f"2-3 {sum(m[i][j] for i in range(n) for j in range(n) if 2<=i+j<=3):.1%} | "
          f"4-6 {sum(m[i][j] for i in range(n) for j in range(n) if 4<=i+j<=6):.1%} | "
          f"7+ {total_gt(m,6):.1%}")
    odd = sum(m[i][j] for i in range(n) for j in range(n) if (i + j) % 2 == 1)
    print(f"Odd {odd:.1%} | Even {1-odd:.1%}")
    print(f"First goal: T1 {first_h:.1%} | T2 {la/(lh+la)*p_goal:.1%} | no goal {1-p_goal:.1%} (0-0: all lose)")
    print(f"To score first & win: T1 {first_h*ph:.1%}")
    for nn in (2, 3):
        p1, p2, pn = race_probs(lh, la, nn)
        print(f"Race to {nn}: T1 {p1:.1%} ({1/p1:.2f}) | T2 {p2:.1%} | neither {pn:.1%}")
    print("== HALVES (constant-rate approx) ==")
    print(f"1H: H {h1h:.1%} | X {d1h:.1%} | A {a1h:.1%} | O0.5 {1-d1h:.1%}")
    print(f"2H: H {h2h:.1%} | X {d2h:.1%} | A {a2h:.1%} | O0.5 {1-d2h:.1%}")
    print(f"Highest scoring half: 1H {h1h:.1%} | 2H {h2h:.1%} | equal (approx {max(0.0, 1 - max(h1h, h2h)):.1%})")
    t1bh = (1 - sum(mh[i][0] for i in range(n))) * (1 - sum(m2[i][0] for i in range(n)))
    t2bh = (1 - sum(mh[0])) * (1 - sum(m2[0]))
    print(f"T1 win both halves {h1h*h2h:.1%} | at least one {h1h+h2h-h1h*h2h:.1%}")
    print(f"T1 scores both halves {t1bh:.1%} | T2 {t2bh:.1%} | both halves have goals {(1-sum(mh[0])-sum(r[0] for r in mh)+mh[0][0])*(1-sum(m2[0])-sum(r[0] for r in m2)+m2[0][0]):.1%}")
    print("== HT/FT approx (9 combos) ==")
    for r1, lab1 in ((h1h, "W1"), (d1h, "X"), (a1h, "W2")):
        for r2, lab2 in ((h2h, "W1"), (d2h, "X"), (a2h, "W2")):
            print(f"{lab1}/{lab2} {r1*r2:.1%} ({1/(r1*r2):.2f})", end="  ")
        print()
    print("== ASIAN HANDICAP (team 1 view; fair odds push-excluded) ==")
    line = -2.0
    while line <= 2.001:
        p = ah_probs(m, round(line, 2))
        print(f"AH {line:+.2f}: win {p['fw']:.1%} push {p['push']:.1%} lose {p['l']:.1%} | fair {ah_fair(p):.2f}")
        line += 0.25
    print("== EXACT SCORES (top 8) ==")
    top8 = sorted(((i, j, m[i][j]) for i in range(n) for j in range(n)), key=lambda x: -x[2])[:8]
    print(" | ".join(f"{i}-{j} {p:.1%} ({1/p:.2f})" for i, j, p in top8 if p > 0))
    print("Top scores:", ", ".join(f"{i}-{j} {p:.1%}" for i, j, p in top))
    print("NOTE: halves/race/2UP approximations are constant-rate; corners/cards/stats/intervals "
          "need their OWN lambda (see references/14 §3). Exotic families: Tier 4-5 margins — gate first.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--home", "--lh", dest="home", type=float, required=True, help="lambda home xG")
    ap.add_argument("--away", "--la", dest="away", type=float, required=True, help="lambda away xG")
    ap.add_argument("--rho", type=float, default=-0.08)
    ap.add_argument("--max-goals", type=int, default=9)
    ap.add_argument("--full", action="store_true", help="price every derivable market family")
    a = ap.parse_args()
    if a.full:
        full_report(a.home, a.away, a.rho, a.max_goals)
        return
    m = matrix(a.home, a.away, a.rho, a.max_goals)
    ph, pd, pa, btts, top = core(m)
    print(f"lambda H={a.home} A={a.away} rho={a.rho}")
    print(f"Home {ph:.1%} | Draw {pd:.1%} | Away {pa:.1%}")
    for t in (0.5, 1.5, 2.5, 3.5):
        o = total_gt(m, t)
        print(f"Over {t}: {o:.1%} | Under {t}: {1-o:.1%}")
    print(f"BTTS Yes {btts:.1%} | No {1-btts:.1%}")
    print("Top scores:", ", ".join(f"{i}-{j} {p:.1%}" for i, j, p in top))


if __name__ == "__main__":
    main()
