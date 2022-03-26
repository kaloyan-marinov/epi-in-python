from typing import List


# Remove `solution_1_*`, which was correct, but also long and slow.


def solution_2_multiply(A: List[int], B: List[int]) -> List[int]:
    # Handle the case, in which one of the inputs is zero.
    if A == [0] or B == [0]:
        return [0]

    # Determine the sign of the output.
    sign = 1 if A[0] * B[0] > 0 else -1

    # Multiply the absolute values of the inputs.
    A[0] = abs(A[0])
    B[0] = abs(B[0])
    product_of_absolute_values = solution_2__multiply_strictly_positive_inputs(A, B)

    # Ensure that the sign of the output is correct.
    product_of_absolute_values[0] *= sign

    return product_of_absolute_values


def solution_2__multiply_strictly_positive_inputs(
    A: List[int], B: List[int]
) -> List[int]:
    summands = []
    for i in range(1, len(B) + 1):
        i_th_digit_of_B = B[-i]
        if i_th_digit_of_B == 0:
            continue

        summand_i = (
            solution_2__multiply_by_positive_digit(
                A,
                i_th_digit_of_B,
            )
            + (i - 1) * [0]
        )

        summands.append(summand_i)

    running_sum = (len(A) + len(B) + 1) * [0]
    for i in range(1, len(running_sum) + 1):
        for b, s_b in enumerate(summands):
            try:
                i_th_digit_of_s_b = s_b[-i]
            except IndexError:
                i_th_digit_of_s_b = 0
            running_sum[-i] += i_th_digit_of_s_b

        if running_sum[-i] >= 10:
            running_sum[-i - 1] += running_sum[-i] // 10
            running_sum[-i] %= 10

    ind = 0
    while running_sum[ind] == 0:
        ind += 1

    return running_sum[ind:]


def solution_2__multiply_by_positive_digit(A: List[int], d: int) -> List[int]:
    running_sum = (len(A) + 1) * [0]

    for i in range(1, len(A) + 1):
        p_i = A[-i] * d

        running_sum[-i - 1] += p_i // 10
        running_sum[-i] += p_i % 10

        if running_sum[-i] >= 10:
            running_sum[-i - 1] += running_sum[-i] // 10
            running_sum[-i] %= 10

    return running_sum


def solution_3_multiply(A: List[int], B: List[int]) -> List[int]:
    # Handle the case, in which one of the inputs is zero.
    if A == [0] or B == [0]:
        return [0]

    # Determine the sign of the output.
    sign = 1 if A[0] * B[0] > 0 else -1
    A[0] = abs(A[0])
    B[0] = abs(B[0])

    result = [0] * (len(A) + len(B))
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            result[-i - j + 1] += A[-i] * B[-j]
            result[-i - j] += result[-i - j + 1] // 10
            result[-i - j + 1] %= 10

    # Determine the first index with a positive digit.
    ind = 0
    while result[ind] == 0:
        ind += 1

    result[ind] *= sign

    return result[ind:]


if __name__ == "__main__":

    for A, B in (
        ([1, 9, 3, 7, 0, 7, 7, 2, 1], [-7, 6, 1, 8, 3, 8, 2, 5, 7, 2, 8, 7]),
        ([-1, 0, 0, 0], [0]),
        ([1, 4, 7], [8, 9]),
        ([8, 9], [1, 4, 7]),
    ):
        product = solution_3_multiply(A, B)

        print()
        print("multiply")
        print(A)
        print(B)
        print(product)
