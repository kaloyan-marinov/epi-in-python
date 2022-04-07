class Queue:
    """
    A [LIFO] queue data structure.
    Its implementation is based on
    2 stack( data structure)s.

    The idea is to use:
    (a) the 1st stack for the enqueue operations,
    and (b) the 2nd stack the dequeue operations.

    time:   for `m` combined enqueue and dequeue operations,
            O(m)
            (because each element is pushed <= twice
                                   & popped <= twice)
    """

    def __init__(self):
        self._stack_1 = []
        self._stack_2 = []

    def enqueue(self, x: int) -> None:
        self._stack_1.append(x)

    def dequeue(self) -> int:
        if not self._stack_2:
            while self._stack_1:
                self._stack_2.append(self._stack_1.pop())

        return self._stack_2.pop()
