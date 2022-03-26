from typing import List, Set


def decompose_into_dictionary_words(
    domain: str,
    dictionary: Set[str],
) -> List[str]:
    """
    When [the first part of] the algorithm finishes,
    `idx_2_last_dct_wrd_len[i] != -1` indicates that
    (a) `domain[:i + 1]` has a valid decomposition, and
    (b) the length of the last [dictionary word]
        within [that] decomposition is `idx_2_last_dct_wrd_len[i]`.
    """

    idx_2_last_dct_wrd_len: List[int] = [-1] * len(domain)

    for i in range(len(domain)):
        # If `domain[:i + 1]` is a dictionary word,
        # set `idx_2_last_dct_wrd_len[i]` to the length of that word.
        if domain[: i + 1] in dictionary:
            idx_2_last_dct_wrd_len[i] = i + 1
            continue

        # If `domain[:i + 1]` is not a dictionary word,
        # look for `j < i` such that
        #   (a) `domain[:j + 1]` has a valid decomposition, and
        #   (b) `domain[j + 1: i + 1]` is a dictionary word;
        # if such a j is found, record the length of that word in `idx_2_last_dct_wrd_len[i]`.
        for j in range(i):
            if idx_2_last_dct_wrd_len[j] != -1 and domain[j + 1 : i + 1] in dictionary:
                idx_2_last_dct_wrd_len[i] = i - j
                break

    dict_word_decomposition_in_reverse_order: List[str] = []
    if (
        idx_2_last_dct_wrd_len[-1] != -1
    ):  # i.e. `domain[:-1 + 1] = domain` has a valid decomposition.
        idx = len(domain) - 1
        while idx >= 0:
            dict_word_decomposition_in_reverse_order.append(
                domain[idx + 1 - idx_2_last_dct_wrd_len[idx] : idx + 1]
            )
            idx -= idx_2_last_dct_wrd_len[idx]

    return dict_word_decomposition_in_reverse_order[::-1]


if __name__ == "__main__":

    domain = "asseafseaefseefaaffffefafafefe"
    # fmt: off
    dictionary = {
        "af", "afaa", "ss", "efaa", "sfsss", "eas", "sesae", "ses", "efe", "a", "sfef",
        "fafse", "aae", "fs", "fea", "easa", "ee", "asef", "fafa", "aaa", "f", "eeaee",
        "aea", "efs", "eafs", "se", "ase", "easf", "ae", "eaef", "afe", "aass", "ffef",
        "sesef", "ffea", "ass", "sea", "eeas", "fa", "saf", "sasf", "sa", "eesf", "eee",
         "aa", "sas", "ff", "sfeff", "fse", "e"
    }
    # fmt: on

    result = decompose_into_dictionary_words(domain, dictionary)
