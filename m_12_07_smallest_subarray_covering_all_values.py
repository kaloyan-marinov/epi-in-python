from typing import List

from m_12_06_smallest_subarray_covering_set import Subarray


def find_smallest_sequentially_covering_subset(
    paragraph: List[str],
    keywords: List[str],
) -> Subarray:
    """
    Assume that all `keywords` are distinct.
    """
    subarray = Subarray(start=-1, end=-1)
    complete_covering_distance = float("inf")

    # Since `keywords` does not contain any duplicates,
    # each of its entries is uniquely identified by its index within `keywords`.
    # So, we are going to use indices as keys to perform lookups within arrays
    #                         (= "arrays as hash tables").
    keyword_2_idx = {k: i for i, k in enumerate(keywords)}
    latest_occurrence = [-1] * len(keywords)
    # The i-th entry of the following array will represent
    # the length of the shortest subarray that
    # (a) ends at the latest occurrence of "keyword i"
    # and (b) sequentially covers all keywords up to "keyword i".
    partial_covering_distances = [float("inf")] * len(keywords)

    for ii, word_ii in enumerate(paragraph):
        if word_ii in keyword_2_idx:
            keyword_idx = keyword_2_idx[word_ii]

            latest_occurrence[keyword_idx] = ii

            if keyword_idx == 0:  # i.e. we've encountered the first keyword.
                partial_covering_distances[keyword_idx] = 1
            elif partial_covering_distances[keyword_idx - 1] != float("inf"):
                distance_to_prev_keyword = ii - latest_occurrence[keyword_idx - 1]
                partial_covering_distances[keyword_idx] = (
                    partial_covering_distances[keyword_idx - 1]
                    + distance_to_prev_keyword
                )

            # Last keyword, which could potentially improve the [best] `subarray`.
            if (
                keyword_idx == len(keywords) - 1
                and partial_covering_distances[-1] < complete_covering_distance
            ):
                complete_covering_distance = partial_covering_distances[-1]
                subarray = Subarray(
                    start=ii - (complete_covering_distance - 1),
                    end=ii,
                )

    return subarray


if __name__ == "__main__":
    # fmt: off
    paragraph = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "2", "4", "6", "1", "0", "1", "0", "1", "0", "3", "2", "1", "0"]
    keywords = ["0", "2", "9", "4", "6"]
    # fmt: on

    sa = find_smallest_sequentially_covering_subset(paragraph, keywords)
