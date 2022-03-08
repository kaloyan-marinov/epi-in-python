def square_root(k: int) -> int:
    """
    empirically observed to be about twice as slow as the next solution
    """
    L = 0
    U = k

    while True:
        M = (L + U) // 2  # L + (U - L) // 2

        if M ** 2 > k:
            U = M
        else:  # i.e. M ** 2 <= k
            if (M + 1) ** 2 <= k:
                L = M + 1
            else:  # i.e. (M + 1) ** 2 > k
                return M


def square_root_2(k: int) -> int:
    """
    idea: maintain a candidate interval [L, U],
          where everything before L has square <= k
          and everything after U has/ square > k
    """

    L = 0
    U = k

    while L <= U:
        M = (L + U) // 2  # L + (U - L) // 2
        M_squared = M * M
        if M_squared <= k:
            L = M + 1
        else:
            U = M - 1

    return L - 1
