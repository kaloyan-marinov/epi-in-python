from typing import Optional

from m_7_00_common import ListNode


def list_pivoting(L: ListNode, k: int) -> Optional[ListNode]:
    if L is None:
        return

    l = ListNode()
    latest_l = l
    e = ListNode()
    latest_e = e
    g = ListNode()
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

    it = l
    while it.next:
        it = it.next

    if e.next:
        it.next = e.next
    while it.next:
        it = it.next

    if g.next:
        it.next = g.next

    return l.next
