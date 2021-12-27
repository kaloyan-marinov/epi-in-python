from collections import namedtuple
from typing import Iterator, List


HeightIndexPair = namedtuple(
    "HeightIndexPair",
    ("height", "idx"),
)


def examine_buildings_with_sunset(sequence: Iterator[int]) -> List[int]:
    """
    `sequence`:     represents buildings in east-to-west order,
                    with each building specified by its height
    """
    height_index_pairs: List[HeightIndexPair] = []

    for i, s_i in enumerate(sequence):
        if height_index_pairs and height_index_pairs[-1].height <= s_i:
            while height_index_pairs and height_index_pairs[-1].height <= s_i:
                height_index_pairs.pop()
            height_index_pairs.append(HeightIndexPair(s_i, i))
        else:
            height_index_pairs.append(HeightIndexPair(s_i, i))

    return [h_i_p.idx for h_i_p in reversed(height_index_pairs)]


if __name__ == "__main__":
    sequence = [6, 3, 4]
    heights = examine_buildings_with_sunset(sequence)
    print(heights)  # `[6, 4]` (but `[2, 0]` is expected)
