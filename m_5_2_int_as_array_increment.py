import copy
from typing import List


def plus_one(A: List[int]) -> List[int]:
    D = copy.deepcopy(A)
    _incr_by_1(D)
    return D


def _incr_by_1(D: List[int]) -> None:
    for i in reversed(range(len(D))):
        if 0 <= D[i] <= 8:
            D[i] += 1
            break
        else:  # i.e. D[i] == 9
            D[i] = 0

    if D[0] == 0:
        D.insert(0, 1)
