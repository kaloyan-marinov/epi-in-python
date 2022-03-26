from typing import List, DefaultDict, Optional, Set, Dict

import collections
import typing


WHITE, BLACK = range(2)


class Coordinate(typing.NamedTuple):
    x: int
    y: int


def search_maze(
    maze: List[List[int]],  # `List[List[Literal[WHITE, BLACK]]]`
    s: Coordinate,
    e: Coordinate,
) -> List[Coordinate]:

    # Model the maze as a(n undirected) graph.
    vertex_2_neighboring_vertices: DefaultDict[
        Coordinate, Set[Coordinate]
    ] = collections.defaultdict(set)

    m = len(maze)
    n = len(maze[0])
    for i in range(m):
        for j in range(n):
            vertex_i_j = Coordinate(x=i, y=j)

            if i - 1 >= 0 and maze[i - 1][j] == WHITE:
                vertex_2_neighboring_vertices[vertex_i_j].add(
                    Coordinate(x=i - 1, y=j),
                )

            if i + 1 <= m - 1 and maze[i + 1][j] == WHITE:
                vertex_2_neighboring_vertices[vertex_i_j].add(
                    Coordinate(x=i + 1, y=j),
                )

            if j - 1 >= 0 and maze[i][j - 1] == WHITE:
                vertex_2_neighboring_vertices[vertex_i_j].add(
                    Coordinate(x=i, y=j - 1),
                )

            if j + 1 <= n - 1 and maze[i][j + 1] == WHITE:
                vertex_2_neighboring_vertices[vertex_i_j].add(
                    Coordinate(x=i, y=j + 1),
                )

    # Perform a DFS traversal of the graph, starting from `s`.
    vertex_2_parent: Dict[
        Coordinate,
        Optional[Coordinate],
    ] = {}  # Change to `{s: None}`

    def _dfs_visit(start_vertex: Coordinate) -> None:
        for v in vertex_2_neighboring_vertices[start_vertex]:
            if v not in vertex_2_parent:
                vertex_2_parent[v] = start_vertex
                _dfs_visit(v)

    _dfs_visit(s)

    # If the DFS traversal was able to reach `e`,
    # construct a path from `s` to `e` and return it.
    if e in vertex_2_parent:
        path = []

        last_cell = e
        while last_cell in vertex_2_parent:
            path.append(last_cell)
            last_cell = vertex_2_parent[last_cell]

        return path[::-1]

    return []


def search_maze(
    maze: List[List[int]],  # `List[List[Literal[WHITE, BLACK]]]`
    s: Coordinate,
    e: Coordinate,
) -> List[Coordinate]:

    path: List[Coordinate] = []

    def _search_maze_helper(curr: Coordinate) -> bool:
        # Check whether `curr` is within `maze` and whether `curr` is a while pixel.
        if not (
            0 <= curr.x < len(maze)
            and 0 <= curr.y < len(maze[curr.x])
            and maze[curr.x][curr.y] == WHITE
        ):
            return False

        path.append(curr)
        maze[curr.x][curr.y] = BLACK

        if curr == e:
            return True

        if any(
            map(
                _search_maze_helper,
                map(
                    Coordinate,
                    (curr.x - 1, curr.x + 1, curr.x, curr.x),
                    (curr.y, curr.y, curr.y - 1, curr.y + 1),
                ),
            )
        ):
            return True

        # Cannot find a path, remove the entry added in `path.append(curr)`.
        del path[-1]

        return False

    _search_maze_helper(s)

    return path
