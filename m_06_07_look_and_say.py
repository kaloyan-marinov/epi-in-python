import itertools


def look_and_say(n: int) -> str:
    """
    Compute the `n`-th integer in the look-and-say sequence/game,
    _but_ return it as a string.

    For example:
        - for `n = 1`, the return value should (by convention be) `"1"`
        - for `n = 2`, the return value should based on "one 1"
          and thus be "11"
        - for `n = 3`, the return value should based on "two 1s"
          and thus be "21"
        - for `n = 4`, the return value should based on "one 2 one 1"
          and thus be "1211"
        - etc.

    Assume that `n >= 1`.

    time:  precisely,
           a f-n of the lengths of the terms,
           which is extremely hard to analyze

           each successive # can have <= twice as many digits
           (which happens when the current number's digits are all different);
           this means that
           "the maximum length number has length no more than `2 ** n`"

           after `n` iterations,
           a simple upper bound is
           O(n * (2 ** n))
    """

    s = "1"

    for _ in range(n - 1):
        s = _next_in_look_and_say_sequence(s)

    return s


def _next_in_look_and_say_sequence(s: str) -> str:
    """
    time:  O(n)
           n := len(s)

    space: O(n)
    """

    digits = list()

    start = 0

    while start < len(s):
        final = start
        curr_digit = s[start]

        while final < len(s) and s[final] == curr_digit:
            final += 1

        copies_of_curr_digit = final - start
        digits.extend([str(copies_of_curr_digit), curr_digit])

        start = final

    return "".join(digits)


def look_and_say_pythonic(n: int) -> str:
    """
    Compute the `n`-th integer in the look-and-say sequence/game,
    _but_ return it as a string.

    For example:
        - for `n = 1`, the return value should (by convention be) `"1"`
        - for `n = 2`, the return value should based on "one 1"
          and thus be "11"
        - for `n = 3`, the return value should based on "two 1s"
          and thus be "21"
        - for `n = 4`, the return value should based on "one 2 one 1"
          and thus be "1211"
        - etc.

    Assume that `n >= 1`.
    """

    current_string = "1"

    for _ in range(1, n):
        current_string = "".join(
            str(len(list(group))) + key
            for key, group in itertools.groupby(current_string)
        )

    return current_string


if __name__ == "__main__":
    n = 3

    s = look_and_say(n)

    print(s)
