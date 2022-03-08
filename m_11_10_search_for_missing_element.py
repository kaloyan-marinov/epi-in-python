from typing import List

import collections


DuplicateAndMissing = collections.namedtuple(
    "DuplicateAndMissing",
    ("duplicate", "missing"),
)


def find_duplicate_missing(A: List[int]) -> DuplicateAndMissing:
    # fmt: off
    '''
    n = len(A)

    result = DuplicateAndMissing(-1, -1)

    idx_of_duplicate = -1
    prev_xor = A[0]
    for i in range(1, len(A)):
        curr_xor = prev_xor ^ A[i]
        if prev_xor == curr_xor:
            idx_of_duplicate = i
            result.duplicate = A[i]
            break

    for i in range(idx_of_duplicate + 1, len(A)):
        prev_xor ^= A[i]

    xor = 0
    for i in range(1, len(A)):
        xor ^= i

    result.missing = prev_xor ^ xor

    return result
    '''
    # fmt: on
    n = len(A)

    duplicate_value = -1

    idx_of_duplicate = -1
    prev_xor = A[0]
    for i in range(1, len(A)):
        curr_xor = prev_xor ^ A[i]
        if prev_xor == curr_xor:
            idx_of_duplicate = i
            duplicate_value = A[i]
            break
        prev_xor = curr_xor  # NB!

    for i in range(idx_of_duplicate + 1, len(A)):
        prev_xor ^= A[i]

    xor = 0
    for i in range(1, len(A)):
        xor ^= i

    missing_value = prev_xor ^ xor

    return DuplicateAndMissing(duplicate_value, missing_value)


# fmt: off
'''
def find_duplicate_missing(A: List[int]) -> DuplicateAndMissing:
    n = len(A)

    duplicate_value = -1

    idx_of_duplicate = -1
    prev_xor = A[0] + 1
    for i in range(1, len(A)):
        curr_xor = prev_xor ^ (A[i] + 1)
        if prev_xor == curr_xor:
            print('yeah')
            idx_of_duplicate = i
            break
        prev_xor = curr_xor

    print(idx_of_duplicate, prev_xor)

    for i in range(idx_of_duplicate + 1, len(A)):
        print('updating', i)
        prev_xor ^= (A[i] + 1)

    xor = 0
    for i in range(len(A)):
        xor ^= i + 1

    print('prev_xor:', bin(prev_xor))
    print('xor     :',bin(xor))
    missing_value = (prev_xor ^ xor) - 1

    return DuplicateAndMissing(A[idx_of_duplicate], missing_value)
'''
# fmt: on


# fmt: off
'''
def find_duplicate_missing(A: List[int]) -> DuplicateAndMissing:
    idx_of_duplicate = -1
    prev_xor = 0
    for i in range(len(A) - 1):
        prev_xor ^= A[i] + 1
        curr_xor = prev_xor ^ (A[i + 1] + 1)

        if prev_xor == curr_xor:
            idx_of_duplicate = i + 1
            break

    for i in range(idx_of_duplicate + 1, len(A)):
        print("updating", i)
        prev_xor ^= A[i] + 1

    xor = 0
    for i in range(len(A)):
        xor ^= i + 1

    print("prev_xor:", bin(prev_xor))
    print("xor     :", bin(xor))
    missing_value = (prev_xor ^ xor) - 1

    return DuplicateAndMissing(A[idx_of_duplicate], missing_value)
'''
# fmt: on


def find_duplicate_missing_1(A: List[int]) -> DuplicateAndMissing:
    duplicate = None
    seen = set()
    for a in A:
        if a not in seen:
            seen.add(a)
        else:
            duplicate = a

    missing = None
    for i in range(len(A)):
        if i not in seen:
            missing = i
            break

    return DuplicateAndMissing(duplicate, missing)


def find_duplicate_missing_2(A: List[int]) -> DuplicateAndMissing:
    A.sort()

    duplicate = None
    missing = None

    prev = A[0]
    for i in range(1, len(A)):
        curr = A[i]

        if curr == prev:
            duplicate = curr
        elif curr == prev + 2:
            missing = prev + 1

        if duplicate is not None and missing is not None:
            return DuplicateAndMissing(duplicate, missing)

        prev = curr

    return DuplicateAndMissing(duplicate, len(A) - 1)


import functools


def find_duplicate_missing_3(A: List[int]) -> DuplicateAndMissing:
    d_xor_m = functools.reduce(
        lambda v, t: v ^ t[0] ^ t[1],
        enumerate(A),
        0,
    )

    # Since the duplicate value and the missing value are distinct,
    # there exists a bit in which they differ,
    # i.e. at least 1 bit in `d_xor_m` is set to 1.
    # Find such a bit by [means of the following bit-fiddling trick for]
    # isolating the lowest bit that is 1 in `d_xor_m`.
    differ_bit = d_xor_m & (~(d_xor_m - 1))

    # Focusing on _entries and numbers_ in which the `differ-bit`-th bit is 1,
    # compute the XOR of all those _entries and numbers_.
    # (Note that the problem statement implies that the result will be either d or m.)
    h = 0
    for i, a in enumerate(A):
        if i & differ_bit:
            h ^= i
        if a & differ_bit:
            h ^= a

    # `h` is either the duplicate value or the missing value:
    #   - if `h` is in A, it is the duplicate value;
    #   - otherwise, it is the missing value.
    return (
        DuplicateAndMissing(h, h ^ d_xor_m)
        if h in A
        else DuplicateAndMissing(h ^ d_xor_m, h)
    )


def find_duplicate_missing_4(A: List[int]) -> DuplicateAndMissing:
    A = [a + 1 for a in A]

    missing_xor_duplicate = 0
    for a in A:
        missing_xor_duplicate ^= a
    for i in range(len(A)):
        missing_xor_duplicate ^= i + 1

    idx_of_duplicate = -1

    prev_xor = 0
    curr_xor = prev_xor ^ A[0]
    for i in range(1, len(A)):
        a_i = A[i]

        prev_xor = curr_xor
        curr_xor ^= a_i

        if curr_xor ^ missing_xor_duplicate ^ a_i == prev_xor ^ missing_xor_duplicate:
            idx_of_duplicate = i
            break

        prev_xor = curr_xor

    duplicate_value = A[idx_of_duplicate]
    missing_value = missing_xor_duplicate ^ duplicate_value

    return DuplicateAndMissing(duplicate_value - 1, missing_value - 1)


if __name__ == "__main__":
    # A = [0, 0]
    # fmt: off
    A = [12, 14, 41, 74, 79, 22, 16, 11, 24, 76, 101, 27, 60, 31, 0, 13, 53, 90, 89, 1, 4, 85, 9, 77, 43, 93, 51, 86, 35, 5, 67, 71, 21, 46, 56, 95, 66, 19, 20, 44, 73, 91, 61, 69, 83, 34, 17, 29, 58, 78, 36, 49, 99, 38, 96, 40, 92, 37, 33, 15, 47, 5, 23, 3, 26, 64, 52, 81, 82, 8, 28, 25, 32, 65, 68, 70, 72, 94, 63, 7, 55, 10, 45, 100, 84, 2, 54, 98, 50, 39, 6, 88, 48, 97, 57, 59, 87, 62, 75, 30, 18, 42]
    # fmt: on
    r = find_duplicate_missing(A)
