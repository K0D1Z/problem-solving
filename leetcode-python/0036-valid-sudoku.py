class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hash_map = defaultdict(set)
        col_hash_map = defaultdict(set)
        square_hash_map = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    continue
                if board[row][col] in row_hash_map[row] or board[row][col] in col_hash_map[col] or board[row][col] in \
                        square_hash_map[(row // 3, col // 3)]:
                    return False

                row_hash_map[row].add(board[row][col])
                col_hash_map[col].add(board[row][col])
                square_hash_map[(row // 3, col // 3)].add(board[row][col])

        return True
