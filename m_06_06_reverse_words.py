from typing import List


def reverse_words(s: List[str]) -> None:
    # First, reverse the whole string.
    _reverse_slice(s, 0, len(s) - 1)

    # Second, reverse each individual word (that is present within the string).
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
    Perform an in-place change of `s`, reversing `s[start_idx : final_idx + 1]`.
    (Recall that the last entry in `s[start_idx : final_idx + 1]` is `s[final_idx]`.)
    """
    while start_idx < final_idx:
        s[start_idx], s[final_idx] = s[final_idx], s[start_idx]
        start_idx += 1
        final_idx -= 1
