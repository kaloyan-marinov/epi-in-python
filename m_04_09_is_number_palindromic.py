from m_04_08_reverse_digits import reverse


def solution_1_is_palindrome_number(x: int) -> bool:
    """
    time:  O(n)
           where n := the # of digits in the decimal representation of `x`
    """

    if x < 0:
        return False

    return x == reverse(x)


import math


def solution_2_is_palindrome_number(x: int) -> bool:
    if x < 0:
        return False
    elif x == 0:
        return True

    max_index = solution_2__least_power_of_10(x) - 1
    k = 0

    while k <= max_index // 2:
        if solution_2__extract_digit_at_index(
            x, k
        ) != solution_2__extract_digit_at_index(x, max_index - k):
            return False
        k += 1

    return True


def solution_2__least_power_of_10(x: int) -> int:
    # fmt: off
    '''
    power = 0
    while x >= 10 ** power:
        power += 1
    return power
    '''
    # fmt: on

    # The commented-out block above works fine, but is slower than:
    return math.floor(math.log10(x)) + 1


def solution_2__extract_digit_at_index(x: int, k: int) -> int:
    return (x // (10 ** k)) % 10


def solution_3_is_palindrome_number(x: int) -> bool:
    if x < 0:
        return False
    elif x == 0:
        return True

    num_digits = math.floor(math.log10(x)) + 1
    msd_mask = 10 ** (num_digits - 1)

    for i in range(num_digits // 2):
        if x // msd_mask != x % 10:
            return False

        # Remove the most significant digit (MSD) of `x`.
        x %= msd_mask

        # Remove the least significant digit (MLD) of `x`.
        x //= 10

        msd_mask //= 100

    return True


if __name__ == "__main__":
    x = 9
    is_x_palindrome = solution_2_is_palindrome_number(x)
    print(x, is_x_palindrome)
