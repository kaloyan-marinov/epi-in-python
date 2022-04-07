class Queue:
    """
    A [LIFO] queue data structure.
    Its implementation is based on
    a `List`/array that is utilized in an efficient “cyclic” fashion.

    This implementation tracks and maintains the private fields
    in such a way as to ensure that,
    at any given moment,
    the queue's head is `self._available_entries[self._start]`
    and its tail is `self._available_entries[self._final]`.
    """

    def __init__(self, capacity: int) -> None:
        self._available_entries = [None] * capacity
        self._num_occupied_entries = 0
        self._start = 0
        self._final = 0

    def enqueue(self, x: int) -> None:
        """
        amortized time:  O(1)
        """

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
            count_new_entries = len(self._available_entries)
            self._available_entries += [None] * count_new_entries

        # Enqueue x.
        self._available_entries[self._final] = x
        self._final = (self._final + 1) % len(self._available_entries)
        self._num_occupied_entries += 1

    def dequeue(self) -> int:
        """
        time:  O(1)
        """

        value = self._available_entries[self._start]
        self._available_entries[self._start] = None  # NB: this isn't necessary!

        self._start = (self._start + 1) % len(self._available_entries)
        self._num_occupied_entries -= 1

        return value

    def size(self) -> int:
        """
        Return the number of occupied entries
        (which is <= the number of all available entries).

        time:  O(1)
        """

        return self._num_occupied_entries
