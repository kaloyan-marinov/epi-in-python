import collections
from typing import List

from m_9_00_common import BinaryTreeNode


def inorder_traversal_recursive(tree: BinaryTreeNode) -> List[int]:
    values = []

    def _helper(t: BinaryTreeNode, vs: List[int]):
        if t:
            _helper(t.left, vs)

            vs.append(t.data)

            _helper(t.right, vs)

    _helper(tree, values)

    return values


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    # fmt: off
    '''
    result = []

    NodeInProcess = collections.namedtuple(
        "NodeInProcess",
        ("node", "processing_children"),
    )

    nodes_in_process: List[NodeInProcess] = [(tree, False)]
    while nodes_in_process:
        n, processing_children_of_n = nodes_in_process.pop()

        if n:
            if processing_children_of_n:  # i.e. the left subtree has been processed.
                result.append(n.data)
            else:
                nodes_in_process.append(
                    NodeInProcess(node=n.right, processing_children=False)
                )
                nodes_in_process.append(NodeInProcess(node=n, processing_children=True))
                nodes_in_process.append(
                    NodeInProcess(node=n.left, processing_children=False)
                )

    return result
    '''
    # fmt: on

    result = []

    n = tree
    processing_children_of_n = False
    nodes_in_process = [(n, processing_children_of_n)]

    while nodes_in_process:
        n, processing_children_of_n = nodes_in_process.pop()

        if n:
            if processing_children_of_n:
                result.append(n.data)
            else:
                nodes_in_process.append((n.right, False))
                nodes_in_process.append((n, True))
                nodes_in_process.append((n.left, False))

    return result
