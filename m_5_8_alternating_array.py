from typing import List


def rearrange(A: List[int]) -> None:
    if len(A) == 0 or len(A) == 1:
        return

    if A[0] > A[1]:
        A[0], A[1] = A[1], A[0]

    if len(A) == 2:
        return

    for i in range(len(A) - 2):
        nonincreasing = 1 if i % 2 == 0 else -1
        if (A[i + 2] - A[i + 1]) * nonincreasing <= 0:
            continue
        else:
            A[i + 1], A[i + 2] = A[i + 2], A[i + 1]
