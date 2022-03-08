from typing import List

import collections


MinMax = collections.namedtuple("MinMax", ("smallest", "largest"))


def find_min_max_1(A: List[int]) -> MinMax:
    """
    This implements an approach based on brute force,
    which requires 2*(n - 1) comparisons.
    """
    minimum = float("inf")
    maximum = float("-inf")
    for a in A:
        if a < minimum:
            minimum = a
        if a > maximum:
            maximum = a
    return MinMax(minimum, maximum)


def find_min_max_2(A: List[int]) -> MinMax:
    """
    This implements an approach
    motivated by the analogy of searching for the strongest and weakest players
    in a given group of players, assuming the players are totally ordered.

    That approach can be summarized as follows:
    - play n/2 matches between disjoint pairs of players
    - determine the strongest player as the strongest one among the n/2 winners
    - determine the weakest player as the weakest one among the n/2 losers

    # of required comparions: 3*n/2 - 1
    """

    if len(A) == 1:
        return MinMax(A[0], A[0])

    if A[0] < A[1]:
        global_min_max = MinMax(A[0], A[1])
    else:
        global_min_max = MinMax(A[1], A[0])

    # Update `global_min_max`
    # by processing 2 consecutive elements at a time.
    for i in range(2, len(A) - 1, 2):
        if A[i] < A[i + 1]:
            local_min_max = MinMax(A[i], A[i + 1])
        else:
            local_min_max = MinMax(A[i + 1], A[i])

        global_min_max = MinMax(
            min(global_min_max.smallest, local_min_max.smallest),
            max(global_min_max.largest, local_min_max.largest),
        )

    # If `len(A)` is odd,
    # we still need to compare `global_min_max` with the last element.
    if len(A) % 2:
        global_min_max = MinMax(
            min(global_min_max.smallest, A[-1]),
            max(global_min_max.largest, A[-1]),
        )

    return global_min_max


if __name__ == "__main__":
    A = [-11, -14, 5, -2, -3, 7, -3, 10, 11, 14, -6, 4, -1, -6, -4, 12]
    min_max = find_min_max_2(A)
