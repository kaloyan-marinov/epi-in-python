from typing import List
import typing


def minimum_messiness(
    words: List[str],
    line_length: int,
) -> int:
    """
    Assume that none of the given `words` exceeds the specified `line_length`.
    """

    # fmt: off
    # [We are going to iteratively populate `min_messiness_values` so that]
    # `min_messiness_values[i]` is the minimum messiness
    # that is achievable when one has to place only `words[0: i + 1]`.
    num_remaining_blanks = line_length - len(words[0])
    
    min_messiness_values: List[int] = (
        [num_remaining_blanks ** 2] +
        [typing.cast(int, float('inf'))] * (len(words) - 1)   # `typing.cast` appears to be unnecessary
    )
    # fmt: on

    for i in range(1, len(words)):
        # Determine the min messiness
        # that is achievable
        # when one has to place only `words[0: i + 1]`.

        # Add `words[i]` to the last line.
        num_remaining_blanks = line_length - len(words[i])
        min_messiness_values[i] = (
            min_messiness_values[i - 1] + num_remaining_blanks ** 2
        )

        # One at a time,
        # try adding `words[i - 1]`, `words[i - 2]`, ...
        # to the last line.
        for j in reversed(range(i)):
            num_remaining_blanks -= len(words[j]) + 1  # The "+ 1" accounts for 1 blank.

            if num_remaining_blanks < 0:
                # Not enough space to add `words[j]` to the last line.
                break

            first_j_messiness = min_messiness_values[j - 1] if j - 1 >= 0 else 0
            min_messiness_values[i] = min(
                min_messiness_values[i],
                first_j_messiness + num_remaining_blanks ** 2,
            )

    return min_messiness_values[-1]
