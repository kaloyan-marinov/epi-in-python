import collections

from m_9_00_common import BinaryTreeNode


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    BalancedHeightPair = collections.namedtuple(
        "BalancedHeightPair",
        ("balanced", "height"),
    )

    def _check_balanced(tree):
        if not tree:
            return BalancedHeightPair(balanced=True, height=-1)

        left_b_h_p = _check_balanced(tree.left)
        if not left_b_h_p.balanced:
            return left_b_h_p

        right_b_h_p = _check_balanced(tree.right)
        if not right_b_h_p.balanced:
            return right_b_h_p

        return BalancedHeightPair(
            balanced=abs(left_b_h_p.height - right_b_h_p.height) <= 1,
            height=max(left_b_h_p.height, right_b_h_p.height) + 1,
        )

    return _check_balanced(tree).balanced
