def snake_string(s: str) -> str:
    return s[1::4] + s[::2] + s[3::4]


if __name__ == "__main__":
    s = "Hello World!"
    r = snake_string(s)
    print(r)
