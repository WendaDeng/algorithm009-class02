class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:    return 0
        n = len(prices)
        # 三维数组，dp[i][k][j]表示到第 i 天，至多进行 k 次交易，是否持有股票的收益
        dp = [[[0, 0] for k in range(3)] for i in range(n)]

        for i in range(n):
            for k in range(1, 3)[::-1]:
                # 初始化
                if i == 0:
                    dp[i][k][1] = -prices[i]
                else:
                    # 到第 i 天，至多进行 k 次交易，当前未持有股票
                    # 可能的选择：前一天也未持有股票，今天保持 or 前一天持有股票，今天卖出了
                    dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
                    # 到第 i 天，至多进行 k 次交易，当前持有股票
                    # 可能的选择：前一天也持有股票，今天保持 or 前一天未持有股票，今天买入了
                    dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])

        return dp[-1][-1][0]