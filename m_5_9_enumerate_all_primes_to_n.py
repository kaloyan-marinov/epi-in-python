from typing import List


def generate_primes(n: int) -> List[int]:
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
