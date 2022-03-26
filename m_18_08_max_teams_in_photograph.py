import collections
from typing import Deque, List


class GraphVertex:
    def __init__(self) -> None:
        self.edges: List[GraphVertex] = []
        # Set max_distance = 0 to indicate unvisited vertex.
        self.max_distance = 0


def find_largest_number_teams(graph: List[GraphVertex]) -> int:
    """
    This is wrong.
    """

    def _largest_num_teams_with_s_at_back(s: GraphVertex):
        max_num_teams = 1

        q: Deque[GraphVertex] = collections.deque(
            [s],
        )

        while q:
            v = q.popleft()

            for u in v.edges:
                if u.max_distance == 0:
                    u.max_distance = v.max_distance + 1
                    q.append(u)

                    max_num_teams = max(
                        max_num_teams,
                        u.max_distance,  # Change to `u.max_distance + 1`
                    )

        for v in graph:
            v.max_distance = 0

        return max_num_teams

    return max(
        (_largest_num_teams_with_s_at_back(s) for s in graph),
    )  # The generator (expression) must be in parentheses.


def find_largest_number_teams_v2(graph: List[GraphVertex]) -> int:
    def _dfs(curr: GraphVertex) -> int:
        curr.max_distance = max(
            (
                (
                    neighbor_v.max_distance
                    if neighbor_v.max_distance != 0
                    else _dfs(neighbor_v)
                )
                + 1
                for neighbor_v in curr.edges
            ),
            default=1,
        )

        return curr.max_distance

    return max(_dfs(s) for s in graph if s.max_distance == 0)


if __name__ == "__main__":
    # fmt: off
    edges = [
        [0, 13], [9, 11], [4, 18], [5, 7], [2, 17], [19, 21], [18, 19], [6, 12], [5, 9],
        [11, 22], [2, 12], [0, 6], [2, 6], [7, 8], [0, 12], [4, 23], [7, 14], [2, 13],
        [12, 13], [0, 22], [5, 22], [8, 9], [0, 21], [15, 18], [8, 22], [2, 11],
        [1, 12], [6, 15], [7, 13], [0, 14], [1, 13], [7, 11], [2, 4], [10, 19], [4, 12],
        [0, 5], [9, 12], [3, 21], [1, 5], [10, 16], [14, 21], [9, 13], [13, 17],
        [15, 16], [15, 20], [4, 15], [21, 23], [3, 15], [6, 10], [13, 20], [22, 23],
        [2, 8], [0, 9], [8, 14], [14, 16], [10, 22], [15, 23], [2, 3], [6, 20], [7, 21],
        [19, 20], [9, 20], [15, 22], [2, 15], [7, 22], [4, 6], [17, 22], [5, 8], [5, 6],
        [16, 22], [8, 21], [10, 14], [5, 14], [3, 19], [9, 16], [9, 17], [8, 18],
        [14, 17], [1, 20], [1, 9], [12, 20], [14, 18], [11, 19], [3, 17], [2, 7],
        [3, 22], [14, 15], [1, 16], [5, 12], [1, 3], [1, 11], [11, 12], [4, 10],
        [14, 19], [10, 23], [6, 19], [5, 16], [12, 17], [0, 11], [15, 21], [0, 19],
        [5, 21], [10, 11], [3, 5], [6, 13], [6, 21], [9, 21], [0, 4], [11, 15], [0, 7],
        [10, 13], [1, 15], [1, 4], [1, 6], [18, 22], [8, 20], [6, 17], [0, 23], [3, 6],
        [3, 23], [0, 8], [11, 17], [7, 9], [14, 23], [5, 20], [14, 22], [0, 20],
        [4, 22], [9, 18], [9, 22], [7, 15], [5, 11], [18, 23], [0, 10], [2, 23],
        [10, 18], [12, 22], [7, 10], [16, 19], [9, 15], [12, 21], [16, 23], [3, 8],
        [1, 2], [12, 18], [6, 18], [2, 14], [17, 21], [16, 21], [4, 20], [11, 23],
        [7, 23], [1, 23], [6, 14], [0, 17], [7, 16], [1, 22], [2, 9], [5, 19], [3, 12],
        [3, 20], [10, 12], [17, 18], [11, 13], [8, 11], [3, 11], [8, 23], [5, 23],
        [8, 16], [9, 14], [1, 21], [11, 18], [0, 1], [1, 14], [1, 17], [6, 9], [16, 17],
        [17, 20], [13, 23], [13, 15], [4, 19], [19, 23], [9, 23], [4, 13], [8, 13],
        [11, 21], [3, 7], [6, 23], [5, 17], [8, 17], [7, 17], [0, 18], [2, 16], [1, 8],
        [3, 4], [10, 20], [3, 13], [5, 10], [13, 21], [12, 16], [14, 20], [12, 15],
        [8, 15], [13, 18], [4, 9], [4, 14], [19, 22], [2, 10], [4, 8], [8, 19], [6, 11],
        [17, 19], [0, 3], [10, 17], [10, 21], [15, 17], [11, 20], [18, 21], [0, 15],
        [18, 20], [13, 14], [12, 23], [2, 20], [2, 18], [6, 16], [20, 22], [4, 11],
        [2, 5], [10, 15], [3, 9], [20, 21], [4, 21], [6, 7], [5, 13], [20, 23], [3, 14],
        [2, 19]
    ]
    # fmt: on
