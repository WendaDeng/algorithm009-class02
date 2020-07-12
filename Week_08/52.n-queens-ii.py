class Solution:
    def totalNQueens(self, n: int) -> int:
        if n <= 0:  return 0
        self.count = 0
        self.dfs(n, 0, 0, 0, 0)
        return  self.count

    def dfs(self, n, row, cols, pie, na):
        if row == n:
            self.count += 1
            return
        bits = (~(cols | pie | na)) & ((1 << n) - 1)    # 得到当前所有空位
        while bits:
            p = bits & -bits    # 得到第一个可以放置的位置
            self.dfs(n, row + 1, cols | p, (pie | p) << 1, (na | p) >> 1)
            # 因为是传值参数，所以不需要回溯参数
            bits = bits & (bits - 1)    # 表示在位置 p 放上皇后