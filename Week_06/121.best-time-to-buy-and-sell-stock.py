class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:    return 0
        minp = prices[0]
        maxv = 0
        for price in prices:
            maxv = max(maxv, price - minp)
            minp = min(minp, price)
        return maxv
