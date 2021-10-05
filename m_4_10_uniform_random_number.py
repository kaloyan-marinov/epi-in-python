import random


def uniform_random(a: int, b: int) -> int:
    if a != 0:
        return a + uniform_random(0, b - a)

    k = 0
    while b >= 2 ** k - 1:
        k += 1

    outcomes = set(range(b + 1))
    retry = True
    while retry:
        i = _sample_X_k(k)
        if i in outcomes:
            retry = False

    return i


def _sample_X_k(k: int) -> int:
    """
    gen. btwn 0 and (2 ** k - 1)
    """
    x = 0
    for i in range(k):
        digit = random.choice([0, 1])
        x <<= 1
        x = x | digit

    return x


if __name__ == "__main__":
    # xs = []
    # for _ in range(10):
    #     x = _sample_X_k(4)
    #     xs.append(x)
    # print(xs)

    # rs = []
    # for _ in range(10):
    #     r = uniform_random(0, 10)
    #     rs.append(r)
    # print(rs)

    import collections

    d = collections.defaultdict(int)

    num_trials = 10 ** 6
    k = 4
    for _ in range(num_trials):
        x = _sample_X_k(k)
        d[x] += 1

    possible_outcomes = range(2 ** k)
    fmt_str = "{0:>10} {1:>30}"
    print(fmt_str.format("x", "Pr(x)"))
    print(fmt_str.format("-" * 10, "-" * 20))
    for kk in possible_outcomes:
        pr_kk = d.get(kk, 0) / num_trials
        print(fmt_str.format(kk, pr_kk))
