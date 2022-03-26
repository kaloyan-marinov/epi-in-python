from typing import List


def generate_balanced_parentheses(num_pairs: int) -> List[str]:
    """
    For example:

    Test ... ( 4/11) ...
    Arguments
        num_pairs: 3

    ...
        expected:  ['((()))', '(()())', '(())()', '()(())', '()()()']
        ...
    """

    def _guided_generate_balanced_parentheses(
        num_left_parens_needed: int,
        num_right_parens_needed: int,
        valid_prefix: str,
        result: List[str] = [],
    ) -> List[str]:

        if num_left_parens_needed > 0:  # i.e. able to append "(".
            _guided_generate_balanced_parentheses(
                num_left_parens_needed - 1,
                num_right_parens_needed,
                valid_prefix + "(",
            )

        if num_left_parens_needed < num_right_parens_needed:  # i.e. able to append ')'.
            _guided_generate_balanced_parentheses(
                num_left_parens_needed,
                num_right_parens_needed - 1,
                valid_prefix + ")",
            )

        if num_right_parens_needed == 0:
            result.append(valid_prefix)

        return result

    return _guided_generate_balanced_parentheses(
        num_pairs,
        num_pairs,
        "",
    )


if __name__ == "__main__":
    result = generate_balanced_parentheses(0)
    print(result)
