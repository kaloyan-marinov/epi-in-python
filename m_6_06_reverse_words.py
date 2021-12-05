from typing import List


def reverse_words(s: List[str]) -> None:
    # First, reverse the whole string.
    _reverse_slice(s, 0, len(s) - 1)

    start_idx = 0
    while True:
        final_idx = start_idx
        while final_idx < len(s) and s[final_idx] != " ":
            final_idx += 1

        if final_idx == len(s):
            break

        # Reverse each word in the string.
        _reverse_slice(s, start_idx, final_idx - 1)

        start_idx = final_idx + 1

    # Reverse the last word.
    _reverse_slice(s, start_idx, len(s) - 1)


def _reverse_slice(s: List[str], start_idx: int, final_idx: int):
    while start_idx < final_idx:
        s[start_idx], s[final_idx] = s[final_idx], s[start_idx]
        start_idx += 1
        final_idx -= 1
