import math


def square_root(x: float) -> float:
    if x > 1.0:
        L = 1.0
        U = x
    else:
        L = x
        U = 1.0

    while not math.isclose(L, U):
        M = (L + U) / 2

        if M * M > x:
            U = M
        else:
            L = M

    return (L + U) / 2
