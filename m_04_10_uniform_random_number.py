import random


def zero_one_random():
    return random.randrange(2)


def uniform_random(a: int, b: int) -> int:
    """
    Generate (at random) an integer `i` from `{a, ..., b}`
    according to the uniform probability distribution on the set of possible outcomes.
    """

    if a != 0:
        return a + uniform_random(0, b - a)

    # Determine the # of bits needed to represent `b`.
    num_bits_needed_for_b = 0
    while b >= 2 ** num_bits_needed_for_b - 1:
        num_bits_needed_for_b += 1

    # Generate (at random) one positive integer,
    # whose binary representation contains at most `num_bits_needed_for_b` bits that are set.
    i = b + 1  # Anything bigger than `b` will do.
    while i > b:
        i = _sample_X_k(num_bits_needed_for_b)

    return i


def _sample_X_k(k: int) -> int:
    """
    Generate a random integer btwn 0 and (2 ** k - 1)
    with all possible outcomes being equally likely.

    Sample a random integer
    from the uniform distribution
    on { 0, ... , (2 ** k) - 1}
    """
    x = 0

    for _ in range(k):
        digit = zero_one_random()
        x <<= 1
        x = x | digit

    return x


def uniform_random_2(lower_bound: int, upper_bound: int) -> int:
    """
    This is the official solution.
    """

    number_of_outcomes = upper_bound - lower_bound + 1

    while True:
        result = 0
        i = 0
        while (1 << i) < number_of_outcomes:
            result = (result << 1) | zero_one_random()
            i += 1

        if result < number_of_outcomes:
            break

    return result + lower_bound


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
