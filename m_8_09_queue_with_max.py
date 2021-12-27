from typing import Any, Deque

import collections


class QueueWithMax:
    def __init__(self):
        self._entries: Deque[Any] = collections.deque()
        self._candidates: Deque[Any] = collections.deque()

    def enqueue(self, x: int) -> None:  # Harder than `dequeue`!
        self._entries.append(x)

        while self._candidates and self._candidates[-1] < x:
            self._candidates.pop()

        self._candidates.append(x)

    def dequeue(self) -> int:
        v = self._entries.popleft()

        if self._candidates[0] == v:
            self._candidates.popleft()

        return v

    def max(self):
        return self._candidates[0]
