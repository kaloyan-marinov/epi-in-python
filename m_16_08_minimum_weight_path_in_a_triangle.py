from typing import List


def minimum_path_weight(triangle: List[List[int]]) -> int:
    global min_weight
    min_weight = float("inf")

    # TODO: add decorator
    def _helper(level: int, idx: int, weight: int) -> None:
        global min_weight

        if level == len(triangle):  # TODO: replace with `len(triangle) - 1`
            min_weight = min(
                min_weight,
                weight + triangle[level][idx],
            )
            return

        _helper(level + 1, idx, weight + triangle[level][idx])

        _helper(level + 1, idx + 1, weight + triangle[level][idx])

    # TODO: replace with `if triangle: ... else: ...`
    _helper(0, 0, 0)

    return min_weight


def minimum_path_weight(triangle: List[List[int]]) -> int:
    # fmt: off
    '''
    def _path_weight(target_level: int, target_idx: int) -> int:
        if target_level == 0:
            return triangle[0][0]

        return (
            min(
                _path_weight(target_level - 1, target_idx),
                _path_weight(target_level - 1, target_idx - 1),
            )
            if target_idx < target_level
            else _path_weight(target_level - 1, target_idx - 1)
        )

    return min(_path_weight(len(triangle), idx) for idx in range(len(triangle)))
    '''
    # fmt: on
    # TODO: add decorator
    def _min_path_weight_to_xy(target_level: int, target_idx: int) -> int:
        if target_level == 0:
            return triangle[0][0]

        # TODO: handle _both_ edge cases separately!
        if target_idx == 0:
            prefix_weight = _min_path_weight_to_xy(target_level - 1, target_idx)
        elif target_idx == target_level:
            prefix_weight = _min_path_weight_to_xy(target_level - 1, target_idx - 1)
        else:
            prefix_weight = min(
                _min_path_weight_to_xy(target_level - 1, target_idx),
                _min_path_weight_to_xy(target_level - 1, target_idx - 1),
            )

        return prefix_weight + triangle[target_level][target_idx]

    # TODO: special-case the handling of an empty triangle!
    return (
        min(
            _min_path_weight_to_xy(len(triangle) - 1, idx)
            for idx in range(len(triangle))
        )
        if triangle
        else 0
    )


def minimum_path_weight(triangle: List[List[int]]) -> int:
    min_weights_to_curr_row: List[int] = [0]

    for curr_row in triangle:
        min_weights_to_curr_row = [
            curr_row[idx]
            + min(
                min_weights_to_curr_row[max(idx - 1, 0)],
                min_weights_to_curr_row[min(idx, len(min_weights_to_curr_row) - 1)],
            )
            for idx in range(len(curr_row))
        ]

    return min(min_weights_to_curr_row)


def minimum_path_weight(triangle: List[List[int]]) -> int:

    # fmt: off
    '''
    n = len(triangle)

    if n == 0:
        return 0

    min_weights_to_prev_row = [triangle[0][0]]

    for i in range(1, n):

        min_weights_to_curr_row = [
            min_weights_to_prev_row[0] + triangle[i][0]
        ] + [
            min(
                min_weights_to_prev_row[i - 1], # i >> idx
                min_weights_to_prev_row[i], # i >> idx
            ) + triangle[i][idx]
            #for idx in range(1, n - 1)
            for idx in range(1, i - 1)  # i - 1 >> i
        ] + [
            min_weights_to_prev_row[-1] + triangle[i][-1]
        ]

        min_weights_to_prev_row = min_weights_to_curr_row

    return min(min_weights_to_curr_row)
    '''
    # fmt: on

    n = len(triangle)

    if n == 0:
        return 0

    min_weights_to_curr_row = [triangle[0][0]]

    for i in range(1, n):

        min_weights_to_prev_row = min_weights_to_curr_row

        min_weights_to_curr_row = [min_weights_to_prev_row[0] + triangle[i][0]]

        for idx in range(1, i):

            min_weights_to_curr_row.append(
                min(
                    min_weights_to_prev_row[idx - 1],
                    min_weights_to_prev_row[idx],
                )
                + triangle[i][idx]
                # for idx in range(1, n - 1)
            )

        min_weights_to_curr_row.append(min_weights_to_prev_row[-1] + triangle[i][-1])

    return min(min_weights_to_curr_row)


if __name__ == "__main__":
    triangle = [[0]]
    result = minimum_path_weight(triangle)
    print(result)
