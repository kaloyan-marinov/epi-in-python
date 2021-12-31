from typing import List

import random


def compute_random_permutation_1(n: int) -> List[int]:
    """
    Generate a (uniformly random) permutation of `n` elements
    / Sample an element from S_n at random.

    space: O(n)
           beyond that of the result array

    time:  O(n log(n))

           the time complexity is slightly challenging to analyze:
           (a) early on, it takes very few iterations
               (and, with that, very few calls to the provided random number generator)
               to get more new values
           (b) it takes a long time to collect the last few values

           Computing the average # of tries (required)
           [to compute the permutation in this way]
           is known as the Coupon Collector's Problem.
           It is known that
           the average # of tries (and hence the average time complexity)
           is O(n log(n)).

    Test PASSED (6/6) [  13  s]
    Average running time:    7  s
    Median running time:     7  s
    *** You've passed ALL tests. Congratulations! ***
    """
    permutation = [None] * n
    added_indices = set()

    i = 0
    while len(added_indices) < n:
        candidate = random.randrange(n)

        if candidate not in added_indices:
            permutation[i] = candidate
            added_indices.add(candidate)
            i += 1

    return permutation


from m_5_12_offline_sampling import (
    random_sampling as generate_random_sample_in_inplace_manner,
)


def compute_random_permutation_2(n: int) -> List[int]:
    """
    Generate a (uniformly random) permutation of `n` elements
    / Sample an element from $S_n$ at random.

    space: none
           outside of the needed for the result array itself

    time:  O(n)

    Test PASSED (6/6) [   8  s]
    Average running time:    5  s
    Median running time:     5  s
    *** You've passed ALL tests. Congratulations! ***
    """
    permutation = list(range(n))

    generate_random_sample_in_inplace_manner(n, permutation)

    return permutation
