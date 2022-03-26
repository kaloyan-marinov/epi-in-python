from typing import List


def has_two_sum(A: List[int], t: int) -> bool:
    """
    Assume that `A` is sorted.

    Determine whether
    there are 2 (not-necessarily-distinct) entries in `A`
    that add up to `t`.
    """

    i = 0
    j = len(A) - 1

    while i <= j:
        if A[i] + A[j] == t:
            return True
        elif A[i] + A[j] < t:
            i += 1
        else:  # i.e. A[i] + A[j] > t
            j -= 1

    return False
