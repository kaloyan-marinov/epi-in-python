from typing import Optional

from m_7_00_common import ListNode


def even_odd_merge_1(L: Optional[ListNode]) -> Optional[ListNode]:
    """
    Consider the nodes of (the linked list) L to be indexed starting at 0.
    """

    if L is None:
        return

    even = L
    odd = L.next

    while odd and odd.next:
        odd_next = odd.next
        # fmt: off
        (
            even.next,
            odd.next,
            odd_next.next,
        ) = (
            odd.next,
            odd_next.next,
            even.next
        )
        # fmt: on

        even = even.next
        odd = odd.next

    return L


def even_odd_merge_2(L: Optional[ListNode]) -> Optional[ListNode]:
    """
    Consider the nodes of (the linked list) L to be indexed starting at 0.
    """

    if L is None:
        return

    # Allocate 2 new nodes,
    # which will serve as dummy heads of 2 initially single-node lists.
    even_dummy_head = ListNode(data=0, next=L)
    odd_dummy_head = ListNode(data=0, next=L)

    # Re-use the nodes of the input list
    # by iterating through the list
    #    and appending even elements to the 1st "new list"
    #              and odd elements to the 2nd "new list".
    tails = [even_dummy_head, odd_dummy_head]
    turn = 0  # represents a 0/1 variable to indicate which list to append to.
    while L:
        tails[turn].next = L
        L = L.next
        tails[turn] = tails[turn].next
        turn ^= 1  # achieves alternation between even and odd.

    # Append "the odd list" to "the even one".
    tails[1].next = None
    tails[0].next = odd_dummy_head.next

    return even_dummy_head.next
