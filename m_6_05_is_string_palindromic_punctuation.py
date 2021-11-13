def is_palindrome(s: str) -> bool:
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
        else:
            i += 1
            j -= 1

    return True


def is_palindrome_pythonic(s: str) -> bool:
    return all(
        a == b
        for a, b in zip(
            map(str.lower, filter(str.isalnum, s)),
            map(str.lower, filter(str.isalnum, reversed(s))),
        )
    )
