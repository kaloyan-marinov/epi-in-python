def is_well_formed(s: str) -> bool:
    """
    Assume that `s` is a string over the characters '{', '}', '[', ']', '(', ')'.
    """
    closing_2_opening = {
        "}": "{",
        "]": "[",
        ")": "(",
    }

    opening_parentheses = []
    for c in s:
        if c not in closing_2_opening:
            opening_parentheses.append(c)
        else:
            if (
                len(opening_parentheses) == 0
                or opening_parentheses[-1] != closing_2_opening[c]
            ):
                return False
            else:
                opening_parentheses.pop()

    return len(opening_parentheses) == 0


def is_well_formed_2(s: str) -> bool:
    """
    Assume that `s` is a string over the characters '{', '}', '[', ']', '(', ')'.
    """
    opening_2_closing = {
        "{": "}",
        "[": "]",
        "(": ")",
    }

    opening_parentheses = []
    for c in s:
        if c in opening_2_closing:
            opening_parentheses.append(c)
        elif (
            not opening_parentheses or opening_2_closing[opening_parentheses.pop()] != c
        ):
            # The current character is a right/closing one,
            # but is not matched by the correct opening/left one.
            return False

    return not opening_parentheses


if __name__ == "__main__":
    s = "()"
    well_formed = is_well_formed(s)
