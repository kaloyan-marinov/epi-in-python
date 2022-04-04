"""
We illustrate what it means to write a string in sinusoidal fashion
by means of an example.
The string "Hello World!" written in sinusoidal fashion is
```
 e    [blank]   l
H  l o       W r d
    l         o   !
```

Define "the snakestring of `s: str`" to be the left-to-right top-to-bottom sequence
in which characters appear when `s` is written in sinusoidal fashion.
For example, the snakestring of `"Hello World!" is "e lHloWrdlo!".
"""


def snake_string_1(s: str) -> str:
    """
    Return the snakestring of `s`.

    time:  O(n)
           n := len(s)

    space: O(n)
    """
    return s[1::4] + s[::2] + s[3::4]


def snake_string_2(s: str) -> str:
    """
    Return the snakestring of `s`.

    time:  O(n)
           n := len(s)

    space: O(n)
    """
    result = []
    for i in range(1, len(s), 4):
        result.append(s[i])
    for i in range(0, len(s), 2):
        result.append(s[i])
    for i in range(3, len(s), 4):
        result.append(s[i])
    return "".join(result)


if __name__ == "__main__":
    s = "Hello World!"
    r = snake_string_1(s)
    print(r)
