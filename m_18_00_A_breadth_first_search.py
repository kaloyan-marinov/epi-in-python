from typing import Dict, List


Vertex = str


def bfs(
    Adj: Dict[Vertex, List[Vertex]],
    s: Vertex,
) -> Dict[Vertex, List[Vertex]]:
    """
    space: O(|V| + |E|)
    time:  O(|V| + |E|)
    """

    vertex_2_level: Dict[Vertex, int] = {s: 0}
    # (The following is optional;
    # just gives us another potentially helpful structure.)
    vertex_2_parent: Dict[Vertex, Vertex] = {s: None}

    i = 1
    frontier: List[Vertex] = s

    while frontier:
        next_frontier = []  # Reachable in `i` moves.

        for u in frontier:
            for v in Adj[u]:
                if v not in vertex_2_level:
                    vertex_2_level[v] = i
                    vertex_2_parent[v] = u
                    next_frontier.append(v)

        frontier = next_frontier
        i += 1

    return vertex_2_level


if __name__ == "__main__":
    adj: Dict[Vertex, List[Vertex]] = {
        "a": ["s", "z"],
        "z": ["a"],
        "s": ["a", "x"],
        "x": ["s", "c", "d"],
        "d": ["x", "c", "f"],
        "c": ["x", "d", "f", "v"],
        "f": ["d", "c", "v"],
        "v": ["c", "f"],
    }

    v_2_lvl: Dict[Vertex, int] = bfs(adj, "s")

    print(v_2_lvl)
