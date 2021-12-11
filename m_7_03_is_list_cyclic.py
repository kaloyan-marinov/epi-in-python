from typing import Optional

from m_7_00_common import ListNode


def has_cycle(head: ListNode) -> Optional[ListNode]:
    seen_nodes = set()
    while head:
        if id(head) in seen_nodes:
            return head
        else:
            seen_nodes.add(id(head))
            head = head.next


if __name__ == "__main__":
    L = ListNode.from_list([16, 14, 17, 10])

    result = has_cycle(L)
    if result is not None and isinstance(result, ListNode):
        print(result.data)
    else:
        print(None)
