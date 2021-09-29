def swap_bits(x: int, i: int, j: int) -> int:
    if i >= j:
        i, j = j, i

    bit_i = x >> i & 1
    # print(bin(x))
    bit_j = x >> j & 1
    # print(i, bit_i)
    # print(j, bit_j)
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
        # print(count, new_bit)
        count += 1
        x >>= 1

    return y


def swap_bits_2(x: int, i: int, j: int) -> int:
    if i >= j:
        i, j = j, i

    bit_i = x >> i & 1
    # print(bin(x))
    bit_j = x >> j & 1
    # print(i, bit_i)
    # print(j, bit_j)
    if bit_i == bit_j:
        return x

    def _toggle_bit(_x, _i):
        bit_i = _x >> _i & 1
        # print("bit_i", bit_i)

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

    # print(bin(x))
    x = _toggle_bit(x, i)
    # print(bin(x))
    x = _toggle_bit(x, j)
    # print(bin(x))
    return x


result = swap_bits(int("01001001", 2), 1, 6)
print(bin(result), result)

result = swap_bits(int("0b1101010", 2), 3, 7)
print(bin(result), result)
