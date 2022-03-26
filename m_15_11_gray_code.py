from typing import List, Set


def gray_code(num_bits: int) -> List[int]:
    """
    Assume that `num_bits >= 0`.
    """
    if num_bits == 0:
        return [0]

    gr_c = gray_code(num_bits - 1)

    # fmt: off
    '''
    If all the documented modifications to this function are done
    but the following statement remains as is,
    the so-modified function will pass the EPIJudge's test suite.

    That is somewhat surprising,
    because the next statement _has to_ be modified to `mask = 1 << (num_bits - 1)`.
    
    A: Why does it _have to_ be modified like that?
    Q: Look at the examples in the the `if __name__ == "__main__"` block
       and, even better, document them as unit test(-case)s of your own!
    '''
    # fmt: on
    mask = 1 << num_bits

    return gr_c + [value | mask for value in reversed(gr_c)]


def differ_by_1_bit(a: int, b: int) -> bool:
    # Ensure that a <= b.
    if a > b:
        a, b = b, a

    xor = a ^ b

    # Check whether `xor` is an exact power of 2.
    num = 1
    while num <= b:
        if xor == num:
            return True
        num <<= 1

    # fmt: off
    return False
'''
This function can be re-implemented in the following way,
which is both shorter and more efficient (but also more slick):
'''
'''
    bit_difference = a ^ b

    return bit_difference != 0 and (
        bit_difference & (bit_difference - 1) == 0
    )
'''
# fmt: on


def gray_code_3(num_bits: int) -> List[int]:
    """
    Assume that `num_bits >= 0`.

    Compared to this module's other functions,
    this one is more based on brute force than on analysis.

    Build a Gray-code sequence incrementally,
    adding a value only if
    it distinct from all values currently in the sequence
    and [it] differs in exactly 1 [bit] from the previous value.
    (
    For the last value, we ahve to check [whether]
    it differs in [exactly] one [bit] from the 1st value.
    )
    """

    result: List[int] = [0]

    def _guided_gray_code(history: Set[int]) -> bool:
        if len(result) == 1 << num_bits:
            return differ_by_1_bit(result[-1], result[0])

        for i in range(num_bits):
            previous_value = result[-1]
            candidate_next_value = previous_value ^ (1 << i)

            if candidate_next_value not in history:
                history.add(candidate_next_value)
                result.append(candidate_next_value)

                if _guided_gray_code(history):
                    return True

                del result[-1]
                history.remove(candidate_next_value)

        return False

    _guided_gray_code(set([0]))

    return result


def gray_code_4(num_bits: int) -> List[int]:
    """
    Assume that `num_bits >= 0`.

    This is identical to the `gray_code` f-n.
    """

    if num_bits == 0:
        return [0]

    # These implicitly begin with [= hold] 0 at bit-index `num_bits - 1`.
    gray_code_num_bits_minus_1 = gray_code(num_bits - 1)

    # Create an auxiliary bitmask,
    # which enables one to add a 1 at bit-index `num_bits - 1`
    # to all entries in `gray_code_num_bits_minus_1`.
    leading_bit_one = 1 << (num_bits - 1)

    # Process in reverse order
    # to achieve reflection of `gray_code_num_bits_minus_1`.
    return gray_code_num_bits_minus_1 + [
        leading_bit_one | value for value in reversed(gray_code_num_bits_minus_1)
    ]


def gray_code_5_pythonic_iterative(num_bits: int) -> List[int]:
    """
    Assume that `num_bits >= 0`.
    """

    result = [0]

    for i in range(num_bits):
        result += [x + 2 ** i for x in reversed(result)
        ]

    return result


if __name__ == "__main__":
    result = gray_code(0)
    print([bin(x) for x in result])  # [0]

    result = gray_code(1)
    print([bin(x) for x in result])  # [0, 1]

    result = gray_code(2)
    print([bin(x) for x in result])

    result = gray_code(3)
    print([bin(x) for x in result])

    result = gray_code(4)
    print([bin(x) for x in result])

    result = gray_code_3(2)
    print([bin(x) for x in result])
