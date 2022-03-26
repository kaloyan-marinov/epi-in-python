import unittest

from typing import Dict, List

from m_18_00_A_breadth_first_search import bfs


class TestBfs(unittest.TestCase):
    def test_bfs_output(self):
        Vertex = str

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

        # fmt: off
        self.assertEqual(
            v_2_lvl,
            {
                's': 0,
                'a': 1, 'x': 1,
                'z': 2, 'c': 2, 'd': 2,
                'f': 3, 'v': 3,
            },
        )
        # fmt: on
