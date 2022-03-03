from typing import List, Tuple

import heapq


def merge_sorted_arrays(
    sorted_arrays: List[List[int]],
) -> List[int]:
    """
    works but missed the point completely
    """

    H = []
    heapq.heapify(H)

    for s_a in sorted_arrays:
        heapq.heapify(s_a)

        while s_a:
            item = heapq.heappop(s_a)
            heapq.heappush(H, item)

    return H


def merge_sorted_arrays(
    sorted_arrays: List[List[int]],
) -> List[int]:

    min_heap: List[Tuple[int, int]] = []

    # Initialize a list of iterators for each of the given `sorted_arrays`.
    sorted_array_iters = [iter(s_a) for s_a in sorted_arrays]

    # Push the 1st element from each iterator onto `min_heap`.
    for i, s_a_iter in enumerate(sorted_array_iters):
        first_element = next(s_a_iter, None)
        if first_element is not None:  # NB!
            heapq.heappush(
                min_heap,
                (first_element, i),
            )

    result = []
    while min_heap:
        smallest_entry, smallest_array_idx = heapq.heappop(min_heap)

        result.append(smallest_entry)

        smallest_array_iter = sorted_array_iters[smallest_array_idx]
        next_element = next(smallest_array_iter, None)
        if next_element is not None:  # NB!
            heapq.heappush(
                min_heap,
                (next_element, smallest_array_idx),
            )

    return result
