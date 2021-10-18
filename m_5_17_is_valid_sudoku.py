import itertools

from typing import List, Iterable


def is_valid_sudoku(
    partial_assignment: List[List[int]],
) -> bool:
    # Check the rows.
    for row in partial_assignment:
        if not is_iterable_valid(row):
            return False

    # Check the columns.
    n_cols = len(partial_assignment)
    n_rows = len(partial_assignment[0])

    for col_idx in range(n_cols):
        column = (partial_assignment[r_idx][col_idx] for r_idx in range(n_rows))
        if not is_iterable_valid(column):
            return False

    # Check the subgrids.
    for r_ulc in range(0, n_rows, 3):
        for c_ulc in range(0, n_cols, 3):
            subgrid_flattened = itertools.chain.from_iterable(
                (
                    row[c_ulc : c_ulc + 3]
                    for row in partial_assignment[r_ulc : r_ulc + 3]
                ),
            )
            if not is_iterable_valid(subgrid_flattened):
                return False

    return True


def is_iterable_valid(numbers: Iterable[int]) -> bool:
    seen = set()
    for n in numbers:
        if n in seen and n != 0:
            return False
        seen.add(n)
    return True


if __name__ == "__main__":
    partial_assignment = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 5, 9, 8, 0, 2, 1],
        [0, 1, 0, 4, 0, 0, 9, 0, 3],
        [3, 0, 6, 7, 0, 0, 4, 0, 8],
        [8, 2, 0, 1, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 8, 4, 3, 0, 7, 0, 5, 0],
        [6, 9, 0, 0, 0, 0, 2, 0, 0],
        [1, 3, 0, 0, 0, 2, 8, 0, 7],
    ]

    is_valid = is_valid_sudoku(partial_assignment)  # should be True

    print("partial_assignment:")
    print(partial_assignment)
    print("is_valid:")
    print(is_valid)
