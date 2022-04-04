from typing import Optional

from m_7_00_common import ListNode
from m_7_03_is_list_cyclic import has_cycle
from m_7_04_do_terminated_lists_overlap import overlapping_no_cycle_lists


def overlapping_lists(l0: ListNode, l1: ListNode) -> Optional[ListNode]:
    # Test for cycles in each list.
    cycle_start_0 = has_cycle(l0)
    cycle_start_1 = has_cycle(l1)

    if not cycle_start_0 and not cycle_start_1:
        return overlapping_no_cycle_lists(l0, l1)
    elif (cycle_start_0 and not cycle_start_1) or (not cycle_start_0 and cycle_start_1):
        # Exactly 1 of the lists has a cycle,
        # hence, no overlap between the lists.
        return None

    # At this stage, both lists are known to have cycles.
    # Determine whether both lists end in a common cycle
    # by making one pass through the 1st cycle:
    #   at each iteration,
    #   check if that iteration's node _is_ the 2nd cycle's start node.
    temp = cycle_start_0
    have_overlap = temp is cycle_start_1

    while temp.next is not cycle_start_0:
        if have_overlap:
            break
        temp = temp.next
        have_overlap = temp is cycle_start_1

    return cycle_start_0 if have_overlap else None
