from typing import List

from m_14_00_common import BstNode


def find_k_largest_in_bst_1(tree: BstNode, k: int) -> List[int]:
    # global greatest_values
    # fmt: off
    '''
    For some reason that I don't yet understand,
    the next statement causes a crash with
    ```
    SyntaxError: annotated name 'greatest_values' can't be global
    ```
    '''
    # fmt: on
    greatest_values: List[int] = []

    def _helper(t: BstNode, k) -> None:
        global greatest_values

        if len(greatest_values) == k:
            return

        if t:
            _helper(t.right, k)

            if greatest_values and greatest_values[-1] != t.data:
                greatest_values.append(t.data)

            _helper(t.left, k)

    _helper(tree, k)

    return greatest_values


def find_k_largest_in_bst_2(tree: BstNode, k: int) -> List[int]:
    def _helper(t: BstNode, k: int, greatest_vals: List[int]) -> None:

        if len(greatest_vals) == k:
            return

        if t:
            _helper(t.right, k, greatest_vals)

            # if greatest_vals and greatest_vals[-1] != t.data:
            # if not greatest_vals or (greatest_vals and greatest_vals[-1] != t.data):
            if not greatest_vals or (
                greatest_vals and len(greatest_vals) < k and greatest_vals[-1] != t.data
            ):
                greatest_vals.append(t.data)

            _helper(t.left, k, greatest_vals)

    greatest_values: List[int] = []
    _helper(tree, k, greatest_values)

    return greatest_values


def find_k_largest_in_bst_3(tree: BstNode, k: int) -> List[int]:
    k_greatest_values: List[int] = []

    def _helper(t: BstNode) -> None:
        if t and len(k_greatest_values) < k:
            _helper(t.right)

            if len(k_greatest_values) < k:
                k_greatest_values.append(t.data)

                _helper(t.left)

    _helper(tree)

    return k_greatest_values


if __name__ == "__main__":
    n_1 = BstNode(data=1)
    n_4 = BstNode(data=4)
    n_6 = BstNode(data=6)

    n_2 = BstNode(data=2, left=n_1)
    n_5 = BstNode(data=5, left=n_4, right=n_6)

    n_3 = BstNode(data=3, left=n_2, right=n_5)

    result = find_k_largest_in_bst_2(n_3, 2)
