def parity_1_a(x: int) -> int:
    """
    This is based on brute force.

    time:  O(# of bits in x)
    space: O(1)
    """
    num_ones = 0
    while x:
        num_ones += x & 1
        x >>= 1
    return num_ones % 2


def parity_1_b(x: int) -> int:
    """
    This is also based on brute force.

    time:  O(# of bits in x)
    space: O(1)
    """
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result


def parity_2_a(x: int) -> int:
    """
    This is better than brute force.

    time:  O(# of set bits in x)
    space: O(1)
    """
    num_ones = 0
    while x:
        x = x & (x - 1)  # Drops `x`'s lowest set bit.
        num_ones += 1
    return num_ones % 2


def parity_2_b(x: int) -> int:
    """
    This is also better than brute force.

    time:  O(# of set bits in x)
    space: O(1)
    """
    result = 0
    while x:
        x = x & (x - 1)  # Drops `x`'s lowest set bit.
        result ^= 1
    return result


def parity_3(x: int) -> int:
    """
    This is also better than brute force.

    `x` is a 64-bit integer word
    """
    # Assume that
    # a `WORD_OF_16_BITS_2_PARITY: List[int]` is pre-computed
    # within the scope, in which this f-n will be called many times.

    bitmask_size = 16
    bitmask = int("1" * bitmask_size, 2)  # Same as `bitmask = 0xFFFF`

    return (
        WORD_OF_16_BITS_2_PARITY[x >> (3 * bitmask_size)]
        ^ WORD_OF_16_BITS_2_PARITY[x >> (2 * bitmask_size) & bitmask]
        ^ WORD_OF_16_BITS_2_PARITY[x >> bitmask_size & bitmask]
        ^ WORD_OF_16_BITS_2_PARITY[x & bitmask]
    )


def parity_4(x: int) -> int:
    """
    This is also better than brute force.
    But it requires you to know several important but non-obvious facts
    about parity and the bitwise XOR operator.
    (I have written up those facts in my notes).

    `x` is a (2**n)-bit integer word

    time:  O(log n)
    space: O(1)
    """

    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1

    return x & 1
