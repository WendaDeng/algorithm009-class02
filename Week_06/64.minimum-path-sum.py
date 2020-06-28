class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if m * n == 0:  return 0
        # 使用二维数组
        # path = grid
        # for i in range(m - 1)[::-1]:    # last col
        #     path[i][-1] += path[i + 1][-1]
        # for j in range(n - 1)[::-1]:  # last row
        #     path[-1][j] += path[-1][j + 1]
        # for i in range(m - 1)[::-1]:
        #     for j in range(n - 1)[::-1]:
        #         path[i][j] = min(path[i][j + 1], path[i + 1][j]) + grid[i][j]
        # return path[0][0]

        # 仅用一维数组
        path = grid[-1]
        for j in range(n - 1)[::-1]:  # last row
            path[j] += path[j + 1]
        for i in range(m - 1)[::-1]:
            for j in range(n)[::-1]:
                if j == n - 1:
                    path[j] += grid[i][j]
                else:
                    path[j] = min(path[j + 1], path[j]) + grid[i][j]
        return path[0]
