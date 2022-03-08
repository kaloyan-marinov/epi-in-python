from typing import List

import collections


class Team:
    Player = collections.namedtuple(
        "Player",
        ("height"),
    )

    def __init__(self, heights: List[int]) -> None:
        self._players = [Team.Player(h) for h in heights]

    # fmt: off
    '''
    # Checks if team0 can be placed in front of team1.
    @staticmethod
    def valid_placement_exists(team0: "Team", team1: "Team") -> bool:
        s = set()
        for p0 in team0._players:
            c = sum(p0.height < p1.height for p1 in team1._players)
            s.add(c)

        ss = set()
        for p1 in team1._players:
            c = sum(p1.height < p0.height for p0 in team0._players)
            ss.add(c)
        return s == set(x + 1 for x in range(len(team0._players))) or ss == set(
            x + 1 for x in range(len(team0._players))
        )
    '''

    # Checks if team0 can be placed in front of team1.
    @staticmethod
    def valid_placement_exists(team0: "Team", team1: "Team") -> bool:
        return all(
            p0 < p1
            for p0, p1 in zip(sorted(team0._players), sorted(team1._players))
        )
    # fmt: on
