from m_09_00_common import BinaryTreeNode


def sum_root_to_leaf_1(tree: BinaryTreeNode) -> int:
    s = 0
    x = 0

    def _accumulate(t: BinaryTreeNode) -> None:
        nonlocal s
        nonlocal x

        if t is None:
            s += x
            x <<= 1

        x <<= 1
        x |= t.data

        _accumulate(t.left)

        _accumulate(t.right)

    _accumulate(tree)

    return s


# fmt: off
'''
def sum_root_to_leaf_2(tree: BinaryTreeNode) -> int:
    s = 0
    x = 0

    def _accumulate(t: BinaryTreeNode) -> None:
        nonlocal s
        nonlocal x

        if not t:
            return

        x <<= 1
        x |= t.data

        if not t.left and not t.right:
            s += x
            x >>= 1
            return

        _accumulate(t.left)

        _accumulate(t.right)

    _accumulate(tree)

    return s
'''
# fmt: on
def sum_root_to_leaf_2(tree: BinaryTreeNode) -> int:
    s = 0

    def _accumulate(t: BinaryTreeNode, x) -> None:
        nonlocal s

        if not t:
            return

        x <<= 1
        x |= t.data

        if not t.left and not t.right:
            s += x
            return

        _accumulate(t.left, x)

        _accumulate(t.right, x)

    _accumulate(tree, 0)

    return s


def sum_root_to_leaf(tree: BinaryTreeNode) -> int:
    def _helper(t, running_sum=0):
        if not t:
            return 0

        running_sum = running_sum * 2 + t.data

        if not t.left and not t.right:  # Leaf.
            return running_sum

        # Not a leaf.
        return _helper(t.left, running_sum=running_sum) + _helper(
            t.right, running_sum=running_sum
        )

    s = _helper(tree, running_sum=0)

    return s


if __name__ == "__main__":
    D = BinaryTreeNode(data=0)
    E = BinaryTreeNode(data=1)

    H = BinaryTreeNode(data=0)

    M = BinaryTreeNode(data=1)
    N = BinaryTreeNode(data=0)

    P = BinaryTreeNode(data=0)

    C = BinaryTreeNode(data=0, left=D, right=E)

    G = BinaryTreeNode(data=1, left=H)
    F = BinaryTreeNode(data=1, right=G)

    L = BinaryTreeNode(data=1, right=M)
    K = BinaryTreeNode(data=0, left=L, right=N)

    O = BinaryTreeNode(data=0, right=P)

    J = BinaryTreeNode(data=0, right=K)

    B = BinaryTreeNode(data=0, left=C, right=F)

    I = BinaryTreeNode(data=1, left=J, right=O)

    A = BinaryTreeNode(data=1, left=B, right=I)

    s = sum_root_to_leaf_2(A)
    print(s)
