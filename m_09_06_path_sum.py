from m_09_00_common import BinaryTreeNode


def has_path_sum(tree: BinaryTreeNode, remaining_weight: int) -> bool:
    found = False

    def _helper(t, x: int) -> bool:
        nonlocal found

        if found:
            return True

        x += t.data

        if not t.left and not t.right:
            found = x == remaining_weight

        _helper(t.left, x)
        _helper(t.right, x)

    return _helper(tree, 0)
