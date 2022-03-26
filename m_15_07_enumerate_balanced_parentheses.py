from typing import List


def generate_balanced_parentheses(num_pairs: int) -> List[str]:
    """
    Test FAILED ( 4/11) [  21 us]
    Arguments
        num_pairs: 3

    Failure info
        expected:  ['((()))', '(()())', '(())()', '()(())', '()()()']
        result:    ['((()))', '(()())', '()(())', '()()()']
    """
    # fmt: off
    '''
    result: List[str] = []

    def _helper(n_pairs) -> List[str]:
        if n_pairs == 0:
            return [""]
        if n_pairs == 1:
            return ["()"]

        temp = _helper(n_pairs - 1)
        return ["(" + p + ")" for p in temp] + ["()" + p for p in temp]

    return _helper(num_pairs)
    '''
    # fmt: on
    result: List[str] = []

    def _helper(n_pairs) -> List[str]:
        if n_pairs == 2:
            return ["(())"]

        temp = _helper(n_pairs - 1)
        return (
            ["(" + p + ")" for p in temp]
            + ["()" + p for p in temp[:-1]]
            + [p + "()" for p in temp[:-1]]
        )

    if num_pairs == 0:
        return [""]
    elif num_pairs == 1:
        return ["()"]

    return _helper(num_pairs) + ["()" * num_pairs]


def generate_balanced_parentheses_2(num_pairs: int) -> List[str]:
    def _directed_generate_balanced_parentheses(
        num_left_parens_needed: int,
        num_right_parens_needed: int,
        valid_prefix: str,
        result: List[str] = [],
    ) -> List[str]:

        if num_left_parens_needed > 0:  # i.e. able to append "(".
            _directed_generate_balanced_parentheses(
                num_left_parens_needed - 1,
                num_right_parens_needed,
                valid_prefix + "(",
            )

        if num_left_parens_needed < num_right_parens_needed:  # i.e. able to append ')'.
            _directed_generate_balanced_parentheses(
                num_left_parens_needed,
                num_right_parens_needed - 1,
                valid_prefix + ")",
            )

        if num_right_parens_needed == 0:
            result.append(valid_prefix)

        return result

    return _directed_generate_balanced_parentheses(
        num_pairs,
        num_pairs,
        "",
        result=[],  # This _must_ be removed!
    )


if __name__ == "__main__":
    result = generate_balanced_parentheses_2(0)
    print(result)
