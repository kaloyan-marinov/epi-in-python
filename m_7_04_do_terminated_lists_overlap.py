from typing import Optional

from m_7_00_common import ListNode, length


def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> Optional[ListNode]:
    if l0 is None or l1 is None:
        return None

    # Check if the two lists terminate with the same node.
    t0 = l0
    while t0.next:
        t0 = t0.next

    t1 = l1
    while t1.next:
        t1 = t1.next

    if t0 is not t1:
        # The 2 lists don't overlap.
        return None

    # The 2 lists are now known to overlap
    # - go on to find the 1st overlapping node.
    length_0 = length(l0)
    length_1 = length(l1)

    # To simplify the code, ensure that `l1` is the longer linked list.
    if length_0 > length_1:
        l0, l1 = l1, l0
        length_0, length_1 = length_1, length_0

    # Advance `l1` by the length difference.
    i = length_1 - length_0
    while i > 0:
        l1 = l1.next
        i -= 1

    while True:
        if l0 is l1:
            return l0
        l0 = l0.next
        l1 = l1.next
