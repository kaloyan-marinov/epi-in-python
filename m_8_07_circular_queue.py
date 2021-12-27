class Queue:
    SCALE_FACTOR = 2

    def __init__(self, capacity: int) -> None:
        self._entries = [None] * capacity
        self._num_elements = 0
        self._start = 0
        self._final = 0

    def enqueue(self, x: int) -> None:
        if self._num_elements == len(self._entries):
            # Make the queue elements appear consecutively.
            self._entries = self._entries[self._start :] + self._entries[: self._final]

            # Reset the head and tail.
            self._start = 0
            self._final = self._num_elements

            # Resize the underlying array.
            count_new_entries = (self.SCALE_FACTOR - 1) * len(self._entries)
            self._entries += [0] * count_new_entries

        self._entries[self._final] = x
        self._final = (self._final + 1) % len(self._entries)
        self._num_elements += 1

    def dequeue(self) -> int:
        value = self._entries[self._start]
        self._start = (self._start + 1) % len(self._entries)
        self._num_elements -= 1
        return value

    def size(self) -> int:
        return self._num_elements


if __name__ == "__main__":
    q = Queue(1)

    q.enqueue(-394)
    q.enqueue(-304)

    v = q.dequeue()
    print(v)
