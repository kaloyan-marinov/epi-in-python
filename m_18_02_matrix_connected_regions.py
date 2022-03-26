from typing import DefaultDict, Deque, Dict, List, Optional, Set, Tuple


def flip_color(
    x: int,
    y: int,
    image: List[List[int]],  # change `int` to `bool` (or to `Literal[0, 1]`)
) -> None:
    """
    Flip the values/colors of the connected component of the `image`,
    which component contains `(x ,y)`.
    """
    # Model the connected component of the `image`,
    # which component contains `(x, y)`, as a graph.
    adj: DefaultDict[
        Tuple[int, int],
        Set[Tuple[int, int]],
    ] = {}  # change to `collections.defaultdict(set)`

    m = len(image)
    for i in range(m):
        n = len(image[i])
        for j in range(n):

            v_i_j = (i, j)

            if i - 1 >= 0 and image[i - 1][j] == image[i][j]:
                adj[v_i_j].append((i - 1, j))  # change to `.add`

            if i + 1 <= m - 1 and image[i + 1][j] == image[i][j]:
                adj[v_i_j].append((i + 1, j))  # change to `.add`

            if j - 1 >= 0 and image[i][j - 1] == image[i][j]:
                adj[v_i_j].append((i, j - 1))  # change to `.add`

            if j + 1 <= n - 1 and image[i][j + 1] == image[i][j]:
                adj[v_i_j].append((i, j + 1))  # change to `.add`

    # Perform a BFS traversal starting at `(x, y)`.
    def _bfs_visit(
        s: Tuple[int, int]
    ) -> Dict[Tuple[int, int], Optional[Tuple[int, int]]]:
        vertex_2_parent: Dict[
            Tuple[int, int],
            Optional[Tuple[int, int]],
        ] = {(x, y): None}

        frontier = [s]

        while frontier:
            next_frontier = []

            for u in frontier:
                for v in adj[u]:
                    if v not in vertex_2_parent:
                        vertex_2_parent[v] = u
                        next_frontier.append(v)

            frontier = next_frontier

        return vertex_2_parent

    vertex_2_bfs_parent = _bfs_visit((x, y))

    # Flip the values, as required.
    for v in vertex_2_bfs_parent:
        image[v[0]][v[1]] = not image[v[0]][v[1]]


import collections


def flip_color_v2(
    x: int,
    y: int,
    image: List[List[bool]],  # change `int` to `bool` (or to `Literal[0, 1]`)
) -> None:
    """
    Flip the values/colors of the connected component of the `image`,
    which component contains `(x ,y)`.
    """
    original_color_at_x_y = image[x][y]

    # Flip the color of (x, y).
    image[x][y] = not image[x][y]

    q: Deque[Tuple[int, int]] = collections.deque(
        [(x, y)],
    )

    while q:
        x, y = q.popleft()

        for next_x, next_y in (
            (x, y + 1),
            (x, y - 1),
            (x + 1, y),
            (x - 1, y),
        ):
            if (
                0 <= next_x < len(image)
                and 0 <= next_y < len(image[next_x])
                and image[next_x][next_y] == original_color_at_x_y
            ):
                image[next_x][next_y] = not image[next_x][next_y]
                q.append((next_x, next_y))


def flip_color_v3(
    x: int,
    y: int,
    image: List[List[bool]],  # change `int` to `bool` (or to `Literal[0, 1]`)
) -> None:
    """
    Flip the values/colors of the connected component of the `image`,
    which component contains `(x ,y)`.
    """
    original_color_at_x_y = image[x][y]

    # Flip the color of (x, y).
    image[x][y] = not image[x][y]

    for next_x, next_y in (
        (x, y + 1),
        (x, y - 1),
        (x + 1, y),
        (x - 1, y),
    ):
        if (
            0 <= next_x < len(image)
            and 0 <= next_y < len(image[next_x])
            and image[next_x][next_y] == original_color_at_x_y
        ):
            flip_color(next_x, next_y, image)
