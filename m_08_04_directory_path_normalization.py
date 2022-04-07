"""
A file or directory can be specified via a string called the pathname.

The string may be:
    (a) an absolute path (starting from the root, such as `/usr/bin/gcc`), or
    (b) a path relative to the current working directory (such as `scripts/python`).

The same file (or directory) may be specified by multiple pathnames. For example:
    (A) `/usr/lib/../bin/gcc` is equivalent to the absolute path in (a), and
    (B) `scripts/./../scripts/python/././` is equivalent to the relative path in (b).
"""

from typing import List


def shortest_equivalent_path(path: str) -> str:
    """
    (This is my own solution.)

    Assume that:
        (a) `path` specifies a pathname to a file or directory,
        (b) individual directories or files have names
            that use only alphanumeric characters, and
        (c) subdirectory names may be combined using
            forward slashes (/), the current directory (.), and parent directory (..).

    Compute the shortest equivalent pathname.
    """

    original_parts = path.split("/")

    if original_parts[0] == "":
        parts = [""]
    else:
        parts = []

    for o_p in original_parts:
        # fmt: off
        if o_p == "":  # i.e. if `path` is an absolute one, or if it contains consecutive slash chars (like "/a//b///c")
            continue
        # fmt: on

        if o_p == ".":
            continue

        if o_p == "..":
            if parts and parts[-1] != o_p:
                parts.pop()
            else:  # i.e. the normalized path starts with 1 or more copies of '..'
                parts.append(o_p)
            continue

        parts.append(o_p)

    if parts == [""]:
        return "/"
    else:
        return "/".join(parts)


def shortest_equivalent_path_2(path: str) -> str:
    """
    (This is the official solution, "version 3".)

    Assume that:
        (a) `path` specifies a pathname to a file or directory,
        (b) individual directories or files have names
            that use only alphanumeric characters, and
        (c) subdirectory names may be combined using
            forward slashes (/), the current directory (.), and parent directory (..).

    Compute the shortest equivalent pathname.
    """

    if not path:
        raise ValueError("Empty string is not a valid path.")

    parts: List[str] = []  # Uses a Python list as a stack.

    for token in (
        tkn_i
        for i, tkn_i in enumerate(path.split("/"))
        if tkn_i not in {".", ""} or (tkn_i == "" and i == 0)
    ):
        if token == "..":
            if not parts or parts[-1] == "..":
                parts.append(token)
            else:
                if parts[-1] == "/":
                    raise ValueError("Path error")
                parts.pop()
        else:  # Must be a name.
            parts.append(token)

    if parts == [""]:
        result = "/"
    else:
        result = "/".join(parts)

    return result


if __name__ == "__main__":
    path = "./../"
    p = shortest_equivalent_path(path)
    print(p)  # `..`
