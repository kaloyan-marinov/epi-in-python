from typing import List


def evaluate(expression: str) -> int:
    """
    The `expression` input represents a string in Reverse Polish Notation.
    For example,
        3,4,+,2,*,1,+

    In that case, this function returns the value of (3 + 4) * 2 + 1 = 15
    """
    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x // y,
    }

    recorded_values: List[int] = []
    for token in expression.split(","):
        if token not in operations:
            recorded_values.append(int(token))
        else:
            b = recorded_values.pop()
            a = recorded_values.pop()
            r = operations[token](a, b)
            recorded_values.append(r)

    return recorded_values[0]
