from typing import Optional

from m_7_00_common import ListNode


def remove_duplicates(L: ListNode) -> Optional[ListNode]:
    """
    Assume that (the linked list starting at) L is sorted.
    """
    slow = L

    while slow:
        fast = slow.next
        while fast and fast.data == slow.data:
            fast = fast.next

        slow.next = fast
        slow = slow.next

    return L
