class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        if (grid.empty())   return 0;

        int count = 0;
        for (int i = 0; i < grid.size(); ++i) {
            for (int j = 0; j < grid[0].size(); ++j) {
                if (grid[i][j] == '1') {
                    count++;
                    DFSMarker(grid, i, j);
                }
            }
        }
        return count;
    }
private:
    void DFSMarker(vector<vector<char>> &grid, int i, int j) {
        if (i < 0 || j < 0 || i >= grid.size() || j >= grid[0].size() || grid[i][j] == '0')
            return;
        grid[i][j] = '0';
        DFSMarker(grid, i - 1, j);
        DFSMarker(grid, i + 1, j);
        DFSMarker(grid, i, j - 1);
        DFSMarker(grid, i, j + 1);
    }
};
