import unittest

from typing import Dict, List

from m_18_00_A_breadth_first_search import bfs_v_1, bfs_v_2


class TestBfs(unittest.TestCase):
    def setUp(self):
        self.Vertex = str

        self.adj: Dict[self.Vertex, List[self.Vertex],] = {
            "a": ["s", "z"],
            "z": ["a"],
            "s": ["a", "x"],
            "x": ["s", "c", "d"],
            "d": ["x", "c", "f"],
            "c": ["x", "d", "f", "v"],
            "f": ["d", "c", "v"],
            "v": ["c", "f"],
        }

        # fmt: off
        self.expected_vertex_2_level = {
            's': 0,
            'a': 1, 'x': 1,
            'z': 2, 'c': 2, 'd': 2,
            'f': 3, 'v': 3,
        }
        # fmt: on

    def test_bfs_v_1(self):
        v_2_lvl: Dict[self.Vertex, int] = bfs_v_1(self.adj, "s")

        self.assertEqual(
            v_2_lvl,
            self.expected_vertex_2_level,
        )

    def test_bfs_v_2(self):
        v_2_lvl: Dict[self.Vertex, int] = bfs_v_2(self.adj, "s")

        self.assertEqual(
            v_2_lvl,
            self.expected_vertex_2_level,
        )
