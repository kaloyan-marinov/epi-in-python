from typing import Deque, Dict, List, Optional, Set


import collections
import typing


def _differ_in_exactly_1_character(s: str, t: str) -> bool:
    differences = 0
    for a, b in zip(s, t):
        if a != b:
            differences += 1

        if differences > 1:
            return False

    return True


def transform_string(D: Set[str], s: str, t: str) -> int:
    """
    This function
    works
    but is _very_ slow.

    Assume that `s`, `t`, and every string in `D` is of the same length.

    (The auxiliary function relies on that assumption to hold true.)
    """
    vertex_2_parent: Dict[str, Optional[str]] = {s: None}

    q: Deque[str] = collections.deque(
        [s],
    )

    while q:
        q_word = q.popleft()

        for d_word in D:
            if (
                _differ_in_exactly_1_character(q_word, d_word)
                and d_word not in vertex_2_parent
            ):
                vertex_2_parent[d_word] = q_word
                q.append(d_word)

                if d_word == t:
                    production_sequence: List[str] = []
                    w = t
                    while w:
                        production_sequence.append(w)
                        w = vertex_2_parent[w]
                    return len(production_sequence) - 1

    return -1


import string


def transform_string_v2(D: Set[str], s: str, t: str) -> int:
    """
    Assume that all characters are lowercase alphabet characters.

    "Assume that `s`, `t`, and every string in `D` is of the same length."
    """
    vertex_2_parent: Dict[str, Optional[str]] = {s: None}

    q: Deque[str] = collections.deque(
        [s],
    )

    while q:
        q_word = q.popleft()

        q_word_characters = list(q_word)
        for i in range(len(q_word_characters)):
            old_character_i = q_word_characters[i]

            for new_character_i in string.ascii_lowercase:
                q_word_characters[i] = new_character_i

                q_next_word_candidate = "".join(q_word_characters)
                if (
                    q_next_word_candidate in D
                    and q_next_word_candidate not in vertex_2_parent
                ):
                    vertex_2_parent[q_next_word_candidate] = q_word
                    q.append(q_next_word_candidate)

                    if q_next_word_candidate == t:
                        production_sequence: List[str] = []
                        w = t
                        while w:
                            production_sequence.append(w)
                            w = vertex_2_parent[w]
                        return len(production_sequence) - 1

                q_word_characters[i] = old_character_i

    return -1


def transform_string_v3(D: Set[str], s: str, t: str) -> int:
    """
    Assume that all characters are lowercase alphabet characters.

    "Assume that `s`, `t`, and every string in `D` is of the same length."
    """
    vertex_2_level: Dict[str, int] = {s: 0}

    q: Deque[str] = collections.deque(
        [s],
    )

    while q:
        q_word = q.popleft()

        q_word_characters = list(q_word)
        for i in range(len(q_word_characters)):
            old_character_i = q_word_characters[i]

            for new_character_i in string.ascii_lowercase:
                q_word_characters[i] = new_character_i

                q_next_word_candidate = "".join(q_word_characters)
                if (
                    q_next_word_candidate in D
                    and q_next_word_candidate not in vertex_2_level
                ):
                    vertex_2_level[q_next_word_candidate] = vertex_2_level[q_word] + 1
                    q.append(q_next_word_candidate)

                    if q_next_word_candidate == t:
                        return vertex_2_level[t]

                q_word_characters[i] = old_character_i

    return -1


class StringDistancePair(typing.NamedTuple):
    candidate_string: str
    distance: int


def transform_string_v4(
    D: Set[str],
    s: str,
    t: str,
) -> int:
    """
    (This is the official solution.)

    Assume that all characters are lowercase alphabet characters.

    "Assume that `s`, `t`, and every string in `D` is of the same length."
    """
    q: Deque[StringDistancePair] = collections.deque(
        [StringDistancePair(s, 0)],
    )

    D.remove(s)  # Marks `s` as visited by erasing it from `D`.

    while q:
        w_d_pair = q.popleft()

        if w_d_pair.candidate_string == t:
            return w_d_pair.distance

        # Try all possible 1-character transformations of `w_d_pair.candidate_string`.
        for i in range(len(w_d_pair.candidate_string)):
            for c in string.ascii_lowercase:
                candidate_w = (
                    w_d_pair.candidate_string[:i]
                    + c
                    + w_d_pair.candidate_string[i + 1 :]
                )
                if candidate_w in D:
                    D.remove(candidate_w)
                    q.append(
                        StringDistancePair(candidate_w, w_d_pair.distance + 1),
                    )

    return -1
