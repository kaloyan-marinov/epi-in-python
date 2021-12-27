class Queue:
    """
    This class implements a queue using 2 stacks.
    """

    def __init__(self):
        self._stack_1 = []
        self._stack_2 = []

    def enqueue(self, x: int) -> None:
        """
        time: O(1)
        """
        self._stack_1.append(x)

    def dequeue(self) -> int:
        """
        time: O(n)
              n := the # of entries
        """
        while self._stack_1:
            self._stack_2.append(self._stack_1.pop())
        v = self._stack_2.pop()
        while self._stack_2:
            self._stack_1.append(self._stack_2.pop())
        return v
