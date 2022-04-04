from typing import Optional

from m_07_00_A_singly_linked_list import ListNode


def remove_duplicates(L: Optional[ListNode]) -> Optional[ListNode]:
    """
    Assume that (the linked list starting at) L is sorted.

    Perform an in-place modification of the linked list
    by "removing" duplicate-data nodes from it,
    and return the head of the resulting linked list.

    time:  O(n)
           where n := the # of nodes in `L`

    space: O(1)
    """

    slow = L

    while slow:
        fast = slow.next
        while fast and fast.data == slow.data:
            fast = fast.next

        slow.next = fast
        slow = slow.next  # Achieves the same effect as `slow = fast`.

    return L
