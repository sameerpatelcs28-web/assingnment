class Solution:
    def setZeroes(self, grid):
        r, c = len(grid), len(grid[0])

        firstRowZero = False
        firstColZero = False

        for j in range(c):
            if grid[0][j] == 0:
                firstRowZero = True

        for i in range(r):
            if grid[i][0] == 0:
                firstColZero = True

        for i in range(1, r):
            for j in range(1, c):
                if grid[i][j] == 0:
                    grid[i][0] = grid[0][j] = 0

        for i in range(1, r):
            for j in range(1, c):
                if grid[i][0] == 0 or grid[0][j] == 0:
                    grid[i][j] = 0

        if firstRowZero:
            for j in range(c):
                grid[0][j] = 0

        if firstColZero:
            for i in range(r):
                grid[i][0] = 0
