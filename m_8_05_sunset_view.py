from collections import namedtuple
from typing import Iterator, List


def examine_buildings_with_sunset(sequence: Iterator[int]) -> List[int]:
    heights = []
    for i, s_i in enumerate(sequence):
        if heights and heights[-1] <= s_i:
            while heights and heights[-1] <= s_i:
                heights.pop()
            heights.append(s_i)
        else:
            heights.append(s_i)
    return heights


if __name__ == "__main__":
    sequence = [6, 3, 4]
    heights = examine_buildings_with_sunset(sequence)
    print(heights)  # `[6, 4]` (but `[2, 0]` is expected)
