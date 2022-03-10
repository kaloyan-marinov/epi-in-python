from m_14_00_common import BstNode


def pair_includes_ancestor_and_descendant_of_m_1(
    possible_anc_or_desc_0: BstNode,
    possible_anc_or_desc_1: BstNode,
    middle: BstNode,
) -> bool:
    """
    Assume all keys are unique.

    time:  O(h)

    shortcoming:    in the scenario,
                    where the 3 nodes are totally ordered
                          (= this function is expected to return `True`),
                          and the 3 nodes are very close [together],
                    if this function begins the search from the lower of the 2 nodes,
                    it will incur the full O(h) time complexity

    each of this module's other functions
    handles the above-described scenario more efficiently
    """

    def _has_as_proper_descendant(
        start_n: BstNode,
        test_n: BstNode,
    ):
        if test_n is start_n:
            return False

        while start_n:
            if start_n.data < test_n.data:
                start_n = start_n.right
            else:  # i.e. start_n.data > test_n.data
                start_n = start_n.left

            if start_n is test_n:
                return True

        return False

    m_has_0_as_proper_desc = _has_as_proper_descendant(middle, possible_anc_or_desc_0)
    m_has_1_as_proper_desc = _has_as_proper_descendant(middle, possible_anc_or_desc_1)

    if (m_has_0_as_proper_desc and m_has_1_as_proper_desc) or (
        not m_has_0_as_proper_desc and not m_has_1_as_proper_desc
    ):
        return False

    if m_has_0_as_proper_desc and not m_has_1_as_proper_desc:
        return _has_as_proper_descendant(possible_anc_or_desc_1, middle)

    if not m_has_0_as_proper_desc and m_has_1_as_proper_desc:
        return _has_as_proper_descendant(possible_anc_or_desc_0, middle)


def pair_includes_ancestor_and_descendant_of_m_2(
    possible_anc_or_desc_0: BstNode,
    possible_anc_or_desc_1: BstNode,
    middle: BstNode,
) -> bool:
    """
    Assume all keys are unique.
    """

    search_0 = possible_anc_or_desc_0
    search_1 = possible_anc_or_desc_1

    # Perform interleaved searching
    # from `possible_anc_or_desc_0` and [from] `possible_anc_or_desc_1`
    # for `middle`.
    while (
        search_0 is not possible_anc_or_desc_1
        and search_0 is not middle
        and search_1 is not possible_anc_or_desc_0
        and search_1 is not middle
        and (search_0 or search_1)
    ):
        if search_0:
            search_0 = search_0.left if search_0.data > middle.data else search_0.right

        if search_1:
            search_1 = search_1.left if search_1.data > middle.data else search_1.right

    # If
    #   both searches were unsuccessful,
    #   or we got from `possible_anc_or_desc_0` to `possible_anc_or_desc_1` w/o seeing middle,
    #   or we got from `possible_anc_or_desc_1` to `possible_anc_or_desc_0` w/o seeing middle,
    # then `middle` cannot lie between `possible_anc_or_desc_0` and `possible_anc_or_desc_1`.
    if (
        (search_0 is not middle and search_1 is not middle)
        or search_0 is possible_anc_or_desc_1
        or search_1 is possible_anc_or_desc_0
    ):
        return False

    def _search_target(
        source: BstNode,
        target: BstNode,
    ) -> bool:
        while source and source is not target:
            source = source.left if source.data > target.data else source.right

        return source is target

    # If we get here,
    # we already know one of `possible_anc_or_desc_0` or `possible_anc_or_desc_1`
    # has a path to `middle`.
    # Check if `middle` has a path to `possible_anc_or_desc_1` or `possible_anc_or_desc_0`.
    return _search_target(
        middle,
        possible_anc_or_desc_1 if search_0 is middle else possible_anc_or_desc_0,
    )


def pair_includes_ancestor_and_descendant_of_m_3(
    possible_anc_or_desc_0: BstNode,
    possible_anc_or_desc_1: BstNode,
    middle: BstNode,
) -> bool:
    """
    Assume all keys are distinct.

    This is a cleaner refactoring of the *_2 function.
    """

    search_0 = possible_anc_or_desc_0
    search_1 = possible_anc_or_desc_1

    if search_0 is search_1 or search_0 is middle or search_1 is middle:  # NB!
        return False

    # Perform interleaved searching
    # from `possible_anc_or_desc_0` and [from] `possible_anc_or_desc_1`
    # for `middle`.
    while (
        search_0 is not possible_anc_or_desc_1
        and search_0 is not middle
        and search_1 is not possible_anc_or_desc_0
        and search_1 is not middle
        # and (search_0 or search_1)
    ):

        if search_0:
            search_0 = search_0.left if search_0.data > middle.data else search_0.right

        if search_1:
            search_1 = search_1.left if search_1.data > middle.data else search_1.right

        if search_0 is None and search_1 is None:
            # `search_0` has reached its terminal value
            # without encountering `middle` or `possible_anc_or_desc_0`
            # and the same holds true for `search_1`
            return False

    # If
    #   we got from `possible_anc_or_desc_0` to `possible_anc_or_desc_1` w/o seeing middle,
    #   or we got from `possible_anc_or_desc_1` to `possible_anc_or_desc_0` w/o seeing middle,
    # then `middle` cannot lie between `possible_anc_or_desc_0` and `possible_anc_or_desc_1`.
    if (
        # (search_0 is not middle and search_1 is not middle)
        search_0 is possible_anc_or_desc_1
        or search_1 is possible_anc_or_desc_0
    ):
        return False

    def _has_as_descendant(
        source: BstNode,
        target: BstNode,
    ) -> bool:
        """
        Check if `source` has `target` as a (not-necessarily-proper) descendant.
        """
        while source and source is not target:
            source = source.left if source.data > target.data else source.right

        return source is target

    # If we get here,
    # we already know one of `possible_anc_or_desc_0` or `possible_anc_or_desc_1`
    # has a path to `middle`.
    # Check if `middle` has a path to `possible_anc_or_desc_1` or `possible_anc_or_desc_0`.
    return _has_as_descendant(
        middle,
        possible_anc_or_desc_1 if search_0 is middle else possible_anc_or_desc_0,
    )


if __name__ == "__main__":
    n_10 = BstNode(data=10)
    n_2 = BstNode(data=2, right=n_10)

    result = pair_includes_ancestor_and_descendant_of_m_3(
        n_2,
        n_10,
        n_2,
    )
    print(result)
