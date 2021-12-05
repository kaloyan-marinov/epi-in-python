from typing import List


def get_valid_ip_addresses(s: str) -> List[str]:
    def _is_valid(part: str) -> bool:
        return len(part) == 1 or (part[0] != "0" and int(part) <= 255)

    valid_ips = []

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
