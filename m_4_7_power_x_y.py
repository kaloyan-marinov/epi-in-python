def solution_1_raise_to_arbitrary_power(x: int, y: int) -> int:
    result = 1

    while y:
        # Isolate the last set bit of y.
        last_set_bit_of_y = y & ~(y - 1)

        result *= solution_1_raise_to_2_to_j(x, last_set_bit_of_y)

        # Turn off the last bit of y that is set.
        y = y & (y - 1)

    return result


def solution_1_raise_to_2_to_j(x: int, two_to_the_j: int) -> int:
    """
    Assume j >= 1.
    """
    result = x
    two_to_the_j >>= 1

    while two_to_the_j:
        result = result * result
        two_to_the_j >>= 1
    return result


def failed_attempt_at_solution_2_raise_to_arbitrary_power(x, y):
    """
    Appears to get stuck in an infinite loop...
    """
    if y == 0:
        return x

    last_set_bit_of_y = y & (y - 1)
    contrib = solution_1_raise_to_2_to_j(x, last_set_bit_of_y)
    r = contrib
    y = y & (~(y - 1))

    while y:
        contrib *= 2
        if contrib == y & (y - 1):
            r += contrib
            y = y & (~(y - 1))

    return r


def failed_attempt_at_solution_3_raise_to_arbitrary_power(x, y):
    """
    Appears to return the square of the correct answer...
    """

    contrib = x
    result = 1

    while y:
        contrib = contrib ** 2

        if y & 1 == 1:
            result *= contrib

        y >>= 1

    return result


def solution_4_power(x: float, y: int) -> float:
    if y < 0:
        x, y = 1 / x, -y

    result = 1
    contrib = x
    if y == 0:
        return 1
    elif y & 1 == 1:
        result *= x

    y >>= 1

    while y:
        contrib = contrib ** 2

        if y & 1 == 1:
            result *= contrib

        y >>= 1

    return result


if __name__ == "__main__":
    x = 1.4434757236195281
    y = 12
    r3 = failed_attempt_at_solution_3_raise_to_arbitrary_power(x, y)
    r4 = solution_4_power(x, y)
    print(r3)
    print(r4)
