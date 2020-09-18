from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        max_profit = 0
        buy_price = prices[0]
        sell_price = prices[0]
        for price in prices:
            if price > sell_price:
                sell_price = price
            if price < buy_price:
                max_profit = max(max_profit, sell_price - buy_price)
                buy_price = price
                sell_price = price
            print(price, buy_price, sell_price, max_profit)
        return max(max_profit, sell_price - buy_price)