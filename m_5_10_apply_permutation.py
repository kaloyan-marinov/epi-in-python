from typing import List


def apply_permutation(perm: List[int], A: List[int]) -> None:
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
