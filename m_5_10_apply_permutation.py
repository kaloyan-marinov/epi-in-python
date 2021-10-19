from typing import List


def apply_permutation(perm: List[int], A: List[int]) -> None:
    n = len(A)

    for i in range(n):
        while perm[i] != i:
            A[i], A[perm[i]] = A[perm[i]], A[i]
            perm[i], perm[perm[i]] = perm[perm[i]], perm[i]


if __name__ == "__main__":
    # perm = [7, 2, 11, 10, 4, 1, 15, 3, 9, 17, 18, 16, 14, 5, 0, 8, 6, 12, 13]
    # A = [7, 10, 14, 1, 15, 9, 16, 4, 0, 11, 12, 18, 3, 13, 5, 8, 17, 2, 6]

    perm = [2, 0, 1, 3]
    A = ["a", "b", "c", "d"]

    # fmt: off
    '''
    instead of modifying `A` in-place into `['b', 'c', 'a', 'd'],
    the next statement gets stuck in an infinite loop

    the reason is that the first pass through the first `while` loop
    updates the arrays to the following state:

    A =     ['c', 'b', 'a', 'd']
    perm =  [  1,   2,   1,   3]   # should instead be [1, 0, 2, 3]
    '''
    # fmt : on
    apply_permutation(perm, A)
