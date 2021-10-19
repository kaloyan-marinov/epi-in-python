from typing import List


def apply_permutation(perm: List[int], A: List[int]) -> None:
    target_ind = perm[0]
    source_val = A[0]

    while target_ind != None:
        perm[target_ind], A[target_ind], target_ind = (
            None,
            source_val,
            perm[target_ind],
        )

        """
        source_val = A[target_ind]

        if perm[target_ind] is None:
            for i in range(len(A)):
                if perm[i] is not None:
                    target_ind = perm[i]
                    source_val = A[i]
                    break
        """
        if target_ind is None:
            for i in range(len(A)):
                if perm[i] is not None:
                    target_ind = perm[i]
                    source_val = A[i]
                    break
        else:
            source_val = A[target_ind]


if __name__ == "__main__":
    perm = [7, 2, 11, 10, 4, 1, 15, 3, 9, 17, 18, 16, 14, 5, 0, 8, 6, 12, 13]
    A = [7, 10, 14, 1, 15, 9, 16, 4, 0, 11, 12, 18, 3, 13, 5, 8, 17, 2, 6]

    apply_permutation(perm, A)
