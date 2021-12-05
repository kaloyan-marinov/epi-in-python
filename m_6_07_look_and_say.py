import itertools


def look_and_say(n: int) -> str:
    s = "1"

    for _ in range(n - 1):
        s = _next_in_look_and_say_sequence(s)

    return s


def _next_in_look_and_say_sequence(s: str) -> str:
    digits = list()

    start = 0

    while start < len(s):
        final = start
        d = s[start]

        while final < len(s) and s[final] == d:
            final += 1

        digits.extend([str(final - start), d])

        start = final

    return "".join(digits)


if __name__ == "__main__":
    n = 3

    s = look_and_say(n)

    print(s)
