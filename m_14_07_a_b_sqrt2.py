from typing import List

import math
import bintrees


class Number:
    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b

    @property
    def value(self):
        return self.a + self.b * math.sqrt(2)

    def __lt__(self, other: "Number") -> bool:
        return self.value < other.value

    def __eq__(self, other: "Number") -> bool:
        return self.value == other.value  # >> `math.isclose(self.value, other.value)` ?


def generate_first_k_a_b_sqrt2_1(k: int) -> List[float]:
    r_b_tree_of_candidates: bintrees.RBTree = bintrees.RBTree(
        [
            (Number(0, 0), None),
        ],
    )

    result: List[float] = []
    for _ in range(k):
        next_smallest, __ = r_b_tree_of_candidates.pop_min()

        result.append(next_smallest.value)

        r_b_tree_of_candidates.insert(
            Number(next_smallest.a + 1, next_smallest.b), None
        )
        r_b_tree_of_candidates.insert(
            Number(next_smallest.a, next_smallest.b + 1), None
        )

    return result


def generate_first_k_a_b_sqrt2_2(k: int) -> List[float]:
    numbers: List[Number] = [Number(0, 0)]
    i = 0
    j = 0

    for _ in range(k):  # change to either `range(k - 1)` or `range(1, k)`
        candidate_i = Number(numbers[i].a + 1, numbers[i].b)
        candidate_j = Number(numbers[j].a, numbers[j].b + 1)

        next_number = min(candidate_i, candidate_j)
        numbers.append(next_number)

        if next_number == candidate_i:
            i += 1
        if next_number == candidate_j:
            j += 1

    return [n_obj.value for n_obj in numbers]
