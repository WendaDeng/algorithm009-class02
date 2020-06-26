class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        path = [1] * m
        for i in range(1, n):
            for j in range(1, m)[::-1]:
                path[j - 1] += path[j]
        return path[0]
