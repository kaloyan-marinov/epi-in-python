def is_palindrome(s: str) -> bool:
    """
    Determine whether `s`,
    when all its non-alphanumeric characters are removed
    and character case is ignored,
    reads the same back-to-front.

    time:  O(n)
           where n := len(s)

    space: O(1)
    """

    i = 0
    j = len(s) - 1

    while i < j:
        if not s[i].isalnum():
            i += 1
            continue

        if not s[j].isalnum():
            j -= 1
            continue

        if s[i].lower() != s[j].lower():
            return False

        i += 1
        j -= 1

    return True


def is_palindrome_pythonic(s: str) -> bool:
    """
    Determine whether `s`,
    when all its non-alphanumeric characters are removed
    and character case is ignored,
    reads the same back-to-front.

    time:  O(n)
           where n := len(s)

    space: O(1)
    """
    return all(
        a == b
        for a, b in zip(
            map(str.lower, filter(str.isalnum, s)),
            map(str.lower, filter(str.isalnum, reversed(s))),
        )
    )
