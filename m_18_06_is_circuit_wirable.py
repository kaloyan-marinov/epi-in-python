import collections
from typing import Deque, List, Set


class GraphVertex:
    def __init__(self) -> None:
        self.d = -1  # The meaning is described in the docstring of the next function.
        self.edges: List[GraphVertex] = []


def is_any_placement_feasible(graph: List[GraphVertex]) -> bool:
    """
    Determine if it is possible to split the graph vertices into two disjoint subsets,
    which will be called the "left" and the "right" subsets,
    s.t. each edge is between the left and right subsets.
    """

    """
    In reality, the following is not checked by the EPI Judge:

    "Return such a division if it exists"
    [in the sense that
    the `d` field of each left `GraphVertex` should be set equal to -1,
    whereas the `d` field of each right `GraphVertex` should be set equal to 1.]
    """

    left_vertices: Set[GraphVertex] = set()
    right_vertices: Set[GraphVertex] = set()

    def _bfs_visit(start_v: GraphVertex) -> bool:
        if start_v.d == -1:
            left_vertices.add(start_v)

        q: Deque[GraphVertex] = collections.deque([start_v])

        while q:
            v = q.popleft()

            for u in v.edges:
                # u_d = -1 if v in left_vertices else 1
                u_d = (-1) * v.d

                if (u_d == -1 and u in right_vertices) or (
                    u_d == 1 and u in left_vertices
                ):
                    return False

                if u not in left_vertices and u not in right_vertices:
                    u.d = u_d
                    if u_d == -1:
                        left_vertices.add(u)
                    else:  # i.e. `u_d == 1`
                        right_vertices.add(u)

                q.append(u)  # Shift this statement one indent to the right.

        return True

    for s in graph:
        if s not in left_vertices and s not in right_vertices:
            is_component_containing_s_splittable = _bfs_visit(s)

            if not is_component_containing_s_splittable:
                return False

    return True


def is_any_placement_feasible(graph: List[GraphVertex]) -> bool:
    """
    Determine if it is possible to split the graph vertices into two disjoint subsets,
    which will be called the "left" and the "right" subsets,
    s.t. each edge is between the left and right subsets.
    """

    """
    In reality, the following is not checked by the EPI Judge:
    
    "Return such a division if it exists"
    [in the sense that,
    if the `d` field of a `GraphVertex` `v` is >= 0,
    this means that `v` is at a distance of `v.d`
    from where the BFS of `v`'s connected component started.]

    If the `d` field of a `GraphVertex` is -1,
    that means that the vertex in question has not been visited.]
    """

    def _bfs_visit(start_v: GraphVertex) -> bool:
        start_v.d = 0

        q: Deque[GraphVertex] = collections.deque([start_v])

        while q:

            for u in q[0].edges:
                if u.d == -1:  # i.e. `u` has not been visited yet.
                    u.d = q[0].d + 1
                    q.append(u)
                elif u.d == q[0].d:
                    return False

            del q[0]

        return True

    return all(_bfs_visit(s) for s in graph if s.d == -1)
