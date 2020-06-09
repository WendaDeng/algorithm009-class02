class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        if (grid.empty())   return 0;

        int m = grid.size(), n = m ? grid[0].size() : 0, maxArea = 0;
        for (int r = 0; r < m; ++r) {
            for (int c = 0; c < n; ++c) {
                if (grid[r][c] == 1) {
                    int area = areaOfIsland(grid, r, c);
                    maxArea = max(maxArea, area);
                }
            }
        }
        return maxArea;
    }
private:
    int areaOfIsland(vector<vector<int>> &grid, int r, int c) {
        if (r < 0 || c < 0 || r >= grid.size() || c >= grid[0].size() || grid[r][c] != 1)
            return 0;

        grid[r][c] = 2;

        return 1 + areaOfIsland(grid, r - 1, c)
                + areaOfIsland(grid, r + 1, c)
                + areaOfIsland(grid, r, c - 1)
                + areaOfIsland(grid, r, c + 1);
    }
};
