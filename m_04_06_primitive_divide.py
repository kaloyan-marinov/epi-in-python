"""
Assume that:
    - each of `x` and `y` is a positive integer
    - you are allowed to use only the addition, subtraction, and shifting operations

Return:
    - the quotient `x / y`
"""


def solution_2_divide(x: int, y: int) -> int:
    """
    This works,
    but can easily be made more efficient.

    time:  O(n**2)
           where n := the # of bits required to represent `x / y`

           assuming that each of the individual shift and add operations takes O(1)
    """

    q = 0
    while x >= y:
        power = solution_2_max_power_of_2(x, y)
        q += 1 << power
        x -= y << power
    return q


def solution_2_max_power_of_2(x: int, y: int) -> int:
    """
    Compute the maximum integer `k` s.t. `x >= y * (2**k)`.

    time:  O(n)
           where n := the # of bits required to represent `x / y`
    """

    power = 0
    while x >= y << power:
        power += 1
    return power - 1


def solution_3_divide(x: int, y: int) -> int:
    """
    This f-n
        is based on the same idea as
        but is more efficient than
    the previous f-n.

    This f-n achieves greater efficiency
    by taking advantage of the fact that
    the `power`/`k` quantity is guaranteed to decrease across consecutive iterations.

    time:  O(n)
           where n := the # of bits required to represent `x / y`

           assuming that each of the individual shift and add operations takes O(1)
    """

    k = solution_3_min_power_of_2(x, y)
    q = 0
    y_times_2_to_the_k = y << k

    while x >= y:
        while y_times_2_to_the_k > x:
            k -= 1
            y_times_2_to_the_k >>= 1

        q += 1 << k
        x -= y_times_2_to_the_k

    return q


def solution_3_min_power_of_2(x: int, y: int) -> int:
    """
    Compute the minimum integer `k` s.t. `x < y * (2**k)`.

    time:  O(n)
           where n := the # of bits required to represent `x / y`
    """

    power = 0
    while x >= y:
        y <<= 1
        power += 1
    return power


if __name__ == "__main__":
    q = solution_3_divide(64, 1)
    print(q)
