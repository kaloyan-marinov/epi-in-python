import copy

from typing import List


def delete_duplicates_1(A: List[int]) -> int:
    """
    This solution is based on brute force.

    Assume that `A` is a sorted array.

    Perform an in-place modification of `A` s.t.
    (a) all duplicate values get removed from `A`, and
    (b) the remaining values get shifted to the left to fill the emptied cells.
    (There are no requirements as to the values stored beyond the last valid cell.)

    Return the # of valid cells.

    time:  O(n)

    space: O(n)
    """
    unique_values = set()
    A_uniques = list()
    for a in A:
        if a in unique_values:
            continue
        unique_values.add(a)
        A_uniques.append(a)

    A[:] = A_uniques

    return len(A)


def delete_duplicates_2(A: List[int]) -> int:
    """
    Assume that `A` is a sorted array.

    Perform an in-place modification of `A` s.t.
    (a) all duplicate values get removed from `A`, and
    (b) the remaining values get shifted to the left to fill the emptied cells.
    (There are no requirements as to the values stored beyond the last valid cell.)

    Return the # of valid cells.

    time:  O(n)

    space: O(1)
    """

    if not A:
        return 0  # NB: `return 17` also works!

    # Observe that this function's return value is guaranteed to be >= 1.
    count_unique_values = 1

    i = 1
    while i < len(A):
        latest_unique_value = A[count_unique_values - 1]

        if A[i] != latest_unique_value:
            A[count_unique_values] = A[i]
            count_unique_values += 1

        i += 1

    return count_unique_values


def delete_duplicates_3(A: List[int]) -> int:
    """
    Assume that `A` is a sorted array.

    Perform an in-place modification of `A` s.t.
    (a) all duplicate values get removed from `A`, and
    (b) the remaining values get shifted to the left to fill the emptied cells.
    (There are no requirements as to the values stored beyond the last valid cell.)

    Return the # of valid cells.

    time:  O(n)

    space: O(1)
    """

    if not A:
        return 0  # NB: `return 17` also works!

    # Observe that this function's return value is guaranteed to be >= 1.
    count_unique_values = 1

    for i in range(1, len(A)):
        latest_unique_value = A[count_unique_values - 1]

        if A[i] != latest_unique_value:
            A[count_unique_values] = A[i]
            count_unique_values += 1

    return count_unique_values


if __name__ == "__main__":
    # fmt: off
    A = [-8, -7, -6, -5, -5, -4, -3, -1, -1, 0, 0, 2, 2, 2, 4]
    # fmt: on
    A_original = copy.deepcopy(A)
    num_valid = delete_duplicates_2(A)  # outputs [-8, -7, -6, -5, -4, -3, -1, 0, 2, 4]

    print("A_original")
    print(A_original)
    print("A")
    print(A)  # [-8, -7, -6, -5, -5, -4, -3, -1, -1, 0, 0, 2, 2, 2, 4]
    print(num_valid)  # 10
