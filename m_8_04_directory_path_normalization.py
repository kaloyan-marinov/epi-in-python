def shortest_equivalent_path(path: str) -> str:
    original_parts = path.split("/")

    parts = []
    for o_p in original_parts:
        if o_p == ".":
            continue
        elif o_p == "..":
            if parts:
                parts.pop()
            else:
                parts.append(o_p)
        else:
            parts.append(o_p)

    return "/".join(parts)


if __name__ == "__main__":
    path = "./../"
    p = shortest_equivalent_path(path)
    print(p)  # `../` but expected `..`
