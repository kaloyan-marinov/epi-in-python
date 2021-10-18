import random

from typing import List


def nonuniform_random_number(
    numbers: List[int],
    probabilities: List[float],
) -> int:
    p = random.random()

    cumulative_prob = 0.0
    idx = -1

    while cumulative_prob < p:
        idx += 1
        cumulative_prob += probabilities[idx]

    return numbers[idx]
