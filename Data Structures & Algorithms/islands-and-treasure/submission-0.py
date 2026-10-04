class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #4/10
        # instead of starting from 0,0 , first note the pos of all treasure chest and start from there to nearby nodes
        rows, cols = len(grid), len(grid[0])
        q = deque()

        # Step 1: Add all treasure chests to the queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))

        # Step 2: Traverse outward from all treasure chests simultaneously
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            r, c = q.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # Only visit valid land cells that haven't been reached yet
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))