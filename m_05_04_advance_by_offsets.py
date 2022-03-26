from typing import List


def can_reach_end(A: List[int]) -> bool:
    """
    Assume that `A` represents a [linear] board for a game,
    in which the goal is to advance from the start index of `A` to its last index.

    For each index `i`,
    `A[i]` denotes the max # of cells that the player is allowed to advance from `i`.

    Returns whether it is possible to achieve the goal of the game.
    """

    last_index = len(A) - 1

    furthest_reachable_idx = 0
    i = 0
    while i <= furthest_reachable_idx and furthest_reachable_idx < last_index:
        furthest_reachable_idx = max(
            furthest_reachable_idx,
            i + A[i],
        )
        i += 1

    return furthest_reachable_idx >= last_index


if __name__ == "__main__":
    # A = [3, 3, 1, 0, 2, 0, 1]  # expected: True
    # A = [3, 2, 0, 0, 2, 0, 1]  # expected False
    # A = [0]  # expected: True
    A = [5, 1, 4, 0, 1, 0, 0]  #  expected: True

    a = can_reach_end(A)

    print(A)
    print(a)
