from typing import List


def solution_1_dutch_national_flag(pivot_index: int, A: List[int]) -> None:
    """
    Assume that `pivot_index in range(len(A))`.

    Perform an in-place modification of `A`,
    which consists in re-arranging its elements s.t.
        - all elements < "the pivot value" appear first,
        - followed by all elements = "the pivot value",
        - followed by all elements > "the pivot value".

    time:  O(n)
           where n := len(A)

    space: O(1)
    """

    # Save "the pivot value".
    pivot_value = A[pivot_index]

    # 1st pass: re-arrange all elements that are `< pivot_value`.
    idx_for_smaller = 0
    for i in range(len(A)):
        if A[i] < pivot_value:
            A[i], A[idx_for_smaller] = A[idx_for_smaller], A[i]
            idx_for_smaller += 1

    # 2nd pass: re-arrange all elements that are `> pivot_value`.
    idx_for_larger = len(A) - 1
    for j in reversed(range(len(A))):
        if A[j] > pivot_value:
            A[j], A[idx_for_larger] = A[idx_for_larger], A[j]
            idx_for_larger -= 1


def solution_2_dutch_national_flag(pivot_index: int, A: List[int]) -> None:
    """
    This algorithm:
        - is similar to the previous one;
        - differs from the previous one
          by "performing classification" into elements <, =, and > the pivot value
          in a single pass;
        - reduces the time complexity but is trickier to implement.

    Assume that `pivot_index in range(len(A))`.

    Perform an in-place modification of `A`,
    which consists in re-arranging its elements s.t.
        - all elements < "the pivot value" appear first,
        - followed by all elements = "the pivot value",
        - followed by all elements > "the pivot value".

    time:  O(n)
           where n := len(A)

    space: O(1)
    """

    # Save "the pivot value".
    pivot_value = A[pivot_index]

    # During partitioning
    # / During processing
    # / As part of iteratively constructing the [desired] partitioning,
    # maintain the following as "supporting invariants":
    #     smaller          A[:first_equal]
    #     equal            A[first_equal:first_unclassified]
    #     unclassified     A[first_unclassified:first_larger]
    #     larger           A[first_larger:]
    first_equal = 0
    first_unclassified = 0
    first_larger = len(A)

    # Iterate through the "unclassified" elements.
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
