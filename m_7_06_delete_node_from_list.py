from m_7_00_common import ListNode


def deletion_from_list(node_to_delete: ListNode) -> None:
    """
    Assume `node_to_delete` is not the tail node.
    """
    n = node_to_delete  # actually, can use `node_to_delete` directly instead of `n`

    n.data = n.next.data

    n_next_next = n.next.next
    n.next.next = None  # actually, this can be commented out, b/c `n.next` represents the deleted node
    n.next = n_next_next
