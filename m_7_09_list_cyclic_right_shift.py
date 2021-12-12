from typing import List, Optional

from m_7_00_common import ListNode, length as compute_length


def cyclically_right_shift_list(L: Optional[ListNode], k: int) -> Optional[ListNode]:
    length = compute_length(L)
    if length == 0:
        return

    k %= length

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

    if new_tail is not tail:
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
    print(new_head)  # None (but `<ListNode(data=1)>` is expected)
