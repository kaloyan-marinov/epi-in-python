from typing import List

import bintrees
import typing


def find_closest_elements_in_sorted_arrays(
    sorted_arrays: List[List[int]],
) -> int:
    """
    Return the length of the shortest interval
    that contains >= 1 element from each of the `sorted_arrays`.

    Assume that:
        - each of the `sorted_arrays` is non-empty
        - each of the `sorted_arrays` doesn't contain any duplicate values
        - a single value may be present in more than 1 array

    time:  O(n * log k),
           where `n := sum(len(array) for array in sorted_arrays)`
           and `k := len(sorted_arrays)`

    space: O(k)
    """

    r_b_tree = bintrees.RBTree()

    # For each array,
    # insert its min value as well as an iterator for that array
    # into `r_b_tree`.
    for idx, array_idx in enumerate(sorted_arrays):
        it_idx = iter(array_idx)

        next_value_from_it_idx = next(it_idx, None)
        r_b_tree.insert(
            (next_value_from_it_idx, idx),  # TODO: understand why `idx` is needed
            it_idx,
        )

    currently_shortest_interval_length = float("inf")
    while True:
        min_value, min_idx = r_b_tree.min_key()
        max_value, __ = r_b_tree.max_key()
        currently_shortest_interval_length = min(
            currently_shortest_interval_length,
            max_value - min_value,
        )

        __, min_it = r_b_tree.pop_min()
        next_value_from_min_it = next(min_it, None)
        if next_value_from_min_it is None:  # i.e. the array has no remaining elements.
            return typing.cast(int, currently_shortest_interval_length)

        r_b_tree.insert(
            (next_value_from_min_it, min_idx),
            min_it,
        )
