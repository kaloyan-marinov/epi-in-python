import concurrent.futures
from typing import Set


def worker(lower: int, upper: int) -> None:
    """
    Perform a basic unit of work.
    [= Test each Collatz sequence starting with a number from `[lower, upper]`.]
    """

    for i in range(lower, upper + 1):
        assert test_collatz_sequence(i, set())

    print(f"[{lower}, {upper}]")


def test_collatz_sequence(c_0: int, collatz_sequence: Set[int]) -> bool:
    """
    Test the Collatz sequence starting with `c_0`.
    """

    if c_0 == 1:
        return True
    elif c_0 in collatz_sequence:
        return False

    collatz_sequence.add(c_0)

    if c_0 & 1:  # i.e. if `c_0` is odd
        return test_collatz_sequence(3 * c_0 + 1, collatz_sequence)
    else:  # i.e. `c_0` is even
        return test_collatz_sequence(c_0 >> 1, collatz_sequence)  # Or `c_0 // 2`


def main(n: int, num_threads: int, range_size: int) -> None:
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        for i in range(n // range_size):
            executor.submit(worker, i * range_size, (i + 1) * range_size)


if __name__ == "__main__":
    main(10 ** 6, 30, 100)
