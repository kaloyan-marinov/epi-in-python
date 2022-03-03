from typing import Iterator, List

import itertools
import heapq


def sort_approximately_sorted_array(
    sequence: Iterator[int],
    k: int,
) -> List[int]:
    """
    add m_10_03_sort_almost_sorted_array.py which is almost correct but has a few small bugs
    """

    min_heap = itertools.islice(sequence, k)
    heapq.heapify(min_heap)

    result = []
    while min_heap:
        next_value = next(sequence, None)
        if next_value is not None:
            heapq.heappush(min_heap, next_value)

        v = heapq.heappop(min_heap)
        result.append(v)

    return result


def sort_approximately_sorted_array_2(
    sequence: Iterator[int],
    k: int,
) -> List[int]:

    min_heap: List[int] = []

    # Push the first k elements onto `min_heap`,
    # stopping if there are fewer than k elements.
    for x in itertools.islice(sequence, k):
        heapq.heappush(min_heap, x)

    result = []

    # For each new element, push it onto `min_heap` and pop the smallest value.
    for x in sequence:
        smallest = heapq.heappushpop(min_heap, x)
        result.append(smallest)

    # At this stage, `sequence` has been exhausted,
    # so iteratively extract the remaining elements.
    while min_heap:
        smallest = heapq.heappop(min_heap)
        result.append(smallest)

    return result
