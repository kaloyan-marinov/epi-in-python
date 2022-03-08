from typing import List


def search_entry_equal_to_its_index(A: List[int]) -> int:
    left = 0
    right = len(A) - 1

    while left <= right:
        middle = (left + right) // 2  # left + (right - left) // 2

        if A[middle] - middle == 0:
            return middle
        elif A[middle] - middle < 0:
            right = middle - 1
        else:  # i.e. 0 < A[middle] - middle
            left = middle + 1

    return -1
