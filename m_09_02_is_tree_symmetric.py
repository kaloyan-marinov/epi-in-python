import collections

from m_9_00_common import BinaryTreeNode


def is_symmetric(tree: BinaryTreeNode) -> bool:
    def _check_symmetric(tree):
        if not tree:
            return True

        is_left_symmetric = _check_symmetric(tree.left)
        if not is_left_symmetric:
            return False

        is_right_symmetric = _check_symmetric(tree.right)
        if not is_right_symmetric:
            return False

        return is_left_symmetric and is_right_symmetric

    return _check_symmetric(tree)


def is_symmetric(tree: BinaryTreeNode) -> bool:
    SymmetricValuePair = collections.namedtuple(
        "SymmetricValuePair",
        ("symmetric", "value"),
    )

    def _check_symmetric(tree):
        if not tree:
            return SymmetricValuePair(
                symmetric=True,
                value=None,
            )

        left_s_v_p = _check_symmetric(tree.left)
        if not left_s_v_p.symmetric:
            return left_s_v_p

        right_s_v_p = _check_symmetric(tree.right)
        if not right_s_v_p.symmetric:
            return right_s_v_p

        return SymmetricValuePair(
            symmetric=left_s_v_p.value == right_s_v_p.value,
            value=tree.data,
        )

    return _check_symmetric(tree).symmetric


def is_symmetric(tree: BinaryTreeNode) -> bool:
    def _check_symmetric(left_subtree, right_subtree):
        if not left_subtree and not right_subtree:
            return True
        elif (not left_subtree and right_subtree) or (
            left_subtree and not right_subtree
        ):  # One subtree is empty, but the other one is not.
            return False
        else:  # Neither subtree is empty.
            roots_match = left_subtree.data == right_subtree.data
            if not roots_match:
                return False

            outer_subtrees_match = _check_symmetric(
                left_subtree.left, right_subtree.right
            )
            if not outer_subtrees_match:
                return False

            inner_subtrees_match = _check_symmetric(
                left_subtree.right, right_subtree.left
            )

            return inner_subtrees_match

    return not tree or _check_symmetric(tree.left, tree.right)


if __name__ == "__main__":
    D = BinaryTreeNode(data=3)
    G = BinaryTreeNode(data=1)

    C = BinaryTreeNode(data=561, right=D)
    F = BinaryTreeNode(data=2, left=G)

    B = BinaryTreeNode(data=6, right=C)
    E = BinaryTreeNode(data=6, left=F)

    A = BinaryTreeNode(data=314, left=B, right=E)

    print(is_symmetric(A))
