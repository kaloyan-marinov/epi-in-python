from typing import Optional, Set

from m_9_00_common import BinaryTreeNodeWithParent as BinaryTreeNode


def lca_1(node0: BinaryTreeNode, node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    """
    Arguments
        tree:              [1, 2, 3, 4]
        node0:             3
        node1:             1

    Failure info
        exception message: 'NoneType' object has no attribute 'parent'
    """
    # fmt: off
    '''
    ancestors_of_node_0 = set()
    while True:
        if node0:
            ancestors_of_node_0.add(node0)
            node0 = node0.parent

        if node1 in ancestors_of_node_0:
            return node1

        node1 = node1.parent
    '''
    # fmt: on

    ancestors_of_node_0 = {node0}
    ancestors_of_node_1 = {node1}

    while True:
        if ancestors_of_node_0.intersection(ancestors_of_node_1):
            break

        if node0.parent:
            node0 = node0.parent
            ancestors_of_node_0.add(node0)

        if node1.parent:
            node1 = node1.parent
            ancestors_of_node_1.add(node1)

    for n in ancestors_of_node_0.intersection(ancestors_of_node_1):
        return n


def lca_2(node0: BinaryTreeNode, node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    n0 = node0
    n1 = node1
    visited_nodes: Set[BinaryTreeNode] = set()

    while n0 or n1:
        if n0:
            if n0 in visited_nodes:
                return n0
            visited_nodes.add(n0)
            n0 = n0.parent

        if n1:
            if n1 in visited_nodes:
                return n1
            visited_nodes.add(n1)
            n1 = n1.parent

    raise ValueError("node0 and node1 aren't in the same tree")
