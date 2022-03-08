from typing import List


def h_index(citations: List[int]) -> int:
    """
    sorted_citations = sorted(citations)

    for i, c_i in enumerate(sorted_citations):
        if c_i >= len(sorted_citations) - i:
            return len(sorted_citations) - i
    """
    citations.sort(reverse=True)

    for i, c_i in enumerate(citations):
        if c_i < i + 1:
            return i

    return 0


def h_index_2(citations: List[int]) -> int:
    citations.sort(reverse=True)

    h = 0
    for i, c_i in enumerate(citations):
        if c_i >= i + 1:
            h += 1  # or:   h = i + 1
        else:
            break

    return h


# A = [1]
A = [12, 12, 14, 19, 19, 19, 20, 20, 21, 21, 21, 22]

print(h_index(A))
