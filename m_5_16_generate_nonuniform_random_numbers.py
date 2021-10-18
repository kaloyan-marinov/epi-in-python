import bisect
import itertools
import random

from typing import List


def solution_1_nonuniform_random_number(
    values: List[int],
    probabilities: List[float],
) -> int:
    """
    time:  <= O(n) where n := len(values)
    space: O(1)    beyond the inputs

    Test PASSED (10/10) [ 462 ms]
    Average running time:  534 ms
    Median running time:   531 ms
    """
    p = random.random()

    cumulative_prob = 0.0
    idx = -1

    while cumulative_prob < p:
        idx += 1
        cumulative_prob += probabilities[idx]

    return values[idx]


def solution_2_nonuniform_random_number(
    values: List[int],
    probabilities: List[float],
) -> int:
    """
    time:  to compute a single value
           O(n) [which is the time to create the array of intervals]

           once the array is constructed,
           O(log n)

    space: O(n) [which is the space required by the array of intervals]

    Test PASSED (10/10) [   2  s]
    Average running time:    1  s
    Median running time:     1  s
    """

    prefix_sum_of_probabilities = list(
        itertools.accumulate(probabilities),
    )

    interval_idx = bisect.bisect(
        prefix_sum_of_probabilities,
        random.random(),
    )

    return values[interval_idx]


if __name__ == "__main__":
    values = [0, 1, 2, 3, 4]

    # fmt: off
    '''
    probabilities = [0, 0.5, 0.3, 0.1, 0.1]
    prefix_sum_of_probabilities = list(
        itertools.accumulate(probabilities),
    )
    print(prefix_sum_of_probabilities)  # [0.0, 0.5, 0.8, 0.9, 1]
    '''
    # fmt: on

    probabilities = [0.05, 0.1, 0.25, 0.2, 0.4]
    prefix_sum_of_probabilities = list(
        itertools.accumulate(probabilities),
    )
    print(prefix_sum_of_probabilities)  # [0.05, 0.15, 0.4, 0.6, 1.0]
