from typing import Dict, Tuple

import functools


def number_of_ways(n: int, m: int) -> int:
    # Must add `functools.lru_cache(None)` here!
    def _helper(rows: int, cols: int) -> int:
        if rows == 1 or cols == 1:
            return 1

        return _helper(rows - 1, cols) + _helper(rows, cols - 1)

    return _helper(n, m)


def number_of_ways_2(n: int, m: int) -> int:
    input_2_result: Dict[Tuple[int, int], int] = {}

    def _helper(rows: int, cols: int) -> int:
        if rows == 1 or cols == 1:
            return 1

        # aa := _helper(rows - 1, cols)
        input_tuple = (rows - 1, cols)
        if input_tuple in input_2_result:
            aa = input_2_result[input_tuple]
        elif input_tuple[::-1] in input_2_result:
            aa = input_2_result[input_tuple[::-1]]
        else:
            aa = _helper(*input_tuple)
            input_2_result[input_tuple] = aa

        # bb := _helper(rows, cols - 1)
        input_tuple = (rows, cols - 1)
        if input_tuple in input_2_result:
            bb = input_2_result[input_tuple]
        elif input_tuple[::-1] in input_2_result:
            bb = input_2_result[input_tuple[::-1]]
        else:
            bb = _helper(*input_tuple)
            input_2_result[input_tuple] = bb

        return aa + bb

    return _helper(n, m)


def number_of_ways(n: int, m: int) -> int:
    """
    (n, m) represents the dimensions of a 2D array.
    """

    @functools.lru_cache(None)
    def _num_ways_to_xy(x: int, y: int) -> int:
        """
        (x, y) represents a location/cell within an n-by-m 2D array.
        """
        if x == 0 and y == 0:
            return 1

        ways_top = 0 if x == 0 else _num_ways_to_xy(x - 1, y)
        ways_left = 0 if y == 0 else _num_ways_to_xy(x, y - 1)

        return ways_top + ways_left

    return _num_ways_to_xy(n - 1, m - 1)
