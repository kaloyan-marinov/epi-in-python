from typing import List


def get_valid_ip_addresses_1(s: str) -> List[str]:
    """
    Assume that `s` represents some valid IP[v4] address with all its periods removed.

    Return all valid IP[v4] addresses that `s` could have originated from.

    time:  O(1)
           (b/c the total # of IP[v4] addresses is constant (2 ** 32).)
    """

    valid_ips: List[str] = []

    for i in range(1, len(s) - 2):
        part_1 = s[:i]

        if not _is_valid(part_1):
            continue

        for j in range(i + 1, len(s) - 1):
            part_2 = s[i:j]

            if not _is_valid(part_2):
                continue

            for k in range(j + 1, len(s)):
                part_3 = s[j:k]
                part_4 = s[k:]

                if not _is_valid(part_3) or not _is_valid(part_4):
                    continue

                valid_ips.append(".".join([part_1, part_2, part_3, part_4]))

    return valid_ips


def _is_valid(part: str) -> bool:
    """
    Determine whether
    `part` could be among the 8-bit components of a valid IP[v4] address.

    (
        Neither one of `00`, `01, `000` is valid.
        But `0` is valid.
    )
    """
    return len(part) == 1 or (part[0] != "0" and int(part) <= 255)


def get_valid_ip_addresses_2(s: str) -> List[str]:
    """
    (This is a mild refactoring of the official solution.)

    Assume that `s` represents some valid IP[v4] address with all its periods removed.

    Return all valid IP[v4] addresses that `s` could have originated from.

    time:  O(1)
           (b/c the total # of IP[v4] addresses is constant (2 ** 32).)
    """

    valid_ips: List[str] = []
    parts: List[str] = [""] * 4

    for i in range(1, min(4, len(s))):
        parts[0] = s[:i]

        if not _is_valid(parts[0]):
            continue

        for j in range(1, min(4, len(s) - i)):
            parts[1] = s[i : i + j]

            if not _is_valid(parts[1]):
                continue

            for k in range(1, min(4, len(s) - i - j)):
                parts[2] = s[i + j : i + j + k]
                parts[3] = s[i + j + k :]

                if not _is_valid(parts[2]) or not _is_valid(parts[3]):
                    continue

                valid_ips.append(".".join(parts))

    return valid_ips
