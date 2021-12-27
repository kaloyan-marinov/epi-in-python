from collections import namedtuple
from typing import Iterator, List


def examine_buildings_with_sunset(sequence: Iterator[int]) -> List[int]:
    heights = []
    for i, s_i in enumerate(sequence):
        if heights and heights[-1] <= s_i:
            while heights and heights[-1] <= s_i:
                heights.pop()
            heights.append(i)
        else:
            heights.append(i)
    return heights


if __name__ == "__main__":
    sequence = [6, 3, 4]
    heights = examine_buildings_with_sunset(sequence)
    print(heights)  # `[2]` (but `[2, 0]` is expected)
