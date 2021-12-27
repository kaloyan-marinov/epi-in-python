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

    left_characters = []
    for c in s:
        if c in opening_2_closing:
            left_characters.append(c)
        elif not left_characters or opening_2_closing[left_characters.pop()] != c:
            # Unmatched right character.
            return False

    return not left_characters


if __name__ == "__main__":
    s = "()"
    well_formed = is_well_formed(s)
