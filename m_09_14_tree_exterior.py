from typing import List

from m_09_00_common import BinaryTreeNode
from m_09_13_tree_connect_leaves import create_list_of_leaves


def exterior_binary_tree(tree: BinaryTreeNode) -> List[BinaryTreeNode]:
    """
    add m_9_14_tree_exterior.py which is incorrect
    """

    def _left(t, l_ns):
        while t:
            l_ns.append(t)
            t = t.left

    left_nodes = []
    _left(tree, left_nodes)

    leaves = create_list_of_leaves(tree)

    def _right(t, r_ns):
        while t:
            r_ns.append(t)
            t = t.right

    right_nodes = []
    _right(tree, right_nodes)
    right_nodes = right_nodes[::-1]

    end_left_nodes = -1 if left_nodes[-1] is leaves[0] else len(left_nodes)
    end_leaves = -1 if leaves[-1] is right_nodes[0] else len(leaves)
    end_right = -1 if right_nodes[-1] is left_nodes[0] else len(right_nodes)

    return left_nodes[:end_left_nodes] + leaves[:end_leaves] + right_nodes[:end_right]


def exterior_binary_tree(tree: BinaryTreeNode) -> List[BinaryTreeNode]:
    """
    fix the bug in the previous commit
    """
    if not tree:
        return []

    def _left(t, l_ns):
        while t:
            l_ns.append(t)
            t = t.left if t.left else t.right

    left_nodes = []
    _left(tree.left, left_nodes)

    left_leaves = create_list_of_leaves(tree.left)

    if left_nodes and left_nodes[-1] is left_leaves[0]:
        left_nodes = left_nodes[:-1]

    def _right(t, r_ns):
        while t:
            r_ns.append(t)
            t = t.right if t.right else t.left

    right_nodes = []
    _right(tree.right, right_nodes)
    right_nodes = right_nodes[::-1]

    right_leaves = create_list_of_leaves(tree.right)

    if right_nodes and right_leaves[-1] is right_nodes[0]:
        right_nodes = right_nodes[1:]

    return [tree] + left_nodes + left_leaves + right_leaves + right_nodes


def exterior_binary_tree(tree: BinaryTreeNode) -> List[BinaryTreeNode]:
    """
    add a 2nd solution to m_9_14_tree_exterior.py
    """

    if not tree:
        return []

    exterior = [tree]

    # Computes the nodes from the root to _but excluding_ the leftmost leaf.
    def _left_boundary(subtree):
        if not subtree or (not subtree.left and not subtree.right):
            return

        exterior.append(subtree)

        if subtree.left:
            _left_boundary(subtree.left)
        else:
            _left_boundary(subtree.right)

    # Computes the nodes from _but excluding_ the rightmost leaf to the root.
    def _right_boundary(subtree):
        if not subtree or (not subtree.left and not subtree.right):
            return

        if subtree.right:
            _right_boundary(subtree.right)
        else:
            _right_boundary(subtree.left)

        exterior.append(subtree)

    # Computes the leaves in left-to-right-order.
    def _leaves(subtree):
        if not subtree:
            return

        if not subtree.left and not subtree.right:
            exterior.append(subtree)
            return

        _leaves(subtree.left)
        _leaves(subtree.right)

    # Account for the contributions of the root's left subtree.
    _left_boundary(tree.left)
    _leaves(tree.left)

    # Account for the contributions of the root's right subtree.
    _leaves(tree.right)
    _right_boundary(tree.right)

    return exterior
