def swap_bits(x: int, i: int, j: int) -> int:
    bit_i = x >> i & 1
    bit_j = x >> j & 1
    if bit_i != bit_j:
        bitmask = (1 << i) | (1 << j)
        x ^= bitmask
    return x


def closest_int_same_bit_count(x: int) -> int:
    y = None
    for i in range(1, 63):
        mask = int((i + 1) * "1", 2)
        if (x & mask == 2 ** i) or (x & mask == 2 ** i - 1):
            y = swap_bits(x, i - 1, i)
            break
    return y


if __name__ == "__main__":
    x = int("110000", 2)
    print(bin(x))
    y = closest_int_same_bit_count(x)
    print(bin(y))
