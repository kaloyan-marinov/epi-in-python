def quotient(x: int, y: int) -> int:
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


def is_greater_or_equal(a: int, b: int) -> bool:
    while a and b:
        a >>= 1
        b >>= 1
    return bool(a)


if __name__ == "__main__":
    q = quotient(64, 1)
    print(is_greater_or_equal(64, 64))
    print(is_greater_or_equal(64, 0))
    print(is_greater_or_equal(int("1111", 2), int("1101", 2)))  # False

    print()
    q = quotient(64, 1)
    print(q)
    q = quotient(64, 3)
    print(q)
