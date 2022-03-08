from typing import List

import operator
import random


def find_kth_largest_1(k: int, A: List[int]) -> int:
    # A_sorted = A.sort()
    # A_sorted = sorted(A)
    A_sorted = sorted(A, reverse=True)
    return A_sorted[k - 1]


def find_kth_largest_2(k: int, A: List[int]) -> int:
    """
    Since each iteration _is expected_
    to reduce the number of elements under consideration
    _on average by a factor of 2_,
    the average time complexity T(n) satisfies T(n) = T(n/2) + O(n).
    This solves to T(n) = O(n).

    space: O(1)

    worst-case time complexity: O(n^2)
                                which occurs when the randomly selected pivot is
                                the smallest or largest element in the current subarray

    the probability of the worst case declines exponentially
    with the length of the input array,
    and the worst case is a non-issue in practice

    For this reason, the "randomize[d] selection algorithm" is sometimes said to have
    almost certain O(n) time complexity.
    """

    def _helper(comp):
        """
        Partition `A[left:right + 1]` around `pivot_idx` so that
        `A[left:pivot_idx]` will contain the elements that are > the pivot
        and `A[pivot_idx + 1:right + 1]` will contain the elements that are < the pivot.

        Return `new_pivot_idx` (= the new index of the pivot element after partition).

        Note: ">" and "<" are defined by the `comp` object.
        """

        def partition_around_pivot(left, right, pivot_idx):
            pivot_value = A[pivot_idx]
            new_pivot_idx = left

            A[pivot_idx], A[right] = A[right], A[pivot_idx]

            for i in range(left, right):
                if comp(A[i], pivot_value):
                    A[i], A[new_pivot_idx] = A[new_pivot_idx], A[i]
                    new_pivot_idx += 1

            A[right], A[new_pivot_idx] = A[new_pivot_idx], A[right]

            return new_pivot_idx

        left = 0
        right = len(A) - 1
        while left <= right:
            pivot_idx = random.randint(left, right)

            new_pivot_idx = partition_around_pivot(left, right, pivot_idx)

            if new_pivot_idx == k - 1:
                return A[new_pivot_idx]
            elif new_pivot_idx > k - 1:
                right = new_pivot_idx - 1
            else:  # i.e. new_pivot_idx < k - 1
                left = new_pivot_idx + 1

    return _helper(operator.gt)
