from typing import List


def buy_and_sell_stock(prices: List[float]) -> float:
    """
    Test PASSED (402/402) [ 436  s]
    Average running time:    2  s
    Median running time:   246 us

    time:  O(n^2)
    space: O(1)

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


if __name__ == "__main__":
    prices = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
    max_profit = buy_and_sell_stock(prices)
    print(max_profit)
