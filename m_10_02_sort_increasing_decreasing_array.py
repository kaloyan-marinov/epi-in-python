from typing import List

from m_10_01_sorted_arrays_merge import merge_sorted_arrays


def sort_k_increasing_decreasing_array(A: List[int]) -> List[int]:
    """
    add m_10_02_sort_increasing_decreasing_array.py which is incorrect
    """
    indices = [0]
    sign = 1
    for i in range(1, len(A)):
        if sign * (A[i] - A[i - 1]) >= 0:
            continue
        else:
            indices.append(i)
            sign *= -1

    increasing_subarrays = []
    for i, start, final in enumerate(
        zip(indices[:-1], indices[1:]),
    ):
        if i % 2 == 0:
            increasing_subarrays.append(A[start:final])
        else:
            increasing_subarrays.append(A[start:final:-1])

    return merge_sorted_arrays(increasing_subarrays)


def sort_k_increasing_decreasing_array_pythonic(A: List[int]) -> List[int]:
    class Monotonic:
        def __init__(self):
            self._last = float("-inf")

        def __call__(self, curr):
            result = curr < self._last
            self._last = curr
            return result

    return merge_sorted_arrays(
        [
            list(group)[:: -1 if is_decreasing else 1]
            for is_decreasing, group in itertools.groupby(A, Monotonic())
        ]
    )


if __name__ == "__main__":
    pass
