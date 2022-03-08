from typing import List


class ListNode:
    def __init__(self, data: int = 0, next=None):
        # TODO: determine how to add a type annotation to `next`
        self.data = data
        self.next = next

    @classmethod
    def from_list(cls, values: List[int]):
        """
        TODO: (it should be possible to) refactor this method so that
              its `values` is `Iterator[int]` (instead of what it is now)
        """
        nodes = [cls(data=v) for v in values]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        return nodes[0]

    def __repr__(self):
        return f"<ListNode(data={self.data})>"

    def represent_all_nodes(self) -> str:
        stringified_values: List[str] = []

        it = self
        while it:
            stringified_values.append(str(it.data))
            it = it.next

        return " -> ".join(stringified_values)


def length(L: ListNode) -> int:
    l = 0
    while L:
        l += 1
        L = L.next
    return l


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


class DoublyLinkedListNode:
    def __init__(self, data: int = None):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head: DoublyLinkedListNode = None
        self.tail: DoublyLinkedListNode = None
        self._size: int = 0

    def __len__(self) -> int:
        return self._size

    def insert_after(self, value: int) -> None:
        node = DoublyLinkedListNode(data=value)

        node.prev = self.tail
        if self.tail:  # i.e. inserting into a non-empty doubly-linked list
            self.tail.next = node
        else:  # i.e. inserting in an empty doubly-linked list
            self.head = node
        self.tail = node

        self._size += 1

    def remove(self, node: DoublyLinkedListNode) -> None:
        if node.next:  # i.e. removing a node that is different from the tail
            node.next.prev = node.prev
        else:  # i.e. removing the tail
            self.tail = node.prev

        if node.prev:  # i.e. removing a node that is different from the head
            node.prev.next = node.next
        else:  # i.e. removing the head
            self.head = node.next

        node.next = None
        node.prev = None

        self._size -= 1
