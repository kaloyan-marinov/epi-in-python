from typing import List, NamedTuple, Literal

import collections


Interval = collections.namedtuple(
    "Interval",
    ("left", "right"),
)


class Endpoint(NamedTuple):
    value: int
    is_right: Literal[0, 1]


def add_interval_1(
    disjoint_intervals: List[Interval],
    new_interval: Interval,
) -> List[Interval]:
    """
    time:  O(n * log n)

    space: O(n)
    """

    result: List[Interval] = []

    # fmt: off
    '''
    for i in disjoint_intervals:
        result.append(i)
    '''

    endpoints: List[Endpoint] = [
        e_p for d_i in disjoint_intervals
                for e_p in (
                    Endpoint(d_i.left, 0),
                    Endpoint(d_i.right, 1),
                )
    ]
    
    endpoints.append(Endpoint(new_interval.left, 0))
    endpoints.append(Endpoint(new_interval.right, 1))
    # fmt: on

    endpoints.sort()

    start = None
    final = float("-inf")
    count_start = (
        0  # Represents the # of start endpoints that are currently being handled.
    )
    # count_final = 0
    for e_p in endpoints:
        # The second condition _should_ be omittable.
        if start is None and e_p.is_right == 0:
            start = e_p.value
            count_start += 1
            continue

        # At this stage, we know that `start` is not `None`.
        if e_p.is_right == 0:
            count_start += 1
        else:  # i.e. `e_p.right == 1`
            count_start -= 1
            final = max(final, e_p.value)

        if count_start == 0:
            result.append(
                Interval(start, final),
            )
            start = None
            final = float("-inf")

    return result


def add_interval_2(
    disjoint_intervals: List[Interval],
    new_interval: Interval,
) -> List[Interval]:

    result: List[Interval] = []

    ii = 0

    # Process all (if any!) entries in `disjoint_intervals`,
    # each of which comes[/appears/is located] strictly before `new_interval`.
    while (
        ii < len(disjoint_intervals)
        and disjoint_intervals[ii].right < new_interval.left
    ):
        result.append(disjoint_intervals[ii])
        ii += 1

    # Process all (if any!) entries in `disjoint_intervals`,
    # each of which has a non-empty intersection with `new_interval`.
    union = new_interval
    while ii < len(disjoint_intervals) and disjoint_intervals[ii].left <= union.right:
        union = Interval(
            min(union.left, disjoint_intervals[ii].left),
            max(union.right, disjoint_intervals[ii].right),
        )
        ii += 1

    # Process all (if any!) entries in `disjoint_intervals`,
    # each of which comes[/appears/is located] strictly after `new_interval`.
    return result + [union] + disjoint_intervals[ii:]


if __name__ == "__main__":
    # fmt: off
    disjoint_intervals = [
        Interval(t[0], t[1])
        for t in [[6, 14], [18, 18], [22, 30], [32, 42], [51, 57], [59, 62], [66, 73], [78, 79], [84, 86], [92, 100], [108, 118], [119, 120], [123, 126], [130, 136], [139, 144], [152, 154], [160, 169], [173, 177], [182, 187], [191, 200], [205, 210], [217, 220], [230, 239], [249, 259], [260, 265], [266, 270], [273, 279], [281, 291], [292, 302], [312, 319], [320, 329], [336, 341], [346, 347], [353, 357], [362, 369], [371, 378], [382, 388], [392, 395], [403, 412], [420, 427], [432, 440], [445, 447], [452, 458], [460, 468], [476, 486], [487, 491], [492, 501], [511, 518], [526, 526], [532, 537], [538, 546]]
    ]
    new_interval = Interval(*[553, 572])
    # fmt: on

    add_interval_2(disjoint_intervals, new_interval)
