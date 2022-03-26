"""
Assume that:
        - `x` fits in 64 bits
        - `x != 0`
        - `x != int("1" * 64, 2)`

Return an integer `y` s.t.
    - `y != x`
    - `weight(y) = weight(x)`
      [where
      `weight(z) := the # of bits that are set in the binary representation of `z`]
    - `|y - x|` is as small as possible



The assumptions about `x` imply that
there exists an index $i \in \{ 0, ..., 63 - 1 \}$ s.t.
\[
    (x_{i + 1} x_i)_2 \in \{ (10)_2, (01)_2 \}
\]

Select/Define
\[
    i_{min} := \min \bigg\{ i \in \{ 0, ..., 63 - 1 \} : (x_{i + 1} x_i)_2 \in \{ (10)_2, (01)_2 \} \bigg\}
\]
The minimal property of $i_{min}$ guarantees that
\[
    ( x_{i_{min} + 1} ... x_0 )_2 \in \{ (10...0)_2, (01...1)_2 \}.
\]

It is easy to mathematically justify that,
if $\tilde{x}$ is defined as $x$ with its bits at $i_{min} + 1$ and at $i_{min} swapped,
then setting returning $\tilde{x}$ will do the job.
"""


from m_04_02_swap_bits import swap_bits


def closest_int_same_bit_count_1_a(x: int) -> int:
    """
    time:  O(n)
           where n := the width of the integer word
    space: O(1)
    """

    y = None
    for i in range(63 - 1):
        mask = int((i + 2) * "1", 2)
        if (x & mask == 2 ** (i + 1)) or (x & mask == 2 ** (i + 1) - 1):
            y = swap_bits(x, i, i + 1)
            break
    return y


def closest_int_same_bit_count_1_b(x: int) -> int:
    """
    This is the official solution.

    time:  O(n)
           where n := the width of the integer word
    space: O(1)
    """

    for i in range(64 - 1):
        if (x >> i) & 1 != (x >> (i + 1) & 1):
            x ^= (1 << i) | (1 << (i + 1))
            return x


def closest_int_same_bit_count_2(x: int) -> int:
    """
    time:  O(1)
    space: O(1)
    """
    # Introduce an auxiliary binary integer that ends in (10...0)_2,
    # for some strictly positive # of zeros.
    # fmt: off
    y = (
        x if x & 1 == 0
        else x + 1
    )
    # fmt: on

    # Create bitmasks:
    # (a) one the isolates the lowest bit that is set in `y`:
    mask_1 = y & ~(y - 1)
    # (b) one that isolates the next bit:
    mask_2 = mask_1 >> 1

    # Flip the first two consecutive bits in x that are different from each other.
    return x ^ (mask_1 | mask_2)


if __name__ == "__main__":
    for binary_representation in [
        "110000",
        "101",
        "1001000001101100011000111001100100101101100011",
    ]:
        print()

        x = int(binary_representation, 2)
        print(bin(x))

        y_1 = closest_int_same_bit_count_1_b(x)
        print(bin(y_1))

        y_2 = closest_int_same_bit_count_2(x)
        print(y_2 == y_1)
