from typing import List

import random


def random_subset(n: int, k: int) -> List[int]:
    """
    Assume that n >= k.

    Generate - in a uniformly random manner! - a sample of size `k` from {0, ..., n - 1}.

    -----------

    time:  O(n)

    space: O(n)
    """
    A = list(range(n))

    for i in range(k):
        r = random.randrange(i, len(A))
        A[i], A[r] = A[r], A[i]

    return A[:k]
