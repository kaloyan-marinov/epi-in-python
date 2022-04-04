def snake_string_1(s: str) -> str:
    return s[1::4] + s[::2] + s[3::4]


def snake_string_2(s: str) -> str:
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
