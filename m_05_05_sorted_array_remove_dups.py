import copy

from typing import List


def delete_duplicates_1(A: List[int]) -> int:
    """
    Test PASSED (2003/2003) [  51  s]
    Average running time:   26 ms
    Median running time:    20 us
    """
    num_valid = len(A)

    i = 0
    while i < num_valid:
        if i + 1 == num_valid:
            break

        if A[i] == A[i + 1]:
            A[i:] = A[i + 1 :]
            num_valid -= 1
        else:
            i += 1

    return num_valid


def delete_duplicates_2(A: List[int]) -> int:
    """
    Test PASSED (2003/2003) [  32 ms]
    Average running time:   96 us
    Median running time:    29 us
    """
    i = 0

    while i < len(A):
        num_copies_of_a_i = 1  # error!
        while (
            i + num_copies_of_a_i < len(A) and A[i] == A[i + num_copies_of_a_i]
        ):  # error!
            num_copies_of_a_i += 1

        if num_copies_of_a_i >= 2:
            A[i + 1 :] = A[i + num_copies_of_a_i :]  # error!

        i += 1

    return len(A)


def delete_duplicates_3(A: List[int]) -> int:
    """
    This solution is based on brute force.
    time: O(n)
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


if __name__ == "__main__":
    # fmt: off
    A = [-8, -7, -6, -5, -5, -4, -3, -1, -1, 0, 0, 2, 2, 2, 4]
    # fmt: on
    A_original = copy.deepcopy(A)
    num_valid = delete_duplicates_3(A)  # outputs [-8, -7, -6, -5, -4, -3, -1, 0, 2, 4]

    print("A_original")
    print(A_original)
    print("A")
    print(A)  # [-8, -7, -6, -5, -5, -4, -3, -1, -1, 0, 0, 2, 2, 2, 4]
    print(num_valid)  # 10
