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
    Average running time:   85 us
    Median running time:    24 us
    """
    num_valid = len(A)

    i = 0
    while i < num_valid:
        if i + 1 == num_valid:
            break

        num_copies_of_a_i = 1  # error!
        while (
            i + num_copies_of_a_i < len(A) and A[i] == A[i + num_copies_of_a_i]
        ):  # error!
            num_copies_of_a_i += 1

        if num_copies_of_a_i >= 2:
            A[i + 1 :] = A[i + num_copies_of_a_i :]  # error!
            num_valid -= num_copies_of_a_i - 1

        i += 1

    return num_valid


if __name__ == "__main__":
    # fmt: off
    A = [-27, -24, -21, -21, -20, -19, -19, -19, -18, -18, -16, -14, -13, -13, -11, -10, -7, -5, -4, 1, 2, 2, 4, 4, 4, 4, 8, 9, 10, 10, 10, 10, 11, 12, 13, 13, 14, 14, 15, 16, 16, 17, 17, 17, 20, 20, 21, 21, 22, 25, 25, 25, 26, 26]
    # fmt: on
    A_original = copy.deepcopy(A)
    num_valid = delete_duplicates_2(A)  # outputs [-8, -7, -6, -5, -4, -3, -1, 0, 2, 4]

    print("A_original")
    print(A_original)
    print("A")
    print(A)  # [-8, -7, -6, -5, -5, -4, -3, -1, -1, 0, 0, 2, 2, 2, 4]
    print(num_valid)  # 10
