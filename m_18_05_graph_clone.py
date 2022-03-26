import collections
from typing import Deque, Dict, List


class GraphVertex:
    def __init__(self, label: int) -> None:
        self.label = label
        self.edges: List["GraphVertex"] = []


def clone_graph(graph: GraphVertex) -> GraphVertex:
    if not graph.edges:
        return GraphVertex(graph.label)

    g = GraphVertex(graph.label)
    g.edges = [clone_graph(neighbor_of_graph) for neighbor_of_graph in graph.edges]

    return g


def clone_graph(graph: GraphVertex) -> GraphVertex:
    original_v_2_clone_of_v: Dict[GraphVertex, GraphVertex] = {}

    def _helper(g: GraphVertex):
        original_v_2_clone_of_v[g] = GraphVertex(g.label)

        edges_of_clone = []
        for neighbor_of_g in g.edges:
            if neighbor_of_g not in original_v_2_clone_of_v:
                edges_of_clone.append(clone_graph(neighbor_of_g))
            else:
                edges_of_clone.append(neighbor_of_g)

        original_v_2_clone_of_v[g].edges = edges_of_clone

    _helper(graph)

    return original_v_2_clone_of_v[graph]


def clone_graph(graph: GraphVertex) -> GraphVertex:
    # Perform a BFS traversal of `graph`,
    # as part of which - in addition to one of BFS's usual data structures! -
    # a map from vertices in the original graph to their counterparts in the clone
    # gets populated.
    original_v_2_clone_of_v: Dict[
        GraphVertex, GraphVertex
    ] = {}  # Change to `{graph: GraphVertex(graph.label)}`

    original_v_2_parent: Dict[GraphVertex, GraphVertex] = {graph: None}

    q: Deque[GraphVertex] = collections.deque(graph)  # Change to `[graph]`

    while q:
        v = q.popleft()

        for u in v.edges:
            if u not in original_v_2_parent:
                original_v_2_parent[u] = v
                q.extend(u.edges)  # Change to `q.append(u)`

                original_v_2_clone_of_v[u] = GraphVertex(u.label)

    # Currently, the clone consists of all relevant vertices but has no edges at all
    # - create all relevant/necessary edges in the clone.
    for original_v, clone_v in original_v_2_clone_of_v.items():
        clone_v.edges = [original_v_2_clone_of_v[u] for u in original_v.edges]

    return original_v_2_clone_of_v[graph]


def clone_graph(graph: GraphVertex) -> GraphVertex:
    if graph is None:
        return None

    q: Deque[GraphVertex] = collections.deque([graph])

    original_v_2_clone_of_v: Dict[GraphVertex, GraphVertex] = {
        graph: GraphVertex(graph.label)
    }

    while q:
        v = q.popleft()

        for u in v.edges:
            # Try to copy vertex `u`.
            if u not in original_v_2_clone_of_v:
                original_v_2_clone_of_v[u] = GraphVertex(u.label)
                q.append(u)

            # Copy the edge.
            original_v_2_clone_of_v[v].edges.append(
                original_v_2_clone_of_v[u],
            )
    
    return original_v_2_clone_of_v[graph]


