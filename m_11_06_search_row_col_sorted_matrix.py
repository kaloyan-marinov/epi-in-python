from typing import List


def matrix_search(A: List[List[int]], x: int) -> int:
    """
    measly attempt
    (= contemptibly small[/inadequate])

        a measly amount of money
        a measly little present

    meager
    = 2 a : lacking desirable qualities (such as richness or strength)

        leading a meager life

    = 2 b : deficient in quality or quantity
        a meager diet
    """
    row_count = len(A)
    col_count = len(A[0])

    row_min = 0
    row_max = row_count - 1

    col_min = 0
    col_max = col_count - 1

    for i in reversed(range(col_count)):
        if A[row_min][i] <= x:
            col_max = i
            break


def matrix_search(A: List[List[int]], x) -> bool:
    n_row = len(A)
    n_col = len(A[0])

    row = 0
    col = n_col - 1

    while col >= 0 and row <= n_row - 1:
        if A[row][col] == x:
            return True
        elif A[row][col] > x:
            # Eliminate the `col`-th column
            # from our (algorithm's) remaining/subsequent considerations.
            col -= 1
        else:  # i.e. A[row][col] < x
            # Eliminate the `row`-th row
            # from our (algorithm's) remaining/subsequent considerations.
            row += 1

    return False
