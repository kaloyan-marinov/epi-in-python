def solution_1_divide(x: int, y: int) -> int:
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


def solution_2_divide(x: int, y: int) -> int:
    q = 0
    while x >= y:
        power = solution_2_max_power_of_2(x, y)
        q += 1 << power
        x -= y << power
    return q


def solution_2_max_power_of_2(x: int, y: int) -> int:
    power = 0
    while x >= y << power:
        power += 1
    return power - 1


def solution_3_least_power_of_2(x: int, y: int) -> int:
    power = 0
    while x >= y:
        y <<= 1
        power += 1
    return power


def solution_3_divide(x: int, y: int) -> int:
    k = solution_3_least_power_of_2(x, y)
    q = 0
    y_times_2_to_the_k = y << k

    while x >= y:
        while y_times_2_to_the_k > x:
            k -= 1
            y_times_2_to_the_k >>= 1

        q += 1 << k
        x -= y_times_2_to_the_k

    return q


if __name__ == "__main__":
    q = solution_2_divide(64, 1)

    q = solution_1_divide(64, 1)
    print(is_greater_or_equal_1(64, 64))
    print(is_greater_or_equal_1(64, 0))
    print(is_greater_or_equal_1(int("1111", 2), int("1101", 2)))  # False

    print()
    q = solution_1_divide(64, 1)
    print(q)
    q = solution_1_divide(64, 3)
    print(q)
