from typing import List, Optional

from m_09_00_common import BinaryTreeNode


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    result: List[int] = []
    prev_n: Optional[BinaryTreeNode] = None

    while tree:
        if prev_n is tree.parent:  # i.e. we came down to `tree` from `prev_n`
            if tree.left:
                next_n = tree.left
            else:
                result.append(tree.data)
                # Ready to move on from the current `tree`, so:
                # - if right is not empty, go right;
                # - else, go up.
                next_n = tree.right or tree.parent
        elif prev_n is tree.left:  # i.e. we came up to `tree` from its left child
            result.append(tree.data)
            # Ready to move on from the current `tree`, so:
            # - if right is not empty, go right;
            # - else, go up.
            next_n = tree.right or tree.parent
        else:  # i.e. done with both children
            next_n = tree.parent

        prev_n = tree
        tree = next_n

    return result
