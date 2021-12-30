from typing import List

import random

from m_5_12_offline_sampling import (
    random_sampling as generate_random_sample_in_inplace_manner,
)


def random_subset(n: int, k: int) -> List[int]:
    """
    Assume that n >= k.

    Generate - in a uniformly random manner! - a sample of size `k` from {0, ..., n - 1}.

    -----------

    time:  O(n)

    space: O(n)
    """
    A = list(range(n))

    # The next statement is identical to the following commented-out block of code.
    generate_random_sample_in_inplace_manner(k, A)
    # fmt: off
    '''
    for i in range(k):
        r = random.randrange(i, len(A))
        A[i], A[r] = A[r], A[i]
    '''
    # fmt: on

    return A[:k]
