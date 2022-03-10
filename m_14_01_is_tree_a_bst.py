from typing import List, Union, Literal, Optional, Tuple, Deque

import typing

import collections


from m_9_00_common import BinaryTreeNode


class ExtremesPair(typing.NamedTuple):
    min: Union[int, Literal[float("inf")]]
    max: Union[int, Literal[float("-inf")]]


def is_binary_tree_bst_1_a(tree: BinaryTreeNode) -> bool:
    """
    This is a solution by me.
    """

    def _helper(t: BinaryTreeNode) -> ExtremesPair:
        if t is None:
            return ExtremesPair(
                min=float("inf"),
                max=float("-inf"),
            )

        result_left = _helper(t.left)
        result_right = _helper(t.right)

        if result_left.max <= t.data <= result_right.min:
            return ExtremesPair(
                min=min(result_left.min, t.data),
                max=max(t.data, result_right.max),
            )
        else:
            return ExtremesPair(
                min=float("-inf"),
                max=float("inf"),
            )

    max_min = _helper(tree)

    return max_min.max != float("inf")
    # fmt: off
    '''
    >>> float('inf') is float('inf')
    False
    >>> float('inf') == float('inf')
    True
    '''
    # fmt: on


def is_binary_tree_bst_1_b(tree: BinaryTreeNode) -> bool:
    """
    This is 1 of the official solutions.
    """

    def _are_keys_in_range(
        t: BinaryTreeNode,
        lower_bdd=float("-inf"),
        upper_bdd=float("inf"),
    ) -> bool:
        if not t:
            return True
        elif not lower_bdd <= t.data <= upper_bdd:
            return False
        else:
            return _are_keys_in_range(
                t.left,
                lower_bdd=lower_bdd,
                upper_bdd=t.data,
            ) and _are_keys_in_range(
                t.right,
                lower_bdd=t.data,
                upper_bdd=upper_bdd,
            )

    return _are_keys_in_range(
        tree,
        lower_bdd=float("-inf"),
        upper_bdd=float("inf"),
    )


def is_binary_tree_bst_2_a(tree: BinaryTreeNode) -> bool:
    """
    This is a solution by me.

    time:  O(n * log n)

    space: O(n)
    """

    def _helper(t: BinaryTreeNode, values: List[int]) -> None:
        if t:
            _helper(t.left, values)
            values.append(t.data)
            _helper(t.right, values)

    lst = []
    _helper(tree, lst)
    return lst == sorted(lst)


def is_binary_tree_bst_2_b_1(tree: BinaryTreeNode) -> bool:
    """
    time:  O(n)

    space: O(h)

    reference:
    https://www.geeksforgeeks.org/a-program-to-check-if-a-binary-tree-is-bst-or-not/
    """

    prev = None

    def _helper(t: BinaryTreeNode) -> bool:

        nonlocal prev

        if t is None:
            return True

        if _helper(t.left) is False:
            return False

        if prev is not None and prev.data > t.data:
            return False

        prev = t

        return _helper(t.right)

    return _helper(tree)


def is_binary_tree_bst_2_b_2(tree: BinaryTreeNode) -> bool:
    def _helper(
        t: BinaryTreeNode,
    ) -> Tuple[bool, Optional[BinaryTreeNode]]:
        # ...
        return is_t_not_less_than_prev, prev

    raise NotImplementedError(
        "Attempt to implement this, as an alternative to the previous function",
    )


class NodeBoundsTuple(typing.NamedTuple):
    node: BinaryTreeNode
    lower: float
    upper: float


def is_binary_tree_bst_3(tree: BinaryTreeNode) -> bool:
    bfs_queue: Deque[NodeBoundsTuple] = collections.deque(
        [
            NodeBoundsTuple(tree, float("-inf"), float("inf")),
        ],
    )

    while bfs_queue:
        entry = bfs_queue.popleft()

        if entry.node:
            if not entry.lower <= entry.node.data <= entry.upper:
                return False

            bfs_queue.extend(
                (
                    NodeBoundsTuple(entry.node.left, entry.lower, entry.node.data),
                    NodeBoundsTuple(entry.node.right, entry.node.data, entry.upper),
                )
            )

    return True


if __name__ == "__main__":
    # fmt: off
    '''
    n_2 = BinaryTreeNode(data=2)
    n_5 = BinaryTreeNode(data=5)
    n_13 = BinaryTreeNode(data=13)
    n_31 = BinaryTreeNode(data=31)
    n_41 = BinaryTreeNode(data=41)
    n_53 = BinaryTreeNode(data=53)

    n_3 = BinaryTreeNode(data=-1, left=n_2, right=n_5)
    n_17 = BinaryTreeNode(data=17, left=n_13)
    n_29 = BinaryTreeNode(data=29, right=n_31)
    n_47 = BinaryTreeNode(data=47, right=n_53)

    n_11 = BinaryTreeNode(data=11, right=n_17)
    n_37 = BinaryTreeNode(data=37, left=n_29, right=n_41)

    n_7 = BinaryTreeNode(data=7, left=n_3, right=n_11)

    n_23 = BinaryTreeNode(data=23, right=n_37)

    n_43 = BinaryTreeNode(data=43, left=n_23, right=n_47)

    n_19 = BinaryTreeNode(data=19, left=n_7, right=n_43)

    result = is_binary_tree_bst_1_a(n_19)
    print(result)
    '''
    # fmt: on

    # fmt: off
    '''
    Construct the following binary tree:

                    -2
                  /    \
                1       2
              /
            0
    '''
    # fmt: on
    n_0 = BinaryTreeNode(data=0)
    n_1 = BinaryTreeNode(data=1, left=n_0)

    n_2 = BinaryTreeNode(data=2)

    n_minus_2 = BinaryTreeNode(data=-2, left=n_1, right=n_2)

    result = is_binary_tree_bst_2_c_2(n_minus_2)
    print(result)
