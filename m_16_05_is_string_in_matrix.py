import functools
from typing import List, Optional, Tuple


# def is_pattern_contained_in_grid(
#     grid: List[List[int]],
#     pattern: List[int],
# ) -> bool:
#     start_loc = {"i": None, "j": None}
#     global final_loc
#     final_loc = {"i": None, "j": None}

#     # fmt: off
#     '''
#     def _helper(i: int, j: int, p_idx: int) -> Tuple[int, int]:
#     '''
#     # fmt: on
#     def _helper(p_idx: int) -> bool:
#         global final_loc

#         if p_idx >= len(pattern):
#             return True

#         if p_idx == 0:
#             for row in range(len(grid)):
#                 for col in range(len(grid[0])):
#                     if grid[row][col] == pattern[p_idx]:
#                         start_loc = {"i": row, "j": col}
#                         final_loc = {"i": row, "j": col}

#                         is_next_available = _helper(p_idx + 1)
#                         return is_next_available

#         i= final_loc['i']
#         j = final_loc['j']
#         if i - 1 >= 0 and grid[i - 1][j] == pattern[p_idx]:

#         above = grid[i - 1][j]
#         below =
#         left =
#         right =


def is_pattern_contained_in_grid(
    grid: List[List[int]],
    pattern: List[int],
) -> bool:
    def _helper(
        p_idx: int,
        row: Optional[int] = None,
        col: Optional[int] = None,
    ) -> bool:

        if p_idx >= len(pattern):
            return True

        if row is None and col is None:  # i.e. `p_idx == 0`
            for ii in range(len(grid)):
                for jj in range(len(grid[0])):

                    if grid[ii][jj] == pattern[p_idx]:
                        is_next_available = _helper(p_idx + 1, row=ii, col=jj)
                        return is_next_available

        # TODO: change the remaining `if`s to `elif`s

        # Now, it is known/guaranteed that `p_idx > 0`.
        elif row - 1 >= 0 and grid[row - 1][col] == pattern[p_idx]:
            return _helper(p_idx + 1, row=row - 1, col=col)

        elif row + 1 <= len(grid) - 1 and grid[row + 1][col] == pattern[p_idx]:
            return _helper(p_idx + 1, row=row + 1, col=col)

        elif col - 1 >= 0 and grid[row][col - 1] == pattern[p_idx]:
            return _helper(p_idx + 1, row=row, col=col - 1)

        elif col + 1 <= len(grid[0]) - 1 and grid[row][col + 1] == pattern[p_idx]:
            return _helper(p_idx + 1, row=row, col=col + 1)

    return _helper(0)


def is_pattern_contained_in_grid(
    grid: List[List[int]],
    pattern: List[int],
) -> bool:
    @functools.lru_cache(maxsize=None)
    def _search_pattern_suffix_starting_at_xy(
        x: int,
        y: int,
        p_idx: int,
    ) -> bool:
        if len(pattern) == p_idx:
            # All of `pattern` has been found/matched, so:
            return True

        # "Return early"
        #   if (x, y) lies outside the `grid`
        #   or the current match attempt fails
        #   or we have already tried this [cell].
        # fmt: off
        if (
            not (
                0 <= x < len(grid)
                and 0 <= y < len(grid[x])
            ) or grid[x][y] != pattern[p_idx]
        ):
            return False
        # fmt: on

        return any(
            _search_pattern_suffix_starting_at_xy(
                adjacent_cell[0], adjacent_cell[1], p_idx + 1
            )
            for adjacent_cell in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1))
        )

    return any(
        _search_pattern_suffix_starting_at_xy(i, j, 0)
        for i in range(len(grid))
        for j in range(len(grid[i]))
    )


if __name__ == "__main__":
    grid = [[21, 7, 7], [7, 7, 7], [9, 21, 25]]
    pattern = [7, 7, 9]

    result = is_pattern_contained_in_grid(grid, pattern)
    print(result)
