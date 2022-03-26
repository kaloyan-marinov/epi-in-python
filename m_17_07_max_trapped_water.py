from typing import List


def get_max_trapped_water(heights: List[int]) -> int:
    """
    Assume that `len(heights) >= 2`.
    """
    max_water = float("-inf")

    for i in range(len(heights) - 1):
        for j in range(i + 1, len(heights)):
            area_i_j = (j - i) * min(heights[i], heights[j])
            if area_i_j > max_water:
                max_water = area_i_j

    return max_water


def get_max_trapped_water_2(heights: List[int]) -> int:
    """
    Assume that `len(heights) >= 2`.
    """
    max_water = float("-inf")

    i = 0
    j = len(heights) - 1

    while i < j:
        area_i_j = (j - i) * min(heights[i], heights[j])

        if area_i_j > max_water:
            max_water = area_i_j

        if heights[i] < heights[j]:
            i += 1
        elif heights[i] > heights[j]:
            j -= 1
        else:  # i.e. `heights[i] == heights[j]`
            i += 1
            j -= 1

    return max_water
