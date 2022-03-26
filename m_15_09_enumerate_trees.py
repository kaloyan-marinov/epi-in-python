from typing import Optional, List

from m_9_00_common import BinaryTreeNode


def generate_all_binary_trees(num_nodes: int) -> List[Optional[BinaryTreeNode]]:
    def _helper(
        size: int,
    ) -> List[BinaryTreeNode]:
        if size == 0:
            return [None]

        trees: List[Optional[BinaryTreeNode]] = []

        for left_size in range(size):
            left_subtrees = _helper(left_size)
            right_subtrees = _helper(
                size - 1 - left_size
            )  # "-1" accounts for the root!

            for l in left_subtrees:
                for r in right_subtrees:
                    trees.append(BinaryTreeNode(left=l, right=r))

        return trees

    return _helper(num_nodes)


def generate_all_binary_trees_2(num_nodes: int) -> List[Optional[BinaryTreeNode]]:
    if num_nodes == 0:
        # Empty tree - add as `None`.
        return [None]

    result: List[Optional[BinaryTreeNode]] = []
    for left_subtree_size in range(num_nodes):
        right_subtree_size = (num_nodes - 1) - left_subtree_size

        left_subtrees = generate_all_binary_trees_2(left_subtree_size)
        right_subtrees = generate_all_binary_trees_2(right_subtree_size)

        result += [
            BinaryTreeNode(left=l, right=r)
            for l in left_subtrees
            for r in right_subtrees
        ]

    return result


if __name__ == "__main__":
    result = generate_all_binary_trees(1)

    print(result)
