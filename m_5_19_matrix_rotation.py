from typing import List


def solution_1_rotate_matrix(square_matrix: List[List[int]]) -> None:
    square_matrix[:] = [list(row[::-1]) for row in zip(*square_matrix)]


def solution_2_rotate_matrix(square_matrix: List[List[int]]) -> None:
    n = len(square_matrix)

    for r in range((n + 1) // 2):
        for c in range(r, n - r):
            (
                square_matrix[r][c],
                square_matrix[c][-1 - r],
                square_matrix[-1 - r][-1 - c],
                square_matrix[-1 - c][r],
            ) = (
                square_matrix[c][-1 - r],
                square_matrix[-1 - r][-1 - c],
                square_matrix[-1 - c][r],
                square_matrix[r][c],
            )


if __name__ == "__main__":
    A = [
        [1, 2],
        [3, 4],
    ]

    solution_2_rotate_matrix(A)

    print(A)  # [[4, 3], [2, 1]] ( instead of the expected [[3, 1], [4, 2]] )
