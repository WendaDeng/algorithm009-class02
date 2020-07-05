class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if len(board) == 0: return False

        rows = [{} for i in range(9)]
        cols = [{} for i in range(9)]
        blocks = [{} for i in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    block_idx = (i // 3) * 3 + j // 3

                    rows[i][num] = rows[i].get(num, 0) + 1
                    cols[j][num] = cols[j].get(num, 0) + 1
                    blocks[block_idx][num] = blocks[block_idx].get(num, 0) + 1

                    if rows[i][num] > 1 or cols[j][num] > 1 or blocks[block_idx][num] > 1:
                        return False
        return True