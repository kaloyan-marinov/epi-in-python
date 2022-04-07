from typing import Optional

from m_09_00_common import BinaryTreeNode


def lca(
    node0: BinaryTreeNode,
    node1: BinaryTreeNode,
) -> Optional[BinaryTreeNode]:
    def _depth(n: BinaryTreeNode) -> int:
        d = 0
        while n.parent:
            d += 1
            n = n.parent
        return d

    d0 = _depth(node0)
    d1 = _depth(node1)

    if d0 > d1:
        node0, node1 = node1, node0
        d0, d1 = d1, d0

    for _ in range(d1 - d0):
        node1 = node1.parent

    while node0 != node1:
        node0 = node0.parent
        node1 = node1.parent

    return node0
