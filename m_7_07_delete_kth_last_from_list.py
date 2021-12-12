from typing import Optional

from m_7_00_common import ListNode


def remove_kth_last(L: ListNode, k: int) -> Optional[ListNode]:
    slow = L
    fast = L

    for _ in range(k):
        fast = fast.next

    while fast.next:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next


if __name__ == "__main__":
    L = ListNode.from_list([2, 1])
    k = 2

    L = remove_kth_last(L, k)
