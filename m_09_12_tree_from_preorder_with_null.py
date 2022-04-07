from typing import List

from m_09_00_common import BinaryTreeNode


def reconstruct_preorder(preorder: List[int]) -> BinaryTreeNode:
    def _helper(preorder_iter):
        subtree_key = next(preorder_iter)

        if subtree_key is None:
            return None

        left = _helper(preorder_iter)
        right = _helper(preorder_iter)

        return BinaryTreeNode(data=subtree_key, left=left, right=right)

    return _helper(iter(preorder))


# fmt: off
'''
preorder = [2, -2, None, 1, None, 0, None, None, None]  # the last 3 copies of `None` were manually added

tree = reconstruct_preorder(preorder)


def visit(t):
    if t:
        visit(t.left)
        print(t.data)
        visit(t.right)


visit(tree) # -2 1 0 2
'''
# fmt: off
