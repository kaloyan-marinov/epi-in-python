from typing import List


def buy_and_sell_stock_1(prices: List[float]) -> float:
    """
    (The last 2 of the provided test cases take a _very_ long time to run.)

    The `prices` represent the daily prices of a particular stock.

    Return the max profit that can be achieved
    by buying 1 share of the stock in question
    and selling the bought share on some later day.
    (If it is impossible to achieve a profit, there is no need to trade at all.)

    time:  O(n^2)
    space: O(1)
    """
    pass


def buy_and_sell_stock_2(prices: List[float]) -> float:
    """
    The `prices` represent the daily prices of a particular stock.

    Return the max profit that can be achieved
    by buying 1 share of the stock in question
    and selling the bought share on some later day.
    (If it is impossible to achieve a profit, there is no need to trade at all.)

    time:  O(n)
    space: O(1)
    """
    running_min_price = float("inf")
    max_profit = 0

    for price in prices:
        running_min_price = min(
            running_min_price,
            price,
        )
        max_profit = max(
            price - running_min_price,
            max_profit,
        )

    return max_profit


if __name__ == "__main__":
    prices = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
    max_profit = buy_and_sell_stock_2(prices)
    print(max_profit)
