from typing import Iterator

import itertools


def find_missing_element(stream: Iterator[int]) -> int:
    """
    Assume that:
        - `stream` consists of 32-bit integers
        - `stream` will not exhaust all 32-bit integers

    Return one 32-bit integer, which was not present in the `stream`.
    """

    stream, stream_copy = itertools.tee(stream)

    num_buckets = 1 << 16

    upper_part_counts = [0] * num_buckets
    for x in stream:
        upper_part_x = x >> 16
        upper_part_counts[upper_part_x] += 1

    # At least one bucket contains strictly less than (1 << 16) elements.
    max_bucket_capacity = 1 << 16
    candidate_upper_part = next(
        i
        for i, u_p_count in enumerate(upper_part_counts)
        if u_p_count < max_bucket_capacity
    )

    # Determine all IP addresses in the stream,
    # whose first 16 bits are equal to `candidate_upper_part`.
    ip_counts = [0] * num_buckets
    for x in stream_copy:
        upper_part_x = x >> 16
        if upper_part_x == candidate_upper_part:
            # Record the presence of `x`'s 16 LSB.
            lower_part_x = x & ((1 << 16) - 1)
            ip_counts[lower_part_x] += 1

    # At least one of the LSB combinations is absent [from `stream`] - find it.
    for lower_part, lower_part_count in enumerate(ip_counts):
        if lower_part_count == 0:
            return (candidate_upper_part << 16) | lower_part
