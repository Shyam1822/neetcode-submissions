class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # 29/9/26

        op = 0
        row = len(grid)
        col = len(grid[0])

        # def searchMax(r, c):
        #     if r < 0 or c < 0 or r == row or c == col or grid[r][c] != 1:
        #         return 0

        #     grid[r][c] = "#"  # mark visited

        #     return (
        #         1
        #         + searchMax(r + 1, c)
        #         + searchMax(r - 1, c)
        #         + searchMax(r, c + 1)
        #         + searchMax(r, c - 1)
        #     )

        # optimized searchMax
        def searchMax(r, c):
            if grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0

            cur = 1

            if r + 1 < row:
                cur += searchMax(r + 1, c)

            if r > 0:
                cur += searchMax(r - 1, c)

            if c + 1 < col:
                cur += searchMax(r, c + 1)

            if c > 0:
                cur += searchMax(r, c - 1)

            return cur

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    op = max(op, searchMax(i, j))

        return op

        # optimization suggestions
        # 1. dont make recursive call always, check for condition and do the recursive call(primary)
        # 2. change '#' to 0 (minor)
