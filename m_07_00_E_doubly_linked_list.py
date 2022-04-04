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
