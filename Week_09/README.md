### 学习笔记

本周学习的内容是高级动态规划和字符串算法。

#### 高级动态规划
使用动态规划算法解决问题的三个步骤：
1.  定义子问题（找出最优子结构）
2.  定义状态
3.  写出状态转移方程


高级动态规划相比之前的学的动态规划难点就在于状态的定义。初级的动态规划状态一般是一维，但高级一般起码有两维，甚至三维。当状态多了之后，状态转移方程就比较难写。我认为一开始只有多练，多见识不同类型的题目，然后反复多做，慢慢地就会总结出一些套路出来。

不同路径II的解法

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



#### 字符串算法
