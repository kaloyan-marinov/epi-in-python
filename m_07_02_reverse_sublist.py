from typing import Optional

from m_07_00_A_singly_linked_list import ListNode


def reverse_sublist(
    L: Optional[ListNode],
    start: int,
    finish: int,
) -> Optional[ListNode]:
    """
    If `L` is not `None`,
    assume its nodes are numbered beginning at 1
    (i.e. the head node is the 1st node).

    Return the head node of a new linked list,
    which is obtained from `L` by reversing the order of the nodes
    from the `start`-th node to the `finish`-th node, inclusive.

    Assume the triplet `L, start, finish` is a valid one.

    This solution allocates only an O(1) number of additional nodes.

    time:  O(finish)
    """

    dummy_head = ListNode(data=0, next=L)

    s_prev = dummy_head
    # Advance `s_prev` until it becomes the sublist's head.
    for _ in range(1, start):  # 1, ..., start - 1
        s_prev = s_prev.next

    # Reverse the sublist.
    n = s_prev.next
    for _ in range(finish - start):
        n_next = n.next
        # fmt: off
        (
            s_prev.next,
            n.next,
            n_next.next,
        ) = (
            n_next,
            n_next.next,
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
