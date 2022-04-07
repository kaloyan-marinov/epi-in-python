import collections

from typing import Deque


class Queue:
    """
    This implements a queue with a naively-implemented max API,
    which relies on composition with a `collections.deque`.
    """

    def __init__(self) -> None:
        self._data: Deque[int] = collections.deque()

    def enqueue(self, x: int) -> None:
        """
        time: O(1)
        """
        self._data.append(x)

    def dequeue(self) -> int:
        """
        time: O(1)
        """
        return self._data.popleft()

    def max(self) -> int:
        """
        time: O(n)
              where n := the # of entries
        """
        return max(self._data)
