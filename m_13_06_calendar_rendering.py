from typing import List

import collections


Event = collections.namedtuple(
    "Event",
    ("start", "finish"),
)


def find_max_simultaneous_events_1(A: List[Event]) -> int:
    # fmt: off
    endpoints: List[int] = [
        p for event in A
            for p in (event.start, event.finish)
    ]
    # fmt: on

    count_max = float("-inf")
    for e_p in endpoints:
        count_e_p = 0
        for a in A:
            if a.start <= e_p <= a.finish:
                count_e_p += 1

        count_max = max(count_max, count_e_p)

    return count_max


# fmt: off
'''
Endpoint = collections.namedtuple(
    "Endpoint",
    ("time", "is_start"),
)


def find_max_simultanous_events_2(A: List[Event]) -> int:
    # fmt: off
    endpoints: List[Endpoint] = [
        e_p for event in A
                for e_p in (
                    Endpoint(event.start, True),
                    Endpoint(event.finish, False),
                )
    ]
    # fmt: on

    endpoints.sort(
        key=lambda e_p: (e_p.time, not e_p.is_start)
    )  # `False < True` evaluates to `True`

    max_count_concurrent_events = 0
    count_concurrent_events = 0
    for e_p in endpoints:
        if e_p.is_start:
            count_concurrent_events += 1
            max_count_concurrent_events = max(
                max_count_concurrent_events,
                count_concurrent_events,
            )
        else:
            count_concurrent_events -= 1

    return max_count_concurrent_events
'''
# fmt: on


from typing import NamedTuple, Literal


class Endpoint(NamedTuple):
    time: int
    is_finish: Literal[0, 1]


def find_max_simultaneous_events_2(A: List[Event]) -> int:
    # fmt: off
    endpoints: List[Endpoint] = [
        e_p for event in A
                for e_p in (
                    Endpoint(event.start, 0),
                    Endpoint(event.finish, 1),
                )
    ]
    # fmt: on

    endpoints.sort()

    max_count_concurrent_events = 0
    count_concurrent_events = 0
    for e_p in endpoints:
        if e_p.is_finish == 0:
            count_concurrent_events += 1
            max_count_concurrent_events = max(
                max_count_concurrent_events,
                count_concurrent_events,
            )
        else:  # i.e. e_p.is_finish == 1
            count_concurrent_events -= 1

    return max_count_concurrent_events
