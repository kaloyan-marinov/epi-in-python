from typing import List


def replace_and_remove(
    size: int,
    s: List[str],
) -> int:
    # Perform a forward iteration
    # to remove all `b`s and to count the number of `a`s.
    write_idx = 0
    a_count = 0
    for i in range(size):
        if s[i] != "b":
            s[write_idx] = s[i]
            write_idx += 1

        if s[i] == "a":
            a_count += 1

    # Perform a backward iteration:
    # replace each `a` with `dd`
    # (starting from the [right] end of the "end result").
    cur_idx = write_idx - 1
    write_idx += a_count - 1
    final_size = write_idx + 1

    while cur_idx >= 0:
        if s[cur_idx] == "a":
            s[write_idx - 1 : write_idx + 1] = "dd"
            write_idx -= 2
        else:
            s[write_idx] = s[cur_idx]
            write_idx -= 1

        cur_idx -= 1

    return final_size
