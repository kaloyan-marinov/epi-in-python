import collections
from typing import Deque, List, Set, Tuple


def fill_surrounded_regions(
    board: List[List[str]],  # change to `List[List[Literal['W', 'B']]]`
) -> None:
    """
    (Assuming that `board` is rectangle-shaped,)
    Replace each 'W' that cannot reach the boundary with a 'B'.
    """

    n_rows = len(board)
    n_cols = len(board[0])

    white_cells_that_can_reach_the_boundary: Set[Tuple[int, int]] = set()

    # fmt: off
    '''
    q: Deque[Tuple[int, int]] = collections.deque(
        board[0]
        + [board[row][0] for row in range(1, n_rows - 1)]
        + [board[row][n_cols - 1] for row in range(1, n_rows - 1)]
        + board[n_rows - 1]
    )
    '''
    # fmt: on
    q: Deque[Tuple[int, int]] = collections.deque(
        [(0, col) for col in range(n_cols)]
        + [(row, 0) for row in range(1, n_rows - 1)]
        + [(row, n_cols - 1) for row in range(1, n_rows - 1)]
        + [(n_rows - 1, col) for col in range(n_cols)]
    )

    while q:
        x, y = q.popleft()

        if board[x][y] == "W":
            # fmt: off
            '''
            white_cells_that_can_reach_the_boundary.append((x, y))
            '''
            # fmt: on
            white_cells_that_can_reach_the_boundary.add((x, y))

            for next_x, next_y in (
                (x + 1, y),
                (x - 1, y),
                (x, y + 1),
                (x, y - 1),
            ):
                # fmt: off
                '''
                if (
                    0 <= next_x < n_rows
                    and 0 <= next_y < n_cols
                    and board[next_x][next_y] == "W"
                ):
                '''
                # fmt: on
                if (
                    0 <= next_x < n_rows
                    and 0 <= next_y < n_cols
                    and (next_x, next_y) not in white_cells_that_can_reach_the_boundary
                    and board[next_x][next_y] == "W"
                ):
                    q.append((next_x, next_y))

        # print(len(q))

    for row in range(n_rows):
        for col in range(n_cols):
            # fmt: off
            '''
            if (row, col) in white_cells_that_can_reach_the_boundary:
            '''
            # fmt: on
            if (row, col) not in white_cells_that_can_reach_the_boundary:
                board[row][col] = "B"


def fill_surrounded_regions_v2(
    board: List[List[str]],  # change to `List[List[Literal['W', 'B']]]`
) -> None:
    """
    (Assuming that `board` is rectangle-shaped,)
    Replace each 'W' that cannot reach the boundary with a 'B'.
    """
    n_rows = len(board)
    n_cols = len(board[0])

    # fmt: off
    q = collections.deque(
        [
            (i, j)
            for k in range(n_rows)
            for i, j in ((k, 0), (k, n_cols - 1))
        ] + [
            (i, j)
            for k in range(n_cols)
            for i, j in ((0, k), (n_rows - 1, k))
        ]
    )
    # fmt: on

    while q:
        x, y = q.popleft()

        if 0 <= x < n_rows and 0 <= y < n_cols and board[x][y] == "W":
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
        ["B" if c != "T" else "W" for c in row]
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
