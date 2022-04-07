from m_09_00_common import BinaryTreeNode as BasicBinaryTreeNode


class BinaryTreeNode(BasicBinaryTreeNode):
    def __init__(self, data=None, left=None, right=None):
        super().__init__(data=data, left=left, right=right)
        self.next = None


def construct_right_sibling(tree: BinaryTreeNode) -> None:
    def populate_children_next_field(start_node):
        while start_node and start_node.left:
            # Populate left child's next field.
            start_node.left.next = start_node.right

            # Populate right child's next field
            # if `start_node` is not the last node at the current level.
            start_node.right.next = start_node.next and start_node.next.left

            start_node = start_node.next

    while tree and tree.left:
        populate_children_next_field(tree)
        tree = tree.left


def construct_right_sibling(tree: BinaryTreeNode) -> None:
    """
    refactor the previous commit's solution in a less mysterious way
    """

    def _process_nodes_at_same_level(start_node):
        """
        Process nodes at the level below `start_node`, from left to right.
        """

        n = start_node

        while n and n.left:
            # Populate left child's next field.
            n.left.next = n.right

            # Populate right child's next field
            # if `n` is not the last node at the current level.
            if n.next:
                n.right.next = n.next.left
            else:
                n.right.next = None

            n = n.next

    while tree and tree.left:  # iterates tree-level by tree-level
        _process_nodes_at_same_level(tree)
        tree = tree.left
