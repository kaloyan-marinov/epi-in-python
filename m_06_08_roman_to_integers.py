import functools


def roman_to_integer_1(s: str) -> int:
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
    Scan `s` from right to left, starting at the 2nd-to-last position:

        if the symbol to the right of the current one is > than the current one:
            subtract the current symbol
        else:
            add the current symbol
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
