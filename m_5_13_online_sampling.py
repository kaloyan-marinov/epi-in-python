from typing import Iterator

import itertools
import random


def online_random_sample(
    stream: Iterator[int],
    k: int,
):
    """
    Assume that there will be >= k elements in the `stream`.
    """
    # Store the 1st k elements.
    reservoir_elements = list(
        itertools.islice(stream, k),
    )

    n = k  # will track the number of elements seen so far.

    for x in stream:
        n += 1

        # According to a probability of k/n:
        #   choose one of the current `reservoir_elements` in a uniformly random manner
        #   and replace it with `x`.
        idx_to_replace = random.randrange(n)
        if idx_to_replace < k:  # i.e. if `idx_to_replace` is in {0, ..., k - 1}
            reservoir_elements[idx_to_replace] = x

    return reservoir_elements
