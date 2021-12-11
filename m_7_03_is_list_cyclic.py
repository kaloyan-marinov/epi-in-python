from typing import Optional

from m_7_00_common import ListNode


def has_cycle(head: ListNode) -> Optional[ListNode]:
    """
    Running this through EPIJudge crashes on the following test: 1/102.
    The given reason for the crash is
        ```
        exception message: unhashable type: 'ListNode'
        ```

    The problematic test in question is included below,
    namely in this module's `if __name__ == "__main__"` block.
    Curiously,
    using this repo's virtual environment to run that same test does not crash
    but returns the correct answer.
    """
    seen_nodes = set()
    while head:
        if head in seen_nodes:
            return head
        else:
            seen_nodes.add(head)
            head = head.next


if __name__ == "__main__":
    L = ListNode.from_list([16, 14, 17, 10])

    result = has_cycle(L)
    if result is not None and isinstance(result, ListNode):
        print(result.data)
    else:
        print(None)
