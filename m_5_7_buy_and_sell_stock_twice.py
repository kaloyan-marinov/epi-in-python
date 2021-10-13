from typing import List

from m_5_6_buy_and_sell_stock import buy_and_sell_stock_2 as buy_and_sell_stock_once


def buy_and_sell_stock_twice(prices: List[float]) -> float:
    """
    Test PASSED (402/402) [ 588  s]
    Average running time:    2  s
    Median running time:   533 us

    The last 2 test cases took _very_ long to run,
    which indicates that the time complexity is _very_ high.
    """
    max_profit = buy_and_sell_stock_once(prices)

    if len(prices) == 1:
        return 0
    elif len(prices) == 2:
        return max_profit

    buy_1 = float("inf")

    for i in range(1, len(prices) - 1):
        buy_1 = min(buy_1, prices[i - 1])
        sell_1 = prices[i]
        max_profit_1 = sell_1 - buy_1

        max_profit_2 = buy_and_sell_stock_once(prices[i + 1 :])

        max_profit = max(
            max_profit,
            max_profit_1 + max_profit_2,
        )

    return max_profit
