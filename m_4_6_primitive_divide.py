def quotient_1(x: int, y: int) -> int:
    q = 0
    next_largest_int_multiple_of_y = y

    # fmt: off
    '''
    while next_largest_int_multiple_of_y <= x:
    '''
    # fmt: on
    while next_largest_int_multiple_of_y <= x:
        q += 1
        next_largest_int_multiple_of_y += y
    return q


def is_greater_or_equal_1(a: int, b: int) -> bool:
    while a and b:
        a >>= 1
        b >>= 1
    return bool(a)


def quotient_2(x: int, y: int) -> int:
    q = 0
    while x >= y:
        power = max_power_of_2(x, y)
        q += 1 << power
        x -= y << power
    return q


def max_power_of_2(x: int, y: int) -> int:
    power = 0
    while x >= y << power:
        power += 1
    return power - 1


if __name__ == "__main__":
    q = quotient_2(64, 1)

    q = quotient_1(64, 1)
    print(is_greater_or_equal_1(64, 64))
    print(is_greater_or_equal_1(64, 0))
    print(is_greater_or_equal_1(int("1111", 2), int("1101", 2)))  # False

    print()
    q = quotient_1(64, 1)
    print(q)
    q = quotient_1(64, 3)
    print(q)
