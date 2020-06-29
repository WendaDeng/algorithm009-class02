class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # memorial recursion
        # def dp(i, j):
        #     if i == -1:
        #         return j + 1
        #     if j == -1:
        #         return i + 1
        #     if (i, j) in memo:
        #         return memo[(i, j)]
        #     if word1[i] == word2[j]:
        #         memo[(i, j)] = dp(i - 1, j - 1)
        #     else:
        #         memo[(i, j)] = min(dp(i, j - 1),  # insert in word1[i]
        #                    dp(i - 1, j),  # delete in word1[i]
        #                    dp(i - 1, j - 1)  # replace
        #                    ) + 1
        #     return memo[(i, j)]
        #
        # memo = {}
        # return dp(len(word1) - 1, len(word2) - 1)

        # 动态规划
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            dp[i][0] = i
        for j in range(1, n + 1):
            dp[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1],    # insert
                                   dp[i - 1][j],    # delete
                                   dp[i - 1][j - 1] # replace
                                   ) + 1
        return dp[-1][-1]

