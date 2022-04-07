from typing import Dict, Iterator, List, Set

import collections

from m_07_00_common import DoublyLinkedList, DoublyLinkedListNode

Subarray = collections.namedtuple(
    "Subarray",
    ("start", "end"),
)


def find_smallest_subarray_covering_set_1(
    paragraph: List[str],
    keywords: Set[str],
) -> Subarray:
    """
    This is my 2nd refactoring of the official solution.
    """

    subarray = Subarray(start=-1, end=-1)

    keyword_2_count_within_subarray: Dict[str, int] = {k: 0 for k in keywords}
    count_keywords_missing_from_subarray = len(keywords)

    ii = 0
    for jj, word_jj in enumerate(paragraph):
        # Process `word_jj`,
        # thus adding that word to the (current) subinterval.
        if word_jj in keywords:
            if keyword_2_count_within_subarray[word_jj] == 0:
                count_keywords_missing_from_subarray -= 1

            keyword_2_count_within_subarray[word_jj] += 1

        # If all `keywords` are covered by the (current) `subarray`,
        # keep advancing its left endpoint `ii`
        # until it no longer covers all `keywords`.
        while count_keywords_missing_from_subarray == 0:
            # Update the `subarray`.
            if (
                subarray == Subarray(start=-1, end=-1)
                or jj - ii < subarray.end - subarray.start
            ):
                subarray = Subarray(start=ii, end=jj)

            # Advance the (current) subinterval's left endpoint `ii`,
            # thus discarding the word at that index.
            word_ii = paragraph[ii]
            if word_ii in keywords:
                keyword_2_count_within_subarray[word_ii] -= 1

                if keyword_2_count_within_subarray[word_ii] == 0:
                    count_keywords_missing_from_subarray += 1
            ii += 1

    return subarray


def find_smallest_subarray_covering_set_2(
    paragraph: Iterator[str],
    keywords: Set[str],
) -> Subarray:
    subarray = Subarray(start=-1, end=-1)

    keyword_2_dll_node: Dict[str, DoublyLinkedListNode] = {k: None for k in keywords}
    dll = DoublyLinkedList()

    for ii, word_ii in enumerate(paragraph):
        if word_ii in keyword_2_dll_node:
            # If `word_ii` has been encountered earlier,
            # remove its corresponding node from `dll`.
            dll_node_ii = keyword_2_dll_node[word_ii]
            if dll_node_ii is not None:
                dll.remove(dll_node_ii)

            # Insert into `dll`
            # a node with `word_ii`'s most recent location.
            dll.insert_after(ii)
            keyword_2_dll_node[word_ii] = dll.tail

            if len(dll) == len(keywords):  # i.e. the `dll` covers all the `keywords`.
                if (
                    subarray == Subarray(start=-1, end=-1)
                    or dll.tail.data - dll.head.data < subarray.end - subarray.start
                ):
                    subarray = Subarray(start=dll.head.data, end=dll.tail.data)

    return subarray
