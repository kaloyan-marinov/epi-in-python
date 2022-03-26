from typing import List, Set


def decompose_into_dictionary_words(
    domain: str,
    dictionary: Set[str],
) -> List[str]:

    # for word in dictionary:
    #     if domain[:len(word)] == word:
    #         docomposition: List[str] = _helper(len(word))

    def _starts_with_concatenation(
        name: str,
    ) -> List[str]:
        # if domain[:final_idx] in dictionary:
        #     return [domain[:final_idx]] + _starts_with_concatenation()
        for start_idx in range(1, len(name) + 1):
            if name[-start_idx:] in dictionary:
                others = _starts_with_concatenation(name[:-start_idx])

                if others:
                    return others + [name[-start_idx:]]

        return []

    return _starts_with_concatenation(domain)


def decompose_into_dictionary_words_2(
    domain: str,
    dictionary: Set[str],
) -> List[str]:
    """
    When [the first part of]the algorithm finishes,
    `idx_2_last_length[i] != -1` indicates that
    (a) `domain[:i + 1]` has a valid decomposition, and
    (b) the length of the last [dictionary word]
        within [that] decomposition is `idx_2_last_length[i]`.
    """

    idx_2_last_length: List[int] = [-1] * len(domain)

    for i in range(len(domain)):
        # If `domain[:i + 1]` is a dictionary word,
        # set `idx_2_last_length[i]` to the length of that word.
        if domain[: i + 1] in dictionary:
            idx_2_last_length[i] = i + 1
            continue

        # If `domain[:i + 1]` is not a dictionary word,
        # look for `j < i` such that
        #   (a) `domain[:j + 1]` has a valid decomposition, and
        #   (b) `domain[j + 1: i + 1]` is a dictionary word;
        # if such a j is found, record the length of that word in `idx_2_last_length[i]`.
        for j in range(i):
            if idx_2_last_length[j] != -1 and domain[j + 1 : i + 1] in dictionary:
                idx_2_last_length[i] = i - j
                break

    dict_word_decomposition_in_reverse_order: List[str] = []
    if (
        idx_2_last_length[-1] != -1
    ):  # i.e. `domain[:-1 + 1] = domain` has a valid decomposition.
        idx = len(domain) - 1
        while idx >= 0:
            dict_word_decomposition_in_reverse_order.append(
                domain[idx + 1 - idx_2_last_length[idx] : idx + 1]
            )
            idx -= idx_2_last_length[idx]

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
