import random


def uniform_random_number(a: int, b: int) -> int:
    if a != 0:
        return a + uniform_random_number(0, b - a)

    k = 0
    while b >= 2 ** k - 1:
        k += 1

    outcomes = set(range(b))
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
