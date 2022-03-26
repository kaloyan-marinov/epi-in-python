import functools
from typing import List

import collections


Item = collections.namedtuple(
    "Item",
    ("weight", "value"),
)


def optimum_subject_to_capacity_2(items: List[Item], capacity: int) -> int:
    """
    My own rendition of the official solution.
    """

    @functools.lru_cache(maxsize=None)
    def _helper(
        start_idx: int,
        remaining_capacity: int,
    ) -> int:

        if start_idx == len(items) or remaining_capacity <= 0:
            return 0

        if remaining_capacity - items[start_idx].weight >= 0:
            value_with_start_idx = items[start_idx].value + _helper(
                start_idx + 1,
                remaining_capacity - items[start_idx].weight,
            )
        else:
            value_with_start_idx = 0

        value_without_start_idx = _helper(
            start_idx + 1,
            remaining_capacity,
        )

        return max(
            value_with_start_idx,
            value_without_start_idx,
        )

    return _helper(0, capacity)


def optimum_subject_to_capacity(items: List[Item], capacity: int) -> int:
    @functools.lru_cache(maxsize=None)
    def _optimum_subject_to_item_and_capacity(
        k: int,
        available_capacity: int,
    ) -> int:
        """
        Return the optimum value
        when we choose from `items[:k + 1]`
        and have a capacity of `available_capacity`.
        """

        if k < 0:
            # No items can be chosen.
            return 0

        without_curr_item = _optimum_subject_to_item_and_capacity(
            k - 1,
            available_capacity,
        )

        with_curr_item = (
            0
            if available_capacity - items[k].weight < 0
            else items[k].value
            + _optimum_subject_to_item_and_capacity(
                k - 1,
                available_capacity - items[k].weight,
            )
        )

        return max(without_curr_item, with_curr_item)

    return _optimum_subject_to_item_and_capacity(
        len(items) - 1,
        capacity,
    )


if __name__ == "__main__":
    items = [
        Item(value=t[0], weight=t[1])
        for t in [
            (65, 20),
            (35, 8),
            (245, 60),
            (195, 55),
            (65, 40),
            (150, 70),
            (275, 85),
            (155, 25),
            (120, 30),
            (320, 65),
            (75, 75),
            (40, 10),
            (200, 95),
            (100, 50),
            (220, 40),
            (99, 10),
        ]
    ]
    capacity = 130

    result = optimum_subject_to_capacity(
        items,
        capacity,
    )

    print(result)
