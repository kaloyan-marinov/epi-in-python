from typing import List


def find_max_subarray(A: List[int]) -> int:
    max_seen = 0

    max_end = 0  # Represents "the current entry" of the auxiliary array `B`.
    for a in A:
        max_end = max(a, a + max_end)
        max_seen = max(max_seen, max_end)

    return max_seen
