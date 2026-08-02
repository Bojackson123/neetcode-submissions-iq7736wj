class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        s,f = 0, 1
        while f < len(prices):
            max_profit = max(max_profit, prices[f] - prices[s])
            if prices[f] < prices[s]:
                s = f
            f += 1
        return max(0, max_profit)
