from typing import List, Optional


from m_04_02_swap_bits import swap_bits


def reverse_bits_1(x: int) -> int:
    """
    This is suitable
    if the operation needs to be performed only once.

    Assume that `x` is a 64-bit integer word.

    time:  O(n)
           where
           n := the # of bits in `x`,
    """
    for i in range(32):
        x = swap_bits(x, i, 63 - i)
    return x


def reverse_bits_2(x: int) -> int:
    """
    This leverages a cache
    if the operation needs to be performed repeatedly.

    Assume that `x` is a 64-bit integer word.

    time:  O(n / L)
           where
           n := the # of bits in `x`,
           L := the # of bits in the cache's keys
    """

    bitmask = 0xFFFF

    x_0 = x & bitmask
    x_1 = (x >> 16) & bitmask
    x_2 = (x >> 32) & bitmask
    x_3 = (x >> 48) & bitmask

    return (
        WORD_OF_16_BITS_2_ITS_REVERSE[x_3]
        | (WORD_OF_16_BITS_2_ITS_REVERSE[x_2] << 16)
        | (WORD_OF_16_BITS_2_ITS_REVERSE[x_1] << 32)
        | (WORD_OF_16_BITS_2_ITS_REVERSE[x_0] << 48)
    )


WORD_OF_16_BITS_2_ITS_REVERSE: List[Optional[int]] = [None for _ in range(2 ** 16)]

for x in range(2 ** 16):
    y = x
    for i in range(8):
        y = swap_bits(y, i, 15 - i)
    WORD_OF_16_BITS_2_ITS_REVERSE[x] = y
