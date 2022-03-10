from typing import Optional, List

from m_14_00_common import BstNode


def find_first_greater_than_k_1(tree: BstNode, k: int) -> Optional[BstNode]:
    """
    time:  O(n)

    space: O(n)
    """

    def _helper(t: BstNode, values: List[BstNode]) -> None:
        if t:
            _helper(t.left, values)

            values.append(t)

            _helper(t.right, values)

    nodes: List[BstNode] = []
    _helper(tree, nodes)

    for n in nodes:
        if n.data > k:
            return n
    # ... is equivalent to the following commented-out block:
    # fmt: off
    '''
    idx = bisect.bisect([n.data for n in nodes], k)
    if idx < len(nodes):
        return nodes[idx]
    '''
    # fmt: on


def find_first_greater_than_k_2(tree: BstNode, k: int) -> Optional[BstNode]:
    """
    time:  O(n)

    space: O(h)
    """

    prev = None
    node = None

    def _helper(t: BstNode, k: int) -> None:

        nonlocal prev
        nonlocal node

        if node:
            return

        if t:
            _helper(t.left, k)

            if prev and t.data > k >= prev.data:
                node = t

            prev = t

            _helper(t.right, k)

    _helper(tree, k)

    return node


def find_first_greater_than_k_3(tree: BstNode, k: int) -> Optional[BstNode]:
    """
    time:  O(h)

    space: O(1)
    """
    curr_node = tree
    candidate_for_first_node = None

    while curr_node:
        if curr_node.data > k:
            candidate_for_first_node = curr_node
            curr_node = curr_node.left
        else:  # i.e. `curr_node` and all nodes in its left subtree have keys that are <= k
            curr_node = curr_node.right

    return candidate_for_first_node


if __name__ == "__main__":
    n_1 = BstNode(data=1)
    n_6 = BstNode(data=6)
    n_10 = BstNode(data=10)

    n_5 = BstNode(data=5, left=n_1, right=n_6)
    n_14 = BstNode(data=14, left=n_10)

    n_7 = BstNode(data=7, left=n_5, right=n_14)

    result = find_first_greater_than_k_2(n_7, 3)

    print(result.data if result else None)
