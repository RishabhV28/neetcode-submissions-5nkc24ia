class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        for i in range(len(prices)):

            future_max = max(prices[i:])

            profit = future_max - prices[i]

            res = max(res, profit)

        return res