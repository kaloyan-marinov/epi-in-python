import random
from typing import List


def random_sampling(k: int, A: List[int]) -> None:
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
