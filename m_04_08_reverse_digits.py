def reverse(x: int) -> int:
    """
    Return the integer corresponding to
    the digits of `x`['s decimal representation] written in reverse order.

    For example, the reverse of 42 is 24, and the reverse of -314 is -413.

    time:  O(n)
           where n := the # of digits in the decimal representation of `x`
    """

    if x < 0:
        return -reverse(-x)

    y = 0
    while x:
        y = y * 10 + (x % 10)
        x //= 10

    return y


def reverse_2(x: int) -> int:
    """
    Return the integer corresponding to
    the digits of `x`['s decimal representation] written in reverse order.

    For example, the reverse of 42 is 24, and the reverse of -314 is -413.

    time:  O(n)
           where n := the # of digits in the decimal representation of `x`
    """

    result, abs_x = 0, abs(x)

    while abs_x:
        result = result * 10 + abs_x % 10
        abs_x //= 10

    return result if x >= 0 else -result
