from typing import Optional

from m_07_00_common import ListNode


def merge_two_sorted_lists(
    L1: Optional[ListNode],
    L2: Optional[ListNode],
) -> Optional[ListNode]:
    """
    Assume that each of `L1` and `L2`

        either equals `None`,

        or is the head node of a linked list,
        whose data are numbers that appear in non-decreasing order.

    Return the head node of a new linked list,
    which consists of the merge of `L1` and `L2`.

    This solution allocates only an O(1) number of additional nodes.
    """

    # Create a placeholder for the result.
    dummy_head = ListNode()
    tail = dummy_head

    while L1 and L2:
        if L1.data <= L2.data:
            tail.next = L1
            L1 = L1.next
        else:
            tail.next = L2
            L2 = L2.next

        tail = tail.next

    # Append the remaining nodes of L1 or L2.
    tail.next = L1 or L2

    return dummy_head.next


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
