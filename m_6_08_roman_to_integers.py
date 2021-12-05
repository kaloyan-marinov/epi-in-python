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
        if i + 1 < len(s):
            if symbol_2_value[s[i]] >= symbol_2_value[s[i + 1]]:
                value += symbol_2_value[s[i]]
                i += 1
                continue

            if symbol_2_value[s[i]] < symbol_2_value[s[i + 1]]:
                value += symbol_2_value[s[i + 1]] - symbol_2_value[s[i]]
                i += 2
                continue
        else:
            value += symbol_2_value[s[i]]
            i += 1

    return value


if __name__ == "__main__":
    s = "II"
    v = roman_to_integer(s)
    print(v)
