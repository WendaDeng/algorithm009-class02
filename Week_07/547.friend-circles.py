class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        def dfs(i):
            for j in range(m):
                if M[i][j] == 1 and not visited[j]:
                    visited[j] = 1
                    dfs(j)

        m = len(M)
        if m == 0:
            return 0
        visited = [False] * m
        count = 0
        for i in range(m):
            if not visited[i]:
                dfs(i)
                count +=1
        return count