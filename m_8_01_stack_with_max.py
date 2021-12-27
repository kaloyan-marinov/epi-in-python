import collections
from typing import List


class StackBruteForce:
    def __init__(self):
        self.values = []

    def empty(self) -> bool:
        return len(self.values) == 0

    def push(self, x: int) -> None:
        self.values.append(x)

    def pop(self) -> int:
        return self.values.pop()

    def max(self) -> int:
        """
        time: O(n)
        """
        return max(self.values)


ElementWithCachedMax = collections.namedtuple(
    "ElementWithCachedMax",
    ("element", "max"),
)


class Stack:
    def __init__(self) -> None:
        self._element_max_pairs: List[ElementWithCachedMax] = []

    def empty(self) -> bool:
        return len(self._element_max_pairs) == 0

    def push(self, x: int) -> None:
        self._element_max_pairs.append(
            ElementWithCachedMax(
                x,
                x if self.empty() else max(x, self.max()),
            )
        )

    def pop(self) -> int:
        return self._element_max_pairs.pop().element

    def max(self) -> int:
        """
        time: O(1)
        """
        return self._element_max_pairs[-1].max
