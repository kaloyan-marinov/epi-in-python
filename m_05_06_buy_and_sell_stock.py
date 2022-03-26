from typing import List


def buy_and_sell_stock_1(prices: List[float]) -> float:
    """
    time:  O(n^2)
    space: O(1)

    Test PASSED (402/402) [ 436  s]
    Average running time:    2  s
    Median running time:   246 us

    The last 2 test cases took _very_ long to run,
    which indicates that the time complexity is _very_ high.
    """
    max_profit = 0

    if len(prices) == 1:
        return max_profit

    for i in range(len(prices) - 1):
        for j in range(i + 1, len(prices)):
            max_profit = max(
                max_profit,
                prices[j] - prices[i],
            )

    return max_profit


def buy_and_sell_stock_2(prices: List[float]) -> float:
    """
    time: O(n)
    space: O(1)

    Test PASSED (402/402) [  26 ms]
    Average running time:  187 us
    Median running time:    27 us
    """
    min_over_previous_days = float("inf")
    max_profit = 0

    for price in prices:
        max_profit = max(
            price - min_over_previous_days,
            max_profit,
        )
        min_over_previous_days = min(
            min_over_previous_days,
            price,
        )

    return max_profit


if __name__ == "__main__":
    prices = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
    max_profit = buy_and_sell_stock_2(prices)
    print(max_profit)
