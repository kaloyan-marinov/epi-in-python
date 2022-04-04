import string


def ss_decode_col_id(col: str) -> int:
    """
    Given a spreadsheet column encoding
    (such as “A”, “B”, ..., “Z”, “AA”, “AB”, ..., “ZZ”, “AAA”, “AAB”, ...),
    convert it to the corresponding `int`,
    where “A” should correspond to 1.
    """
    result = 0
    curr_power_of_26 = 1

    for i in reversed(range(len(col))):
        integer_i = (
            string.ascii_letters.index(col[i]) - string.ascii_letters.index("A") + 1
        )

        result += integer_i * curr_power_of_26

        curr_power_of_26 *= 26

    return result


import functools


def ss_decode_col_id(col: str) -> int:
    """
    This is the official solution.

    Given a spreadsheet column encoding
    (such as “A”, “B”, ..., “Z”, “AA”, “AB”, ..., “ZZ”, “AAA”, “AAB”, ...),
    convert it to the corresponding `int`,
    where “A” should correspond to 1.
    """

    result = functools.reduce(
        lambda r, c: r * 26 + ord(c) - ord("A") + 1,
        col,
        0,
    )

    return result


if __name__ == "__main__":
    col = "A"
    x = ss_decode_col_id(col)

    print(x)  # 0, which is incorrect
