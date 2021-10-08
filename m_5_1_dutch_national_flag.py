from typing import List


def solution_1_dutch_national_flag(pivot_index: int, A: List[int]) -> List[int]:
    pivot_value = A[pivot_index]

    A[0], A[pivot_index] = A[pivot_index], A[0]
    first_ind = 0
    last_ind = 0

    for i in range(1, len(A)):
        if A[i] > pivot_value:
            continue
        elif A[i] == pivot_value:
            A[last_ind + 1], A[i] = A[i], A[last_ind + 1]
            last_ind += 1
        else:  # i.e. A[i] < pivot_value
            if i == last_ind + 1:
                A[first_ind], A[i] = A[i], A[first_ind]
            else:
                A[first_ind], A[last_ind + 1], A[i] = (
                    A[i],
                    A[first_ind],
                    A[last_ind + 1],
                )
            first_ind += 1
            last_ind += 1

    return A


def solution_2_dutch_national_flag(pivot_index: int, A: List[int]) -> None:
    pivot_value = A[pivot_index]

    # fmt: off
    '''
    During partitioning
    / During processing
    / While constructing the [desired] partitioning,
    maintain the following as "supporting invariants":
        smaller          A[: first_equal]
        equal            A[first_equal:first_unclassified]
        unclassified     A[first_unclassified:first_larger]
        larger           A[first_larger:]
    '''
    # fmt: on
    first_equal = 0
    first_unclassified = 0
    first_larger = len(A)

    while first_unclassified < first_larger:
        if A[first_unclassified] < pivot_value:
            A[first_equal], A[first_unclassified] = (
                A[first_unclassified],
                A[first_equal],
            )
            first_equal += 1
            first_unclassified += 1
        elif A[first_unclassified] == pivot_value:
            first_unclassified += 1
        else:  # i.e. A[first_unclassified] > pivot_value
            A[first_unclassified], A[first_larger - 1] = (
                A[first_larger - 1],
                A[first_unclassified],
            )
            first_larger -= 1


if __name__ == "__main__":
    import copy

    # Tests for solution #1.
    inputs = (
        (2, [0, 1, 1, 2]),
        (0, [1, 0, 2, 0, 2, 1]),
    )

    for pivot_index, A in inputs:
        A_initial = copy.deepcopy(A)
        A_final = solution_1_dutch_national_flag(pivot_index, A)

        print()
        print("solution_1", A_initial)
        print("solution_1", A_final)

    # Tests for solution #2.
    print()
    print()
    print()

    # Note that
    # the previous loop modified the value of `input` in-place,
    # which means that we now have to re-initialize `intputs`.
    inputs = (
        (2, [0, 1, 1, 2]),
        (0, [1, 0, 2, 0, 2, 1]),
    )

    for pivot_index, A in inputs:
        A_initial = copy.deepcopy(A)
        solution_2_dutch_national_flag(pivot_index, A)

        print()
        print("solution_2", A_initial)
        print("solution_2", A)
