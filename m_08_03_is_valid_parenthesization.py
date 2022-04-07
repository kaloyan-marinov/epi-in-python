def is_well_formed(s: str) -> bool:
    """
    (This is my own solution.)

    Assume that `s` is a string over the characters '{', '}', '[', ']', '(', ')'.

    Check whether the different types of brackets in `s` match in the correct order.

    For example,
        (a) within each of the following strings,
            the brackets match in the correct order:

            ([]){()}
            [()[]{()()}]

        (b) within none of the following strings
            do the brackets match in the correct order:

            {)
            {(})
            [()[]{()()

    time:  O(n)
           where n := len(s)

    space: O(n)
    """

    # In this function, each occurrence of `len(opening_parentheses) == 0`
    # can be replaced by `not opening_parentheses`,
    # which was empirically observed to make the function execute a little faster.

    CLOSING_2_OPENING = {
        "}": "{",
        "]": "[",
        ")": "(",
    }

    opening_parentheses = []
    for c in s:
        if c not in CLOSING_2_OPENING:
            opening_parentheses.append(c)
        else:
            if (
                len(opening_parentheses) == 0
                or opening_parentheses[-1] != CLOSING_2_OPENING[c]
            ):
                return False
            else:
                opening_parentheses.pop()

    return len(opening_parentheses) == 0


def is_well_formed_2(s: str) -> bool:
    """
    (This is the official solution.)

    Assume that `s` is a string over the characters '{', '}', '[', ']', '(', ')'.

    Check whether the different types of brackets in `s` match in the correct order.

    For example,
        (a) within each of the following strings,
            the brackets match in the correct order:

            ([]){()}
            [()[]{()()}]

        (b) within none of the following strings
            do the brackets match in the correct order:

            {)
            {(})
            [()[]{()()

    time:  O(n)
           where n := len(s)

    space: O(n)
    """

    OPENING_2_CLOSING = {
        "{": "}",
        "[": "]",
        "(": ")",
    }

    opening_parentheses = []
    for c in s:
        if c in OPENING_2_CLOSING:
            opening_parentheses.append(c)
        elif (
            len(opening_parentheses) == 0
            or OPENING_2_CLOSING[opening_parentheses.pop()] != c
        ):
            # The current character is a right/closing one,
            # but is not matched by the correct opening/left one.
            return False

    return len(opening_parentheses) == 0


if __name__ == "__main__":
    s = "()"
    well_formed = is_well_formed(s)
