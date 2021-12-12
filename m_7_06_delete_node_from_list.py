from m_7_00_common import ListNode


def deletion_from_list(node_to_delete: ListNode) -> None:
    """
    Assume `node_to_delete` is not the tail node.
    """
    n = node_to_delete

    n.data = n.next.data

    n_next_next = n.next.next
    n.next.next = None
    n.next = n_next_next
