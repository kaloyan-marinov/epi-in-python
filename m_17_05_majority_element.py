from typing import Iterator


import collections


def majority_search(stream: Iterator[str]) -> str:
    """
    Assume that `stream` is non-empty.

    Assume that more than half of the strings are repetitions of a single string
    (the "majority element" [in the `stream`]).

    While this f-n works,
    it is not an acceptable solution,
    because its space complexity is worse than O(1).
    """

    element_2_count = collections.defaultdict(int)

    max_element = None
    max_count = float("-inf")

    for x in stream:
        element_2_count[x] += 1
        if element_2_count[x] > max_count:
            max_element = x
            # max_count += 1
            max_count = element_2_count[x]

    return max_element


def majority_search_2(stream: Iterator[str]) -> str:
    """
    Assume that `stream` is non-empty.

    Assume that more than half of the strings are repetitions of a single string
    (the "majority element" [in the `stream`]).

    TODO: work through the mathematical justification
    """

    candidate_count = 0

    for x in stream:
        if candidate_count == 0:
            candidate = x
            candidate_count = 1
        elif x == candidate:
            candidate_count += 1
        else:  # i.e. `candidate_count > 0 and x != candidate`
            candidate_count -= 1

    return candidate


if __name__ == "__main__":
    r = majority_search_2([])
