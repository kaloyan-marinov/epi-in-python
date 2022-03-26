import random
from typing import List


# def random_sampling(k: int, A: List[int]) -> None:
def generate_random_sample_inplace(
    k: int,
    A: List[int],
) -> None:
    """
    Assume that `A` is an array of distinct elements.

    Generate a (uniformly random) sample of size `k`
    from (offline data available as) an in-memory array `A`
    (in an in-place manner).
    [
    Return - at random! - a subset of size `k` from `A`,
    in such a way that
    each subset of size `k` is equally likely to be returned.
    ]

    The (random) sample is generated
    by modifying `A` in-place in such a way that
      (a) _the elements of_ the generated random sample are in the `A[:k]` subarray, and
      (b) the remaining elements are in the last `n - k` slots.
    In other words, the generated [random] sample is `set(A[:k])`.

    ---

    (It is worthwhile to) Observe that:
    (a) this implementation "returns" a Python (sub)list (rather than a Python set);
    (b) something stronger holds true,
        i.e. that every permutation of every size-`k` subset of `A`
        is equally likely to be in `A[:k]`.

    ---

    time:  O(k)

    space: O(1)
           in addition to the inputs
    """
    for i in range(k):
        r = random.randrange(i, len(A))  # equivalent to random.randint(i, len(A) - 1)
        A[i], A[r] = A[r], A[i]
