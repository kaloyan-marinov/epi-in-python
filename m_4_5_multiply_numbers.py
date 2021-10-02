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

    r = x ^ y

    apply_carry = False
    carry_mask = 1
    while x or y or apply_carry:
        if apply_carry:
            apply_carry = bool(r & carry_mask)
            r ^= carry_mask

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
    return r


def multiply(x: int, y: int) -> int:
    r = 0
    position = 0
    while y:
        last_bit_of_y = y & 1
        if last_bit_of_y == 1:
            r = add(r, x << position)
        position = add(position, 1)
        y >>= 1
    return r


if __name__ == "__main__":
    fmt_str = "{0:<10} {1:>70}"
    random.seed(a=42)

    for i in range(1000000):
        x = random.randrange(0, 2 ** 3)
        y = random.randrange(0, 2 ** 3)

        # x = int("110", 2)  # random.randrange(0, 2 ** 3)
        # y = int("11", 2)  # random.randrange(0, 2 ** 3)

        # x = int("1", 2)
        # y = int("0", 2)

        s = add(x, y)
        if s != x + y:
            print()
            print(fmt_str.format("x", bin(x)))
            print(fmt_str.format("y", bin(y)))
            print(fmt_str.format("x + y", bin(x + y)))
            print(fmt_str.format("s", bin(s)))
            raise ValueError(f"{s} != {x + y}")

        p = multiply(x, y)
        if p != x * y:
            print()
            print(fmt_str.format("x", bin(x)))
            print(fmt_str.format("y", bin(y)))
            print(fmt_str.format("x * y", bin(x * y)))
            print(fmt_str.format("p", bin(p)))
            raise ValueError(f"{p} != {x * y}")
