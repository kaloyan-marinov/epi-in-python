from typing import Optional

from m_7_00_common import ListNode


def has_cycle_1(head: ListNode) -> Optional[ListNode]:
    """
    time:  < O(n)
    space: < O(n)

    n := the length of (the linked list starting at) `head`
    """
    seen_nodes = set()
    while head:
        if id(head) in seen_nodes:
            return head
        else:
            seen_nodes.add(id(head))
            head = head.next


def has_cycle_2(head: ListNode) -> Optional[ListNode]:
    """
    time:  O(F) + O(C)
           = O(n) - O(F)
           for both pointers to reach the cycle

           O(C)
           for them to overlap

    n := # of nodes in list
    F := # of nodes to start of cycle
    C := # of nodes in cycle

    space: O(1)
    """
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        # Test if a cycle exists.
        if slow is fast:
            # Determine the cycle length.
            cycle_length = 1
            n = slow
            while n.next is not slow:  # NB: not "!="
                n = n.next
                cycle_length += 1

            # Find the 1st node on the cycle.
            slow_new = head

            fast_new = head
            for _ in range(cycle_length):
                fast_new = fast_new.next

            while slow_new is not fast_new:  # NB: not "!="
                slow_new = slow_new.next
                fast_new = fast_new.next

            return slow_new

    # No cycle exists.
    return None


if __name__ == "__main__":
    L = ListNode.from_list([16, 14, 17, 10])

    result = has_cycle_2(L)
    if result is not None and isinstance(result, ListNode):
        print(result.data)
    else:
        print(None)
