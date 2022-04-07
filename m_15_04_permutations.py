from typing import List


def permutations(A: List[int]) -> List[List[int]]:
    """
    Assume that `A` consists of distinct entries.
    """

    if len(A) == 1:
        return [A]

    result: List[List[int]] = []
    for i, a_i in enumerate(A):
        B = []
        B.extend(A[:i])
        B.extend(A[i + 1 :])

        result.extend(
            ([a_i] + partial_permutation for partial_permutation in permutations(B))
        )

    return result


def permutation_2(A: List[int]) -> List[List[int]]:
    """
    Assume that `A` consists of distinct entries.
    """

    result: List[List[int]] = []

    def _guided_permutation(i: int) -> None:
        """
        Generate each permutation for A[i:]
        and, as soon as "the next such permutation" is generated, append it to `result`.
        """
        if i + 1 == len(A):
            result.append(A.copy())
            return

        # Try every possibility for A[i].
        for j in range(i, len(A)):
            A[i], A[j] = A[j], A[i]
            _guided_permutation(i + 1)
            A[i], A[j] = A[j], A[i]

    _guided_permutation(0)

    return result


from m_05_11_next_permutation import next_permutation  # TODO: create this module!


def permutation_3(A: List[int]) -> List[List[int]]:
    """
    Assume that `A` consists of distinct entries.
    """

    result: List[List[int]] = []

    # (Although each of the provided test cases provides a sorted array for `A`,)
    # it seems that,
    # strictly speaking, a call to `A.sort()` is actually needed at this exact point.

    while True:
        result.append(A.copy())
        A = next_permutation(A)
        if not A:
            break

    return result


if __name__ == "__main__":
    A = [0, 1]
    permutations(A)
