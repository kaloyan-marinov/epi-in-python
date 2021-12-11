from typing import Optional

from m_7_00_common import ListNode


def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> Optional[ListNode]:
    t0 = l0
    while t0.next:
        t0 = t0.next

    t1 = l1
    while t1.next:
        t1 = t1.next

    if t0 is not t1:
        return None

    # The 2 lists are now known to overlap.
    length_0 = 0
    i0 = l0
    while i0:
        length_0 += 1
        i0 = i0.next

    length_1 = 0
    i1 = l1
    while i1:
        length_1 += 1
        i1 = i1.next

    if length_0 > length_1:
        l0, l1 = l1, l0
        length_0, length_1 = length_1, length_0
    i = length_1 - length_0
    while i > 0:
        l1 = l1.next
        i -= 1

    while True:
        if l0 is l1:
            return l0
        l0 = l0.next
        l1 = l1.next
