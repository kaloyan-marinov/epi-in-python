from typing import List


def smallest_nonconstructible_value(A: List[int]) -> int:
    A.sort()

    M = 0
    for a in A:
        if a <= M + 1:
            M = M + a
        else:
            break

    return M + 1
