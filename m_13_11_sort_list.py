from typing import List, Optional

from m_07_00_common import ListNode


def stable_sort_list_1(L: ListNode) -> Optional[ListNode]:
    """
    This implements an algorithm based on brute force.

    time:  O(n^2)
           where n:= the # of nodes in L

    space: O(n)
    """

    dummy_head: ListNode = ListNode(data=float("-inf"), next=L)

    new_dummy_head: List = ListNode()
    new_L = new_dummy_head

    while L:

        # Find the first node, whose `data` field holds the list's smallest value.
        min_value = float("inf")
        it = L
        while it:
            if it.data < min_value:
                min_value = it.data
            it = it.next

        pre_node_with_min_value = dummy_head
        node_with_min_value = dummy_head.next
        while node_with_min_value.data != min_value:
            pre_node_with_min_value, node_with_min_value = (
                node_with_min_value,
                node_with_min_value.next,
            )

        # Delete that node from the original list.
        pre_node_with_min_value.next = node_with_min_value.next

        # Add the deleted node to "the end of `new_dummy_head`".
        node_with_min_value.next = None
        new_L.next = node_with_min_value
        new_L = new_L.next

        L = dummy_head.next

    return new_dummy_head.next


def stable_sort_list_2(L: ListNode) -> Optional[ListNode]:
    """
    This implements an algorithm,
    which refines the previous one to improve its space complexity.

    The underlying idea is to iterate through and manipulate the (linked) list
    in a way ensuring that
    the sublist consisting of nodes up to and including the current one
    is sorted in increasing order.
    We do that by swapping [each out-of-place] `L.next`
    with [an appropriate one of its] predecessors in the list.

    time:  O(n^2)

    space: O(n)
    """

    dummy_head = ListNode(next=L)

    while L and L.next:
        if L.data > L.next.data:
            target = L.next

            # Find an "appropriate predecessor".
            pre = dummy_head
            while pre.next.data < target.data:
                pre = pre.next

            # Delete `target` from its original location.
            L.next = target.next

            # Add the deleted `target` right after `pre`.
            # fmt: off
            temp, pre.next = pre.next, target
            target.next = temp
            '''
            pre_next = pre.next
            pre.next = target
            target.next = pre_next
            '''
            '''
            pre.next, target.next = target, pre.next
            '''
            # fmt: on
        else:
            L = L.next

    return dummy_head.next


from m_07_01_sorted_lists_merge import (
    merge_two_sorted_lists_2 as merge_two_sorted_lists,
)


def stable_sort_list_3(L: ListNode) -> Optional[ListNode]:
    """
    This implements an algorithm,
    which improves the previous one
    - both in terms of time and space complexity.

    The underlying idea is
    to implement a recursive approach, in which we recurse down on equal-sized sublists.
    """

    # Base cases for the recursion, in which the solution is immediately available.
    if L is None or L.next is None:
        return L

    # Find the midpoint of `L` using a slow pointer and a fast one.
    pre_slow = None
    slow = L
    fast = L
    while fast and fast.next:
        pre_slow = slow
        slow = slow.next
        fast = fast.next.next

    # Split the list into 2 equal-sized sublists.
    if pre_slow:
        pre_slow.next = None

    return merge_two_sorted_lists(
        stable_sort_list_3(L),
        stable_sort_list_3(slow),
    )


if __name__ == "__main__":
    L = ListNode.from_list([2147483647, 0, -2147483648])
    stable_sort_list_1(L)
