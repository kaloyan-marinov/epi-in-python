from typing import List

from m_17_04_A_two_sum import has_two_sum


def has_three_sum(A: List[int], t: int) -> bool:
    """
    Determine whether
    there are 3 (not-necessarily-distinct) entries in `A`
    that add up to `t`.
    """

    A.sort()

    for i in range(len(A)):
        if has_two_sum(A, t - A[i]):  # Possible to use `has_two_sum(A[i:], t - A[i])`
            return True

    return False


def has_three_sum_2(A: List[int], t: int) -> bool:
    """
    Determine whether
    there are 3 (not-necessarily-distinct) entries in `A`
    that add up to `t`.
    """

    A.sort()

    return any(has_two_sum(A, t - a) for a in A)


if __name__ == "__main__":
    A = [1, 4, 0, -3, -1, 0, -7]
    t = -17

    result = has_three_sum(A, t)
