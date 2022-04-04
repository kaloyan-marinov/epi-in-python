from m_07_00_A_singly_linked_list import ListNode


def length(L: ListNode) -> int:
    l = 0
    while L:
        l += 1
        L = L.next
    return l
