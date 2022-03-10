from typing import List

import collections

from m_14_00_common import BstNode


Interval = collections.namedtuple(
    "Interval",
    ("left", "right"),
)


def range_lookup_in_bst_1(tree: BstNode, interval: Interval) -> List[int]:
    """
    This is based on brute force.

    time:  O(n)
    space: O(h)

    shortcoming:    this f-n does not take advantage of the fact that
                    the `tree` is not a general binary tree,
                    whose keys are all of a data type that's "comparable",
                    but actually is a BST
    """

    def _helper(
        t: BstNode,
        interval: Interval,
        keys: List[int],
    ) -> None:
        if t:
            _helper(t.left, interval, keys)

            if interval.left <= t.data <= interval.right:
                keys.append(t.data)

            _helper(t.right, interval, keys)

    result: List[int] = []

    _helper(tree, interval, result)

    return result


def range_lookup_in_bst_2(tree: BstNode, interval: Interval) -> List[int]:
    """
    TODO: compare this with `range_lookup_in_bst_3`
    """

    def _helper(
        t: BstNode,
        interval: Interval,
        keys: List[int],
    ) -> None:
        if t:
            if interval.left <= t.data:
                _helper(t.left, interval, keys)

            if interval.left <= t.data <= interval.right:
                keys.append(t.data)

            if t.data <= interval.right:
                _helper(t.right, interval, keys)

    result: List[int] = []

    _helper(tree, interval, result)

    return result


def range_lookup_in_bst_3(tree: BstNode, interval: Interval) -> List[int]:
    """
    TODO: compare this with `range_lookup_in_bst_2`
    """

    result: List[int] = []

    def _helper(
        t: BstNode,
    ) -> None:

        if t is None:
            return None

        if interval.left <= t.data <= interval.right:
            _helper(t.left)
            result.append(t.data)
            _helper(t.right)
        elif interval.left > t.data:
            _helper(t.right)
        else:  # i.e. `interval.right < t.data`
            _helper(t.left)

    _helper(tree)

    return result
