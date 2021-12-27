def shortest_equivalent_path(path: str) -> str:
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


if __name__ == "__main__":
    path = "./../"
    p = shortest_equivalent_path(path)
    print(p)  # `..`
