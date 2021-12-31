import random
from typing import List


def random_sampling(k: int, A: List[int]) -> None:
    """
    Assume that `A` is an array of distinct elements.

    Generate - in a uniformly random manner! - a sample of size `k` from `A`.
    (
    Return - at random! - a subset of size `k` from `A`,
    in such a way that
    each subset of size `k` is equally likely to be returned.
    )

    The [random] sample is generated
    by modifying `A` in-place in such a way that
      (a) _the elements of_ the generated random sample are in the `A[:k]` subarray, and
      (b) the remaining elements are in the last `n - k` slots.
    In other words, the generated [random] sample is `set(A[:k])`.

    ---

    time:  O(k)

    space: O(1)
           in addition to the inputs
    """
    for i in range(k):
        r = random.randrange(i, len(A))  # equivalent to random.randint(i, len(A) - 1)
        A[i], A[r] = A[r], A[i]
