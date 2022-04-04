from typing import Optional

from m_07_00_A_singly_linked_list import ListNode


def remove_kth_last_1(L: ListNode, k: int) -> Optional[ListNode]:
    """
    (This is my own solution.)

    Assume `L` has at least `k` nodes.

    Perform an in-place modification of the linked list starting at `L`, which consists in removing the list's `k`-th last element, and return the head node of the resulting list.

    This solution entails a single traversal of the list
    (and, in particular, does not rely on computing the length of the list).

    time:  O(n)
           where n := the # of nodes in `L`

    space: O(1)
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


def remove_kth_last_2(L: ListNode, k: int) -> Optional[ListNode]:
    """
    (This is the official solution. Admittedly, it is safer than the preceding one.)

    Assume `L` has at least `k` nodes.

    Perform an in-place modification of the linked list starting at `L`,
    which consists in removing the list's `k`-th last element,
    and return the head node of the resulting list.

    This solution entails a single traversal of the list
    (and, in particular, does not rely on computing the length of the list).

    time:  O(n)
           where n := the # of nodes in `L`

    space: O(1)
    """

    dummy_head = ListNode(data=0, next=L)

    first = dummy_head.next
    for _ in range(k):
        first = first.next

    second = dummy_head
    while first:
        first = first.next
        second = second.next

    # `second` is now the (k + 1)-th last node.
    second.next = second.next.next

    return dummy_head.next


if __name__ == "__main__":
    L = ListNode.from_list([2, 1])
    k = 2

    L = remove_kth_last_1(L, k)
