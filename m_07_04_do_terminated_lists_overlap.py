from typing import Optional

from m_07_00_A_singly_linked_list import ListNode
from m_07_00_B_length_of_linked_list import length


def overlapping_no_cycle_lists_1(
    l0: Optional[ListNode],
    l1: Optional[ListNode],
) -> Optional[ListNode]:
    """
    Assume that `l0` and `l1` are the heads of 2 cycle-free linked lists.

    Determine whether `l0` and `l1` have a node in common:
        (a) if yes, return their 1st common node,
        (b) if not, return `None`.

    time:  O(n + m)
           n := the # of nodes in `l0`
           m := the # of nodes in `l1`

    space: O(1)
    """

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


def overlapping_no_cycle_lists_2(
    l0: Optional[ListNode],
    l1: Optional[ListNode],
) -> Optional[ListNode]:
    """
    (
    This is the official solution.
    It is empirically observed to be two times faster than the earlier solution,
    but its implementation is a little more difficult to understand.
    )

    Assume that `l0` and `l1` are the heads of 2 cycle-free linked lists.

    Determine whether `l0` and `l1` have a node in common:
        (a) if yes, return their 1st common node,
        (b) if not, return `None`.

    time:  O(n + m)
           n := the # of nodes in `l0`
           m := the # of nodes in `l1`

    space: O(1)
    """

    length_0 = length(l0)
    length_1 = length(l1)

    # To simplify the code, ensure that `l1` is the longer linked list.
    if length_0 > length_1:
        l0, l1 = l1, l0

    # Advance `l1` by the length difference.
    for _ in range(abs(length_0 - length_1)):
        l1 = l1.next

    # fmt: off
    while (
        l0
        and l1
        and l0 is not l1
    ):
    # fmt: on
        l0 = l0.next
        l1 = l1.next
    
    return l0  # `None` implies no overlap
