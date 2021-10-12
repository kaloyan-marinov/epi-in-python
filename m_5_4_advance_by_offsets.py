from typing import List


def can_reach_end_1(A: List[int]) -> bool:
    """
    This function passes all but the last of the EPI Judge tests.

    With respect to that last test,
    the execution of this function ends up taking a _very_ long time,
    indicating that its time complexity is _very_ high.
    """
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
    """
    This function passes all but the last of the EPI Judge tests.

    With respect to that last test,
    the execution of this function ends up taking a _very_ long time,
    indicating that its time complexity is _very_ high.
    """
    if len(A) == 1:
        return True

    good = {len(A) - 1}
    for i in reversed(range(len(A) - 1)):
        reachables_from_i = {i + a_i for a_i in range(1, A[i] + 1)}
        if reachables_from_i.intersection(good):
            good.add(i)

    return 0 in good


def can_reach_end_3(A: List[int]) -> bool:
    furthest_reach = 0

    for i in range(len(A)):
        furthest_reach = max(furthest_reach, i + A[i])

        if i == furthest_reach:
            return False

    return furthest_reach >= len(A) - 1


if __name__ == "__main__":
    # A = [3, 3, 1, 0, 2, 0, 1]  # expected: True
    # A = [3, 2, 0, 0, 2, 0, 1]  # expected False
    A = [0]  # expected: True

    a = can_reach_end_3(A)

    print(A)
    print(a)
