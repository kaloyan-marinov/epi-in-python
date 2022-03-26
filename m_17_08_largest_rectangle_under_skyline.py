from typing import List


def calculate_largest_rectangle_1(heights: List[int]) -> int:
    """
    This function is based on the idea of
    determining the widest rectangle that is "supported" by building `i`,
    for each `i`.

    In other words, the idea is,
    for each building `i`,
    to find the widest rectangle that building `i` acts as a "pillar" for.
    """

    max_rectangle_area = 0

    for i, h_i in enumerate(heights):
        left = i
        while left - 1 >= 0 and heights[left - 1] >= h_i:
            left = left - 1

        right = i
        while right + 1 <= len(heights) - 1 and heights[right + 1] >= h_i:
            right = right + 1

        max_rectangle_area = max(
            max_rectangle_area,
            (right - left + 1) * h_i,
        )

    return max_rectangle_area


def calculate_largest_rectangle_2(heights: List[int]) -> int:
    """
    This function is based on the same idea as the former one.

    However, this function's implementation
    is a modification of the former function's implementation,
    which (modification) sacrifices space for time.
    """

    # As we advance through the buildings:
    # (a) all we really need to keep track of is
    #     the buildings that have not been blocked yet, and
    # (b) we can "replace" existing buildings,
    #     whose heights equal the height of the current building,
    #     "with the current building"
    pillar_indices: List[int] = []

    max_rectangle_area = 0

    # By appending `[0]` to the `heights`,
    # we can uniformly handle the computation for the rectangle area here.
    for i, h_i in enumerate(heights + [0]):

        while pillar_indices and heights[pillar_indices[-1]] >= h_i:
            height = heights[pillar_indices.pop()]

            if pillar_indices:
                width = i - (pillar_indices[-1] + 1)
            else:
                width = i

            max_rectangle_area = max(max_rectangle_area, height * width)

        pillar_indices.append(i)

    return max_rectangle_area


if __name__ == "__main__":
    heights = [1, 4, 2, 5, 6, 3, 2, 6, 6, 5, 2, 1, 3]
    result = calculate_largest_rectangle_2(heights)
