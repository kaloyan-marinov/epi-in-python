import unittest

from typing import Generator, List, Optional

from m_7_00_common import ListNode, length, reverse_list


class Test1ListNode(unittest.TestCase):
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


class Test2LengthOfLinkedList(unittest.TestCase):
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


class Test3ReverseList(unittest.TestCase):
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
