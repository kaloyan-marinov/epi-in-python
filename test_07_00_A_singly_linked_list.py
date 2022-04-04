import unittest

from typing import List

from m_07_00_A_singly_linked_list import ListNode


class TestListNode(unittest.TestCase):
    def test_1_repr(self):
        n: ListNode = ListNode(data=17, next=None)
        self.assertEqual(
            repr(n),
            "<ListNode(data=17)>",
        )

    def test_2_from_list(self):
        numbers: List[int] = [x for x in range(5)]

        head: ListNode = ListNode.from_list(numbers)

        node = head
        for x in numbers:
            self.assertEquals(node.data, x)
            node = node.next
        self.assertEqual(node, None)

    def test_3_represent_all_nodes(self):
        numbers: List[int] = [x for x in range(5)]
        head: ListNode = ListNode.from_list(numbers)

        repr_of_all_nodes: str = head.represent_all_nodes()

        self.assertEqual(
            repr_of_all_nodes,
            "0 -> 1 -> 2 -> 3 -> 4",
        )
