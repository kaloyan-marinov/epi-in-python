from typing import Optional

from m_7_00_common import ListNode


def even_odd_merge(L: Optional[ListNode]) -> Optional[ListNode]:
    if L is None:
        return

    even = L
    odd = L.next

    while odd and odd.next:
        odd_next = odd.next
        # fmt: off
        (
            even.next,
            odd.next,
            odd_next.next,
        ) = (
            odd.next,
            odd_next.next,
            even.next
        )
        # fmt: on

        even = even.next
        odd = odd.next

    return L
