from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        profit = 0
        buy = None
        last_sell = None
        curr_min = None
        for price in prices:
            if not buy:
                if not curr_min:
                    curr_min = price
                elif price < curr_min:
                    curr_min = price
                elif price - curr_min > fee:
                    buy = curr_min
                    last_sell = price
                    curr_min = None
            else:
                if last_sell - price > fee:
                    profit += last_sell - buy - fee
                    curr_min = price
                    buy = None
                    last_sell = None
                elif price > last_sell:
                    last_sell = price
        if buy:
            profit += last_sell - buy - fee
        return profit
