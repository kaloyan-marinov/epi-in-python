import functools


@functools.lru_cache(maxsize=None)
def compute_binomial_coefficient(n: int, k: int) -> int:
    if k == 0 or k == n:
        return 1

    return compute_binomial_coefficient(n - 1, k - 1) + compute_binomial_coefficient(
        n - 1, k
    )
