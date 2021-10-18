import itertools

from typing import List, Iterable


def is_valid_sudoku(
    partial_assignment: List[List[int]],
) -> bool:
    # rows
    for row in partial_assignment:
        if not is_list_valid(row):
            return False

    # columns
    n_cols = len(partial_assignment)
    n_rows = len(partial_assignment[0])

    for col_idx in range(n_cols):
        column = (partial_assignment[r_idx][col_idx] for r_idx in range(n_rows))
        if not is_list_valid(column):
            return False

    # subgrids
    for r_ulc in range(0, n_rows, 3):
        for c_ulc in range(0, n_cols, 3):
            subgrid_flattened = itertools.chain.from_iterable(
                (
                    row[c_ulc : c_ulc + 3 + 1]
                    for row in partial_assignment[r_ulc : r_ulc + 3 + 1]
                ),
            )
            if not is_list_valid(subgrid_flattened):
                return False

    return True


def is_list_valid(numbers: Iterable[int]) -> bool:
    seen = set()
    for n in numbers:
        if n in seen and n != 0:
            return False
        seen.add(n)
    return True
