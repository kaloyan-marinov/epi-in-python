def _add_single_bits_1(x: int, y: int) -> int:
    leftmost_bit = x & y  # 1 only when x = y
    rightmost_bit = x ^ 1
    return leftmost_bit, rightmost_bit


def add_1(x: int, y: int) -> int:
    """
      ||oo
       110
        11
      ----
    + 1001

       110
        11
      ----
    ^  101 =: r
    ^ ||oo =: "global" carry_mask
      ----
      1001 = is the sum
    """

    result = x ^ y

    apply_carry = False
    carry_mask = 1
    while x or y or apply_carry:
        if apply_carry:
            apply_carry = bool(result & carry_mask)
            result ^= carry_mask

        last_bit_of_x = x & 1
        last_bit_of_y = y & 1
        leftmost_bit, rightmost_bit = _add_single_bits_1(
            last_bit_of_x,
            last_bit_of_y,
        )

        carry_mask <<= 1
        x >>= 1
        y >>= 1
        apply_carry = bool(leftmost_bit) or apply_carry
    return result


def multiply_1(x: int, y: int) -> int:
    result = 0
    position = 0
    while y:
        last_bit_of_y = y & 1
        if last_bit_of_y == 1:
            result = add_1(result, x << position)
        position = add_1(position, 1)
        y >>= 1
    return result


def add_2(a: int, b: int) -> int:
    """
    time:  O(n)
           where n := the # of bits needed to represent the operands
    """

    if b == 0:
        return a

    sum_ignoring_carry = a ^ b
    global_carried_amount = (a & b) << 1  # NB: the parentheses are necessary!
    return add_2(sum_ignoring_carry, global_carried_amount)


def multiply_2(x: int, y: int) -> int:
    """
    TODO: double-check the following

    time:  O(n ** 2)
           where n := the # of bits needed to represent the operands
    """

    running_sum = 0

    while y:
        if y & 1:
            running_sum = add_2(
                running_sum,
                x,
            )

        y >>= 1
        x <<= 1

    return running_sum


if __name__ == "__main__":
    import datetime
    import random

    print(f"{datetime.datetime.utcnow().isoformat()} - starting")

    fmt_str = "{0:<20} {1:>70}"
    random.seed(a=42)

    for i in range(1000000):
        x = random.randrange(0, 2 ** 3)
        y = random.randrange(0, 2 ** 3)

        # fmt: off
        '''
        x = int("110", 2)  # random.randrange(0, 2 ** 3)
        y = int("11", 2)  # random.randrange(0, 2 ** 3)

        x = int("1", 2)
        y = int("0", 2)
        '''
        # fmt: on

        sum_computed = add_2(x, y)
        sum_expected = x + y
        if sum_computed != sum_expected:
            print()
            print(fmt_str.format("x", bin(x)))
            print(fmt_str.format("y", bin(y)))
            print(fmt_str.format("sum_expected", bin(sum_expected)))
            print(fmt_str.format("sum_computed", bin(sum_computed)))
            raise ValueError(f"{sum_expected} != {sum_computed}")

        prod_computed = multiply_2(x, y)
        prod_expected = x * y
        if prod_computed != prod_expected:
            print()
            print(fmt_str.format("x", bin(x)))
            print(fmt_str.format("y", bin(y)))
            print(fmt_str.format("prod_expected", bin(prod_expected)))
            print(fmt_str.format("prod_computed", bin(prod_computed)))
            raise ValueError(f"{prod_expected} != {prod_computed}")

    print(f"{datetime.datetime.utcnow().isoformat()} - ending")
