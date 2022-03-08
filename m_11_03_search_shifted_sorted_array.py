from typing import List


def search_smallest(A: List[int]) -> int:
    L = 0
    U = len(A) - 1

    while L < U:  # Note the strict inequality!
        M = (L + U) // 2  # L + (U - L) // 2

        if A[M] > A[U]:
            # The min's index must lie in [M + 1, U].
            L = M + 1
        elif A[M] < A[U]:
            # The min's index cannot lie in [M + 1, U].
            U = M
        # else:  # i.e. A[M] == A[U]
        #   By the problem statement, all elements of A are distinct,
        #   so A[M] == A[U] implies M == U,
        #   which can only happen when L == U,
        #   which cannot be true during any execution of this loop's body.

    return L
