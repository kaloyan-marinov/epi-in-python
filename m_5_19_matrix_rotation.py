from typing import List


def rotate_matrix(square_matrix: List[List[int]]) -> None:
    square_matrix[:] = [list(row[::-1]) for row in zip(*square_matrix)]
