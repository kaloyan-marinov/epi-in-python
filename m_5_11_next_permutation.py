from typing import List


def next_permutation(perm: List[int]) -> List[int]:
    """
    6 2 1 5 4 3 0
                    find the longest decreasing suffix
          - - - -
        ||
        ..
        e
                    find the smallest entry in the suffix that's greater than e
                    (which can be achieved by scanning the suffix from right to left)
              -
                    and swap those 2 entries
    6 2 3 5 4 1 0
                    sort the suffix,
                    which in this case can be achieved by reversing it
    6 2 3 0 1 4 5
    """

    # Find the first entry from the right
    # that is < the entry immediately after it.
    inversion_point = len(perm) - 2
    while inversion_point >= 0 and perm[inversion_point] >= perm[inversion_point + 1]:
        inversion_point -= 1

    if inversion_point == -1:
        # `perm` is the last permutation
        return []

    # Swap the smallest entry after `inversion_point`
    # that is `> perm[inversion_point]`.
    # (
    # Since `perm[inversion_point + 1:]` is in decreasing order,
    # that guarantees/implies that,
    #   if we search in reverse order,
    #   then the first entry that is `> perm[inversion_point]` is the entry to swap with.
    # )
    for i in reversed(range(inversion_point + 1, len(perm))):
        if perm[i] > perm[inversion_point]:
            perm[inversion_point], perm[i] = perm[i], perm[inversion_point]
            break

    # At this stage,
    # `perm[inversion_point + 1:]` is still guaranteed to be in decreasing order,
    # so its smallest lexicographic order
    # - corresponding to sorting it in increasing order! -
    # can be obtained by simply reversing it.
    perm[inversion_point + 1 :] = reversed(perm[inversion_point + 1 :])

    return perm


if __name__ == "__main__":
    A: List[int] = [17, 17, 17, 17]
    print(next_permutation(A))
