from typing import List, Optional

from m_9_00_common import BinaryTreeNode


def binary_tree_from_preorder_inorder(
    preorder: List[int],
    inorder: List[int],
) -> BinaryTreeNode:
    data_2_inorder_idx = {data: i for i, data in enumerate(inorder)}

    # Build the subtree with
    # preorder[preorder_start:preorder_end]
    # and inorder[inorder_start:inorder_end].
    def _helper(
        preorder_start: int, preorder_end: int, inorder_start: int, inorder_end: int
    ) -> Optional[BinaryTreeNode]:
        if preorder_end <= preorder_start or inorder_end <= inorder_start:
            return None

        root_data = preorder[preorder_start]
        root_inorder_idx = data_2_inorder_idx[root_data]
        left_subtree_size = root_inorder_idx - inorder_start  # = k

        # Recursively build the children.
        left = _helper(
            preorder_start + 1,
            preorder_start + 1 + left_subtree_size,
            inorder_start,
            root_inorder_idx,
        )
        right = _helper(
            preorder_start + 1 + left_subtree_size,
            preorder_end,
            root_inorder_idx + 1,
            inorder_end,
        )

        return BinaryTreeNode(
            data=root_data,
            left=left,
            right=right,
        )

    return _helper(
        preorder_start=0,
        preorder_end=len(preorder),
        inorder_start=0,
        inorder_end=len(inorder),
    )
