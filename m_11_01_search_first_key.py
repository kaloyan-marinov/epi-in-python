from typing import List

import bisect


def search_first_of_k(A: List[int], k: int) -> int:
    """
    TODO: before committing this file, commit the changes to m_5_0_C_*.py
    """
    idx = bisect.bisect_left(A, k)

    if idx == len(A):
        return -1
    else:
        return idx


def search_first_of_k_2(A: List[int], k: int) -> int:
    """
    The fundamental idea of
    both "standard binary search" and this problem's "tweaked binary search"
    is to maintain a set of candidate solutions.
    """

    L = 0
    U = len(A) - 1
    result = -1

    # A[L:U + 1] is going to be maintained as
    # _the_ (current iteration's) set of candidate solutions.

    while L <= U:
        M = (L + U) // 2  # M = L + (U - L) // 2

        if A[M] == k:
            result = M
            U = M - 1  # b/c the solution cannot be among the indices that are > M
        elif A[M] < k:
            L = M + 1
        else:  # i.e. k < A[M]
            U = M - 1

    return result
