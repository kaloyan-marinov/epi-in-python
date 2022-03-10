from typing import List, Optional

from m_14_00_common import BstNode


def build_min_height_bst_from_sorted_array_1(A: List[int]) -> Optional[BstNode]:
    """
    Assume that `A` is sorted.

    TODO: check whether the following holds true

        T(n) = 2 T(n/2) + O(n)
                            |
                            |
                            is this actually true, due to using list slicing?
    """

    n = len(A)

    if n == 0:
        return None

    mid = n // 2

    return BstNode(
        data=A[mid],
        left=build_min_height_bst_from_sorted_array_1(A[:mid]),
        right=build_min_height_bst_from_sorted_array_1(A[mid + 1 :]),
    )


def build_min_height_bst_from_sorted_array_2(A: List[int]) -> Optional[BstNode]:
    """
    Assume that `A` is sorted.
    """

    def _min_height_bst_from_index_range(lo_idx: int, hi_idx: int) -> Optional[BstNode]:
        if lo_idx == hi_idx:
            return None

        mid = (lo_idx + hi_idx) // 2

        return BstNode(
            data=A[mid],
            left=_min_height_bst_from_index_range(lo_idx, mid),
            right=_min_height_bst_from_index_range(mid + 1, hi_idx),
        )

    return _min_height_bst_from_index_range(0, len(A))
