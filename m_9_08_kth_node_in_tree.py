from m_9_00_common import BinaryTreeNode as BasicBinaryTreeNode


class BinaryTreeNode(BasicBinaryTreeNode):
    def __init__(self, data=None, left=None, right=None, size=None):
        super().__init__(data=data, left=left, right=right)
        self.size = size


def find_kth_node_in_tree(tree: BinaryTreeNode, k: int) -> Optional[BinaryTreeNode]:
    while tree:
        left_size = tree.left.size if tree.left else 0

        if left_size == k - 1:
            # The k-th node is `tree` itself.
            return tree
        elif left_size < k - 1:
            # The k-th node must be in the right subtree.
            k -= left_size + 1
            tree = tree.right
        else:
            # The k-th node must be in the left subtree.
            tree = tree.left

    # If k is between 1 and the tree size, this is unreachable.
    return None
