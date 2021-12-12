from typing import Optional

from m_7_00_common import ListNode


def remove_kth_last(L: ListNode, k: int) -> Optional[ListNode]:
    """
    Remove the k-th last element from (the linked list starting at) L.
    Return the head node of the resulting list.
    """
    slow = L
    fast = L

    for _ in range(k):
        fast = fast.next

    if fast is None:  # NB: if the k-th last element is the original head node
        L = L.next
    else:
        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

    return L  # NB: return the head node of the resulting list


if __name__ == "__main__":
    L = ListNode.from_list([2, 1])
    k = 2

    L = remove_kth_last(L, k)
