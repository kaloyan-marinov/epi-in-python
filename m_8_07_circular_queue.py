class Queue:
    def __init__(self, capacity: int) -> None:
        self.entries = [None] * capacity
        self.capacity = capacity
        self.start = 0
        self.final = 0

    def enqueue(self, x: int) -> None:
        if self.final >= self.capacity:
            self.entries = (
                self.entries[self.start : self.final] + [None] * self.capacity
            )
            self.capacity = len(self.entries)
            self.final = self.final - self.start
            self.start = 0

        self.entries[self.final] = x
        self.final += 1

    def dequeue(self) -> int:
        value = self.entries[self.start]
        self.entries[self.start] = None
        self.start += 1
        return value

    def size(self) -> int:
        return self.final - self.start
