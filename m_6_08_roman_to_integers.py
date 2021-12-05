import functools


def roman_to_integer(s: str) -> int:
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


if __name__ == "__main__":
    s = "II"
    v = roman_to_integer(s)
    print(v)
