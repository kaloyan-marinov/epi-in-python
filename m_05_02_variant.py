from typing import List


def add(A: List[int], B: List[int]) -> List[int]:
    """
    Add 2 arbitrary-precision positive decimal integers.
    """

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
