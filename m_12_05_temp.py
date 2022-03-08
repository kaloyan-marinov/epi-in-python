from typing import DefaultDict, List

import collections


def find_nearest_repetition(paragraph: List[str]) -> int:
    """
    This is nearly identical to
    `m_12_05_nearest_repeated_entries.find_nearest_repetition_1`.
    """
    word_2_positions: DefaultDict[str, List[int]] = collections.defaultdict(list)
    for i, w_i in enumerate(paragraph):
        word_2_positions[w_i].append(i)

    position_distance_pair = (-1, None)
    for w, w_positions in word_2_positions.items():
        if len(w_positions) == 1:
            continue

        # Now, `len(w_positions)` is known to be >= 2.
        curr_p = w_positions[0]
        for i in range(1, len(w_positions)):
            next_p = w_positions[i]
            if (
                not position_distance_pair[1]
                or next_p - curr_p < position_distance_pair[1]
            ):
                position_distance_pair = (curr_p, next_p - curr_p)

            curr_p = next_p

    return position_distance_pair[1] if position_distance_pair[1] else -1
