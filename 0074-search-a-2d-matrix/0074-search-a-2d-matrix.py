class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        row_l, row_r = 0, len(matrix) - 1
        while row_l <= row_r:
            row_m = (row_l + row_r) // 2
            # potential target row found
            if matrix[row_m][0] <= target <= matrix[row_m][-1]: 
                # search target in the potential row
                l, r = 0, len(matrix[row_m]) - 1
                while l <= r:
                    m = (l + r) // 2
                    if matrix[row_m][m] == target:
                        return True
                    elif matrix[row_m][m] > target:
                        r = m - 1
                    else:
                        l = m + 1
                return False
            elif matrix[row_m][0] > target:
                row_r = row_m - 1
            else:
                row_l = row_m + 1
        return False
        