from typing import Optional

from m_7_00_common import ListNode


def merge_two_sorted_lists(
    L1: Optional[ListNode],
    L2: Optional[ListNode],
) -> Optional[ListNode]:
    head_node = L1 if L1.data <= L2.data else L2

    while L1.next is not None and L2.next is not None:
        print(L1.data)
        if L1.next.data <= L2.data:
            L1 = L1.next
            continue

        L2_next = L2.next
        L2.next = L1.next
        L1.next = L2

        L2 = L2_next

    if L2 is not None:
        L1.next = L2

    return head_node


if __name__ == "__main__":
    L1 = ListNode.from_list([-14, -13, -9, -6, -5, -2, -1, 1, 4, 7, 8, 10, 12, 13])
    L2 = ListNode.from_list(
        [
            -25,
            -23,
            -18,
            -18,
            -14,
            -8,
            -8,
            -6,
            -3,
            -2,
            -1,
            2,
            5,
            8,
            8,
            8,
            12,
            12,
            12,
            14,
            14,
            20,
            20,
            22,
            25,
            26,
        ]
    )

    h = merge_two_sorted_lists(L1, L2)
