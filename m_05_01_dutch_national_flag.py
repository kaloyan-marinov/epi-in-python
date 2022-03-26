from typing import List


def solution_1_dutch_national_flag(pivot_index: int, A: List[int]) -> None:
    """
    Assume that `pivot_index in range(len(A))`.

    Perform an in-place modification of `A`,
    which consists in re-arranging its elements s.t.
        - all elements < "the pivot value" appear first,
        - followed by all elements = "the pivot value",
        - followed by all elements > "the pivot value".
    """

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
