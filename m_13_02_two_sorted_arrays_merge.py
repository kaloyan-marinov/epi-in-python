from typing import List


def merge_two_sorted_arrays_1(
    A: List[int],
    m: int,
    B: List[int],
    n: int,
) -> None:
    # attempt 6
    if n == 0:
        return

    # attempt 1
    """
    # A[-1 - m :] = A[:m]
    A[-m:] = A[:m]
    A[:m] = [None] * m
    """

    # attempt 2
    # fmt: off
    '''
    # for i, idx_i in enumerate((range(m - 1, -1, -1))):
    # for i, idx_i in enumerate(-x for x in range(m)):
        # A[i] = A[idx_i]
        # A[idx_i] = None
    '''
    # fmt: on
    for i, idx_i in enumerate((range(m - 1, -1, -1))):
        A[-i - 1] = A[idx_i]
        A[idx_i] = None

    # attempt 3
    # i = len(A) - m + 1
    # i = len(A) - m
    # i = len(A) - m - 1
    i = len(A) - m
    j = 0
    idx = 0
    while i < len(A) or j < n:
        try:
            if i < len(A) and j < n:
                if A[i] <= B[j]:
                    A[idx], A[i] = A[i], None
                    i += 1
                else:
                    A[idx] = B[j]
                    j += 1
            elif i == len(A) and j < n:
                A[idx] = B[j]
                j += 1
            elif i < len(A) and j == n:
                break  # attempt 5
                A[idx], A[i] = A[i], None
                i += 1  # attempt 4
        except TypeError as e:
            raise e
        except IndexError as e:
            raise e

        idx += 1


def merge_two_sorted_arrays_2(
    A: List[int],
    m: int,
    B: List[int],
    n: int,
) -> None:

    a = m - 1
    b = n - 1

    write_idx = m + n - 1

    while a >= 0 and b >= 0:
        if A[a] > B[b]:
            A[write_idx] = A[a]
            a -= 1
        else:  # i.e. A[a] <= B[b]
            A[write_idx] = B[b]
            b -= 1

        write_idx -= 1

    while b >= 0:
        A[write_idx] = B[b]
        b -= 1
        write_idx -= 1


if __name__ == "__main__":
    # fmt: off
    '''
    A = [-1, 0, 0, 0, 0]
    m = 1
    B = [-3, -1, 0, 3]
    n = 4
    '''
    '''
    A = [-126, -126, -124, -118, -116, -115, -109, -108, -104, -100, -98, -98, -96, -92, -91, -85, -84, -84, -82, -82, -80, -76, -76, -73, -72, -70, -70, -68, -67, -66, -66, -64, -64, -59, -54, -52, -51, -51, -49, -46, -43, -43, -43, -42, -39, -39, -39, -38, -38, -37, -32, -31, -31, -29, -27, -26, -25, -25, -22, -21, -16, -16, -13, -11, -10, -9, -5, -5, 3, 3, 8, 9, 12, 13, 14, 15, 16, 16, 18, 23, 24, 26, 28, 36, 38, 39, 39, 43, 44, 45, 47, 47, 47, 49, 52, 53, 59, 60, 66, 66, 67, 73, 73, 73, 74, 75, 77, 78, 81, 84, 89, 89, 92, 98, 100, 101, 102, 109, 110, 111, 116, 116, 117, 118, 123, 125, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    m = 126
    B = [-95, -93, -93, -93, -87, -87, -86, -85, -84, -82, -81, -80, -79, -79, -75, -74, -73, -73, -73, -68, -67, -67, -66, -64, -62, -61, -60, -60, -58, -57, -57, -56, -54, -53, -53, -52, -50, -47, -45, -44, -42, -42, -41, -41, -41, -36, -30, -30, -28, -18, -13, -12, -10, -2, -1, 2, 4, 4, 5, 6, 8, 10, 10, 12, 12, 14, 15, 16, 19, 20, 21, 24, 25, 26, 26, 28, 29, 33, 38, 42, 44, 44, 55, 60, 63, 71, 71, 72, 73, 75, 75, 79, 80, 82, 85, 89, 91, 91, 92, 96]
    n = 100
    '''
    A = [-7, -5, -4, -2, -1, -1, 1, 2, 7, 9, 10, 10]
    m = 12
    B = []
    n = 0
    # fmt: on

    merge_two_sorted_arrays_1(A, m, B, n)

    print(A)

    # fmt: off
    '''
    A = [3, 13, 17, None, None, None, None, None]
    m = 3
    B = [3, 7, 11, 19]
    n = 4
    '''

    A = [3, 13, 17, None, None, None, None, None, None, None]
    m = 3
    B = [1, 2, 3, 7, 11, 19]
    n = 6
    # fmt: on

    merge_two_sorted_arrays_2(A, m, B, n)

    print(A)
