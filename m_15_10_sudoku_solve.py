import itertools
import math
from typing import List

from m_5_17_is_valid_sudoku import _EMPTY_CELL_CONTENT


def solve_sudoku(partial_assignment: List[List[int]]) -> bool:
    """
    `partial_assignment` represents a partial assignment of a 9-by-9 Sudoku board.

    Assume that each empty cell in `partial_assignment` holds the integer 0.

    TODO:
        (a) determine whether the input actually holds the integer 0 in its emtpy cells

        (b) determine whether the input is assumed to be valid

        (c) record, within this docstring, whether the input gets modified in-place

        (d) refactoring ideas

            (1) extract the computation of common values
                (including but not limited to `region_size` and `len(partial_assignment)`)
                to within the outermost function's scope
    """

    def _is_val_admissible_for_cell_at(
        i: int,
        j: int,
        val: int,
    ) -> bool:
        # Check column constraints.
        if val in (partial_assignment[k][j] for k in range(len(partial_assignment))):
            return False

        # Check row constraints.
        if val in partial_assignment[i]:
            return False

        # Check region constraints.
        region_size = int(
            math.sqrt(len(partial_assignment)),
        )
        I = i // region_size
        J = j // region_size

        return not any(
            val == partial_assignment[region_size * I + a][region_size * J + b]
            for a, b in itertools.product(range(region_size), repeat=2)
        )

    def _fill_in_the_cell_at(i: int, j: int) -> bool:
        if i == len(partial_assignment):
            # Start a new column.
            i = 0
            j += 1

            if j == len(partial_assignment[i]):
                # The entire matrix has been filled out without any violations
                # (i.e. in a valid way).
                return True

        # If the current cell has been filled in already,
        # proceed straight on to the next cell.
        if partial_assignment[i][j] != _EMPTY_CELL_CONTENT:
            return _fill_in_the_cell_at(i + 1, j)

        # Exhaust the possibilities for filling in the cell at (i, j).
        for value in range(1, len(partial_assignment) + 1):
            # There are 2 ways to check
            # whether assigning `value` at (i, j) leads to a valid configuration:
            #   (a) check all of the board's constraints
            #   (b) only check the constraints applicable to (i, j)
            # Option (b) is sufficient (and quicker to perform!),
            # because the only cell that can cause a problem is
            # the most-recently-filled-in one, i.e. the one at (i, j).
            if _is_val_admissible_for_cell_at(i, j, value):
                partial_assignment[i][j] = value
                if _fill_in_the_cell_at(i + 1, j):
                    return True

        # Undo whatever assignment was applied to (i, j).
        partial_assignment[i][j] = _EMPTY_CELL_CONTENT

        return False

    return _fill_in_the_cell_at(0, 0)
