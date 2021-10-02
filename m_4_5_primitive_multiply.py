import datetime
import random


def _add_single_bits(x: int, y: int) -> int:
    leftmost_bit = x & y  # 1 only when x = y
    rightmost_bit = x ^ 1
    return leftmost_bit, rightmost_bit


def add(x: int, y: int) -> int:
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
        leftmost_bit, rightmost_bit = _add_single_bits(
            last_bit_of_x,
            last_bit_of_y,
        )
        # fmt: off
        # The last statement can be replaced by the following one:
        '''
        leftmost_bit = last_bit_of_x & last_bit_of_y  # equals 1 only if both are 1
        '''
        # fmt: on

        carry_mask <<= 1
        x >>= 1
        y >>= 1
        apply_carry = bool(leftmost_bit) or apply_carry
    return result


def multiply(x: int, y: int) -> int:
    result = 0
    position = 0
    while y:
        last_bit_of_y = y & 1
        if last_bit_of_y == 1:
            result = add(result, x << position)
        position = add(position, 1)
        y >>= 1
    return result


if __name__ == "__main__":
    print(f"{datetime.datetime.utcnow().isoformat()} - starting")

    fmt_str = "{0:<20} {1:>70}"
    random.seed(a=42)

    for i in range(1000000):
        x = random.randrange(0, 2 ** 3)
        y = random.randrange(0, 2 ** 3)

        # x = int("110", 2)  # random.randrange(0, 2 ** 3)
        # y = int("11", 2)  # random.randrange(0, 2 ** 3)

        # x = int("1", 2)
        # y = int("0", 2)

        sum_computed = add(x, y)
        sum_expected = x + y
        if sum_computed != sum_expected:
            print()
            print(fmt_str.format("x", bin(x)))
            print(fmt_str.format("y", bin(y)))
            print(fmt_str.format("sum_expected", bin(sum_expected)))
            print(fmt_str.format("sum_computed", bin(sum_computed)))
            raise ValueError(f"{sum_expected} != {sum_computed}")

        prod_computed = multiply(x, y)
        prod_expected = x * y
        if prod_computed != prod_expected:
            print()
            print(fmt_str.format("x", bin(x)))
            print(fmt_str.format("y", bin(y)))
            print(fmt_str.format("prod_expected", bin(prod_expected)))
            print(fmt_str.format("prod_computed", bin(prod_computed)))
            raise ValueError(f"{prod_expected} != {prod_computed}")

    print(f"{datetime.datetime.utcnow().isoformat()} - ending")
