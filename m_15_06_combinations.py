from typing import List


def combinations(n: int, k: int) -> List[List[int]]:
    """
    Generate all size-k subsets of {1, ..., n}.

    (I think we are intended to)
    Assume that `k <= n`.
    """

    size_k_subsets: List[List[int]] = []

    def _helper(
        next_value_to_select: int,
        selected_values: List[int],
    ) -> None:
        if len(selected_values) == k:
            size_k_subsets.append(selected_values)
            return
        elif len(selected_values) > k:
            return

        if next_value_to_select <= n:
            _helper(
                next_value_to_select + 1,
                selected_values,
            )

            _helper(
                next_value_to_select + 1,
                [next_value_to_select] + selected_values,
            )

    _helper(1, [])

    return size_k_subsets


def combinations_2(n: int, k: int) -> List[List[int]]:
    """
    Generate all size-k subsets of {1, ..., n}.

    (I think we are intended to)
    Assume that `k <= n`.
    """

    size_k_subsets: List[List[int]] = []

    def _guided_combinations(
        offset: int,
        partial_combination: List[int],
    ) -> None:
        if len(partial_combination) == k:
            size_k_subsets.append(partial_combination.copy())
            return

        # Generate remaining combinations over {offset, ..., n}
        # of size `num_remaining`.
        num_remaining = k - len(partial_combination)
        i = offset
        while i <= n and num_remaining <= n - i + 1:
            _guided_combinations(
                i + 1,
                partial_combination + [i],
            )
            i += 1

    _guided_combinations(1, [])

    return size_k_subsets


if __name__ == "__main__":
    size_k_subsets = combinations(2, 1)
    print(size_k_subsets)
