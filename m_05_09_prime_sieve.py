import math

from typing import List


def generate_primes_1(n: int) -> List[int]:
    """
    time: O(n^2)
    """
    pass


def generate_primes_2(n: int) -> List[int]:
    """
    This is based on brute force.

    time: <= O(n^(3/2))

    Since most numbers are not prime,
    the actual time complexity of trail-division is actually lower on average,
    since the program's control flow frequently breaks out of the inner loop early.
    It is known that the time complexity is actually

    time: O(n^(3/2) / (log n)^2)
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


def generate_primes_3(n: int) -> List[int]:
    """
    This takes advantage of the fact that
    _all_ primes from 1 to n are being computed as follows:
    as soon as a number `a` is identified as a prime,
    we "sieve" all its integer-multiples out (from future considerations).

    time: O(n/2 + n/3 + n/5 + n/7 + n/11 + ...)
          asymptotically tends to
          O(n * log(log n)),
          although not obvious
    """

    primes = []

    # An initial value of `True` in `number_2_is_prime[a]` indicates that
    # `a` could potentially be [determined to be] a prime.
    number_2_is_prime: List[bool] = [False, False] + [True] * (n - 1)

    for a in range(2, n + 1):
        if number_2_is_prime[a]:
            primes.append(a)

            # Mark all subsequent integer-multiples of `a` as non-primes.
            for b in range(2 * a, n + 1, a):
                number_2_is_prime[b] = False

    return primes


def generate_primes_4(n: int) -> List[int]:
    """
    TODO: it's possible to sieve the integer-multiples of `p`
          from `p**2` (instead of from `p`),
          since all {k * p : k integer, k < p} [will] have already been sieved out

          can also ignore even numbers
    """
    pass


if __name__ == "__main__":
    n = 4
    primes = generate_primes_2(n)

    print("n")
    print(n)
    print("primes")
    print(primes)
