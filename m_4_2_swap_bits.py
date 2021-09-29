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


result = swap_bits(int("01001001", 2), 1, 6)
print(bin(result), result)

result = swap_bits(int("0b1101010", 2), 3, 7)
print(bin(result), result)
