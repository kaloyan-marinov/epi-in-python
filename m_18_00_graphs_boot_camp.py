import collections
from typing import DefaultDict, List


Match = collections.namedtuple(
    "Match",
    ("winning_team", "losing_team"),
)


def can_team_a_beat_team_b(
    matches: List[Match],
    team_a,
    team_b,
) -> bool:
    def _build_graph() -> DefaultDict:
        graph = collections.defaultdict(set)

        for match in matches:
            graph[match.winning_team].add(match.losing_team)

        return graph

    def _is_reachable_dfs(
        graph,
        curr,
        dest,
        visited=set(),
    ) -> bool:
        if curr == dest:
            return True
        elif curr in visited or curr not in graph:
            return False

        visited.add(curr)

        return any(_is_reachable_dfs(graph, team, dest) for team in graph[curr])

    return _is_reachable_dfs(
        _build_graph(),
        team_a,
        team_b,
    )
