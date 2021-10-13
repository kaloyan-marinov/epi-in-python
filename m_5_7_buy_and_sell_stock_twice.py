from typing import List

from m_5_6_buy_and_sell_stock import buy_and_sell_stock_2 as _buy_and_sell_stock_once


def buy_and_sell_stock_twice_1(prices: List[float]) -> float:
    """
    time:  O()
    space: O(1)
    Test PASSED (402/402) [ 588  s]
    Average running time:    2  s
    Median running time:   533 us

    The last 2 test cases took _very_ long to run,
    which indicates that the time complexity is _very_ high.
    """
    max_profit = _buy_and_sell_stock_once(prices)

    if len(prices) == 1:
        return 0
    elif len(prices) == 2:
        return max_profit

    buy_1 = float("inf")

    for i in range(1, len(prices) - 1):
        buy_1 = min(buy_1, prices[i - 1])
        sell_1 = prices[i]
        max_profit_1 = sell_1 - buy_1

        max_profit_2 = _buy_and_sell_stock_once(prices[i + 1 :])

        max_profit = max(
            max_profit,
            max_profit_1 + max_profit_2,
        )

    return max_profit


def buy_and_sell_stock_twice_2(prices: List[float]) -> float:
    """
    time:  O(n)
    space: O(n)

    Test PASSED (402/402) [  78 ms]
    Average running time:  525 us
    Median running time:    85 us
    """
    max_total_profit = 0.0

    # Forward phase:
    # record max profit if we sell on that day.
    first_buy_and_sell_profits = [0.0] * len(prices)

    min_price_so_far = float("inf")
    for i, price in enumerate(prices):
        min_price_so_far = min(min_price_so_far, price)
        max_total_profit = max(max_total_profit, price - min_price_so_far)
        first_buy_and_sell_profits[i] = max_total_profit

    # Backward phase:
    # find max profit if we make the 2nd buy on that day
    max_price_so_far = float("-inf")
    for i, price in reversed(list(enumerate(prices[1:], 1))):
        max_price_so_far = max(max_price_so_far, price)
        max_total_profit = max(
            max_total_profit,
            max_price_so_far - price + first_buy_and_sell_profits[i],
        )

    return max_total_profit
