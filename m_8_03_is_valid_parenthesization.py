def is_well_formed(s: str) -> bool:
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


if __name__ == "__main__":
    s = "()"
    well_formed = is_well_formed(s)
