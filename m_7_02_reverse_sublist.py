from typing import Optional

from m_7_00_common import ListNode


def reverse_sublist(L: ListNode, start: int, finish: int) -> Optional[ListNode]:
    dummy_head = ListNode(data=0, next=L)

    sublist_head = dummy_head
    for _ in range(1, start):
        sublist_head = sublist_head.next

    # Reverse sublist.
    sublist_iter = sublist_head.next
    for _ in range(finish - start):
        temp = sublist_iter.next
        sublist_iter.next, temp.next, sublist_head.next = (
            temp.next,
            sublist_head.next,
            temp,
        )

    return dummy_head.next


if __name__ == "__main__":
    L = ListNode.from_list([11, 3, 5, 7, 2])
    M = reverse_sublist(L, 2, 4)

    while M:
        print(M.data)
        M = M.next
