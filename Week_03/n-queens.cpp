class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        vector<string> board(n, string(n, '.'));
        backtrack(board, 0);
        return res;
    }
private:
    vector<vector<string>> res;
    void backtrack(vector<string> &board, int row) {
        // terminator
        if (row == board.size()) {
            res.push_back(board);
            return;
        }
        int n = board[row].size();
        for (int col = 0; col < n; col++) {
            if (isValid(board, row, col)) {
                // process current level logic（做选择）
                board[row][col] = 'Q';
                // drill down
                backtrack(board, row + 1);
                // reverse state（撤销选择）
                board[row][col] = '.';
            }
        }
    }

    // 是否可以在 borad[row][col] 放置新皇后
    bool isValid(vector<string> &board, int row, int col) {
        int n = board.size();
        // check if col is valid
        for (int i = 0; i < n; i++)
            if (board[i][col] == 'Q')
                return false;
        // check if right diagonal is valid
        for (int i = row - 1, j = col + 1; i >= 0 && j < n; i--, j++)
            if (board[i][j] == 'Q')
                return false;
        // check if left diagonal is valid
        for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--)
            if (board[i][j] == 'Q')
                return false;
        return true;
    }
};
