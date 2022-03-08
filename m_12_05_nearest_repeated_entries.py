from typing import DefaultDict, List, Dict, cast

import collections


def find_nearest_repetition_1(paragraph: List[str]) -> int:
    word_2_positions: DefaultDict[str, List[int]] = collections.defaultdict(list)
    for i, w_i in enumerate(paragraph):
        word_2_positions[w_i].append(i)

    position_distance_pair = (-1, float("inf"))
    for w, w_positions in word_2_positions.items():
        if len(w_positions) == 1:
            continue

        # Now, `len(w_positions)` is known to be >= 2.
        curr_p = w_positions[0]
        for i in range(1, len(w_positions)):
            next_p = w_positions[i]
            if next_p - curr_p < position_distance_pair[1]:
                position_distance_pair = (curr_p, next_p - curr_p)

            curr_p = next_p

    return position_distance_pair[1]


def find_nearest_repetition_2(paragraph: List[str]) -> int:
    word_2_latest_index: Dict[str, int] = {}
    distance_between_nearest_repeats = float("inf")

    for i, w_i in enumerate(paragraph):
        if w_i in word_2_latest_index:
            distance_between_nearest_repeats = min(
                distance_between_nearest_repeats,
                i - word_2_latest_index[w_i],
            )

        word_2_latest_index[w_i] = i

    return (
        cast(int, distance_between_nearest_repeats)
        if distance_between_nearest_repeats != float("inf")
        else -1
    )
