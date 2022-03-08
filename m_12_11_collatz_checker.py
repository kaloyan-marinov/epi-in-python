from typing import Set


def test_collatz_conjecture(n: int) -> bool:
    """
    fail
    """

    def _advance_collatz_sequence(m: int) -> int:
        if n % 2 == 1:
            return n * 3 + 1
        else:
            return n // 2  # NB!

    tested_numbers = set()
    # max_tested_number = 1

    for c in range(1, n + 1):
        collatz_sequence_for_c = {c}

        next_c = c
        while next_c >= c:
            next_c = _advance_collatz_sequence(next_c)
            collatz_sequence_for_c.add(next_c)
            if next_c in tested_numbers or next_c == 1:
                tested_numbers.update(collatz_sequence_for_c)
                # max_tested_number = max(max_tested_number, c)
                break
            # else:
            #     tested_numbers

    return True


def test_collatz_conjecture(n: int) -> bool:
    """
    This is the official solution.
    """
    # Maintain a hash table,
    # each of whose entries is verified to converge to 1.
    verified_odd_numbers: Set[int] = set()

    for ii in range(3, n + 1):  # b/c the hypothesis holds trivially for 1 and 2.
        collatz_sequence_for_ii: Set[int] = set()

        next_ii = ii
        while next_ii >= ii:
            if next_ii in collatz_sequence_for_ii:
                # We previously encountered `next_ii`,
                # so the Collatz sequence has falled into a loop.
                # This disproves the hypothesis, so we short-circuit, returning `False`.
                return False

            collatz_sequence_for_ii.add(next_ii)

            if next_ii % 2:  # Odd number
                if (
                    next_ii in verified_odd_numbers
                ):  # i.e. `next_ii` has already been verified to converge to 1.
                    break
                verified_odd_numbers.add(next_ii)
                next_ii = next_ii * 3 + 1
            else:
                next_ii //= 2

    return True
