from typing import List, Iterator, Tuple

import math
import itertools
import heapq


class Star:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x, self.y, self.z = x, y, z

    @property
    def distance(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __lt__(self, rhs: "Star") -> bool:
        return self.distance < rhs.distance

    def __repr__(self):
        return str(self.distance)

    def __str__(self):
        return self.__repr__()

    def __eq__(self, rhs):
        return math.isclose(self.distance, rhs.distance)


def find_closest_k_stars(stars: Iterator[Star], k: int) -> List[Star]:
    min_heap: List[Tuple[float, Star]] = [
        (-s.distance, s) for s in itertools.islice(stars, k)
    ]
    heapq.heapify(min_heap)

    for s in stars:
        heapq.heappushpop(
            min_heap,
            (-s.distance, s),
        )

    return [t[1] for t in min_heap]
