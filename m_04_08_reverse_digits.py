def reverse_digits(x: int) -> int:
    if x < 0:
        return -reverse_digits(-x)

    y = 0
    while x:
        y = y * 10 + (x % 10)
        x //= 10

    return y
