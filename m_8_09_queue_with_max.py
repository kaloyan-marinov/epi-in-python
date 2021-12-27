from typing import Any, Deque

import collections


class QueueWithMax:
    """
    Consider a queue element `s`,
    which entered the queue before a later element `x` with `x > s`.
    Since `s` will be dequeued before `x`,
    `s` can never in the future become the queue's max
    (regardless of any subsequent enqueues and/or dequeues).

    The idea is to eliminate elements like the above-described `s`
    from consideration [for the queue's max]
    - we can do that by maintaining a separate deque of those queue elements,
    for each of which there doesn't exist a "later and greater" entity.
    """

    def __init__(self):
        self._entries: Deque[Any] = collections.deque()
        self._candidates_for_max: Deque[Any] = collections.deque()

    def enqueue(self, x: int) -> None:  # Harder than `dequeue`!
        self._entries.append(x)

        while self._candidates_for_max and x > self._candidates_for_max[-1]:
            self._candidates_for_max.pop()

        self._candidates_for_max.append(x)

    def dequeue(self) -> int:
        v = self._entries.popleft()

        if self._candidates_for_max[0] == v:
            self._candidates_for_max.popleft()

        return v

    def max(self):
        return self._candidates_for_max[0]
