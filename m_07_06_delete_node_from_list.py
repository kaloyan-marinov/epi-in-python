"""
Given a node in a singly-linked list,
deleting it in O(1) time appears impossible
b/c its predecessor's `next` field has to be updated.

However, that can be achieved
provided the following two conditions are satisfied:

    (a) the node to delete is not the last one in the list, and

    (b) it is easy to copy the value/`data` part of a node.
"""

from m_07_00_common import ListNode


def deletion_from_list(node_to_delete: ListNode) -> None:
    """
    Assume `node_to_delete` is not the tail node.

    time:  O(1)
    space: O(1)
    """
    # Copy the next node's data into the current node.
    node_to_delete.data = node_to_delete.next.data

    # Delete the next node.
    node_to_delete.next = node_to_delete.next.next
