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

DIGIT_2_CHAR = {v: k for k, v in CHAR_2_DIGIT.items()}


def string_to_int(s: str, b: int) -> int:
    sign = -1 if s[0] == "-" else 1

    absolute_value = functools.reduce(
        lambda running_sum, c: b * running_sum + CHAR_2_DIGIT[c],
        s[s[0] in "-+" :],
        0,
    )

    return sign * absolute_value


def int_to_string(x: int, b: int) -> str:
    is_negative = False
    if x < 0:
        x = -x
        is_negative = True

    # fmt: off
    # the following breaks down when x is 0
    '''
    digits = []
    while x:
        d = x % b
        digits.append(DIGIT_2_CHAR[d])
        x //= b
    '''
    # fmt: on
    if x == 0:
        digits = ["0"]
    else:
        digits = []
        while x:
            d = x % b
            digits.append(DIGIT_2_CHAR[d])
            x //= b

    return ("-" if is_negative else "") + "".join(reversed(digits))


def int_to_string_recursively(x: int, b: int) -> str:
    return "" if x == 0 else int_to_string(x // b, b) + string.hexdigits[x % b].upper()


def convert_base(
    num_as_str: str,
    b1: int,
    b2: int,
) -> str:
    x = string_to_int(num_as_str, b1)
    return int_to_string(x, b2)
