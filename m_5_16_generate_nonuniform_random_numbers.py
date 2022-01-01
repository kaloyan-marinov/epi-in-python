import bisect
import itertools
import random

from typing import List


# def nonuniform_random_number_1(
def generate_nonuniform_random_number_1(
    values: List[int],
    probabilities: List[float],
) -> int:
    """
    Given a (not-necessarily-uniform-)probability vector,
    generate (at random) one of the possible outcome( indice)s
    according to the provided probabilities.

    ---

    time:  need to check the documentation of Python's Standard Library

    space: need to check the documentation of Python's Standard Library

    ---

    While this implementation works,
    it does not demonstrate the knowledge/understanding
    that the problem is designed to test.
    """
    choices = random.choices(
        values,
        weights=probabilities,
        k=1,
    )
    return choices[0]


# def nonuniform_random_number_2(
def generate_nonuniform_random_number_2(
    values: List[int],
    probabilities: List[float],
) -> int:
    """
    Given a (not-necessarily-uniform-)probability vector,
    generate (at random) one of the possible outcome( indice)s
    according to the provided probabilities.

    ---

    time:  <= O(n)
           where n := len(values)

    space: O(1)
           beyond the inputs

    Test PASSED (10/10) [ 462 ms]
    Average running time:  534 ms
    Median running time:   531 ms
    """
    p = random.random()

    cumulative_prob = 0.0
    idx = -1

    while cumulative_prob < p:
        idx += 1
        cumulative_prob += probabilities[idx]

    return values[idx]


# def nonuniform_random_number_3(
def generate_nonuniform_random_number_3(
    values: List[int],
    probabilities: List[float],
) -> int:
    """
    Given a (not-necessarily-uniform-)probability vector,
    generate (at random) one of the possible outcome( indice)s
    according to the provided probabilities.

    ---

    time:  to compute a single value
           O(n)
           [which is the time to create the array of intervals]

           once the array is constructed,
           O(log n)

    space: O(n)
           [which is the space required by the array of intervals]

    Test PASSED (10/10) [   2  s]
    Average running time:    1  s
    Median running time:     1  s
    """

    right_endpoints_for_subintervals = list(
        itertools.accumulate(probabilities),
    )

    interval_idx = bisect.bisect(
        right_endpoints_for_subintervals,
        random.random(),
    )

    return values[interval_idx]


if __name__ == "__main__":
    values = [0, 1, 2, 3, 4]

    # fmt: off
    '''
    probabilities = [0, 0.5, 0.3, 0.1, 0.1]
    right_endpoints_for_subintervals = list(
        itertools.accumulate(probabilities),
    )
    print(right_endpoints_for_subintervals)  # [0.0, 0.5, 0.8, 0.9, 1]
    '''
    # fmt: on

    probabilities = [0.05, 0.1, 0.25, 0.2, 0.4]
    right_endpoints_for_subintervals = list(
        itertools.accumulate(probabilities),
    )
    print(right_endpoints_for_subintervals)  # [0.05, 0.15, 0.4, 0.6, 1.0]
