from typing import List


def find_max_subarray(A: List[int]) -> int:
    """
    Find the maximum sum over all [contiguous] subarrays of `A`.
    """

    # Suppose that, for all `i = 1, ..., j - 1`, we know
    # the maximum sum over all [contiguous] subarrays ending at `i` (inclusive);
    # call those maximum sums `B[i]`.
    # Then, there are only 2 possibilities for
    # the maximum sum over all [contiguous] subarrays ending at `j` (inclusive);
    #   - the subarray is just the element `A[j]`, or
    #   - the subarray includes earlier entries, in which case its sum is `B[j - 1] + A[j]`

    max_seen = 0

    max_end = 0  # Represents "the current entry" of the auxiliary array `B`.
    for a in A:
        max_end = max(a, max_end + a)
        max_seen = max(max_seen, max_end)

    return max_seen
