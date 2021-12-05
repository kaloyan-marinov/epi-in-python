def substring_match(t: str, s: str) -> int:
    start_idx = 0

    while start_idx < len(t) - len(s) + 1:
        count_matches = 0
        while (
            start_idx + count_matches < len(t)
            and count_matches < len(s)
            and t[start_idx + count_matches] == s[count_matches]
        ):
            count_matches += 1

        if count_matches == len(s):
            return start_idx

        start_idx += 1

    return -1


if __name__ == "__main__":
    # t = "GACGCCA"
    # s = "CGC"
    t = "babababbaabaabbbbb"
    s = "baabb"

    r = substring_match(t, s)

    print(t)
    print(s)
    print(r)
