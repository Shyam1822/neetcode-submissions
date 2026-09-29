class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        op = 0
        s = len(grid)
        sc = len(grid[0])
        def search(row,col):
            if row<0 or col<0 or row==s or col==sc or grid[row][col]!='1':
                return
            
            grid[row][col]="#" # marking visited

            search(row+1,col)
            search(row,col+1)
            search(row-1,col)
            search(row,col-1)
        
        for i in range(s):
            for j in range(sc):
                if grid[i][j] =='1':
                    search(i,j)
                    op+=1
        return op