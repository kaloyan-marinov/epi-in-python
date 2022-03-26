from typing import List


def apply_permutation(perm: List[int], A: List[int]) -> None:
    """
    Assume that
    (a) `len(A) = len(perm)`, and
    (b) `perm` is/represents a permutation of ${0, ..., n - 1}$.

    Perform an in-place modification of `A` by applying `perm` to `A`
    (where it is allowed to modify `perm`).

    time:  O(n)
    space: ?
    """

    n = len(A)

    for i in range(n):
        while perm[i] != i:
            A[i], A[perm[i]] = A[perm[i]], A[i]

            # NB:
            # If the order on the LHS of the following statement is swapped,
            # then running this module will cause this f-n to get stuck in an infinite loop.
            perm[perm[i]], perm[i] = perm[i], perm[perm[i]]
            # fmt: off
            '''
            perm[i], perm[perm[i]] = perm[perm[i]], perm[i]
            '''
            # fmt: on


def apply_permutation_2(perm: List[int], A: List[int]) -> None:
    """
    Assume that
    (a) `len(A) = len(perm)`, and
    (b) `perm` is/represents a permutation of ${0, ..., n - 1}$.

    Perform an in-place modification of `A` by applying `perm` to `A`
    (where it is allowed to modify `perm`).

    time:  O(n)
    space: ?
    """

    n = len(A)

    for i in range(n):
        while perm[i] != i:
            source_idx, target_idx = i, perm[i]
            A[source_idx], A[target_idx] = A[target_idx], A[source_idx]
            perm[source_idx], perm[target_idx] = perm[target_idx], perm[source_idx]


if __name__ == "__main__":
    # perm = [7, 2, 11, 10, 4, 1, 15, 3, 9, 17, 18, 16, 14, 5, 0, 8, 6, 12, 13]
    # A = [7, 10, 14, 1, 15, 9, 16, 4, 0, 11, 12, 18, 3, 13, 5, 8, 17, 2, 6]

    perm = [2, 0, 1, 3]
    A = ["a", "b", "c", "d"]

    apply_permutation(perm, A)

    # fmt: off
    print(A)     # ['b', 'c', 'a', 'd']
    print(perm)  # [  0,   1,   2,   3]
    # fmt: on
