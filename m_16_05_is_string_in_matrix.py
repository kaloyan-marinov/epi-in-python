import functools
from typing import List, Optional


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
        #   or the current match attempt fails.
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
