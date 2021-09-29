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

    def toggle_bit(X, I):
        bit_i = X >> I & 1
        print("bit_i", bit_i)

        if bit_i == 0:
            mask_i = int("1" + I * "0", 2)
            X = X | mask_i
        else:
            mask_remainder = int((I + 1) * "1", 2)
            r = X - (X & mask_remainder)
            mask_i = int("0" + I * "1", 2)
            X = X & mask_i
            X = X + r
        return X

    print(bin(x))
    x = toggle_bit(x, i)
    print(bin(x))
    x = toggle_bit(x, j)
    print(bin(x))

    # if bit_j == 1 and bit_i == 0:
    #     mask_j = int("0" + j * "1", 2)
    #     x = x & mask_j
    #     mask_i = int("1" + i * "0", 2)
    #     x = x | mask_i

    # if bit_j == 0 and bit_i == 1:
    #     mask_j = int("1" + j * "0", 2)
    #     x = x | mask_j
    #     mask_i = int("0" + i * "1", 2)
    #     x = x & mask_i

    return x


result = swap_bits(int("01001001", 2), 1, 6)
print(bin(result), result)

result = swap_bits(int("0b1101010", 2), 3, 7)
print(bin(result), result)
