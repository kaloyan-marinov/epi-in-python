from typing import List


def longest_contained_range(A: List[int]) -> int:
    unprocessed_entries = set(A)
    max_interval_size = 0

    while unprocessed_entries:
        e = unprocessed_entries.pop()
        curr_interval_size = 1

        e_plus = e + 1
        while e_plus in unprocessed_entries:
            unprocessed_entries.remove(e_plus)
            curr_interval_size += 1
            e_plus += 1

        e_minus = e - 1
        while e_minus in unprocessed_entries:
            unprocessed_entries.remove(e_minus)
            curr_interval_size += 1
            e_minus -= 1

        max_interval_size = max(max_interval_size, curr_interval_size)

    return max_interval_size
