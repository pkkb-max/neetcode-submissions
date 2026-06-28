class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxSoFar = 0
        minSoFar = prices[0]

        for sell in prices:
            maxSoFar = max(maxSoFar, sell - minSoFar)
            minSoFar = min(minSoFar, sell)
        return maxSoFar