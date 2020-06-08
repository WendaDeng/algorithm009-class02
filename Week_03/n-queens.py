class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(queens, xy_dif, xy_sum):
            p = len(queens)
            if p == n:
                result.append(queens)
                return None
            for q in range(n):
                if q not in queens and p-q not in xy_dif and p+q not in xy_sum:
                    # 使用queen保存已经选择的皇后的下标，不需要进行状态设置和恢复
                    backtrack(queens + [q], xy_dif + [p-q], xy_sum + [p+q])

        result = []
        backtrack([], [], [])
        return  [['.' * i + 'Q' + '.' * (n - i - 1) for i in sol] for sol in result]
