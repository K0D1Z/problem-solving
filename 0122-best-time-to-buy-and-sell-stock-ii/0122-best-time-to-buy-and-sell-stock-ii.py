class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        share = None
        for i in range(len(prices) - 1):
            if prices[i] < prices[i+1]:
                if share is None:
                    share = prices[i]
            elif share is not None:
                profit += (prices[i] - share)
                share = None
        if share is not None:
            profit += (prices[len(prices)-1] - share)
        return profit