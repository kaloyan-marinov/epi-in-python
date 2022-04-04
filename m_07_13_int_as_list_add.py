from typing import Optional

from m_07_00_A_singly_linked_list import ListNode


def add_two_numbers(L1: ListNode, L2: ListNode) -> ListNode:
    """
    (
    This is my solution.
    While it works, the official solution is arguably more elegant.
    )

    Assume that each of `L1` and `L2` represents an unbounded integer, i.e.
        (a) the `data` field of each node stores a [decimal] digit,
        (b) the least significant digit is stored in the head node, and
        (c) the `data` field of the tail node is non-zero.

    Return the head of a linked list,
    which corresponds to the sum of the integers represented by `L1` and `L2`.

    time:  O(n + m)
           n := the # of nodes in `L1`
           m := the # of nodes in `L2`

    space: O(max(n, m))
    """

    dummy_head = ListNode(data=0, next=None)

    L = dummy_head
    while L1 or L2:
        s = L.data // 10
        if L1:
            s += L1.data
        if L2:
            s += L2.data

        L.data %= 10

        L_next = ListNode(data=s, next=None)
        L.next = L_next

        L = L_next
        if L1:
            L1 = L1.next
        if L2:
            L2 = L2.next

    if L.data > 9:
        L_next = ListNode(data=L.data // 10, next=None)
        L.data %= 10
        L.next = L_next

    return dummy_head.next


def add_two_numbers_2(L1: ListNode, L2: ListNode) -> Optional[ListNode]:
    """
    (This is the official solution.)

    Assume that each of `L1` and `L2` represents an unbounded integer, i.e.
        (a) the `data` field of each node stores a [decimal] digit,
        (b) the least significant digit is stored in the head node, and
        (c) the `data` field of the tail node is non-zero.

    Return the head of a linked list,
    which corresponds to the sum of the integers represented by `L1` and `L2`.

    time:  O(n + m)
           n := the # of nodes in `L1`
           m := the # of nodes in `L2`

    space: O(max(n, m))
    """

    dummy_head = ListNode(data=0, next=None)

    L = dummy_head
    carry = 0
    while L1 or L2 or carry > 0:
        s = carry + (L1.data if L1 else 0) + (L2.data if L2 else 0)

        L.next = ListNode(data=s % 10)

        L = L.next
        L1 = L1.next if L1 else None
        L2 = L2.next if L2 else None
        carry = s // 10

    return dummy_head.next


if __name__ == "__main__":
    L1 = ListNode.from_list([6, 7, 1, 9, 9])
    L2 = ListNode.from_list([3, 3, 1, 7, 4, 4, 5, 3, 0, 5, 6, 5, 1, 7, 0, 1, 8, 5])

    L = add_two_numbers(L1, L2)
