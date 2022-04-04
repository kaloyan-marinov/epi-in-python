from typing import List


def reverse_words(s: List[str]) -> None:
    """
    This is the official solution.

    Assume that each entry in `s` is a single character.

    Perform an in-place transformation of `s` into a string,
    in which the words appear in reverse order.

    For example,
    `[c for c in "Alice likes Bob"]` should be transformed to
    `[c for c in "Bob likes Alice"]`.

    This implementation:
        - does not keep the original string.
    """
    # First, reverse the whole "string".
    _reverse_slice(s, 0, len(s) - 1)

    # Second, reverse each but the last individual word (that is present within the "string").
    start = 0
    while True:
        finish = start
        while finish < len(s) and s[finish] != " ":
            finish += 1

        if finish == len(s):
            break

        # Reverse the current word.
        _reverse_slice(s, start, finish - 1)

        # Initialize the start for the next word.
        start = finish + 1

    # Reverse the last word.
    _reverse_slice(s, start, len(s) - 1)


def reverse_words(s: List[str]) -> None:
    # First, reverse the whole "string".
    _reverse_slice(s, 0, len(s) - 1)

    # Second, reverse each individual word (that is present within the "string").
    word_start = 0
    while word_start < len(s):
        # Determine the start and final indices that "frame" the current word.
        if s[word_start] == " ":
            word_start += 1
            continue

        word_final = word_start
        while s[word_final] != " ":
            word_final += 1
            if word_final == len(s):
                break

        # Reverse the current word.
        _reverse_slice(s, word_start, word_final - 1)

        # Initialize the start for the next word.
        word_start = word_final + 1


def _reverse_slice(s: List[str], start_idx: int, final_idx: int):
    """
    Perform an in-place modification of `s`
    by reversing `s[start_idx : final_idx + 1]`.
    (Recall that the last entry in `s[start_idx : final_idx + 1]` is `s[final_idx]`.)
    """
    while start_idx < final_idx:
        s[start_idx], s[final_idx] = s[final_idx], s[start_idx]
        start_idx += 1
        final_idx -= 1
