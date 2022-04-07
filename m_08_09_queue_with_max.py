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
    for each of which there doesn't exist a "later and greater" entry.

    (In particular, the last sentence implies that
    the auxiliary deque's entries will always be in non-increasing order.)


    For example:

    primary     [] enqueue 3 [3] enqueue 1 [3, 1] enqueue 3 [3, 1, 3] enqueue 2
                   -------->     -------->        -------->           --------> ...
    secondary   []    *      [3]    *      [3, 1]    *      [3, 3]       *

    ##############################################################################

    primary         [3, 1, 3, 2] enqueue 0 [3, 1, 3, 2, 0] enqueue 1 [3, 1, 3, 2, 0, 1]
                ...              -------->                 -------->
    secondary       [3, 3, 2]       *      [3, 3, 2, 0]              [3, 3, 2, 1]

    ##############################################################################

    primary         dequeue   [1, 3, 2, 0, 1] dequeue   [3, 2, 0, 1] enqueue 2
                ... -------->                 -------->              --------> ...
    secondary                 [3, 2, 1]                 [3, 2, 1]

    ##############################################################################

    primary         [3, 2, 0, 1, 2] enqueue 4 [3, 2, 0, 1, 2, 4] dequeue
                ...                 -------->                    --------> ...
    secondary       [3, 2, 2]                 [4]

    ##############################################################################

    primary         [2, 0, 1, 2, 4] enqueue 4 [2, 0, 1, 2, 4, 4]
                ...                 -------->
    secondary       [4]                       [4]
    """

    def __init__(self):
        self._entries: Deque[Any] = collections.deque()
        self._candidates_for_max: Deque[Any] = collections.deque()

    def enqueue(self, x: int) -> None:  # Harder than `dequeue`!
        """
        A single call may entail many ejections from the auxiliary deque.

        However, the amortized time complexity for `n` enqueues and dequeues is O(n),
        since an element can added and removed from the deque no more than once.
        """

        self._entries.append(x)

        while self._candidates_for_max and x > self._candidates_for_max[-1]:
            self._candidates_for_max.pop()

        self._candidates_for_max.append(x)

    def dequeue(self) -> int:
        """
        time:  O(1)
        """

        v = self._entries.popleft()

        if self._candidates_for_max[0] == v:
            self._candidates_for_max.popleft()

        return v

    def max(self):
        """
        time:  O(1)
        """

        return self._candidates_for_max[0]
