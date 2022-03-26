def swap_bits(x: int, i: int, j: int) -> int:
    bit_i = x >> i & 1
    bit_j = x >> j & 1
    if bit_i != bit_j:
        # Construct a bitmask for "selecting"/"pinpointing" the bits
        # at the positions/indices of interest.
        bitmask = (1 << i) | (1 << j)
        # Utilize the constructed bitmask to flip each of those bits.
        x ^= bitmask
    return x


d = dict()

for x in range(2 ** 16):
    y = x
    for i in range(8):
        y = swap_bits(y, i, 15 - i)
    d[x] = y


def reverse_bits_1(x: int) -> int:
    bitmask = 0xFFFF
    x_0 = x & bitmask
    x_1 = (x >> 16) & bitmask
    x_2 = (x >> 32) & bitmask
    x_3 = (x >> 48) & bitmask
    return d[x_3] | (d[x_2] << 16) | (d[x_1] << 32) | (d[x_0] << 48)


def reverse_bits_2(x: int) -> int:
    for i in range(32):
        x = swap_bits(x, i, 63 - i)
    return x
