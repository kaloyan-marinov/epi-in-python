from typing import Tuple

from m_07_00_A_singly_linked_list import ListNode


def compute_tail_node_and_length(L: ListNode) -> Tuple[ListNode, int]:
    tail = L
    length = 1
    while tail.next:
        length += 1
        tail = tail.next
    return tail, length
