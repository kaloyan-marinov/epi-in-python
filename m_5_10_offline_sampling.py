import random
from typing import List


def random_sampling_1(k: int, A: List[int]) -> None:
    """
    Test PASSED (8/8) [ 419 ms]
    Average running time:  368 ms
    Median running time:   335 ms
    """
    _A = list()
    for i in range(k):
        _a = random.choice(A)
        while _a in _A:
            _a = random.choice(A)
        _A.append(_a)
    A[:] = _A


def random_sampling_2(k: int, A: List[int]) -> None:
    """
    Test PASSED (8/8) [ 312 ms]
    Average running time:  313 ms
    Median running time:   308 ms
    """
    for i in range(k):
        r = random.randrange(i, len(A))
        A[i], A[r] = A[r], A[i]
