def shortest_equivalent_path(path: str) -> str:
    original_parts = path.split("/")

    if original_parts[0] == "":
        parts = [""]
    else:
        parts = []

    for o_p in original_parts:
        if o_p == "" or o_p == ".":
            continue
        elif o_p == "..":
            if parts and parts[-1] != o_p:
                parts.pop()
            else:
                parts.append(o_p)
        else:
            parts.append(o_p)

    if parts == [""]:
        return "/"
    else:
        return "/".join(parts)


if __name__ == "__main__":
    path = "./../"
    p = shortest_equivalent_path(path)
    print(p)  # `..`
