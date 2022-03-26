from typing import List


def is_palindrome(text: str) -> bool:
    n = len(text)

    for i in range(0, n // 2):
        if text[i] != text[n - 1 - i]:
            return False

    return True


def palindrome_decompositions(text: str) -> List[List[str]]:
    """
    This is a solution by me.
    """

    def _helper(
        t: str,
        min_final_idx_for_prefix: int,
    ) -> List[List[str]]:
        if len(t) == 0:
            return []
        elif len(t) == 1:
            return [[t]]

        r: List[List[str]] = []

        prefix_final_idx = min_final_idx_for_prefix
        while prefix_final_idx <= len(t):

            if is_palindrome(t[:prefix_final_idx]):
                if prefix_final_idx == len(t):
                    r.append([t])
                else:
                    # fmt: off
                    '''
                    r.extend(
                        (
                            t[:prefix_final_idx] + decomposition
                            for decomposition in _helper(t[prefix_final_idx:], 1)
                        ),
                    )
                    '''
                    # fmt: on
                    decompositions = _helper(t[prefix_final_idx:], 1)
                    for d in decompositions:
                        r.append([t[:prefix_final_idx]] + d)

            prefix_final_idx += 1

        return r

    return _helper(text, 1)


def palindrome_decompositions_2(text: str) -> List[List[str]]:

    result: List[List[str]] = []

    def _guided_palindrome_decompositions(
        start_idx: int,
        partial_decomposition: List[str],
    ) -> None:
        if start_idx == len(text):
            result.append(partial_decomposition.copy())  # NB: unnecessary to `.copy()`!
            return

        for final_idx in range(start_idx + 1, len(text) + 1):
            prefix = text[start_idx:final_idx]

            if prefix == prefix[::-1]:  # Seems faster than `is_palindrome(prefix)`.
                _guided_palindrome_decompositions(
                    final_idx,
                    partial_decomposition + [prefix],
                )

    _guided_palindrome_decompositions(0, [])

    return result


if __name__ == "__main__":
    print(is_palindrome("Bob"))
    print(is_palindrome("bob"))
    print(is_palindrome("ahhA"))
    print(is_palindrome("ahha"))

    result = palindrome_decompositions("uhxhkhxhu")
    print(result)
