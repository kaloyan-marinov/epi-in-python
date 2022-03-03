from typing import Deque, List, Tuple

import heapq
import collections


def k_largest_in_binary_heap(
    A: List[int],
    k: int,
) -> List[int]:
    """
    add m_10_06_k_largest_in_heap.py which seems overly complicated
    """
    min_heap: List[int] = []

    candidate_indices: Deque[int] = collections.deque([0])

    while candidate_indices:
        i = candidate_indices.popleft()
        if i >= len(A):
            continue

        candidate = A[i]

        if len(min_heap) < k:
            heapq.heappush(min_heap, candidate)

            candidate_indices.append(2 * i + 1)
            candidate_indices.append(2 * i + 2)
        else:  # i.e. len(min_heap) == k
            if candidate > min_heap[0]:
                heapq.heappushpop(
                    min_heap,
                    candidate,
                )

                candidate_indices.append(2 * i + 1)
                candidate_indices.append(2 * i + 2)

    return min_heap


def k_largest_in_binary_heap_2(
    A: List[int],
    k: int,
) -> List[int]:
    result: List[int] = []

    if k <= 0:
        return result

    # Initialize a max-heap, which stores each candidate as a (-value, index)-pair.
    # (Using the negative of `value` achieves the effect of a max-heap.)
    # The largest element in `A` is at index 0.
    candidate_max_heap: List[Tuple[int, int]] = [
        (-A[0], 0),
    ]

    for _ in range(k):
        candidate = heapq.heappop(candidate_max_heap)
        candidate_value, candidate_idx = -candidate[0], candidate[1]

        result.append(candidate_value)

        left_child_idx = 2 * candidate_idx + 1
        if left_child_idx < len(A):
            heapq.heappush(
                candidate_max_heap,
                (-A[left_child_idx], left_child_idx),
            )

        right_child_idx = 2 * candidate_idx + 2
        if right_child_idx < len(A):
            heapq.heappush(
                candidate_max_heap,
                (-A[right_child_idx], right_child_idx),
            )

    return result


if __name__ == "__main__":
    A = [10, 2, 9, 2, 2, 8, 8, 2, 2, 2, 2, 7, 7, 7, 7]
    k = 3

    k_largest = k_largest_in_binary_heap(A, k)
    print(k_largest)
