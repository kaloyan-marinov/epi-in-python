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
    (This is the official solution, "version 5".)

    Assume that:
        (a) `path` specifies a pathname to a file or directory,
        (b) individual directories or files have names
            that use only alphanumeric characters, and
        (c) subdirectory names may be combined using
            forward slashes (/), the current directory (.), and parent directory (..).

    Compute the shortest equivalent pathname.

    time:  O(n)
           where n := len(path)
    """

    if not path:
        raise ValueError("Empty string is not a valid path.")

    parts: List[str] = []  # Uses a Python list as a stack.

    # Special case: `path` is an absolute path.
    if path[0] == "/":
        parts.append("/")

    for token in (tkn for tkn in path.split("/") if tkn not in {".", ""}):
        if token != "..":  # Must be a name.
            parts.append(token)
        else:  # i.e. `token == ".."`
            if not parts or parts[-1] == "..":
                parts.append(token)
            else:
                if parts[-1] == "/":
                    raise ValueError("Path error")
                parts.pop()

    result = "/".join(parts)

    # If `path` was an absolute path, then `result` now starts with `//`,
    # which should be shortened to `/`.
    start_idx = int(result.startswith("//"))

    return result[start_idx:]


if __name__ == "__main__":
    path = "./../"
    p = shortest_equivalent_path(path)
    print(p)  # `..`
