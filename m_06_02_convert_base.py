import functools
import string


CHAR_2_DIGIT = {c: string.digits.index(c) for c in string.digits}
CHAR_2_DIGIT.update(
    {
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15,
    }
)
# fmt: off
# Since `string.hexdigits` equals '0123456789abcdefABCDEF',
# the previous block is equivalent to the following one:
'''
CHAR_2_DIGIT = {c.upper(): string.digits.index(c) for c in string.digits[:16]}
'''
# fmt: on

DIGIT_2_CHAR = {v: k for k, v in CHAR_2_DIGIT.items()}


def string_to_int(s: str, b: int) -> int:
    """
    Assume that:
        (a) `2 <= b <= 16`
        (b) `s` represents a integer in base `b`
        (c) `s` is either '-' or a base-`b` digit

    Return the integer's representation in base 10.
    """

    sign = -1 if s[0] == "-" else 1

    absolute_value = functools.reduce(
        lambda running_sum, c: b * running_sum + CHAR_2_DIGIT[c],
        s[s[0] in "-" :],
        0,
    )

    return sign * absolute_value


def int_to_string(x: int, b: int) -> str:
    """
    Assume that `2 <= b <= 16`.

    Return the representation of `x` in base `b`.
    """

    is_negative = False
    if x < 0:
        x = -x
        is_negative = True

    if x == 0:
        digits = ["0"]
    else:
        digits = []
        while x:
            d = x % b
            digits.append(DIGIT_2_CHAR[d])
            x //= b

    return ("-" if is_negative else "") + "".join(reversed(digits))


def convert_base(
    num_as_str: str,
    b1: int,
    b2: int,
) -> str:
    """
    Assume that:
        (a) `2 <= b1, b2 <= 16`
        (b) `num_as_str` represents an integer in base `b1`

    Return a string representing the integer in base `b2`
    """
    x = string_to_int(num_as_str, b1)
    return int_to_string(x, b2)


def convert_base_2(
    num_as_str: str,
    b1: int,
    b2: int,
) -> str:

    is_negative = False
    if num_as_str[0] == "-":
        is_negative = True
        num_as_str = num_as_str[1:]

    x = string_to_int(num_as_str, b1)

    return ("-" if is_negative else "") + (
        "0" if x == 0 else int_to_string_recursively(x, b2)
    )


def int_to_string_recursively(x: int, b: int) -> str:
    return (
        ""
        if x == 0
        else int_to_string_recursively(x // b, b) + string.hexdigits[x % b].upper()
    )
