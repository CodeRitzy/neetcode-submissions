class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * (9)
        cols = [0] * (9)
        box = [0] * (9)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                bit = (1 << int(board[r][c]))
                if (bit) & rows[r]:
                    return False
                if (bit) & cols[c]:
                    return False
                if (bit) & box[((r // 3) * 3 )+ c // 3]:
                    return False
                rows[r] |= bit
                cols[c] |= bit
                box[((r // 3) * 3 )+ c // 3] |= bit
        return True