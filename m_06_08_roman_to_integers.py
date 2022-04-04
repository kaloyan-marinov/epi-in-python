"""
The Roman numeral representations of positive integers uses the symbols
I, V, X, L, C, D, M.
Each symbol represents a value as specified below:
I 1
V 5
X 10
L 50
C 100
D 500
M 1000

In this problem,
we give simplified rules for representing #'s in this system.
Specifically,
define a string over the Roman number symbols to be a _valid Roman number string_
if symbols appear in non-increasing order, with the following exceptions allowed:
- I can immediately precede V or X
- X can immediately precede L or C
- C can immediately precede D or M
Back-to-back exceptions are no allowed,
e.g. the following are invalid:
- IXC
- CDM

A valid complex Roman number string represents the integer
which is the sum of the symbols that do not correspond to exceptions;
for the exceptions, add the difference of the larger symbol and the smaller symbol.

For example, the following strings are (considered by this problem)
valid Roman number strings representing 59:
- XXXXXIIIIIIIII
- LVIII
- LIX
"""


import functools


def roman_to_integer_1(s: str) -> int:
    """
    Assume that `s` is a valid Roman number string.

    Return the integer that `s` corresponds to.

    (
    Scan `s` from left to right.

    Do not check whether, when a smaller symbol appears to the left of a larger one,
    it is one of the allowed exceptions;
    in other words, rely on the assumption that `s` is a valid Roman number string.
    )

    time:  O(n)
           where n := len(s)

    space: O(1)
    """

    symbol_2_value = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    value = 0
    i = 0

    while i < len(s):
        v_curr = symbol_2_value[s[i]]

        if i + 1 < len(s):
            v_next = symbol_2_value[s[i + 1]]
            if v_curr >= v_next:
                value += v_curr
                i += 1
            else:
                value += v_next - v_curr
                i += 2
        else:
            value += v_curr
            i += 1

    return value


def roman_to_integer_2(s: str) -> int:
    """
    Assume that `s` is a valid Roman number string.

    Return the integer that `s` corresponds to.

    (
    Scan `s` from right to left, starting at the 2nd-to-last position:

        if the symbol to the right of the current one is > than the current one:
            subtract the current symbol
        else:
            add the current symbol

    Do not check whether, when a smaller symbol appears to the left of a larger one,
    it is one of the allowed exceptions;
    in other words, rely on the assumption that `s` is a valid Roman number string.
    )

    time:  O(n)
       where n := len(s)

    space: O(1)
    """

    symbol_2_value = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    value = functools.reduce(
        lambda val, i: val
        + (
            -symbol_2_value[s[i]]
            if symbol_2_value[s[i]] < symbol_2_value[s[i + 1]]
            else symbol_2_value[s[i]]
        ),
        reversed(range(len(s) - 1)),
        symbol_2_value[s[-1]],
    )

    return value


if __name__ == "__main__":
    s = "II"
    v = roman_to_integer_1(s)
    print(v)
