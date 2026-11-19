class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        res = []
        for col in range(len(matrix[0])):
            new_row = []
            for row in range(len(matrix)):
                new_row.append(matrix[row][col])
            res.append(new_row)
        return res
                
        