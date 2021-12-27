from typing import Optional

from m_7_00_common import ListNode


def add_two_numbers(L1: ListNode, L2: ListNode) -> Optional[ListNode]:
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
        L = L_next  # can be commented out

    return dummy_head.next


def add_two_numbers_2(L1: ListNode, L2: ListNode) -> Optional[ListNode]:
    dummy_head = ListNode(data=0, next=None)

    L = dummy_head
    while L1 or L2:
        s = L.data // 10 + (L1.data if L1 else 0) + (L2.data if L2 else 0)

        L.data %= 10
        L_next = ListNode(data=s, next=None)
        L.next = L_next

        L = L.next
        if L1:
            L1 = L1.next
        if L2:
            L2 = L2.next

    if L.data > 9:
        s = L.data // 10

        L.data %= 10
        L_next = ListNode(data=s, next=None)
        L.next = L_next

        L = L.next  # can be commented out

    return dummy_head.next


if __name__ == "__main__":
    L1 = ListNode.from_list([6, 7, 1, 9, 9])
    L2 = ListNode.from_list([3, 3, 1, 7, 4, 4, 5, 3, 0, 5, 6, 5, 1, 7, 0, 1, 8, 5])

    L = add_two_numbers(L1, L2)
