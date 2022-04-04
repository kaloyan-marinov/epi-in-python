from typing import List, Optional

from m_7_00_common import ListNode, length as compute_length


def cyclically_right_shift_list(L: Optional[ListNode], k: int) -> Optional[ListNode]:
    # Guard clause against an empty linked list.
    if not L:
        return

    length = compute_length(L)

    # Handle the special case,
    # in which the resulting list is the identical to the input list.
    k %= length
    if k == 0:
        return L

    # Handle the general case,
    # in which the head of the resulting list is different from that of the input list.
    head = L
    new_tail = None
    new_head = None
    tail = None

    idx = 1
    while L:
        if idx == length - k:
            new_tail = L
            new_head = L.next

        if idx == length:
            tail = L

        L = L.next
        idx += 1

    tail.next = head
    new_tail.next = None
    L = new_head

    return L


if __name__ == "__main__":
    # Test 1/507
    L = None
    k = 0
    new_head = cyclically_right_shift_list(L, k)
    print(new_head)  # None (as expected)

    # Test 9/507
    L = ListNode(data=1)
    k = 0
    new_head = cyclically_right_shift_list(L, k)
    print(new_head)  # <ListNode(data=1)> (as expected)
