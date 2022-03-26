class A:
    def __init__(self, x: int) -> None:
        self.x = x

    def __eq__(self, other: 'A') -> bool:
        return isinstance(other, A) and self.x == other.x

    def __hash__(self) -> int:
        return self.x * 113 + 119


def main():
    u = A(42)
    v = A(42)

    U = (u,)
    V = (v,)

    s = set()
    s.add(U)

    for t in s:
        print(t[0].x)  # 42

    print(U in s)  # True
    print(V in s)  # True (b/c we implemented `__eq__` and `__hash__`)

    u.x = 28
    print(U in s)  # False (b/c `U.__hash__()` has changed)

    for t in s:
        print(t[0].x)  # 28


if __name__ == '__main__':
    main()

