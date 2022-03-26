import functools


def levenshtein_distance(A: str, B: str) -> int:
    @functools.lru_cache(None)
    def _dist_between_prefixes(A_idx: int, B_idx) -> int:
        if A_idx < 0:
            # A is empty,
            # so the only way of transforming A into B
            # is to insert all of B's characters into A.
            return B_idx + 1
        elif B_idx < 0:
            # B is empty,
            # so the only way of transforming A into B
            # is to delete all of A's characters.
            return A_idx + 1

        if A[A_idx] == B[B_idx]:
            return _dist_between_prefixes(A_idx - 1, B_idx - 1)

        # The rest of this represents/implements an observation,
        # which is quite intuitive to make;
        # its rigorous proof is based on reordering steps in/of
        # an optimum solution for the original problem.
        substitute_last = _dist_between_prefixes(A_idx - 1, B_idx - 1) + 1
        add_last_of_B = _dist_between_prefixes(A_idx, B_idx - 1) + 1
        delete_last_of_A = _dist_between_prefixes(A_idx - 1, B_idx) + 1

        return min(
            substitute_last,
            add_last_of_B,
            delete_last_of_A,
        )

    return _dist_between_prefixes(len(A) - 1, len(B) - 1)
