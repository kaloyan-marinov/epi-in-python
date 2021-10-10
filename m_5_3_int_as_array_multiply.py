from typing import List


def multiply(A: List[int], B: List[int]) -> List[int]:
    # Handle the case, in which one of the inputs is zero.
    if A == [0] or B == [0]:
        return [0]

    # Determine the sign of the output.
    sign = 1 if A[0] * B[0] > 0 else -1

    # Multiply the absolute values of the inputs.
    A[0] = abs(A[0])
    B[0] = abs(B[0])
    product_of_absolute_values = _multiply_strictly_positive_inputs(A, B)

    # Ensure that the sign of the output is correct.
    product_of_absolute_values[0] *= sign

    return product_of_absolute_values


def _multiply_strictly_positive_inputs(A: List[int], B: List[int]) -> List[int]:
    running_sum = [0]  # represents 0

    for i in range(1, len(B) + 1):
        i_th_digit_of_B = B[-i]
        if i_th_digit_of_B == 0:
            continue

        contrib_i = _multiply_by_positive_digit(A, i_th_digit_of_B) + (i - 1) * [0]

        running_sum = _add(
            running_sum,
            contrib_i,
        )

    return running_sum


def _multiply_by_positive_digit(A: List[int], d: int) -> List[int]:
    running_sum = [0]

    for i in range(1, len(A) + 1):
        p_i = A[-i] * d

        if 0 <= p_i <= 9:
            contrib_i = [p_i] + (i - 1) * [0]
        else:  # i.e. if p_i >= 10
            contrib_i = [p_i // 10, p_i % 10] + (i - 1) * [0]

        running_sum = _add(
            running_sum,
            contrib_i,
        )

    return running_sum


def _add(A: List[int], B: List[int]) -> List[int]:
    if len(A) < len(B):
        A, B = B, A

    sum = [0] * (len(A) + 1)

    for i in range(1, len(A) + 1):
        i_th_digit_of_A = A[-i]
        try:
            i_th_digit_of_B = B[-i]
        except IndexError:
            i_th_digit_of_B = 0

        sum[-i] += i_th_digit_of_A + i_th_digit_of_B

        if sum[-i] >= 10:
            sum[-i] %= 10
            sum[-i - 1] += 1

    if sum[0] == 0:
        return sum[1:]
    else:
        return sum


if __name__ == "__main__":
    A_add = [9, 9, 7, 0]
    B_add = [3, 4, 2]
    sum = _add(A_add, B_add)

    print()
    print("add")
    print(A_add)
    print(B_add)
    print(sum)

    A_mult = [9, 9]
    d_mult = 9
    prod = _multiply_by_positive_digit(A_mult, d_mult)

    print()
    print("_multiply_by_positive_digit")
    print(A_mult)
    print(d_mult)
    print(prod)

    for A, B in (
        ([0], [-1, 0, 0, 0]),
        ([-1, 0, 0, 0], [0]),
        ([1, 4, 7], [8, 9]),
        ([8, 9], [1, 4, 7]),
    ):
        product = multiply(A, B)

        print()
        print("multiply")
        print(A)
        print(B)
        print(product)
