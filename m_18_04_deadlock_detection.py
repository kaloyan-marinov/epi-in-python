from typing import Dict, List, Set


class GraphVertex:
    def __init__(self) -> None:
        self.edges: List["GraphVertex"] = []


def is_deadlocked(graph: List[GraphVertex]) -> bool:
    # fmt: off
    '''
    vertex_2_parent: Dict[GraphVertex, GraphVertex] = {}

    def _dfs_visit(start_vertex: GraphVertex):
        for u in start_vertex.edges:
            if u not in vertex_2_parent:
                vertex_2_parent[u] = start_vertex
                _dfs_visit(u)

    for s in graph:
        if s not in vertex_2_parent:
            vertex_2_parent[s] = None
            _dfs_visit(s)
    '''
    # fmt: on

    # fmt: off
    '''
    vertex_2_parent: Dict[GraphVertex, GraphVertex] = {}

    vertices_in_process: Set[GraphVertex] = set()

    def _dfs_visit(start_vertex: GraphVertex) -> bool:
        vertices_in_process.add(start_vertex)

        for u in start_vertex.edges:
            if u in vertices_in_process:
                return True

            if u not in vertex_2_parent:
                # if u in vertices_in_process:
                #     return True

                vertex_2_parent[u] = start_vertex
                _dfs_visit(u)

        vertices_in_process.remove(start_vertex)

        return False

    for s in graph:
        if s not in vertex_2_parent:
            vertex_2_parent[s] = None
            component_of_s_contains_cycle = _dfs_visit(s)
            if component_of_s_contains_cycle:
                return True

    return False
    '''
    # fmt: on

    vertex_2_parent: Dict[GraphVertex, GraphVertex] = {}

    vertices_in_process: Set[GraphVertex] = set()

    def _dfs_visit(start_vertex: GraphVertex) -> bool:
        """
        Determine whether there is a cycle in the connected component,
        which contains `start_vertex`.
        """
        # if start_vertex in vertices_in_process:
        #    return True

        vertices_in_process.add(start_vertex)

        for u in start_vertex.edges:
            if u in vertices_in_process:
                return True

            if u not in vertex_2_parent:
                # fmt: off
                '''
                if u in vertices_in_process:
                    return True
                '''
                # fmt: on

                vertex_2_parent[u] = start_vertex

                has_cycle: bool = _dfs_visit(u)
                if has_cycle:
                    return True

        vertices_in_process.remove(start_vertex)

        return False

    for s in graph:
        if s not in vertex_2_parent:
            vertex_2_parent[s] = None
            component_of_s_contains_cycle = _dfs_visit(s)
            if component_of_s_contains_cycle:
                return True

    return False


def is_deadlocked_v2(graph: List[GraphVertex]) -> bool:
    def _has_cycle(curr_v: GraphVertex) -> bool:
        # Visiting a gray vertex means a cycle.
        if curr_v.color == GraphVertex.GRAY:
            return True

        # Color the current vertex gray.
        curr_v.color = GraphVertex.GRAY

        # Traverse the [adjacent] vertices.
        if any(
            next_v.color != GraphVertex.BLACK and _has_cycle(next_v)
            for next_v in curr_v.edges
        ):
            return True

        # Color the current vertex black.
        curr_v.color = GraphVertex.BLACK

        return False

    # fmt: off
    # Since the graph may not be strongly connected,
    # we must examine each `vertex`,
    # and run DFS from `vertex` if it has not already been explored.
    return any(
        vertex.color == GraphVertex.WHITE and _has_cycle(vertex)
        for vertex in graph
    )
    # fmt: on


if __name__ == "__main__":
    vertices: List[GraphVertex] = [GraphVertex() for _ in range(2)]
    vertices[0].edges = [vertices[1]]
    vertices[1].edges = [vertices[0]]

    result = is_deadlocked(vertices)

    print(result)
