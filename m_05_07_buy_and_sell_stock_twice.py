from typing import List

# from m_05_06_buy_and_sell_stock import buy_and_sell_stock_2


def buy_and_sell_stock_twice_1(prices: List[float]) -> float:
    """
    (The last 2 of the provided test cases take a _very_ long time to run.)

    The `prices` represent the daily prices of a particular stock.

    Return the max profit that can be achieved
    by buying and selling 1 share of the stock in question at most twice.

    time:  O(n^2)
    space: O(1)
    """
    pass


def buy_and_sell_stock_twice_2(prices: List[float]) -> float:
    """
    (The last 2 of the provided test cases take a _very_ long time to run.)

    The `prices` represent the daily prices of a particular stock.

    Return the max profit that can be achieved
    by buying and selling 1 share of the stock in question at most twice.

    time:  O(n)
    space: O(n)
    """

    # Forward pass: (pre-)compute a cache,
    # whose `i`-th cell stores the max profit if
    # (a) we are allowed to make a single sale, and
    # (b) do make the sale on day `i`.
    day_idx_2_max_profit_for_single_sale_on_or_before_day_idx: List[float] = [
        0.0
    ] * len(prices)

    max_total_profit = 0.0
    min_price_over_prev_days = float("inf")

    for i, p_i in enumerate(prices):
        min_price_over_prev_days = min(
            min_price_over_prev_days,
            p_i,
        )
        max_total_profit = max(
            p_i - min_price_over_prev_days,
            max_total_profit,
        )
        day_idx_2_max_profit_for_single_sale_on_or_before_day_idx[i] = max_total_profit

    # Backward pass: iteratively determine the max profit if
    # we make the 2nd buy on day `j`.
    max_total_profit = 0.0
    max_price_over_day_j_and_later = float("-inf")

    for j in reversed(range(1, len(prices))):
        p_j = prices[j]
        max_price_over_day_j_and_later = max(max_price_over_day_j_and_later, p_j)

        profit_from_1st_buy_sell = (
            day_idx_2_max_profit_for_single_sale_on_or_before_day_idx[j]
        )
        profit_from_2nd_buy_sell = max_price_over_day_j_and_later - p_j
        max_total_profit = max(
            max_total_profit,
            profit_from_1st_buy_sell + profit_from_2nd_buy_sell,
        )

    return max_total_profit
