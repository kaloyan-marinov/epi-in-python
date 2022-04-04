from typing import Optional

from m_07_00_common import ListNode


def even_odd_merge_1(L: Optional[ListNode]) -> Optional[ListNode]:
    """
    (This is my own solution.)

    Perform an in-place modification of the linked list starting at `L`
    by making the even-numbered nodes be followed by the odd-numbered nodes,
    and return the head of the resulting linked list.

    Consider the nodes of (the input linked list) `L` to be indexed starting at 0.

    time:  O(n)
           where n := the # of nodes in `L`

    space: O(1)
    """

    if L is None:
        return

    even = L
    odd = L.next

    while odd and odd.next:
        odd_next = odd.next  # NB: W/o defining this variable, infinite looping occurs!
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
    (This is the official solution.)

    Perform an in-place modification of the linked list starting at `L`
    by making the even-numbered nodes be followed by the odd-numbered nodes,
    and return the head of the resulting linked list.

    Consider the nodes of (the input linked list) `L` to be indexed starting at 0.

    time:  O(n)
           where n := the # of nodes in `L`

    space: O(1)
    """

    if L is None:
        return

    # Allocate 2 new nodes,
    # which will serve as dummy heads of 2 initially single-node lists.
    even_dummy_head = ListNode(data=17)
    odd_dummy_head = ListNode(data=17)

    # Re-use the nodes of the input list
    # by iterating through the list
    #    and appending even elements to the 1st "new list"
    #              and odd elements to the 2nd "new list".
    tails = [even_dummy_head, odd_dummy_head]
    turn = 0  # represents a 0/1 variable to indicate which list to append to.
    while L:
        tails[turn].next = L
        tails[turn] = tails[turn].next

        turn ^= 1  # Achieves alternation between even and odd. Same as `(turn + 1) % 2`

        L = L.next

    # Append "the odd list" to "the even one".
    tails[1].next = None
    tails[0].next = odd_dummy_head.next

    return even_dummy_head.next
