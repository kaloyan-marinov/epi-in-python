import collections


Point2D = collections.namedtuple(
    "Point2D",
    ["x", "y"],
)


# fmt: off
def rectangles_intersection(
    r_1_llc: Point2D, r_1_urc: Point2D,
    r_2_llc: Point2D, r_2_urc: Point2D,
):
    """
    Determine the intersection of the rectangles r_1 and r_2,
    where each rectangle is specified by its lower-left corner and upper-right corner
    (i.e. by its "llc" and "urc").
    """
    intersection_x = _intervals_intersection(
        r_1_llc.x, r_1_urc.x,
        r_2_llc.x, r_2_urc.x,
    )
    intersection_y = _intervals_intersection(
        r_1_llc.y, r_1_urc.y,
        r_2_llc.y, r_2_urc.y,
    )

    if not intersection_x or not intersection_y:
        return None
    else:
        '''
        return (
            intersection_x[0],
            intersection_y[0],
            intersection_x[1],
            intersection_y[1]
        )
        '''
        llc = (intersection_x[0], intersection_y[0])
        urc = (intersection_x[1], intersection_y[1])
        return llc, urc
# fmt: on


def _intervals_intersection(a_1: float, b_1: float, a_2: float, b_2: float):
    """
    Determine the intersection of the intervals [a_1, b_1] and [a_2, b_2].
    """
    a = max(a_1, a_2)
    b = min(b_1, b_2)
    if a > b:
        return None
    else:
        return a, b
