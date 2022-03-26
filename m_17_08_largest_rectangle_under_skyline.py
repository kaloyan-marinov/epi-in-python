from typing import List


def calculate_largest_rectangle(heights: List[int]) -> int:
    """
    This is _very_ incomplete and consequently also incorrect.
    """
    start_indices: List[int] = [None] * len(heights)
    start_indices[0] = 0

    max_area = float("-inf")

    for i, h_i in enumerate(heights[1:]):
        # if heights[i - 1] <= h_i:
        if heights[i - 1] > h_i:
            start_indices[i] = start_indices[i - 1]
        else:
            start_indices[i] = i

        max_area = max(
            max_area,
            (i - start_indices[i] + 1) * h_i,
        )

    return max_area


def calculate_largest_rectangle(heights: List[int]) -> int:
    pillar_indices: List[int] = []

    max_rectangle_area = 0

    # By appending `[0]` to the `heights`,
    # we can uniformly handle the computation for the rectangle area here.
    for i, h_i in enumerate(heights + [0]):

        while pillar_indices and heights[pillar_indices[-1]] >= h_i:
            height = heights[pillar_indices.pop()]

            # width = i if not pillar_indices else i - pillar_indices[-1] - 1
            if pillar_indices:
                width = i - (pillar_indices[-1] + 1)
            else:
                width = i

            max_rectangle_area = max(max_rectangle_area, height * width)

        pillar_indices.append(i)

    return max_rectangle_area


if __name__ == "__main__":
    heights = [1, 4, 2, 5, 6, 3, 2, 6, 6, 5, 2, 1, 3]
    result = calculate_largest_rectangle(heights)
