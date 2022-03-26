from typing import List


def rearrange_1(A: List[int]) -> None:
    """
    Perform an in-place modification of `A`
    so that the modified `A` will have the property that `A[0] <= A[1] >= A[2] <= ...`.

    time:  O(n)
    space: O(1)
    """
    if len(A) == 0 or len(A) == 1:
        return

    if A[0] > A[1]:
        A[0], A[1] = A[1], A[0]

    for i in range(len(A) - 2):
        nonincreasing = 1 if i % 2 == 0 else -1
        if (A[i + 2] - A[i + 1]) * nonincreasing <= 0:
            continue
        else:
            A[i + 1], A[i + 2] = A[i + 2], A[i + 1]


def rearrange_2(A: List[int]) -> None:
    """
    Perform an in-place modification of `A`
    so that the modified `A` will have the property that `A[0] <= A[1] >= A[2] <= ...`.

    time:  O(n)
    space: O(1)
    """
    for i in range(len(A)):
        A[i : i + 2] = sorted(
            A[i : i + 2],
            reverse=bool(i % 2),
        )
