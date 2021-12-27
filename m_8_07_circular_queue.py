class Queue:
    def __init__(self, capacity: int) -> None:
        self._entries = [None] * capacity
        self._capacity = capacity
        self._start = 0
        self._final = 0

    def enqueue(self, x: int) -> None:
        if self._final >= self._capacity:
            self._entries = (
                self._entries[self._start : self._final] + [None] * self._capacity
            )
            self.capacity = len(self._entries)
            self._final = self._final - self._start
            self._start = 0

        self._entries[self._final] = x
        self._final += 1

    def dequeue(self) -> int:
        value = self._entries[self._start]
        self._entries[self._start] = None
        self._start += 1
        return value

    def size(self) -> int:
        return self._final - self._start
