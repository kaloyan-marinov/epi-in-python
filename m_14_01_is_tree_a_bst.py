from typing import List, NamedTuple, Optional

import collections


from m_9_00_common import BinaryTreeNode


ExtremesPair = collections.namedtuple(
    "ExtremesPair",
    ("min", "max"),
)


# fmt: off
'''
def is_binary_tree_bst_1_a(tree: BinaryTreeNode) -> bool:
    def _helper(t: BinaryTreeNode) -> ExtremesPair:
        print()
        print(t)
        
        if t is None:
            return ExtremesPair(
                min=float('inf'),
                max=float('-inf'),
            )


        t_left_result = _helper(t.left)
        t_right_result = _helper(t.right)

        print('    ', t.data)
        print('    ', t_left_result)
        print('    ', t_right_result)
        if ( 
            t_left_result.max <= t.data
         and
            t.data <= t_right_result.min
        and
            t_right_result.min is not float('inf')
        ):
            e = ExtremesPair(
                min=min(t_left_result.min, t.data, t_right_result.min),
                max=max(t_left_result.max, t.data, t_right_result.max),
            )
            print(t.data, e)
            return e
        else:
            e = ExtremesPair(
                min=float("-inf"),
                max=float("inf"),
            )
            print(t.data, e)
            return e

    max_min = _helper(tree)

    return max_min.max != float("inf")
'''
# fmt: on


def is_binary_tree_bst_1_a(tree: BinaryTreeNode) -> bool:
    def _helper(t: BinaryTreeNode) -> ExtremesPair:
        if t is None:
            return ExtremesPair(
                min=float("inf"),
                max=float("-inf"),
            )

        result_left = _helper(t.left)
        result_right = _helper(t.right)

        if result_left.max < t.data <= result_right.min:  # <= t.data
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

    return max_min.max is not float("inf")  # !=


def is_binary_tree_bst_1_b(tree: BinaryTreeNode) -> bool:
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
                t.left, lower_bdd=lower_bdd, upper_bdd=t.data
            ) and _are_keys_in_range(t.right, lower_bdd=t.data, upper_bdd=upper_bdd)

    return _are_keys_in_range(
        tree,
        lower_bdd=float("-inf"),
        upper_bdd=float("inf"),
    )


def is_binary_tree_bst_2_a(tree: BinaryTreeNode) -> bool:
    """
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


def is_binary_tree_bst_2_b(tree: BinaryTreeNode) -> bool:
    """
    time:  O(n)

    space: O(h)

    reference:
    https://www.geeksforgeeks.org/a-program-to-check-if-a-binary-tree-is-bst-or-not/
    """

    global prev
    prev = None

    def _helper(t: BinaryTreeNode) -> bool:

        global prev

        if t is None:
            return True

        if _helper(t.left) is False:
            return False

        if prev is not None and prev.data > t.data:
            return False

        prev = t

        return _helper(t.right)

    return _helper(tree)


def is_binary_tree_bst_2_c_1(tree: BinaryTreeNode) -> bool:
    """
    not yet working!

    when the recursion "arrives back" at the node holding 1,
    `prev` does NOT equal the expected (= the node holding 0) but instead equals `None`!

    reference:
    https://www.geeksforgeeks.org/a-program-to-check-if-a-binary-tree-is-bst-or-not/
        - the reference has two typos in its corresponding function
        - this file corrects both of the reference's typos
    """

    def _helper(
        t: BinaryTreeNode,
        prev: Optional[BinaryTreeNode] = None,
    ) -> bool:

        if t is None:
            return True

        a = _helper(t.left, prev)
        if a is False:  # corrects the reference's typo #1
            return False

        print(t.data)

        if prev is not None and prev.data > t.data:  # corrects the reference's typo #2
            return False

        prev = t

        b = _helper(t.right, prev)

        return b

    print()

    return _helper(tree, None)


OkPrevPair = collections.namedtuple(
    "OkPrevPair",
    ("ok", "prev"),
)


def is_binary_tree_bst_2_c_2(tree: BinaryTreeNode) -> bool:
    """
    not yet working!
    """

    def _helper(
        t: BinaryTreeNode,
        aux: Optional[OkPrevPair] = OkPrevPair(True, None),
    ) -> OkPrevPair:

        if aux.ok is False:
            return aux

        if t is None:
            return OkPrevPair(True, aux.prev)

        a = _helper(t.left, aux)
        if a.ok is False:
            return OkPrevPair(False, aux.prev)

        print(t.data)

        if a.prev is not None and a.prev.data > t.data:
            return OkPrevPair(False, aux.prev)

        b = _helper(t.right, OkPrevPair(True, t))

        return OkPrevPair(b.ok, t.right)

    return _helper(
        tree,
        OkPrevPair(True, None),
    ).ok


def is_binary_tree_bst_2_c_3(tree: BinaryTreeNode) -> bool:
    """
    a hacky way of "hacking" is_binary_tree_bst_2_c_1 into working as expected

    in fact, one can say that
    this implementation combines ideas from each of the following:
        - is_binary_tree_bst_2_b
        - is_binary_tree_bst_2_c_1
    (but that _actually_ defeats the point of trying to eliminate the global variable)
    """

    def _helper(
        t: BinaryTreeNode,
        prev_2_node={"prev": None},
    ) -> bool:

        if t is None:
            return True

        a = _helper(t.left, prev_2_node)
        if a is False:
            return False

        print(t.data)

        if prev_2_node["prev"] is not None and prev_2_node["prev"].data > t.data:
            return False

        prev_2_node["prev"] = t

        b = _helper(t.right, prev_2_node)

        return b

    print()

    return _helper(tree)


NodeBoundsTuple = collections.namedtuple(
    "NodeBoundsTuple",
    ("node", "lower", "upper"),
)


def is_binary_tree_bst_3(tree: BinaryTreeNode) -> bool:
    bfs_queue = collections.deque(
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
