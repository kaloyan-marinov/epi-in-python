from typing import List


class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

    @classmethod
    def from_list(cls, values: List[int]):
        nodes = [cls(data=v) for v in values]
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
        return nodes[0]


def length(L: ListNode) -> int:
    l = 0
    while L:
        l += 1
        L = L.next
    return l


def reverse_list(L: ListNode) -> ListNode:
    # new_head = L
    # while L:
    #     L_next = L.next
    #     L.next = new_head
    #     new_head = L
    #     L = L_next
    # return new_head
    dummy_head = ListNode(data=0, next=None)

    while L:
        L_next = L.next
        L.next = dummy_head.next
        dummy_head.next = L
        L = L_next

    return dummy_head.next
