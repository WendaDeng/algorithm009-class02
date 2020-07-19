class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if m == 0:  return 0
        n = len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        maxarea = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':   continue
                # 计算第 i 行第 j 列的宽度，第 0 列需要单独处理
                width = dp[i][j] = dp[i][j - 1] + 1 if j else 1

                # 计算以第 i 行第 j 列为右下角的矩形的面积
                for k in range(i, -1, -1):
                    width = min(width, dp[k][j])
                    maxarea = max(maxarea, width * (i - k + 1))
        return maxarea
