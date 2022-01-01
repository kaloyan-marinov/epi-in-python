from typing import Dict, List

import random

from m_5_12_offline_sampling import generate_random_sample_inplace


# def random_subset_1(n: int, k: int) -> List[int]:
def generate_random_sample_1(n: int, k: int) -> List[int]:
    """
    Assume that n >= k.

    Generate a (uniformly random) sample of size `k` from ${0, ..., n - 1}$.

    -----------

    time:  O(n)

    space: O(n)
    """
    A = list(range(n))

    # The next statement is identical to the following commented-out block of code.
    generate_random_sample_inplace(k, A)
    # fmt: off
    '''
    for i in range(k):
        r = random.randrange(i, len(A))
        A[i], A[r] = A[r], A[i]
    '''
    # fmt: on

    return A[:k]


# def random_subset_2(n: int, k: int) -> List[int]:
def generate_random_sample_2(n: int, k: int) -> List[int]:
    """
    [
    This function basically/essentially implements the same algorithm as the one above,
    but this function's realization of the algorithm is different
    in a subtle but important way.

    Concretely,
    instead of explicitly allocating a list `A` equal to `[0, ..., n]`,
    this function _simulates_ that list by means of a hash table `idx_2_A_idx`.

    Firstly, `idx_2_A_idx` is initialized as an empty dictionary.
    Then, each iteration updates `idx_2_A_idx` in a way analogous to
    the way in which the previous function updates `A`.

        Throughout all of that,
        `A[i]` is _simulated_ by `idx_2_A_idx.get(i, i)`.
    ]

    -----------

    time:  O(k)

    space: O(k)
    """
    idx_2_A_idx: Dict[int, int] = {}

    for i in range(k):
        r = random.randrange(i, n)

        A_i = idx_2_A_idx.get(i, i)
        A_r = idx_2_A_idx.get(r, r)

        idx_2_A_idx[i] = A_r
        idx_2_A_idx[r] = A_i

    return [idx_2_A_idx[idx] for idx in range(k)]
