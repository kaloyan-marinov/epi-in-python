import copy

from typing import List


def solution_1_plus_one(A: List[int]) -> List[int]:
    """
    Assume that
    each entry of `A` is a decimal digit,
    and `A` represents an arbitrary-precision non-negative integer `d`.

    Return an array of digits encoding the integer `d + 1`.

    time:  O(n)
           where n := len(A)
    """

    D = copy.deepcopy(A)  # NB: `D = A` also passes the tests, but modifies the input!

    for i in reversed(range(len(D))):
        if 0 <= D[i] <= 8:
            D[i] += 1
            break
        else:  # i.e. D[i] == 9
            D[i] = 0

    if D[0] == 0:
        D.insert(0, 1)

    return D


def solution_2_plus_one(A: List[int]) -> List[int]:
    """
    This is the official solution.
    My impression about it is that it:
        - reads "kind of backwards",
        - seems hard to come up with, but
        - is undeniably slick.

    Assume that
    each entry of `A` is a decimal digit,
    and `A` represents an arbitrary-precision non-negative integer `d`.

    Return an array of digits encoding the integer `d + 1`.

    time:  O(n)
           where n := len(A)
    """

    A[-1] += 1

    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break

        A[i] = 0
        A[i - 1] += 1
    else:  # the loop completed without encountering a `break` statement
        if A[0] == 10:
            # There is a carry-out from the input's most significant digit,
            # which means that there is not enough storage in the array for the result,
            # so we need 1 more digit to store the result.
            # A slick way to do this is to append 0 to the end of the array,
            # and update the first entry to 1.
            A.append(0)
            A[0] = 1

    return A
