from typing import Dict, OrderedDict

import collections
import time


class LruCache:
    def __init__(self, capacity: int) -> None:
        self._isbn_2_price = {}
        self._lru = None

    def lookup(self, isbn: int) -> int:
        price = self._isbn_2_price.get(isbn, -1)

        if price != -1:
            self._lru = isbn

        return price

    def insert(self, isbn: int, price: int) -> None:
        if isbn not in self._isbn_2_price:
            self._isbn_2_price[isbn] = price

        self._lru = isbn

    def erase(self, isbn: int) -> bool:
        is_present = isbn in self._isbn_2_price

        if is_present:
            del self._isbn_2_price[isbn]

        return is_present


# fmt: off
'''
PriceTimestampPair = collections.namedtuple(
    "PriceTimestampPair",
    ("price", "timestamp"),
)


class LruCache:
    def __init__(self, capacity: int) -> None:
        self._isbn_2_pt_pair: Dict[int, PriceTimestampPair] = {}
        self._capacity = capacity

    def lookup(self, isbn: int) -> int:
        if isbn not in self._isbn_2_pt_pair:
            price = -1
        else:
            price = self._isbn_2_pt_pair.pop(isbn).price

            self._isbn_2_pt_pair[isbn] = PriceTimestampPair(price, time.time())

        return price

    def insert(self, isbn: int, price: int) -> None:
        if len(self._isbn_2_pt_pair) == self._capacity:
            max_k = None
            max_v = PriceTimestampPair(-1, -1)
            for k, v in self._isbn_2_pt_pair.items():
                pass

    def erase(self, isbn: int) -> bool:
        pass
'''
# fmt: on


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
            price = self._isbn_2_price.pop(isbn)
        elif len(self._isbn_2_price) == self._capacity:
            self._isbn_2_price.popitem(
                last=False
            )  # causes a pop in FIFO (instead of LIFO) order!
        self._isbn_2_price[isbn] = price

    def erase(self, isbn: int) -> bool:
        return self._isbn_2_price.pop(isbn, None) is not None
