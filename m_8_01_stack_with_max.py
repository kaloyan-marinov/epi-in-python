class Stack:
    def __init__(self):
        self.values = []

    def empty(self) -> bool:
        return len(self.values) == 0

    def push(self, x: int) -> None:
        self.values.append(x)

    def pop(self) -> int:
        return self.values.pop()

    def max(self) -> int:
        return max(self.values)
