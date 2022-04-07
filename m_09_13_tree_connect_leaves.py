from typing import List

from m_09_00_common import BinaryTreeNode


def create_list_of_leaves(
    tree: BinaryTreeNode,
) -> List[BinaryTreeNode]:

    leaves: List[BinaryTreeNode] = []

    def _helper(t: BinaryTreeNode, ls: List[BinaryTreeNode]):
        if t:
            _helper(t.left, ls)

            if not t.left and not t.right:
                ls.append(t)

            _helper(t.right, ls)

    _helper(tree, leaves)

    return leaves
