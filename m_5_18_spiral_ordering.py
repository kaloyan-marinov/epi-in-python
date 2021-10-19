from typing import List


def s_1_matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    def matrix_layer_in_clockwise(offset):
        if offset == len(square_matrix) - offset - 1:
            # `square_matrix` has odd dimension, and we are at its center.
            spiral_ordering.append(square_matrix[offset][offset])
            return

        spiral_ordering.extend(square_matrix[offset][offset : -1 - offset])
        spiral_ordering.extend(
            list(zip(*square_matrix))[-1 - offset][offset : -1 - offset]
        )
        spiral_ordering.extend(square_matrix[-1 - offset][-1 - offset : offset : -1])
        spiral_ordering.extend(
            list(zip(*square_matrix))[offset][-1 - offset : offset : -1]
        )

    spiral_ordering: List[int] = []
    for offset in range((len(square_matrix) + 1) // 2):
        matrix_layer_in_clockwise(offset)

    return spiral_ordering


def s_1_matrix_in_spiral_order_refactored(square_matrix: List[List[int]]) -> List[int]:
    spiral_ordering: List[int] = []
    for offset in range((len(square_matrix) + 1) // 2):
        if offset == len(square_matrix) - offset - 1:
            # `square_matrix` has odd dimension, and we are at its center.
            spiral_ordering.append(square_matrix[offset][offset])
            break

        spiral_ordering.extend(square_matrix[offset][offset : -1 - offset])
        spiral_ordering.extend(
            list(zip(*square_matrix))[-1 - offset][offset : -1 - offset]
        )
        spiral_ordering.extend(square_matrix[-1 - offset][-1 - offset : offset : -1])
        spiral_ordering.extend(
            list(zip(*square_matrix))[offset][-1 - offset : offset : -1]
        )

    return spiral_ordering


def s_2_matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    value_absent_from_original_input = 0
    directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

    d_idx = 0
    x = y = 0
    spiral_ordering = []
    for _ in range(len(square_matrix) ** 2):
        spiral_ordering.append(square_matrix[x][y])

        square_matrix[x][y] = value_absent_from_original_input

        next_x = x + directions[d_idx][0]
        next_y = y + directions[d_idx][1]
        if (
            next_x not in range(len(square_matrix))
            or next_y not in range(len(square_matrix))
            or square_matrix[next_x][next_y] == value_absent_from_original_input
        ):
            d_idx = (
                d_idx + 1
            ) & 3  # Equivalent to `(d_idx + 1) % 4`, since `d_idx in range(4)`.
            next_x = x + directions[d_idx][0]
            next_y = y + directions[d_idx][1]

        x, y = next_x, next_y

    return spiral_ordering


if __name__ == "__main__":
    A = [[1]]

    s_2_matrix_in_spiral_order(A)

    B = [
        [4, 2],
        [3, 1],
    ]
    s_2_matrix_in_spiral_order(B)
