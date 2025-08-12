#322. Coin Change
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize DP array with a large number
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0  # Base case: 0 coins to make 0 amount
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        
        return dp[amount] if dp[amount] != amount + 1 else -1
