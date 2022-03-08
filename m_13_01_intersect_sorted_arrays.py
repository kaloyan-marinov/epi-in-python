from typing import List


def intersect_two_sorted_arrays_1(A: List[int], B: List[int]) -> List[int]:
    """
    Assume that each of A and B may contain duplicates.
    The returned list should be free of duplicates.

    time:  O( max(m + n,  len(s) * log len(s)) )

    space: O(m_uniques + n_uniques)  (?)
    """
    s = set(A) & set(B)
    return sorted([x for x in s])


def intersect_two_sorted_arrays_2(A: List[int], B: List[int]) -> List[int]:
    """
    time: O(mn)
    """
    # fmt: off
    return [
        a for i, a in enumerate(A)
        if (i == 0 or a != A[i - 1]) and a in B
    ]
    # fmt: on


import bisect


def intersect_two_sorted_arrays_3(A: List[int], B: List[int]) -> List[int]:
    """
    Improve upon `intersect_two_sorted_arrays_2`
    by utilizing binary search to check if a is in B
    (which is possible b/c B is sorted).

    time: O( min(m, n) *  log max(m, n))
    """

    # An extra improvement: choose the shorter array for the outer loop.
    if len(A) > len(B):
        A, B = B, A

    def _is_present(k):
        i = bisect.bisect_left(B, k)
        return i < len(B) and B[i] == k

    # fmt: off
    return [
        a for i, a in enumerate(A)
        if (i == 0 or a != A[i - 1]) and _is_present(a)
    ]
    # fmt: on


def intersect_two_sorted_arrays_4(A: List[int], B: List[int]) -> List[int]:
    i = 0
    j = 0
    intersection = []

    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            intersection.append(A[i])
            i += 1
            j += 1

            # fmt: off
            # The previous block can be replaced with the following one:
            '''
            intersection.append(A[i])

            a_i = A[i]
            while i < A[i] and A[i] == a_i:
                i += 1
            
            b_j = B[j]
            while j < B[j] and B[j] == b_j:
                j += 1
            '''
            # fmt: on
        elif A[i] < B[j]:
            i += 1
        else:  # i.e. A[i] > B[j]
            j += 1

    return intersection
