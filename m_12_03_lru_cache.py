from typing import OrderedDict

import collections


class LruCache:
    def __init__(self, capacity: int) -> None:
        self._isbn_2_price: OrderedDict[int, int] = collections.OrderedDict()
        self._capacity = capacity

    def lookup(self, isbn: int) -> int:
        if isbn not in self._isbn_2_price:
            return -1

        price = self._isbn_2_price.pop(isbn)
        self._isbn_2_price[isbn] = price
        return price

    def insert(self, isbn: int, price: int) -> None:
        if isbn in self._isbn_2_price:
            p = self._isbn_2_price.pop(isbn)
            self._isbn_2_price[isbn] = p
            return

        if len(self._isbn_2_price) == self._capacity:
            self._isbn_2_price.popitem(
                last=False
            )  # causes a pop in FIFO (instead of LIFO) order!

        self._isbn_2_price[isbn] = price

    def erase(self, isbn: int) -> bool:
        return self._isbn_2_price.pop(isbn, None) is not None
