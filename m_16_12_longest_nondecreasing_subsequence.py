from typing import List

import functools


def longest_nondecreasing_subsequence_length(A: List[int]) -> int:
    """
    For example, if `A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9]`,
    then the length of a longest nondecreasing subsequence is 4.
    There are multiple subsequences which achieve that length
    (such as `[0, 4, 10, 14]` and `[0, 2, 6, 9]`).

    Note that the elements of a nondecreasing subsequence
    are not required to immediately follow each other.
    """

    @functools.lru_cache(maxsize=None)
    def _longest_nondecreasing_subsequence_ending_at(idx: int) -> int:
        """
        Return the length of a longest nondecreasing subsequence ending at `A[idx]`.
        """
        if idx == 0:
            return 1

        length = 1
        for j in range(idx):
            if A[j] <= A[idx]:
                length = max(
                    length,
                    _longest_nondecreasing_subsequence_ending_at(j) + 1,
                )

        return length

    return max(_longest_nondecreasing_subsequence_ending_at(l) for l in range(len(A)))


def longest_nondecreasing_subsequence_length_2_a(A: List[int]) -> int:
    """
    For example, if `A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9]`,
    then the length of a longest nondecreasing subsequence is 4.
    There are multiple subsequences which achieve that length
    (such as `[0, 4, 10, 14]` and `[0, 2, 6, 9]`).

    Note that the elements of a nondecreasing subsequence
    are not required to immediately follow each other.
    """

    solution_for_subarray_ending_at = [1] * len(A)

    for idx in range(1, len(A)):
        for j in range(idx):
            if A[j] <= A[idx]:
                solution_for_subarray_ending_at[idx] = max(
                    solution_for_subarray_ending_at[idx],
                    solution_for_subarray_ending_at[j] + 1,
                )

    return max(solution_for_subarray_ending_at)


def longest_nondecreasing_subsequence_length_2_b(A: List[int]) -> int:
    """
    For example, if `A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9]`,
    then the length of a longest nondecreasing subsequence is 4.
    There are multiple subsequences which achieve that length
    (such as `[0, 4, 10, 14]` and `[0, 2, 6, 9]`).

    Note that the elements of a nondecreasing subsequence
    are not required to immediately follow each other.
    """

    max_lengths = [1] * len(A)

    for idx in range(1, len(A)):
        max_lengths[idx] = (
            max((max_lengths[j] for j in range(idx) if A[j] <= A[idx]), default=0) + 1
        )

    return max(max_lengths)


if __name__ == "__main__":
    A = [5, 16, 5, 3, 9, 16, 20, 0, 6, 10, 12, 11, 6, 16, 10, 19, 20, 16, 13, 6]
    result = longest_nondecreasing_subsequence_length(A)
    print(result)
