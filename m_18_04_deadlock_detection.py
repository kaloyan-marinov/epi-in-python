from typing import Dict, List, Set, Literal


WHITE, GRAY, BLACK = range(3)


class GraphVertex:
    def __init__(self) -> None:
        self.edges: List["GraphVertex"] = []
        self.color: Literal[
            WHITE, GRAY, BLACK
        ] = WHITE  # TODO: fix this type annotation


def is_deadlocked(graph: List[GraphVertex]) -> bool:
    """
    This function does not rely on or use `GraphVertex.color` in any way.

    TODO: check hand-written notes & make any appropriate updates to this function
    """

    vertex_2_parent: Dict[GraphVertex, GraphVertex] = {}

    vertices_being_processed: Set[GraphVertex] = set()

    def _dfs_visit(start_vertex: GraphVertex) -> bool:
        """
        Determine whether there is a cycle in the connected component,
        which contains `start_vertex`.
        """
        # if start_vertex in vertices_being_processed:
        #    return True

        vertices_being_processed.add(start_vertex)

        for u in start_vertex.edges:
            if u in vertices_being_processed:
                return True

            if u not in vertex_2_parent:
                # fmt: off
                '''
                if u in vertices_being_processed:
                    return True
                '''
                # fmt: on

                vertex_2_parent[u] = start_vertex

                has_cycle: bool = _dfs_visit(u)
                if has_cycle:
                    return True

        vertices_being_processed.remove(start_vertex)

        return False

    for s in graph:
        if s not in vertex_2_parent:
            vertex_2_parent[s] = None
            component_of_s_contains_cycle = _dfs_visit(s)
            if component_of_s_contains_cycle:
                return True

    return False


def is_deadlocked_v2(graph: List[GraphVertex]) -> bool:
    """
    This function relies on or uses `GraphVertex.color`, where
    `WHITE` means "not yet processed",
    `GRAY` means "being processed",
    `BLACK` means "processed".
    """

    def _has_cycle(curr_v: GraphVertex) -> bool:
        # Visiting a gray vertex means a cycle.
        if curr_v.color == GRAY:
            return True

        # Color the current vertex gray.
        curr_v.color = GRAY

        # Traverse the [adjacent] vertices.
        if any(next_v.color != BLACK and _has_cycle(next_v) for next_v in curr_v.edges):
            return True

        # Color the current vertex black.
        curr_v.color = BLACK

        return False

    # fmt: off
    # Since
    # (a) the graph may consist of disconnected components, or
    # (b) it may look like v_0 -> v_1 -> v_2 but we start the DFS from v_1,
    # we must examine each `vertex`,
    # and run DFS from `vertex` if it has not already been explored.
    return any(
        vertex.color == WHITE and _has_cycle(vertex)
        for vertex in graph
    )
    # fmt: on


if __name__ == "__main__":
    vertices: List[GraphVertex] = [GraphVertex() for _ in range(2)]
    vertices[0].edges = [vertices[1]]
    vertices[1].edges = [vertices[0]]

    result = is_deadlocked(vertices)

    print(result)
