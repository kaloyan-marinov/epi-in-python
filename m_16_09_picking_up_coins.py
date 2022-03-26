from typing import List

import functools


def maximum_revenue(coins: List[int]) -> int:
    """
    Assume that `coins` consists of an even number of positive(?) integers.
    """

    @functools.lru_cache(maxsize=None)
    def _optimum_achievable_revenue(a: int, b: int) -> int:
        """
        Return the optimum value that a player can achieve
        assuming that
        (a) it is his turn to start, and
        (b) the (remaining) coins on the table are `coins[a : b + 1]`.
        """

        if a == b:  # change to a > b
            return coins[a]  # change to 0

        pick_a_remaining_value = min(
            _optimum_achievable_revenue(a + 2, b),
            _optimum_achievable_revenue(a + 1, b - 1),
        )

        pick_b_remaining_value = min(
            _optimum_achievable_revenue(a + 1, b - 1),
            _optimum_achievable_revenue(a, b - 2),
        )

        return max(
            coins[a] + pick_a_remaining_value,
            coins[b] + pick_b_remaining_value,
        )

    return _optimum_achievable_revenue(0, 0)  # change to (0, len(coins) - 1)
