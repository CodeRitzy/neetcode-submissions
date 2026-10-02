class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [0] * 9
        col = [0] * 9
        box = [0] * 9

        for r in range(9):
            for c in range(9):
                if (board[r][c] == '.'):
                    continue
                bit = 1 << int(board[r][c])
                if (bit & row[r] |
                bit & col[c] |
                bit & box[(r // 3 * 3) + (c // 3)]):
                    return False
                row[r] |= bit
                col[c] |= bit
                box[(r // 3 * 3) + (c // 3)] |= bit
        return True