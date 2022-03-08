from typing import Counter

import collections


def is_letter_constructible_from_magazine_1(
    letter_text: str,
    magazine_text: str,
) -> bool:
    char_2_l_count: Counter[str, int] = collections.Counter(letter_text)
    char_2_m_count: Counter[str, int] = collections.Counter(magazine_text)

    for c in char_2_l_count:
        if char_2_l_count[c] > char_2_m_count[c]:
            return False

    return True


def is_letter_constructible_from_magazine_2(
    letter_text: str,
    magazine_text: str,
) -> bool:
    # fmt: off
    # This is a bugfix.
    '''
    if letter_text == "":
        return True
    '''
    # fmt: on

    char_2_l_count: Counter[str, int] = collections.Counter(letter_text)

    for m_char in magazine_text:
        if m_char in char_2_l_count:
            char_2_l_count[m_char] -= 1
            # fmt: off
            # This is a bugfix.
            '''
            if char_2_l_count[m_char] == 0:
                del char_2_l_count[m_char]
            '''
            # fmt: on
        if not char_2_l_count:
            return True

    return False


def is_letter_constructible_from_magazine_3_pythonic(
    letter_text: str,
    magazine_text: str,
):
    """
    This solution is Pythonic in nature.
    In general terms, it exploits `collections.Counter`;
    in more specific terms, it exploits the fact that,
    when one `collections.Counter` is subtracted from another `collections.Counter`,
    only those keys whose resulting counts are positive are kept.
    """
    return not collections.Counter(letter_text) - collections.Counter(magazine_text)


if __name__ == "__main__":
    letter_text_1 = "123"
    magazine_text_1 = "1123"
    result_1 = is_letter_constructible_from_magazine_2(letter_text_1, magazine_text_1)
    print(result_1)  # `False` (but `True` is expected)

    letter_text_2 = ""
    magazine_text_2 = ""
    result_2 = is_letter_constructible_from_magazine_2(letter_text_2, magazine_text_2)
    print(result_2)  # `False` (but `True` is expected)
