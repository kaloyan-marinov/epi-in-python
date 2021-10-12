import copy

from typing import List


def delete_duplicates(A: List[int]) -> int:
    num_valid = len(A)

    i = 0
    while i < num_valid:
        if i + 1 == num_valid:
            break

        if A[i] == A[i + 1]:
            A = A[:i] + A[i + 1 :]
            num_valid -= 1

        i += 1

    print(A)

    return num_valid


if __name__ == "__main__":
    A = [-8, -7, -6, -5, -5, -4, -3, -1, -1, 0, 0, 2, 2, 2, 4]
    A_original = copy.deepcopy(A)
    num_valid = delete_duplicates(A)  # outputs [-8, -7, -6, -5, -4, -3, -1, 0, 2, 2, 4]

    print(A_original)  # [-8, -7, -6, -5, -5, -4, -3, -1, -1, 0, 0, 2, 2, 2, 4]
    # print(A)
    print(num_valid)  # 11
