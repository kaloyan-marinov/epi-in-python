import unittest

from typing import Optional, Generator

from m_07_00_A_singly_linked_list import ListNode
from m_07_00_B_length_of_linked_list import length


class TestLengthOfLinkedList(unittest.TestCase):
    def setUp(self):
        self.head: Optional[ListNode] = None

    def test_empty_list(self):
        length_of_empty_list = length(self.head)
        self.assertEqual(length_of_empty_list, 0)

    def test_nonempty_list(self):
        node_count: int = 17
        numbers: Generator[int] = (x for x in range(node_count))
        self.head = ListNode.from_list(numbers)

        length_of_nonempty_list = length(self.head)

        self.assertEqual(length_of_nonempty_list, node_count)
