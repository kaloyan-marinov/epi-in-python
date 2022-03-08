from typing import List, NamedTuple, Optional


class Endpoint(NamedTuple):
    is_closed: bool
    val: int


class Interval(NamedTuple):
    left: Endpoint
    right: Endpoint


def union_of_intervals(intervals: List[Interval]) -> List[Interval]:
    intervals.sort(
        key=lambda interval: (
            interval.left.val,
            0 if interval.left.is_closed else 1,
        )
    )

    result: List[Interval] = []

    curr_result_piece: Optional[Interval] = None

    for interval in intervals:

        if curr_result_piece is None:
            curr_result_piece = interval
            continue

        can_be_joined = False
        if curr_result_piece.right.val == interval.left.val and (
            curr_result_piece.right.is_closed or interval.left.is_closed
        ):
            can_be_joined = True
        if curr_result_piece.right.val > interval.left.val:
            can_be_joined = True

        if not can_be_joined:
            result.append(curr_result_piece)
            curr_result_piece = interval
        else:
            left_endpoint_val = min(
                curr_result_piece.left.val,
                interval.left.val,
            )
            right_endpoint_val = max(
                curr_result_piece.right.val,
                interval.right.val,
            )

            left_endpoint_is_closed = (
                curr_result_piece.left.is_closed
            )  # No need to bother with `interval.left.val`, b/c of the secondary criterion used for/by the sorting!
            right_endpoint_is_closed = curr_result_piece.right.is_closed
            if curr_result_piece.right.val < interval.right.val:
                right_endpoint_is_closed = interval.right.is_closed

            curr_result_piece = Interval(
                Endpoint(left_endpoint_is_closed, left_endpoint_val),
                Endpoint(right_endpoint_is_closed, right_endpoint_val),
            )

    if curr_result_piece is not None:
        result.append(curr_result_piece)

    return result


if __name__ == "__main__":
    # fmt: off
    raw_intervals = [[610, False, 613, True], [204, True, 205, True], [1117, True, 1124, True], [379, False, 381, True], [136, True, 137, False], [129, False, 137, True], [584, True, 592, True], [760, False, 766, False], [743, False, 748, False], [745, True, 753, False], [104, True, 113, True], [1007, True, 1010, False], [573, True, 577, False], [765, True, 770, False], [62, True, 66, False], [578, False, 581, True], [760, True, 768, True], [1020, False, 1023, True], [663, False, 665, False], [720, False, 728, True], [595, True, 596, True], [911, False, 916, True], [332, True, 336, True], [34, True, 38, False], [956, True, 963, True], [17, False, 19, False], [230, False, 237, False], [1097, False, 1100, False], [634, True, 639, False], [141, True, 142, True], [396, True, 404, False], [959, True, 963, True], [131, True, 133, True], [179, False, 184, False], [920, True, 921, False], [621, True, 630, True], [140, False, 143, True], [122, False, 131, False], [224, False, 226, False], [13, True, 14, True], [1190, True, 1192, False], [995, False, 997, True], [548, True, 549, False], [218, False, 227, False], [23, True, 28, False], [518, True, 527, True], [1119, True, 1127, False], [632, True, 640, False], [424, False, 432, False], [1063, False, 1071, False], [278, True, 281, False], [2, True, 10, False], [505, True, 508, True], [1177, True, 1184, True], [396, True, 401, True], [588, False, 593, False], [840, False, 845, False], [352, True, 354, False], [99, True, 100, False], [1125, True, 1127, True], [328, False, 331, True], [758, False, 767, False], [1149, True, 1157, True], [1060, True, 1066, True], [220, True, 229, False], [230, False, 235, True], [1095, True, 1098, True], [527, True, 530, False], [205, True, 206, False], [663, True, 669, True], [940, True, 941, True], [656, False, 657, False], [706, False, 715, False], [755, True, 757, False], [755, True, 762, False], [950, True, 953, False], [541, False, 542, True], [1103, False, 1110, True], [826, False, 831, False], [807, True, 813, True], [453, False, 459, True], [823, False, 825, True], [460, False, 461, True], [154, False, 155, False], [751, False, 752, False], [242, False, 247, False], [636, True, 641, False], [891, True, 897, True], [629, False, 634, False], [407, True, 415, False], [51, True, 54, True], [161, True, 169, True], [1183, False, 1192, False], [852, True, 858, True], [250, True, 257, False], [952, False, 960, False], [210, False, 217, False], [353, True, 360, True], [1034, False, 1039, True], [887, False, 895, True], [85, True, 87, True], [564, True, 569, True], [156, False, 157, False], [285, False, 292, True], [791, False, 794, False], [86, True, 94, True], [582, True, 588, False], [1135, False, 1144, True], [797, True, 805, True], [280, False, 283, True], [363, False, 368, True], [538, False, 544, True], [442, True, 451, False], [1017, False, 1020, True], [1140, False, 1147, True], [707, False, 713, True], [24, False, 31, True], [524, False, 532, False], [669, True, 678, False], [76, True, 80, False]]
    # fmt: on
    intervals = [
        Interval(
            Endpoint(is_closed=r_i[1], val=r_i[0]),
            Endpoint(is_closed=r_i[3], val=r_i[2]),
        )
        for r_i in raw_intervals
    ]

    result = union_of_intervals(intervals)
