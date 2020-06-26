class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        width = len(obstacleGrid[0])
        path = [0] * width
        path[0] = 1
        for row in obstacleGrid:
            for j in range(width):
                if row[j] == 1:
                    path[j] = 0
                elif j > 0:
                    path[j] += path[j - 1]
        return path[-1]

