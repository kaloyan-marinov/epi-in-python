from typing import List


def generate_pascal_triangle(n: int) -> List[List[int]]:
    """
    Return the first `n` rows of Pascal's triangle.
    """

    if n == 0:
        return []

    rows = [[1]]
    if n == 1:
        return rows

    rows.append([1, 1])

    for new_r_idx in range(2, n):
        prev_row = rows[new_r_idx - 1]  # rows[-1]
        new_row = (
            [1]
            + [prev_row[i] + prev_row[i + 1] for i in range(len(prev_row) - 1)]
            + [1]
        )
        rows.append(new_row)

    return rows


def generate_pascal_triangle(n: int) -> List[List[int]]:
    """
    Return the first `n` rows of Pascal's triangle.
    """

    rows: List[int] = [[1] * (i + 1) for i in range(n)]

    for i in range(n):
        for j in range(1, i):
            rows[i][j] = rows[i - 1][j - 1] + rows[i - 1][j]

    return rows
