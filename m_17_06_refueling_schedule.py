from typing import List
import typing


MPG = 20


def find_ample_city(
    gallons: List[int],
    distances: List[int],
) -> int:
    """
    Assume that an ample city exists.
    """

    reservoir = 0
    reservoir_min = float("inf")

    idx = None

    for i, (g_i, d_i) in enumerate(zip(gallons, distances)):
        g_needed_to_next_city = d_i / MPG
        reservoir += g_i - g_needed_to_next_city

        if reservoir < reservoir_min:
            idx = i
            reservoir_min = reservoir

    return idx + 1


class CityAndRemainingGas(typing.NamedTuple):
    city: int
    remaining_gallons: int


def find_ample_city_2(
    gallons: List[int],
    distances: List[int],
) -> int:
    """
    Assume that an ample city exists.
    """

    remaining_gallons = 0
    city_remaining_gallons_pair = CityAndRemainingGas(
        city=0, remaining_gallons=remaining_gallons
    )

    num_cities = len(gallons)
    for idx in range(1, num_cities):
        remaining_gallons += gallons[idx - 1] - distances[idx - 1] // MPG

        if remaining_gallons < city_remaining_gallons_pair.remaining_gallons:
            city_remaining_gallons_pair = CityAndRemainingGas(
                city=idx,
                remaining_gallons=remaining_gallons,
            )

    return city_remaining_gallons_pair.city
