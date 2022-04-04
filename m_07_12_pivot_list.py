from typing import Optional

from m_07_00_A_singly_linked_list import ListNode


def list_pivoting(L: Optional[ListNode], k: int) -> Optional[ListNode]:
    """
    Perform an in-place modification of the linked list starting at `L`,
    consisting in a re-ordering of its nodes s.t.
    all nodes containing keys `< k` appear before all nodes containing `k`
    and all nodes containing `k` appear before all nodes containing keys `> k`,
    and return the head node of the resulting linked list.

    The relative ordering of the nodes with keys `< k` remain unchanges;
    the same holds true for the nodes with keys `= k`;
    the same holds true for the nodes with keys `> k`.

    time:  O(n)
           n := the # of nodes in `L`

    space: O(1)
    """

    l_dummy_head = ListNode(data=0, next=None)
    l_tail = l_dummy_head
    e_dummy_head = ListNode(data=0, next=None)
    e_tail = e_dummy_head
    g_dummy_head = ListNode(data=0, next=None)
    g_tail = g_dummy_head

    while L:
        L_next = L.next

        L.next = None  # NB: This can be commented out, and the f-n will still work!
        if L.data < k:
            l_tail.next = L
            l_tail = l_tail.next
        elif L.data == k:
            e_tail.next = L
            e_tail = e_tail.next
        else:
            g_tail.next = L
            g_tail = g_tail.next

        L = L_next

    g_tail.next = None
    e_tail.next = g_dummy_head.next
    l_tail.next = e_dummy_head.next

    return l_dummy_head.next
