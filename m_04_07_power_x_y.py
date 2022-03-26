def solution_2_power(x: float, y: int) -> float:
    """
    Return x**y.

    time:  O(log y) = O(n)
           where n := the # of bits needed to represent `y`
    """

    if y < 0:
        x, y = 1 / x, -y

    result = 1
    contrib = x

    while y:

        if y & 1 == 1:
            result *= contrib

        contrib = contrib ** 2

        y >>= 1

    return result


def solution_3_power(x: float, y: int) -> float:
    """
    This function is identical to the previous one.
    """

    if y < 0:
        x, y = 1.0 / x, -y

    result = 1.0
    x_to_two_to_the_j = x

    while y:
        if y & 1 == 1:
            result *= x_to_two_to_the_j

        x_to_two_to_the_j = x_to_two_to_the_j ** 2

        y >>= 1

    return result


if __name__ == "__main__":
    x = -1.4434757236195281
    y = 12

    r4 = solution_2_power(x, y)
    print(r4)
