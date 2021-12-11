import functools


def substring_match(t: str, s: str) -> int:
    """
    This approach is based on brute force.

    Use 2 nested loops:
    - the 1st loop iterates through t
    - the 2nd loop tests if
      s occurs starting at the current index in t

    The worst-case time complexity is high:
    if t = n * 'a' and s = (n / 2) * 'a' + 'b'
    this algorithm will perform n/2 unsuccessful string comparison,
    each of which will entail (n/2 + 1) character comparisons,
    so the time complexity on each example within this 1-param family of examples
    is O(n^2).

    Intuitively, this brute-force approach is slow because
    (a) it advances though t one character at a time,
    and (b) it potentially does O(m) computations with each advance, where m := len(s).
    """
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


def robin_karp(t: str, s: str) -> int:
    """
    There are 3 [sub]string-matching algorithms,
    whose time complexity is linear:
    - KMP
    - Boyer-Moore
    - Robin-Karp (by far the simplest to understand and implement)

    This function implements the Robin-Karp algorithm for [sub]string-matching.

    Linear time complexity is achieved,
    because (unlike the brute-force approach!)
    the Robin-Karp algorithm doesn't require 2 nested loops.
    That is achieved by computing a hash code for each subsequent substring;
    the really clever part is to find/choose a hash function with the property that
    it is very fast to evaluate upon a _sliding window of characters_.
    (Such a hash function is sometimes called a _rolling hash function_
    or an _incremental hash function_.)
    """
    def ord(c):
        return {
            "A": 0,
            "C": 1,
            "G": 2,
            "T": 3,
        }.get(c, "ninja")

    if len(s) > len(t):
        # s is not a substring of t.
        return -1

    # Hash code for s.
    base = 10
    s_hash = functools.reduce(
        lambda h, c: h * base + ord(c),
        s,
        0,
    )

    # Hash code for the 1st substring of t (of length len(s)).
    t_hash = functools.reduce(
        lambda h, c: h * base + ord(c),
        t[: len(s)],
        0,
    )

    power_s = base ** max(len(s) - 1, 0)

    for final_idx in range(len(s), len(t)):
        # Check the current substring.
        start_idx = final_idx - len(s)
        if t_hash == s_hash and t[start_idx:final_idx] == s:
            return start_idx

        # Update the current substring's hash
        # into the subsequent substring's hash.
        t_hash -= ord(t[start_idx]) ** power_s
        t_hash = t_hash * base + ord(t[final_idx])

    # Check the very last substring.
    if t_hash == s_hash and t[-len(s) :] == s:
        return len(t) - len(s)

    # s is not a substring of t.
    return -1


if __name__ == "__main__":
    t = "GACGCCA"
    s = "CGC"
    # t = "babababbaabaabbbbb"
    # s = "baabb"

    r = robin_karp(t, s)

    print(t)
    print(s)
    print(r)
