from typing import List


def num_combinations_for_final_score(
    final_score: int,
    individual_play_scores: List[int],
) -> int:
    # There is only 1 way to achieve a final score of 0.
    A: List[List[int]] = [[1] + [0] * final_score for _ in individual_play_scores]

    for j in range(1, final_score + 1):
        for i in range(len(individual_play_scores)):
            without_plays_of_type_i = A[i - 1][j] if i - 1 >= 0 else 0

            with_plays_of_type_i = (
                A[i][j - individual_play_scores[i]]
                if j - individual_play_scores[i] >= 0
                else 0
            )

            A[i][j] = without_plays_of_type_i + with_plays_of_type_i

    return A[-1][-1]


if __name__ == "__main__":
    result = num_combinations_for_final_score(12, [2, 3, 7])

    print(result)
