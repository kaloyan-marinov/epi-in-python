from re import I
from typing import List


def generate_power_set_1(input_set: List[int]) -> List[List[int]]:
    """
    (I think we are intended to)
    Assume that `input_set` consists of distinct entries.
    """

    result: List[List[int]] = []

    for i in range(2 ** len(input_set)):
        indices = []
        for idx in range(len(input_set)):
            if i & (1 << idx):
                indices.append(idx)

        result.append([input_set[idx] for idx in indices])

    return result


def generate_power_set_2(input_set: List[int]) -> List[List[int]]:
    """
    (I think we are intended to)
    Assume that `input_set` consists of distinct entries.
    """

    power_set: List[List[int]] = []

    # Generate all subsets whose intersection with
    # `input_set[0], ..., input_set[next_idx_to_select - 1]`
    # is exactly `selected_entries`.
    def _directed_power_set(
        next_idx_to_select: int,
        selected_entries: List[int],
    ) -> None:
        if next_idx_to_select == len(input_set):
            power_set.append(selected_entries)
            return

        _directed_power_set(
            next_idx_to_select + 1,
            selected_entries,
        )

        # Generate all subsets that contain `input_set[next_idx_to_select]`.
        _directed_power_set(
            next_idx_to_select + 1,
            [input_set[next_idx_to_select]] + selected_entries,
        )

    _directed_power_set(0, [])

    return power_set


import math


def generate_power_set_3(input_set: List[int]) -> List[List[int]]:
    """
    (I think we are intended to)
    Assume that `input_set` consists of distinct entries.
    """

    power_set: List[List[int]] = []

    for subset_identifier in range(1 << len(input_set)):
        bit_array = subset_identifier
        subset: List[int] = []

        while bit_array:
            # fmt: off
            idx = int(
                math.log2(
                    bit_array & ~(bit_array - 1),  # isolates the lowest set bit of `bit_array`.
                )
            )
            # fmt: on
            subset.append(input_set[idx])

            # Erase the lowest set bit of `bit_array`.
            bit_array = bit_array & (bit_array - 1)

        power_set.append(subset)

    return power_set
