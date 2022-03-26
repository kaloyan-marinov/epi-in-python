from typing import List


def n_queens(n: int) -> List[List[int]]:
    result: List[List[int]] = []
    # Here, a Python sequence is used to _emulate_ a Python dictionary.
    row_2_col_placement: List[int] = [0] * n

    def _place_next_queen(row: int) -> None:
        """
        Help by placing the next queen
        - within the `row`-th row.
        """

        if row == n:
            # All queens [have been] legally placed.
            # (We add a copy since subsequent calls modify `row_2_col_placement`.)
            result.append(row_2_col_placement.copy())
            return

        for col in range(n):
            # Test if placing the `row`-th queen at `(row, col)`
            # would confict with any of the earlier-placed queens.
            if all(
                abs(col - c)
                not in (
                    0,
                    row - r,
                )  # equivalent to `abs(col - c) != 0 and abs(col - c) != row - r`
                for r, c in enumerate(row_2_col_placement[:row])
            ):
                row_2_col_placement[row] = col
                _place_next_queen(row + 1)

    _place_next_queen(0)

    return result
