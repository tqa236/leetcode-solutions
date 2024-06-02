from typing import List
import sys

sys.setrecursionlimit(10**9)
CACHE = {}


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        coins = [coin for coin in sorted(coins, reverse=True) if coin <= amount]
        if not coins:
            return -1

        min_coins = self.coinChangeRecursive(coins, amount)
        if min_coins == float("inf"):
            return -1
        return min_coins

    def coinChangeRecursive(
        self, coins: List[int], amount: int, min_coins: int = None
    ) -> int:
        # print(CACHE)
        # print(coins, amount)
        if amount == 0:
            return 0
        coins = [coin for coin in sorted(coins, reverse=True) if coin <= amount]
        if not coins:
            return float("inf")
        if amount in coins:
            return 1
        if len(coins) == 1 and amount % coins[0] != 0:
            return float("inf")
        if min_coins is None:
            min_coins = float("inf")
        for coin in coins:
            if (tuple(coins), amount - coin) in CACHE:
                return CACHE[(tuple(coins), amount - coin)]
            val = self.coinChangeRecursive(coins, amount - coin, min_coins)
            if val < min_coins:
                min_coins = val
        CACHE[(tuple(coins), amount)] = min_coins + 1
        return min_coins + 1

    # def find_fewest_coins_recursive(
    #     self, coins: List[int], target: int, coin_list: Optional[List[int]] = None
    # ) -> None:
    #     """Find the fewest number of coins for a given price recursively."""
    #     print(target, coins)
    #     coins = [coin for coin in coins if coin <= target]
    #     if not coins:
    #         return []
    #     if coin_list is None:
    #         coin_list = []
    #     if target % coins[0] == 0:
    #         return coin_list + [coins[0]] * (target // coins[0])
    #     best_coin_list = []
    #     min_length = target // min(coins) + len(coin_list) + 1
    #     for coin in coins:
    #         if len(coin_list) + target // coin < min_length:
    #             target_coin_list = self.find_fewest_coins_recursive(
    #                 coins, target - coin, coin_list + [coin]
    #             )
    #             CACHE[(coins, target)] =
    #             if target_coin_list and len(target_coin_list) < min_length:
    #                 min_length = len(target_coin_list)
    #                 best_coin_list = target_coin_list
    #     return best_coin_list

    # def coinChangeRecursive(
    #     self, coins: List[int], amount: int, coin_nums: Optional[int] = None
    # ) -> None:
    #     print(coins, amount, coin_nums)
    #     if amount == 0:
    #         return 0
    #     coins = [coin for coin in coins if coin <= amount]
    #     if not coins:
    #         return -1
    #     if coin_nums is None:
    #         coin_nums = 0
    #     if amount % coins[0] == 0:
    #         return coin_nums + amount // coins[0]
    #     min_coins = -1
    #     min_length = amount // min(coins) + coin_nums + 1
    #     for coin in coins:
    #         if coin_nums + amount // coin < min_length:
    #             target_coin_nums = self.coinChangeRecursive(
    #                 coins, amount - coin, coin_nums + 1
    #             )
    #             if target_coin_nums >= 0 and target_coin_nums < min_length:
    #                 min_length = target_coin_nums
    #                 min_coins = target_coin_nums
    #     return min_coins
