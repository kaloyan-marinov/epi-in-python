import collections
import functools
import heapq
from typing import Dict, List


def compute_top_k_variance(
    students: List[str], scores: List[float], k: int
) -> Dict[str, float]:
    """
    Assume that `students` and `scores` have the same length.

    This function computes, for each string that appears at least `k` times,
    the variance of the top k scores that correspond to it.
    Strings that appear fewer than `k` times are not considered.
    """
    all_scores: Dict[str, List[float]] = collections.defaultdict(list)
    for student, score in zip(students, scores):
        all_scores[student].append(score)

    top_k_scores: Dict[str, List[float]] = {
        student: heapq.nlargest(k, scores)
        for student, scores in all_scores.items()
        if len(scores) >= k
    }

    top_k_variance: Dict[str, float] = {
        student: functools.reduce(
            lambda variance, score: variance + (score - mean) ** 2,
            scores,
            0,
        )
        for student, scores, mean in (
            (student, scores, sum(scores) / k)
            for student, scores in top_k_scores.items()
        )
    }

    return top_k_variance
