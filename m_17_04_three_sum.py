from typing import List


def has_two_sum(A: List[int], t: int) -> bool:
    i = 0
    j = len(A) - 1

    while i <= j:
        if A[i] + A[j] == t:
            return True
        elif A[i] + A[j] < t:
            i += 1
        else:  # i.e. A[i] + A[j] > t
            j -= 1

    return False


def has_three_sum(A: List[int], t: int) -> bool:
    # A.sort()

    for i in range(len(A)):
        # if has_two_sum(A[i:], t - A[i]):
        if has_two_sum(A, t - A[i]):
            return True

    return False


if __name__ == "__main__":
    A = [1, 4, 0, -3, -1, 0, -7]
    t = -17

    result = has_three_sum(A, t)
