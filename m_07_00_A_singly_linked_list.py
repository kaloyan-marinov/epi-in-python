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
