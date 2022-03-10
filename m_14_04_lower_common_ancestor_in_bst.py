from typing import Optional

from m_14_00_common import BstNode


def find_lca_1(tree: BstNode, s: BstNode, b: BstNode) -> Optional[BstNode]:
    """
    Assume that:
        - all the nodes in `tree` have distinct keys
        - the input nodes are nonempty
        - the input nodes are part of the `tree`
    """

    # Ensure that `s.data < b.data`.
    # (The following ensures that,
    # since the keys have already been assumed to be pairwise distinct.)
    if s.data > b.data:
        s, b = b, s

    while tree and (b.data < tree.data or tree.data < s.data):
        if b.data < tree.data:
            tree = tree.left
        elif tree.data < s.data:
            tree = tree.right

    return tree


def find_lca_2(tree: BstNode, s: BstNode, b: BstNode) -> Optional[BstNode]:
    """
    Assume that:
        - all the nodes in `tree` have distinct keys
        - the input nodes are nonempty
        - the input nodes are part of the `tree`
        - `s.data < b.data` (since the keys have already been assumed to be pairwise distinct)
    """

    while tree.data < s.data or b.data < tree.data:
        # Keep searching since `tree` is outside [s, b].

        while tree.data < s.data:  # this can be converted into an `if` statement
            # LCA must be in `tree`'s right subtree.
            tree = tree.right

        while b.data < tree.data:  # this can be converted into an `if` statement
            # LCA must be in `tree`'s left subtree.
            tree = tree.left

    # Now, `s.data <= tree.data and tree.data <= b.data`.
    return tree


if __name__ == "__main__":
    # fmt: off
    '''
    The following example demonstrates that
    each of the `<=` operators has to be replaced by `<`.
    '''
    # fmt: on

    n_1 = BstNode(data=1)
    # null
    n_4 = BstNode(data=4)
    n_6 = BstNode(data=6)

    n_2 = BstNode(data=2, left=n_1)
    n_5 = BstNode(data=5, left=n_4, right=n_6)

    n_3 = BstNode(data=3, left=n_2, right=n_5)

    tree = n_3
    s = n_1
    b = n_2
    result = find_lca_1(n_3, s, b)
    print(result.data)
