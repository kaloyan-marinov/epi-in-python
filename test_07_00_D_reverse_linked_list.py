import unittest

from typing import Optional

from m_07_00_A_singly_linked_list import ListNode
from m_07_00_D_reverse_linked_list import reverse_list


class TestReverseList(unittest.TestCase):
    def setUp(self):
        self.head: Optional[ListNode] = None

    def test_empty_list(self):
        head_of_reversed_list = reverse_list(self.head)

        self.assertIsNone(head_of_reversed_list)

    def test_nonempty_list(self):
        self.head: ListNode = ListNode.from_list([num for num in range(5)])

        head_of_reversed_list = reverse_list(self.head)

        self.assertEqual(
            head_of_reversed_list.represent_all_nodes(),
            "4 -> 3 -> 2 -> 1 -> 0",
        )
