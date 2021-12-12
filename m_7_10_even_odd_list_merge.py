from typing import Optional

from m_7_00_common import ListNode


def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    """
    Test 1/1015 gets stuck in an infinite loop.
    """

    if L is None:
        return

    even = L
    odd = L.next

    while odd and odd.next:
        # fmt: off
        (
            even.next,
            odd.next,
            odd.next.next,
        ) = (
            odd.next,
            odd.next.next,
            even.next
        )
        # fmt: on

        even = even.next
        odd = odd.next

    return L
