# https://leetcode.com/problems/coin-change/description/?envType=study-plan-v2&envId=top-interview-150

# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
# You may assume that you have an infinite number of each kind of coin.

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.coins = sorted(coins)
        self.solutions = { 0: 0 }
        return self.recursive_coinChange(amount)
    def recursive_coinChange(self, n: int) -> int:
        if n not in self.solutions: 
            usable_coins = []
            i = 0
            while i < len(self.coins) and self.coins[i] <= n:
                usable_coins.append(self.coins[i])
                i += 1
            solutions = []
            for coin in usable_coins:
                subproblem = self.recursive_coinChange(n - coin)
                if subproblem >= 0:
                    solutions.append(subproblem + 1)
            self.solutions[n] = min(solutions) if len(solutions) > 0 else -1
        return self.solutions[n]