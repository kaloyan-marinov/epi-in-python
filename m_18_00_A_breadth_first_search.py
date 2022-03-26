from typing import Dict, List, Deque


import collections


Vertex = str


def bfs_v_1(
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


def bfs_v_2(
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

    q: Deque[Vertex] = collections.deque(
        [s],
    )

    while q:
        u = q.popleft()

        for v in Adj[u]:
            if v not in vertex_2_level:
                vertex_2_level[v] = vertex_2_level[u] + 1
                vertex_2_parent[v] = u

                q.append(v)

    return vertex_2_level
