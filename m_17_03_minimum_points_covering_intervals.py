from typing import List

import typing


class Interval(typing.NamedTuple):
    left: int
    right: int


def find_minimum_visits(intervals: List[Interval]) -> int:
    intervals.sort(key=lambda i: (i.left, i.right - i.left))

    points: List[int] = []
    idx = 0
    while idx < len(intervals):

        intersection = intervals[idx]

        next_idx = idx + 1
        while (
            next_idx < len(intervals) and intersection.right >= intervals[next_idx].left
        ):
            intersection = Interval(
                left=max(intersection.left, intervals[next_idx].left),
                right=min(intersection.right, intervals[next_idx].right),
            )
            next_idx += 1

        points.append(intersection.left)  # or any pt. inside

        idx = next_idx

    return len(points)


import operator


def find_minimum_visits(intervals: List[Interval]) -> int:
    intervals.sort(
        key=operator.attrgetter("right"),
    )

    last_visit_time = float("-inf")
    count_visits = 0
    for interval in intervals:
        if interval.left > last_visit_time:
            # The current right endpoint, which is `last_visit_time`,
            # will not cover [`interval` and therefore] any more intervals.

            last_visit_time = interval.right
            count_visits += 1

    return count_visits


if __name__ == "__main__":
    find_minimum_visits(
        [
            Interval(0, 3),
            Interval(2, 6),
            Interval(3, 4),
            Interval(6, 9),
        ]
    )
