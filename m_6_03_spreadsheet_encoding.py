import string


def ss_decode_col_id(col: str) -> int:
    result = 0
    curr_power_of_26 = 1

    for i in reversed(range(1, len(col))):
        integer_i = (
            string.ascii_letters.index(col[i]) - string.ascii_letters.index("A") + 1
        )

        result += integer_i * curr_power_of_26

        curr_power_of_26 *= 26

    return result


if __name__ == "__main__":
    col = "A"
    x = ss_decode_col_id(col)

    print(x)  # 0, which is incorrect
