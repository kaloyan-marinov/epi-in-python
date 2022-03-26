from typing import List


def compute_tower_hanoi(num_rings: int) -> List[List[int]]:
    def _helper(
        n_rings: int,
        peg_0_idx: int,
        peg_1_idx: int,
        peg_2_idx: int,
    ) -> List[List[int]]:
        if n_rings == 1:
            return [
                [peg_0_idx, peg_1_idx],
            ]

        return (
            _helper(n_rings - 1, peg_0_idx, peg_2_idx, peg_1_idx)
            + [
                [peg_0_idx, peg_1_idx],
            ]
            + _helper(n_rings - 1, peg_2_idx, peg_1_idx, peg_0_idx)
        )

    return _helper(num_rings, 0, 1, 2)


def compute_tower_hanoi_2(num_rings: int) -> List[List[int]]:
    # fmt: off
    # This commented-out block is actually unnecessary.
    '''
    # Initialize pegs.
    NUM_PEGS = 3
    # Here, a Python sequence is used to _emulate_ a Python dictionary.
    peg_2_rings: List[List[int]] = [
        list(reversed(range(1, num_rings + 1))),
    ] + [[] for _ in range(1, NUM_PEGS)]
    '''
    # fmt: on

    result: List[List[int]] = []

    def _compute_tower_hanoi_steps(
        n_rings: int,
        source_peg: int,
        target_peg: int,
        intermediary_peg: int,
    ) -> None:

        if n_rings > 0:
            _compute_tower_hanoi_steps(
                n_rings - 1, source_peg, intermediary_peg, target_peg
            )

            # fmt: off
            # This commented-out block is actually unnecessary.
            '''
            peg_2_rings[target_peg].append(
                peg_2_rings[source_peg].pop(),
            )
            '''
            # fmt: on
            result.append(
                [source_peg, target_peg],
            )

            _compute_tower_hanoi_steps(
                n_rings - 1, intermediary_peg, target_peg, source_peg
            )

    _compute_tower_hanoi_steps(num_rings, 0, 1, 2)

    return result
