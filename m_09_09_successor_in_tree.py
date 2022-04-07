from typing import Optional

from m_9_00_common import BinaryTreeNodeWithParent as BinaryTreeNode


def find_successor(node: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    if node.right:
        s = node.right
        while s.left:
            s = s.left
        return s

    s = node.parent
    t = node
    while s and s.right is t:
        t = s
        s = s.parent

    if s:
        return s.parent
    else:
        return None
