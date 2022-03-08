from typing import List


class Name:
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name, self.last_name = first_name, last_name

    def __lt__(self, other) -> bool:
        return (
            self.first_name < other.first_name
            if self.first_name != other.first_name
            else self.last_name < other.last_name
        )


def eliminate_duplicate_1(A: List[Name]) -> None:
    A.sort()

    indices = []
    for i, a_i in enumerate(A):
        if i == 0:
            indices.append(i)
        elif a_i.first_name != A[i - 1].first_name:
            indices.append(i)

    A[:] = [A[idx] for idx in indices]


def eliminate_duplicate_2(A: List[Name]) -> None:
    first_name_2_repr = {}

    for a in A:
        if a.first_name not in first_name_2_repr:
            first_name_2_repr[a.first_name] = a

    for i, repr_i in enumerate(first_name_2_repr.values()):
        A[i] = repr_i
    n_unique_first_names = len(first_name_2_repr)
    del A[n_unique_first_names:]  # NB: a valid way of modifying a list in-place!


def eliminate_duplicate_3(A: List[Name]) -> None:
    # Make "equal/identical" elements become neighbors.
    A.sort()

    write_idx = 1
    for candidate in A[1:]:
        if candidate.first_name != A[write_idx - 1].first_name:
            A[write_idx] = candidate
            write_idx += 1

    del A[write_idx:]  # NB: a valid way of modifying a list in-place!


if __name__ == "__main__":
    A = [
        Name(first, last) for first, last in [["Foo", "1"], ["ABC", "1"], ["Foo", "1"]]
    ]

    eliminate_duplicate_1(A)

    print(A)
