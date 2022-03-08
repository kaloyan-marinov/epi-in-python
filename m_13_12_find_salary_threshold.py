from typing import List


def find_salary_cap_1(target_payroll: int, current_salaries: List[int]) -> float:
    current_salaries.sort()

    unadjusted_contrib_to_payroll = 0.0
    for k, salary_k in enumerate(current_salaries):
        count_adjusted = len(current_salaries) - k
        adjusted_contrib_to_payroll = count_adjusted * salary_k

        if (
            unadjusted_contrib_to_payroll + adjusted_contrib_to_payroll
            >= target_payroll
        ):
            return (target_payroll - unadjusted_contrib_to_payroll) / count_adjusted

        unadjusted_contrib_to_payroll += salary_k

    # No solution, since `target_payroll > sum(current_salaries)`.
    return -1.0


def find_salary_cap_2(target_payroll: int, current_salaries: List[int]) -> float:
    current_salaries.sort()

    unadjusted_contrib_to_payroll = 0.0
    for k, salary_k in enumerate(current_salaries):
        # (k + 1) salaries are unaffected by the cap.
        unadjusted_contrib_to_payroll += salary_k

        # n - (k + 1) salaries are affected by the cap.
        count_adjusted = len(current_salaries) - (k + 1)
        adjusted_contrib_to_payroll = count_adjusted * salary_k

        if (
            unadjusted_contrib_to_payroll + adjusted_contrib_to_payroll
            >= target_payroll
        ):
            return (target_payroll - (unadjusted_contrib_to_payroll - salary_k)) / (
                count_adjusted + 1
            )

    # No solution, since `target_payroll > sum(current_salaries)`.
    return -1.0


if __name__ == "__main__":
    target_payroll = 210
    current_salaries = [20, 30, 40, 90, 100]

    cap = find_salary_cap_2(target_payroll, current_salaries)
