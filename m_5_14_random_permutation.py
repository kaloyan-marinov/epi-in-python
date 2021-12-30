from typing import List

import random


def compute_random_permutation(n: int) -> List[int]:
    """
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
    perm = [None] * n
    added = set()

    i = 0
    while len(added) < n:
        candidate = random.randrange(n)

        if candidate not in added:
            perm[i] = candidate
            added.add(candidate)
            i += 1

    return perm
