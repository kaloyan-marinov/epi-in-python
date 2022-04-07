class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTreeNodeWithParent(BinaryTreeNode):
    def __init__(self, data=None, left=None, right=None, parent=None):
        super().__init__(data=data, left=left, right=right)
        self.parent = parent
