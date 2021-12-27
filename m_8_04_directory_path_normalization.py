def shortest_equivalent_path(path: str) -> str:
    original_parts = path.split("/")

    parts = []
    for o_p in original_parts:
        if o_p == ".":
            continue
        elif o_p == "..":
            parts.pop()
        else:
            parts.append(o_p)

    return "/".join(parts)


if __name__ == "__main__":
    path = "./../"
    p = shortest_equivalent_path(path)  # `IndexError: pop from empty list`
