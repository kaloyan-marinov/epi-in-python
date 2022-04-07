import collections
from typing import Optional

from m_09_00_common import BinaryTreeNode


def lca(
    tree: BinaryTreeNode,
    node0: BinaryTreeNode,
    node1: BinaryTreeNode,
) -> Optional[BinaryTreeNode]:

    LCAStatus = collections.namedtuple(
        "LCAStatus",
        ("num_target_nodes", "ancestor"),
    )

    def _lca_status(t, n0, n1) -> LCAStatus:
        if t is None:
            return LCAStatus(num_target_nodes=0, ancestor=None)

        left_lca_status = _lca_status(t.left, n0, n1)
        if left_lca_status.num_target_nodes == 2:
            return left_lca_status

        right_lca_status = _lca_status(t.right, n0, n1)
        if right_lca_status.num_target_nodes == 2:
            return right_lca_status

        num_target_nodes = (
            left_lca_status.num_target_nodes
            + right_lca_status.num_target_nodes
            + (n0, n1).count(t)
        )

        return LCAStatus(
            num_target_nodes=num_target_nodes,
            ancestor=t if num_target_nodes == 2 else None,
        )

    return _lca_status(tree, node0, node1).ancestor
