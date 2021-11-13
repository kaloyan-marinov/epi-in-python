from typing import List


def int_to_string(x: int) -> str:
    if x == 0:
        return "0"

    if x < 0:
        return "-" + int_to_string(-x)

    digits: List[int] = []
    while x:
        d = x % 10
        digits.append(str(d))
        x //= 10

    return "".join(digits[::-1])


def string_to_int(s: str) -> int:
    if s[0] == "-":
        return -string_to_int(s[1:])

    if s[0] == "+":
        return string_to_int(s[1:])

    x = 0
    for i in reversed(range(1, len(s) + 1)):
        x += int(s[-i]) * (10 ** (i - 1))

    return x


if __name__ == "__main__":
    x = 4176473
    s = int_to_string(x)
    print(s)

    x_1 = string_to_int(s)
    print(x_1)
