from typing import Counter

import collections


def can_form_palindrome(s: str) -> bool:
    char_2_count: Counter[str, int] = collections.Counter(s)

    num_of_odd_counts = 0
    for count in char_2_count.values():
        num_of_odd_counts += count % 2
        if num_of_odd_counts > 1:
            return False

    return True
