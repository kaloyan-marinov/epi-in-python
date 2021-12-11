from typing import Optional

from m_7_00_common import ListNode


def reverse_sublist(L: ListNode, start: int, finish: int) -> Optional[ListNode]:
    dummy_head = ListNode(data=0, next=L)

    s_prev = dummy_head
    # Advance `s_prev` until it becomes the sublist's head.
    for _ in range(1, start):  # 1, ..., start - 1
        s_prev = s_prev.next

    # Reverse the sublist.
    s = s_prev.next
    for _ in range(finish - start):
        s_next = s.next
        # fmt: off
        (
            s_prev.next,
            s.next,
            s_next.next,
        ) = (
            s_next,
            s_next.next,
            s_prev.next,
        )
        # fmt: on

    return dummy_head.next


if __name__ == "__main__":
    L = ListNode.from_list([11, 3, 5, 7, 2])
    M = reverse_sublist(L, 2, 4)

    while M:
        print(M.data)
        M = M.next
