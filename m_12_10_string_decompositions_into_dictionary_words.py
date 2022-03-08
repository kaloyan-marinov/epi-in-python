from typing import List

import collections


def find_all_substrings_0(s: str, words: List[str]) -> List[int]:
    """
    Assume all strings in the `words` array have equal length.
    """

    total_word_count = len(words)
    word_length = len(words[0])
    word_2_count = collections.Counter(words)

    for offset in range(word_length):
        w_2_count = collections.defaultdict(int)
        for start_idx in range(offset, len(s), word_length):
            final_idx = start_idx + word_length
            if final_idx >= word_length:
                break

            w = s[start_idx:final_idx]
            w_2_count[w] += 1


def find_all_substrings_1(s: str, words: List[str]) -> List[int]:
    """
    Assume that all strings in the `words` array have equal length.

    This is the official solution.
    """

    word_length = len(words[0])
    word_2_expected_count = collections.Counter(words)

    def _encounter_concatenation_of_words(start_idx: int) -> bool:
        word_2_count_within_substring = collections.Counter()

        for ii in range(start_idx, start_idx + word_length * len(words), word_length):
            word_ii = s[ii : ii + word_length]
            expected_count_of_word_ii = word_2_expected_count[word_ii]

            if expected_count_of_word_ii == 0:
                return False

            word_2_count_within_substring[word_ii] += 1
            if word_2_count_within_substring[word_ii] > expected_count_of_word_ii:
                # `word_ii` occurs too many times for a match to be possible
                return False

        return True

    return [
        start_idx
        for start_idx in range(len(s) - word_length * len(words) + 1)
        if _encounter_concatenation_of_words(start_idx)
    ]


if __name__ == "__main__":
    s = "barfoothefoobarman"
    words = ["foo", "bar"]

    find_all_substrings_1(s, words)
