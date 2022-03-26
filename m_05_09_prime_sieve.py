import math

from typing import List


def generate_primes_1(n: int) -> List[int]:
    """
    time: O(n^2)

    Test PASSED (24/24) [3111  s]
    Average running time:  131  s
    Median running time:    10 us
    """
    primes = list()

    if n == 1:
        return primes

    i = 2
    while i <= n:
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
        i += 1

    return primes


def generate_primes_2(n: int) -> List[int]:
    """
    time: O(n^(3/2))

    Test PASSED (24/24) [   5  s]
    Average running time:  233 ms
    Median running time:    23 us
    """
    primes = list()

    if n == 1:
        return primes

    i = 2
    while i <= n:
        is_prime = True
        for j in range(
            2,
            math.floor(math.sqrt(i)) + 1,
        ):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
        i += 1

    return primes


if __name__ == "__main__":
    n = 4
    primes = generate_primes_2(n)

    print("n")
    print(n)
    print("primes")
    print(primes)
