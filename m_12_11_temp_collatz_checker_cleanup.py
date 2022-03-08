from typing import Set


def test_collatz_checker(n: int) -> bool:
    verified_numbers: Set[int] = set()

    for ii in range(3, n + 1):

        collatz_sequence_starting_at_ii: Set[int] = set()
        next_ii = ii
        while next_ii >= ii:
            if next_ii in verified_numbers:
                break
            elif next_ii in collatz_sequence_starting_at_ii:
                # `next_ii` was encountered earlier on in the Collatz sequence starting at `ii`,
                # which means that the sequence will go on forever as a loop;
                # since 1 was not encountered in the sequence earlier, that means that
                # the hypothesis is false for for the Collatz sequence starting at `ii`.
                # So, we short-circuit this function's execution.
                return False

            collatz_sequence_starting_at_ii.add(next_ii)

            if next_ii % 2 == 1:
                next_ii = next_ii * 3 + 1
            else:
                next_ii //= 2

            verified_numbers.add(next_ii)
        # verified_numbers.add(next_ii)

    return True
