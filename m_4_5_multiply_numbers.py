import random


def _add_single_bits(x: int, y: int) -> int:
    leftmost_bit = x & y  # 1 only when x = y
    rightmost_bit = x ^ 1
    return leftmost_bit, rightmost_bit


def add(x: int, y: int) -> int:
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

        carry_mask <<= 1
        x >>= 1
        y >>= 1
        apply_carry = bool(leftmost_bit) or apply_carry
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
