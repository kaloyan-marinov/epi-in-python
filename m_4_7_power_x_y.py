def solution_1_raise_to_arbitrary_power(x: int, y: int) -> int:
    if y < 0:
        x, y = 1 / x, -y

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
    Assume two_to_the_j = (1 0 ... 0)_2
    """
    if two_to_the_j & 1 == 1:
        return x

    result = x
    two_to_the_j >>= 1

    while two_to_the_j:
        result = result * result
        two_to_the_j >>= 1

    return result


def solution_2_power(x: float, y: int) -> float:
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


def solution_3_power(x: float, y: int) -> float:
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

    r = solution_1_raise_to_2_to_j(x, 1)
    print(r)

    r4 = solution_2_power(x, y)
    print(r4)
