class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
       
      rows, cols = len(grid), len(grid[0])
      q = collections.deque()
      visit =set()

      def istrhelp(i,j):
        if i<0 or i==rows or j<0 or j==cols or (i,j) in visit or grid [i][j] == -1:
            return
        q.append([i,j])
        visit.add((i,j))

      for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                q.append([i,j])
                visit.add((i,j))
      dist = 0
      while q:
        for _ in range(len(q)):
            i,j = q.popleft()
            grid[i][j] = dist
            istrhelp(i+1,j)
            istrhelp(i-1,j)
            istrhelp(i,j-1)
            istrhelp(i,j+1)
        dist += 1
      


