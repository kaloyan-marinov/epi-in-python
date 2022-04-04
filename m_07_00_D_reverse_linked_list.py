from m_07_00_A_singly_linked_list import ListNode


def reverse_list(L: ListNode) -> ListNode:
    """
    Reverse the input linked list, by modifying it in-place.
    Return the head node of the reversed list.
    """
    dummy_head = ListNode(data=0, next=None)

    while L:
        L_next = L.next
        L.next = dummy_head.next
        dummy_head.next = L
        L = L_next

    return dummy_head.next
