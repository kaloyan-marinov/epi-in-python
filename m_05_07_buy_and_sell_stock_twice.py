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

    Test PASSED (402/402) [  67 ms]
    Average running time:  486 us
    Median running time:    81 us
    """
    max_total_profit = 0.0

    # Forward phase:
    # record max profit if we make the 1st sell on that day.
    profits_for_1st_sell_on_i_th_day = [0.0] * len(prices)

    min_price_over_prev_days = float("inf")
    for i, p_i in enumerate(prices):
        profit_from_first_sell_on_day_i = p_i - min_price_over_prev_days
        max_total_profit = max(max_total_profit, profit_from_first_sell_on_day_i)
        min_price_over_prev_days = min(min_price_over_prev_days, p_i)
        profits_for_1st_sell_on_i_th_day[i] = max_total_profit

    # Backward phase:
    # find max profit if we make the 2nd buy on that day.
    max_price_over_next_days = float("-inf")
    for i in reversed(range(1, len(prices))):
        p_i = prices[i]
        profit_from_2nd_buy_on_day_i = max_price_over_next_days - p_i
        max_price_over_next_days = max(max_price_over_next_days, p_i)
        max_total_profit = max(
            max_total_profit,
            profits_for_1st_sell_on_i_th_day[i] + profit_from_2nd_buy_on_day_i,
        )

    return max_total_profit
