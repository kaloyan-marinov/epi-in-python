from typing import List, Optional

from m_14_00_common import BstNode


def rebuild_bst_from_preorder_1(preorder_sequence: List[int]) -> Optional[BstNode]:
    """
    Assume that `preorder_sequence` is composed of unique keys.
    """

    if not preorder_sequence:
        return None

    # The following is unnecessary.
    if len(preorder_sequence) == 1:
        return BstNode(data=preorder_sequence[0])

    i = 1
    # fmt: off
    '''
    while preorder_sequence[i] <= preorder_sequence[0]:
    '''
    # fmt: on
    while i < len(preorder_sequence) and preorder_sequence[i] < preorder_sequence[0]:
        i += 1

    return BstNode(
        data=preorder_sequence[0],
        left=rebuild_bst_from_preorder_1(preorder_sequence[1:i]),
        right=rebuild_bst_from_preorder_1(preorder_sequence[i:]),
    )


def rebuild_bst_from_preorder_2(preorder_sequence: List[int]) -> Optional[BstNode]:
    """
    Assume that `preorder_sequence` is composed of unique keys.
    """

    if not preorder_sequence:
        return None

    i = next(
        (i for i, a in enumerate(preorder_sequence) if a > preorder_sequence[0]),
        len(preorder_sequence),
    )

    return BstNode(
        data=preorder_sequence[0],
        left=rebuild_bst_from_preorder_2(preorder_sequence[1:i]),
        right=rebuild_bst_from_preorder_2(preorder_sequence[i:]),
    )


def rebuild_bst_from_preorder_3(preorder_sequence: List[int]) -> Optional[BstNode]:
    """
    Assume that `preorder_sequence` is composed of unique keys.
    """

    root_idx = [0]

    def _rebuild_bst_from_preorder_on_value_range(
        lower_bound: int, upper_bound: int
    ) -> Optional[BstNode]:
        if root_idx[0] == len(preorder_sequence):
            return None

        root_value = preorder_sequence[root_idx[0]]

        if not lower_bound <= root_value <= upper_bound:  # each ineq can be strict!
            return None

        root_idx[0] += 1

        # Note that, since this function updates `root_idx[0]`,
        # the order of the following two calls is critical.
        left_subtree = _rebuild_bst_from_preorder_on_value_range(
            lower_bound,
            root_value,
        )
        right_subtree = _rebuild_bst_from_preorder_on_value_range(
            root_value,
            upper_bound,
        )

        return BstNode(
            data=root_value,
            left=left_subtree,
            right=right_subtree,
        )

    return _rebuild_bst_from_preorder_on_value_range(
        float("-inf"),
        float("inf"),
    )
