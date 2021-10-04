def is_palindrome(x: int) -> bool:
    if x < 0:
        return False
    return x == _reverse_digits(x)


def _reverse_digits(x: int) -> int:
    if x < 0:
        return -_reverse_digits(abs(x))

    y = 0
    while x:
        y = y * 10 + (x % 10)
        x //= 10

    return y