if __name__ == "__main__":
    # fmt: off
    edges = [
        [0, 1], [1, 0], [1, 2], [2, 1], [2, 3], [3, 2], [3, 4], [4, 3], [4, 5], [5, 4],
        [5, 6], [6, 5], [6, 7], [7, 6], [7, 8], [8, 7], [8, 9], [9, 8], [9, 10],
        [10, 9], [10, 11], [11, 10], [11, 12], [12, 11], [12, 13], [13, 12], [13, 14],
        [14, 13], [7, 0], [0, 7], [0, 10], [10, 0], [5, 11], [11, 5], [13, 10],
        [10, 13], [6, 11], [11, 6], [14, 12], [12, 14], [6, 2], [2, 6], [14, 6],
        [6, 14], [9, 11], [11, 9], [3, 8], [8, 3], [3, 11], [11, 3], [0, 8], [8, 0],
        [13, 9], [9, 13], [9, 2], [2, 9], [14, 2], [2, 14], [5, 2], [2, 5], [14, 4],
        [4, 14], [6, 1], [1, 6], [0, 2], [2, 0], [3, 10], [10, 3], [14, 1], [1, 14],
        [3, 7], [7, 3], [14, 7], [7, 14], [12, 5], [5, 12], [10, 7], [7, 10], [10, 12],
        [12, 10], [8, 4], [4, 8], [4, 13], [13, 4], [14, 3], [3, 14], [11, 14],
        [14, 11], [7, 2], [2, 7], [12, 1], [1, 12], [1, 11], [11, 1], [9, 14], [14, 9],
        [6, 9], [9, 6], [12, 4], [4, 12], [6, 13], [13, 6], [9, 4], [4, 9], [10, 1],
        [1, 10], [14, 0], [0, 14], [8, 12], [12, 8], [12, 9], [9, 12], [2, 4], [4, 2],
        [7, 12], [12, 7], [4, 0], [0, 4], [2, 12], [12, 2], [13, 7], [7, 13], [12, 3],
        [3, 12], [10, 4], [4, 10], [7, 9], [9, 7], [1, 5], [5, 1], [9, 1], [1, 9],
        [14, 8], [8, 14], [7, 1], [1, 7], [8, 11], [11, 8], [9, 0], [0, 9], [8, 5],
        [5, 8], [0, 13], [13, 0], [0, 6], [6, 0], [9, 5], [5, 9], [10, 14], [14, 10],
        [6, 8], [8, 6], [13, 1], [1, 13], [4, 11], [11, 4], [1, 4], [4, 1], [7, 5],
        [5, 7], [5, 14], [14, 5], [1, 8], [8, 1], [2, 13], [13, 2], [13, 8], [8, 13],
        [4, 6], [6, 4], [5, 10], [10, 5], [0, 3], [3, 0], [3, 9], [9, 3], [11, 2],
        [2, 11], [10, 8], [8, 10], [2, 8], [8, 2], [5, 13], [13, 5], [3, 5], [5, 3],
        [12, 0], [0, 12], [5, 0], [0, 5], [6, 3], [3, 6], [6, 10], [10, 6]
    ]

    edges = [
        [0, 1], [1, 0], [1, 2], [2, 1], [2, 3], [3, 2], [3, 4], [4, 3], [4, 5], [5, 4],
        [5, 6], [6, 5], [6, 7], [7, 6], [7, 8], [8, 7], [8, 9], [9, 8], [9, 10],
        [10, 9], [10, 11], [11, 10], [11, 12], [12, 11], [12, 13], [13, 12], [13, 14],
        [14, 13], [14, 15], [15, 14], [15, 16], [16, 15], [16, 17], [17, 16], [17, 18],
        [18, 17], [18, 19], [19, 18], [19, 20], [20, 19], [20, 21], [21, 20], [21, 22],
        [22, 21], [22, 23], [23, 22], [23, 24], [24, 23], [24, 25], [25, 24], [25, 26],
        [26, 25], [26, 27], [27, 26], [27, 28], [28, 27], [28, 29], [29, 28], [29, 30],
        [30, 29], [30, 31], [31, 30], [31, 32], [32, 31], [32, 33], [33, 32], [33, 34],
        [34, 33]
    ]
    # fmt: on

    vertex_indices = set()
    for e in edges:
        vertex_indices.add(e[0])
        vertex_indices.add(e[1])
    n_vertices = len(vertex_indices)

    vertices = [GraphVertex(idx) for idx in range(n_vertices)]
    for e in edges:
        vertices[e[0]].edges.append(vertices[e[1]])

    clone_0 = clone_graph(vertices[0])
