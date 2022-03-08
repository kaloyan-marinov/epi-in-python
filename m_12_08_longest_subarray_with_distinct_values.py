from typing import Dict, List


def longest_subarray_with_distinct_entries_1(A: List[int]) -> int:
    curr_length = 0
    max_length = 0

    seen_entries = set()
    ii = 0
    for jj, a_jj in enumerate(A):  # but note that `jj` is unused!
        if a_jj not in seen_entries:
            seen_entries.add(a_jj)
            curr_length += 1
        else:  # i.e. `a_jj in seen_entries`
            # max_length = max(max_length, curr_length)  # shift for ex 2

            while True:
                a_ii = A[ii]
                seen_entries.discard(a_ii)
                curr_length -= 1  # add for ex 1
                ii += 1
                if a_ii == a_jj:
                    seen_entries.add(a_jj)  # add for ex 2
                    curr_length += 1  # add for ex 2
                    break

        max_length = max(max_length, curr_length)

    return max_length


def longest_subarray_with_distinct_entries_2(A: List[int]) -> int:
    curr_length = 0
    max_length = 0

    seen_entries = set()

    ii = 0
    jj = 0
    while jj < len(A):
        a_jj = A[jj]

        if a_jj not in seen_entries:
            seen_entries.add(a_jj)
            curr_length += 1
            jj += 1
        else:
            while True:
                a_ii = A[ii]
                seen_entries.discard(a_ii)
                curr_length -= 1
                ii += 1
                if a_ii == a_jj:
                    break

        max_length = max(max_length, curr_length)

    return max_length


def longest_subarray_with_distinct_entries_3(A: List[int]) -> int:
    entry_2_latest_occurrence: Dict[int, int] = {}
    start_idx_of_longest_dup_free_subarray = 0
    max_length = 0

    for i, a_i in enumerate(A):
        # [Defer updating dup_idx until we see a duplicate.]
        if a_i in entry_2_latest_occurrence:  # i.e. if a_i has appeared before.
            latest_occurrence_of_a_i = entry_2_latest_occurrence[a_i]

            if (
                latest_occurrence_of_a_i >= start_idx_of_longest_dup_free_subarray
            ):  # i.e. if a_i appeared in the currently longest dup-free subarray
                max_length = max(
                    max_length,
                    i - start_idx_of_longest_dup_free_subarray,
                )
                start_idx_of_longest_dup_free_subarray = latest_occurrence_of_a_i + 1

        entry_2_latest_occurrence[a_i] = i

    return max(max_length, len(A) - start_idx_of_longest_dup_free_subarray)


if __name__ == "__main__":
    # ex 1
    # A = [1, 2, 1, 3, 1, 2, 1]
    # max_length = longest_subarray_with_distinct_entries(A)

    # print(max_length)

    # ex 2
    A = [13, 13, 79]
    max_length = longest_subarray_with_distinct_entries_1(A)

    print(max_length)  # 1 (instead of 2)
