import collections
from typing import Deque, List, Set, Tuple, Literal


def fill_surrounded_regions(
    board: List[List[Literal["W", "B"]]],
) -> None:
    """
    (Assuming that `board` is rectangle-shaped,)
    Replace each 'W', which cannot reach the boundary, with a 'B'.
    """

    n_rows = len(board)
    n_cols = len(board[0])

    white_cells_that_can_reach_the_boundary: Set[Tuple[int, int]] = set()

    q: Deque[Tuple[int, int]] = collections.deque(
        [(0, col) for col in range(n_cols)]
        + [(row, 0) for row in range(1, n_rows - 1)]
        + [(row, n_cols - 1) for row in range(1, n_rows - 1)]
        + [(n_rows - 1, col) for col in range(n_cols)]
    )

    while q:
        x, y = q.popleft()

        if board[x][y] == "W":
            white_cells_that_can_reach_the_boundary.add((x, y))

            for next_x, next_y in (
                (x + 1, y),
                (x - 1, y),
                (x, y + 1),
                (x, y - 1),
            ):
                if (
                    0 <= next_x < n_rows
                    and 0 <= next_y < n_cols
                    and (next_x, next_y) not in white_cells_that_can_reach_the_boundary
                    and board[next_x][next_y] == "W"
                ):
                    q.append((next_x, next_y))

    for row in range(n_rows):
        for col in range(n_cols):
            if (row, col) not in white_cells_that_can_reach_the_boundary:
                board[row][col] = "B"


def fill_surrounded_regions_v2(
    board: List[List[Literal["W", "B"]]],
) -> None:
    """
    (Assuming that `board` is rectangle-shaped,)
    Replace each 'W', which cannot reach the boundary, with a 'B'.
    """
    n_rows = len(board)
    n_cols = len(board[0])

    q: Deque[Tuple[int, int]] = collections.deque(
        [(0, col) for col in range(n_cols)]
        + [(row, 0) for row in range(1, n_rows - 1)]
        + [(row, n_cols - 1) for row in range(1, n_rows - 1)]
        + [(n_rows - 1, col) for col in range(n_cols)]
    )

    while q:
        x, y = q.popleft()

        if 0 <= x < n_rows and 0 <= y < n_cols and board[x][y] == "W":
            # The following statement,
            # while inconsistent with the type annotation of this function's input,
            # represents a clever way of introducing and utilizing a Temporary color.
            board[x][y] = "T"

            q.extend(
                [
                    (x - 1, y),
                    (x + 1, y),
                    (x, y - 1),
                    (x, y + 1),
                ]
            )

    # fmt: off
    board[:] = [
        ["W" if c == "T" else "B" for c in row]
        for row in board
    ]
    # fmt: on


if __name__ == "__main__":
    board = [
        ["W", "W", "W", "W", "B", "W", "W", "B", "B", "W"],
        ["B", "W", "W", "B", "W", "B", "W", "B", "B", "W"],
        ["B", "W", "W", "W", "B", "B", "B", "B", "B", "W"],
        ["B", "B", "B", "B", "W", "B", "W", "B", "W", "B"],
        ["W", "W", "B", "B", "W", "B", "B", "W", "B", "B"],
        ["W", "W", "W", "B", "B", "B", "B", "W", "W", "W"],
        ["B", "B", "W", "B", "W", "B", "B", "W", "W", "B"],
        ["B", "W", "W", "W", "B", "W", "B", "W", "B", "W"],
        ["W", "W", "W", "W", "B", "W", "W", "W", "B", "B"],
        ["W", "W", "W", "W", "B", "B", "W", "B", "B", "B"],
        ["B", "B", "W", "B", "B", "B", "W", "B", "W", "B"],
        ["B", "W", "W", "B", "B", "B", "W", "W", "B", "B"],
        ["B", "B", "W", "B", "W", "W", "B", "W", "W", "B"],
        ["B", "B", "B", "W", "B", "B", "B", "B", "W", "W"],
        ["W", "B", "W", "B", "B", "B", "W", "B", "B", "B"],
    ]

    print()
    for row in board:
        print(row)

    fill_surrounded_regions(board)

    print()
    for row in board:
        print(row)
