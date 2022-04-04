import string

from typing import List


def int_to_string(x: int) -> str:
    """
    Convert the integer `x` to a string.

    For example:
        314     >>      "314"
        -314    >>      "-314"

    (
    This solution is based on:

        (a) https://docs.python.org/3/library/functions.html#chr

            Given an `i: int`, `chr(i) returns the string representing a character
            whose Unicode code point is the integer `i`.

            This is the inverse of `ord()`.

        (b) https://docs.python.org/3/library/functions.html#ord

            Given an `c: str` representing one Unicode character,
            `ord(c)` returns an integer representing the Unicode code point of `c`.

            This is the inverse of `chr()`.

        (c) the following examples

            ```
            >>> ord('0')
            48
            >>> [ord(d_str) for d_str in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']]
            [48, 49, 50, 51, 52, 53, 54, 55, 56, 57]
            >>> chr(ord('0') + 7)
            '7'
            ```
    )
    """

    if x == 0:
        return "0"

    if x < 0:
        return "-" + int_to_string(-x)

    digits: List[int] = []
    while x:
        d = x % 10
        digits.append(
            chr(ord("0") + d),
        )
        x //= 10

    return "".join(digits[::-1])


def string_to_int(s: str) -> int:
    """
    Assume that `s` encodes an integer.

    Convert `s` to the corresponding integer.

    For example:
        "123"   >>      123
        "-123"  >>      -123
        "+123"  >>      123

    (
    This solution is based on:

        (a) beginning with the rightmost character
            and iteratively adding `d_i * (10 ** i)`

        (b) the following examples

            ```
            >>> import string
            >>> string.digits
            '0123456789'
            >>> string.digits.index('7')
            7
            ```
    )
    """

    if s[0] == "-":
        return -string_to_int(s[1:])

    if s[0] == "+":
        return string_to_int(s[1:])

    i = 0
    ten_to_the_i = 1
    x = 0
    while i < len(s):
        x += string.digits.index(s[-i - 1]) * ten_to_the_i

        i += 1
        ten_to_the_i *= 10

    return x


import functools


def string_to_int_2(s: str) -> int:
    """
    (
    This solution is based on:

        (a) beginning with the leftmost character;
            with each successive character,
            multiply the _partial result_ by 10
            and add the character's corresponding digit

        (b) the following examples

            ```
            >>> s = 'abcd'
            >>> s[True:]
            'bcd'
            >>> s[False:]
            'abcd'
            ```
    )
    """

    sign = -1 if s[0] == "-" else 1

    absolute_value = functools.reduce(
        lambda running_sum, c: running_sum * 10 + string.digits.index(c),
        s[s[0] in "-+" :],
        0,
    )

    return sign * absolute_value


if __name__ == "__main__":
    x = 4176473
    s = int_to_string(x)
    print(s)

    x_1 = string_to_int(s)
    print(x_1)
