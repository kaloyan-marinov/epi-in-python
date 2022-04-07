from typing import List, Optional

from m_9_00_common import BinaryTreeNode


def binary_tree_depth_order(tree: Optional[BinaryTreeNode]) -> List[List[int]]:
    """
    Return a list of [sub]lists,
    where each sublist consists of the keys at a fixed depth in `tree`
    and the sublists should appear in the order of increasing depths.

    For example, for the binary tree

                                314
                    /                       \
            6                                       6
          /    \                                  /      \
        271     561                             2           271
       /   \       \                              \            \
    28      0       3                               1           28
                  /                                /  \
                17                              401     257
                                                   \
                                                    641
    the return value should be

    [
        [314],
        [6, 6],
        [271, 561, 2, 271],
        [28, 0, 3, 1, 28],
        [17, 401, 257],
        [641],
    ]

    time:  O(n)
           where n := the # of nodes in the `tree`

    space: O(m)
           where m := the max # of nodes at any given depth in the `tree`
    """

    result: List[List[int]] = []
    if not tree:
        return result

    curr_depth_nodes = [tree]
    while curr_depth_nodes:
        result.append([c_d_n.data for c_d_n in curr_depth_nodes])

        next_depth_nodes: List[BinaryTreeNode] = []
        for c_d_n in curr_depth_nodes:
            for child in (c_d_n.left, c_d_n.right):
                if child:
                    next_depth_nodes.append(child)

        curr_depth_nodes = next_depth_nodes

    return result
