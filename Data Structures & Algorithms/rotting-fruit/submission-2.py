class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        empty, fresh, rotten = 0,1,2
        q = deque()
        fresh_num = 0
        rows,cols = len(grid), len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == fresh:
                    fresh_num += 1
                if grid[i][j] == rotten:
                    q.append((i,j))
        if fresh_num ==0:
            return 0
        num_min = -1
        
        while q:
            num_min += 1
            q_size = len(q)
            for _ in range(q_size):
                i,j = q.popleft()
                for r,c in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                    if 0<=r<rows and 0<=c<cols and grid[r][c]==fresh:
                        grid[r][c] = rotten
                        fresh_num -= 1
                        q.append((r,c))
        
        if fresh_num == 0:
            return num_min
        else:
            return -1
