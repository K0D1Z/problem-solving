class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        res = 0
        row = len(mat) - 1
        for i in range(len(mat)):
            res += mat[i][i]
            res += mat[i][row]
            row -= 1
        if len(mat) % 2 != 0:
            res -= mat[len(mat) // 2][len(mat) // 2]
        return res