from typing import Optional

from m_7_00_common import ListNode


def list_pivoting(L: ListNode, k: int) -> Optional[ListNode]:
    l = ListNode(data=0, next=None)
    latest_l = l
    e = ListNode(data=0, next=None)
    latest_e = e
    g = ListNode(data=0, next=None)
    latest_g = g

    while L:
        L_next = L.next

        L.next = None
        if L.data < k:
            latest_l.next = L
            latest_l = latest_l.next
        elif L.data == k:
            latest_e.next = L
            latest_e = latest_e.next
        else:
            latest_g.next = L
            latest_g = latest_g.next

        L = L_next

    latest_g.next = None
    latest_e.next = g.next
    latest_l.next = e.next

    return l.next
