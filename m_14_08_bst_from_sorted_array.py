from typing import List, Optional

from m_14_00_common import BstNode


def build_min_height_bst_from_sorted_array_1(A: List[int]) -> Optional[BstNode]:
    """
    Assume that `A` is sorted.
    """

    n = len(A)

    if n == 0:
        return None

    mid = n // 2

    return BstNode(
        data=A[mid],
        left=build_min_height_bst_from_sorted_array_1(
            A[: mid - 1]
        ),  # change `mid - 1` to `mid`
        right=build_min_height_bst_from_sorted_array_1(A[mid + 1 :]),
    )


def build_min_height_bst_from_sorted_array_2(A: List[int]) -> Optional[BstNode]:
    """
    Assume that `A` is sorted.
    """

    def _min_height_bst_from_index_range(lo_idx: int, hi_idx: int) -> Optional[BstNode]:
        if lo_idx == hi_idx:
            return None

        mid = (hi_idx - lo_idx + 1) // 2  # change to `(hi_idx + low_idx) // 2`

        return BstNode(
            data=A[mid],
            left=_min_height_bst_from_index_range(lo_idx, mid),
            right=_min_height_bst_from_index_range(mid + 1, hi_idx),
        )

    return _min_height_bst_from_index_range(0, len(A) - 1)  # change to `(0, len(A))`
