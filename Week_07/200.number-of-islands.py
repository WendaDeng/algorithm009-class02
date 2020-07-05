class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:  return 0

        def DFSMarker(row:int, col:int):
            if row < 0 or col < 0 or row >= len(grid) or \
                col >= len(grid[0]) or grid[row][col] == '0':
                return
            grid[row][col] = '0'
            DFSMarker(row - 1, col)
            DFSMarker(row + 1, col)
            DFSMarker(row, col - 1)
            DFSMarker(row, col + 1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    DFSMarker(i, j)
        return count