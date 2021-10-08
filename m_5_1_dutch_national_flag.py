from typing import List


def dutch_national_flag(pivot_index: int, A: List[int]) -> List[int]:
    pivot_value = A[pivot_index]

    A[0], A[pivot_index] = A[pivot_index], A[0]
    first_ind = 0
    last_ind = 0

    for i in range(1, len(A)):
        if A[i] > pivot_value:
            continue
        elif A[i] == pivot_value:
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


if __name__ == "__main__":
    import copy

    for pivot_index, A in (
        (2, [0, 1, 1, 2]),
        (0, [1, 0, 2, 0, 2, 1]),
    ):
        A_initial = copy.deepcopy(A)
        A_final = dutch_national_flag(pivot_index, A)

        print()
        print(A_initial)
        print(A_final)
