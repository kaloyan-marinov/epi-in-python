from typing import List


def can_reach_end_1(A: List[int]) -> bool:
    reachable_indices = {0}

    for i in range(len(A)):
        if i not in reachable_indices:
            continue

        if A[i] == 0:
            continue

        for j in range(A[i]):
            reachable_indices.add(i + j + 1)

    return len(A) - 1 in reachable_indices


def can_reach_end_2(A: List[int]) -> bool:
    if len(A) == 1:
        return True

    good = {len(A) - 1}
    for i in reversed(range(len(A) - 1)):
        reachables_from_i = {i + a_i for a_i in range(1, A[i] + 1)}
        if reachables_from_i.intersection(good):
            good.add(i)

    return 0 in good


if __name__ == "__main__":
    A = [3, 3, 1, 0, 2, 0, 1]

    can_reach_end_2(A)
