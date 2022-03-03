from typing import Iterator, List

import heapq


def online_median(sequence: Iterator[int]) -> List[float]:
    """
    official but somewhat mysterious
    """
    min_heap: List[int] = []
    max_heap: List[int] = []

    medians = []

    for x in sequence:
        heapq.heappush(
            max_heap,
            -heapq.heappushpop(min_heap, x),
        )
        print()
        print(x)
        print(min_heap)
        print(max_heap)

        if len(max_heap) > len(min_heap):
            heapq.heappush(
                min_heap,
                -heapq.heappop(max_heap),
            )
            print(min_heap)
            print(max_heap)

        if len(min_heap) == len(max_heap):
            median = (min_heap[0] + (-max_heap[0])) / 2
        else:
            median = min_heap[0]
        medians.append(median)

    return medians


def online_median(sequence: Iterator[int]) -> List[float]:
    min_heap: List[int] = []  # stores the "larger" half seen so far
    max_heap: List[int] = []  # stores the "smaller" half seen so far

    medians = []

    for x in sequence:
        heapq.heappush(min_heap, x)

        heapq.heappush(
            max_heap,
            -heapq.heappop(min_heap),
        )
        print()
        print(x)
        print(min_heap)
        print(max_heap)

        # Ensure that
        # either both heaps will have the same # of elements,
        # or `min_heap` will have 1 more element than `max_heap`.
        if len(max_heap) > len(min_heap):
            heapq.heappush(
                min_heap,
                -heapq.heappop(max_heap),
            )
            print(min_heap)
            print(max_heap)

        if len(min_heap) == len(max_heap):
            median = (min_heap[0] + (-max_heap[0])) / 2
        else:
            median = min_heap[0]
        medians.append(median)

    return medians


if __name__ == "__main__":
    sequence = iter([1, 0, 3, 5, 2, 0, 1])

    medians = online_median(sequence)

    print()
    print("medians:")
    print(medians)
