class Queue:
    """
    This implementation tracks and maintains the private fields
    in such a way as to ensure that,
    at any given moment,
    the queue's head is `self._available_entries[self._start]`
    and its tail is `self._available_entries[self._final]`.
    """

    SCALE_FACTOR = 2

    def __init__(self, capacity: int) -> None:
        self._available_entries = [None] * capacity
        self._num_occupied_entries = 0
        self._start = 0
        self._final = 0

    def enqueue(self, x: int) -> None:
        if self._num_occupied_entries == len(self._available_entries):
            # Make the queue elements appear consecutively.
            self._available_entries = (
                self._available_entries[self._start :]
                + self._available_entries[: self._final]
            )

            # Reset the head and tail.
            self._start = 0
            self._final = self._num_occupied_entries

            # Resize the underlying array.
            count_new_entries = (self.SCALE_FACTOR - 1) * len(self._available_entries)
            self._available_entries += [None] * count_new_entries

        # Enqueue x.
        self._available_entries[self._final] = x
        self._final = (self._final + 1) % len(self._available_entries)
        self._num_occupied_entries += 1

    def dequeue(self) -> int:
        value = self._available_entries[self._start]
        # Note that the array entry doesn't have to be set to `None`.

        self._start = (self._start + 1) % len(self._available_entries)
        self._num_occupied_entries -= 1

        return value

    def size(self) -> int:
        return self._num_occupied_entries


if __name__ == "__main__":
    q = Queue(1)

    q.enqueue(-394)
    q.enqueue(-304)

    v = q.dequeue()
    print(v)
