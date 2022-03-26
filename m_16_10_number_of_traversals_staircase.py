import functools


"""
Assume that the client-provided input will satisfy `top >= maximum_step`.
"""


@functools.lru_cache(maxsize=None)
def number_of_ways_to_top(
    top: int,
    maximum_step: int,
) -> int:
    if top == 1:  # change to 0
        return 1

    return sum(
        number_of_ways_to_top(top - last_step, maximum_step)
        for last_step in range(1, maximum_step + 1)
        if last_step <= top
    )

    # fmt: off
    '''
    options: List[int] = []
    for last_step in range(1, maximum_step + 1):
        if last_step <= top:
            option = number_of_ways_to_top(top - last_step, maximum_step)
            options.append(option)

    return sum(options)
    '''
    # fmt: on


def number_of_ways_to_top(
    top: int,
    maximum_step: int,
) -> int:
    """
    Assume that `top >= maximum_step`.
    """

    @functools.lru_cache(maxsize=None)
    def _number_of_ways_to_h(h: int) -> int:

        if h <= 1:
            return 1

        return sum(
            _number_of_ways_to_h(h - i) for i in range(1, min(maximum_step, h) + 1)
        )

    return _number_of_ways_to_h(top)


if __name__ == "__main__":
    result = number_of_ways_to_top(2, 2)
