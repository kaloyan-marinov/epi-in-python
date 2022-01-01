from typing import List

from m_9_00_common import BinaryTreeNode


def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:

    result: List[List[int]] = []
    if not tree:
        return result

    curr_depth_nodes = [tree]
    while curr_depth_nodes:
        result.append([c_d_n.data for c_d_n in curr_depth_nodes])

        curr_depth_nodes = [
            child
            for c_d_n in curr_depth_nodes
            for child in (c_d_n.left, c_d_n.right)
            if child
        ]

    return result
