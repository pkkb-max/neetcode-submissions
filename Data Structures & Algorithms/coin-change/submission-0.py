class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = float('inf')
        dp = [0] + [INF] * amount
        for i in range(1, amount + 1):
            for c in coins:
                if c <= i and dp[i] > dp[i-c] + 1:
                    dp[i] = dp[i-c]+1
        return dp[amount] if dp[amount] != INF else -1
        