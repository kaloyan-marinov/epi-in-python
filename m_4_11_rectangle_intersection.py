import collections
from typing import Tuple, Optional


Point2D = collections.namedtuple(
    "Point2D",
    ["x", "y"],
)


# fmt: off
def _rectangles_intersection(
    r_1_llc: Point2D, r_1_urc: Point2D,
    r_2_llc: Point2D, r_2_urc: Point2D,
) -> Optional[Tuple[Point2D, Point2D]]:
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
        llc = Point2D(intersection_x[0], intersection_y[0])
        urc = Point2D(intersection_x[1], intersection_y[1])
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


Rect = collections.namedtuple("Rect", ("x", "y", "width", "height"))


def intersect_rectangle(r1: Rect, r2: Rect) -> Rect:
    r1_llc = Point2D(r1.x, r1.y)
    r1_urc = Point2D(r1.x + r1.width, r1.y + r1.height)

    r2_llc = Point2D(r2.x, r2.y)
    r2_urc = Point2D(r2.x + r2.width, r2.y + r2.height)

    rect_intersection: Optional[Tuple[Point2D, Point2D]] = _rectangles_intersection(
        r1_llc, r1_urc, r2_llc, r2_urc
    )
    if rect_intersection is None:
        return Rect(0, 0, -1, -1)
    else:
        x = rect_intersection[0].x
        y = rect_intersection[0].y
        width = rect_intersection[1].x - x
        height = rect_intersection[1].y - y
        return Rect(x, y, width, height)


# def intersect_rectangle_wrapper(r1, r2):
#     return intersect_rectangle(Rect(*r1), Rect(*r2))


if __name__ == "__main__":
    # Example for fixing the crash, which was encountered:
    # `exception message: 'tuple' object has no attribute 'x'`

    # fmt: off
    '''
    r1 = Rect(76, 9, 12, 14)
    r2 = Rect(20, 1, 62, 60)

    rect_intersection = intersect_rectangle(r1, r2)
    print(rect_intersection)
    '''
    # fmt: on

    # Example that indicated a failed unit test:

    # fmt: off
    '''
    Arguments
	r1:       [54, 66, 66, 24]
	r2:       [27, 97, 68, 95]

    Failure info
        expected: [0, 0, -1, -1]
        result:   None
    '''
    # fmt: on
    r1 = Rect(54, 66, 66, 24)
    r2 = Rect(27, 97, 68, 95)

    rect_intersection = intersect_rectangle(r1, r2)
    print(rect_intersection)
