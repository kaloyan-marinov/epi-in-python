def solution_1_is_palindrome(x: int) -> bool:
    if x < 0:
        return False
    return x == solution_1__reverse_digits(x)


def solution_1__reverse_digits(x: int) -> int:
    if x < 0:
        return -solution_1__reverse_digits(abs(x))

    y = 0
    while x:
        y = y * 10 + (x % 10)
        x //= 10

    return y


def solution_2_is_palindrome(x: int) -> bool:
    if x < 0:
        return False

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
    power = 0
    while x >= 10 ** power:
        power += 1
    return power


def solution_2__extract_digit_at_index(x: int, k: int) -> int:
    return (x // (10 ** k)) % 10


if __name__ == "__main__":
    x = 9
    is_x_palindrome = solution_2_is_palindrome(x)
    print(x, is_x_palindrome)
