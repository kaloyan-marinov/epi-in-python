def swap_bits(x: int, i: int, j: int) -> int:
    if (x >> i) & 1 != (x >> j) & 1:  # i.e. if the bits of interest differ
        # Construct a bitmask for "selecting"/"pinpointing" the bits
        # at the positions/indices of interest.
        bitmask = (1 << i) | (1 << j)

        # Utilize the constructed bitmask to flip each of those bits.
        # (
        # Since, for any binary digit x,
        #       x ^ 0 = x,
        #       x ^ 1 = flip(x),
        # the XOR operator with the `bitmask` will flip each of the bits of interest.
        # )
        x ^= bitmask

    return x


def swap_bits_1(x: int, i: int, j: int) -> int:
    if i >= j:
        i, j = j, i

    bit_i = x >> i & 1
    bit_j = x >> j & 1
    if bit_i == bit_j:
        return x

    count = 0
    y = 0
    while count <= j or x:
        bit = x & 1
        if count == i:
            new_bit = int(not bit_i)
        elif count == j:
            new_bit = int(not bit_j)
        else:
            new_bit = bit
        y += new_bit * (2 ** count)
        count += 1
        x >>= 1

    return y


def swap_bits_2(x: int, i: int, j: int) -> int:
    bit_i = x >> i & 1
    bit_j = x >> j & 1
    if bit_i == bit_j:
        return x

    def _toggle_bit(_x, _i):
        bit_i = _x >> _i & 1

        if bit_i == 0:
            mask_i = int("1" + _i * "0", 2)
            _x = _x | mask_i
        else:
            mask_remainder = int((_i + 1) * "1", 2)
            r = _x - (_x & mask_remainder)
            mask_i = int("0" + _i * "1", 2)
            _x = _x & mask_i
            _x = _x + r
        return _x

    x = _toggle_bit(x, i)
    x = _toggle_bit(x, j)
    return x


if __name__ == "__main__":
    result = swap_bits_1(int("01001001", 2), 1, 6)
    print(bin(result), result)

    result = swap_bits_2(int("0b1101010", 2), 3, 7)
    print(bin(result), result)
