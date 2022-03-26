def swap_bits(x: int, i: int, j: int) -> int:
    bit_i = x >> i & 1
    bit_j = x >> j & 1
    if bit_i != bit_j:
        bitmask = (1 << i) | (1 << j)
        x ^= bitmask
    return x


def closest_int_same_bit_count_1(x: int) -> int:
    y = None
    for i in range(63 - 1):
        mask = int((i + 2) * "1", 2)
        if (x & mask == 2 ** (i + 1)) or (x & mask == 2 ** (i + 1) - 1):
            y = swap_bits(x, i, i + 1)
            break
    return y


def closest_int_same_bit_count_2(x: int) -> int:
    y = x if x & 1 == 0 else x + 1
    mask_1 = y & ~(y - 1)  # isolates the lowest bit that is set in y
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

        y_1 = closest_int_same_bit_count_1(x)
        print(bin(y_1))

        y_2 = closest_int_same_bit_count_2(x)
        print(y_2 == y_1)
