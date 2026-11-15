class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        perimeter = 0
        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):
                # Process only land cells
                if grid[i][j] == 1:
                    perimeter += 4

                    # Check the top neighbor; subtract 2 for the shared boundary
                    if i > 0 and grid[i - 1][j] == 1:
                        perimeter -= 2

                    # Check the left neighbor; subtract 2 for the shared boundary
                    if j > 0 and grid[i][j - 1] == 1:
                        perimeter -= 2

        return perimeter