from typing import Optional

from m_7_00_common import ListNode, length as compute_length


def cyclically_right_shift_list(L: ListNode, k: int) -> Optional[ListNode]:
    # fmt: off
    '''
    (L: Optional[ListNode], k:int) -> Optional[ListNode]
    '''
    # fmt: on

    length = compute_length(L)

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

    # When the next statement is executed, the script crashes with
    #   ```
    #     File "m_7_09_list_cyclic_right_shift.py", line 15, in cyclically_right_shift_list
    #       k %= length
    #   ZeroDivisionError: integer division or modulo by zero
    #   ```
    new_head = cyclically_right_shift_list(L, k)
