from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        p_queue = deque()
        p_seen = set()

        a_queue = deque()
        a_seen = set()

        m,n = len(heights), len(heights[0])

        for j in range(n):
            p_queue.append((0,j))
            p_seen.add((0,j))
        
        for i in range(1,m):
            p_queue.append((i,0))
            p_seen.add((i,0))
        
        for i in range(m):
            a_queue.append((i, n-1))
            a_seen.add((i, n-1))
        
        for j in range(0, n-1):
            a_queue.append((m-1,j))
            a_seen.add((m-1,j))
        
        def coords(que, seen):

            while que:
                i,j = que.popleft()

                for i_off,j_off in [(1,0),(0,1),(-1,0),(0,-1)]:
                    r,c = i+i_off, j+j_off

                    if 0<=r<m and 0<=c<n and heights[r][c]>=heights[i][j] and (r,c) not in seen:
                        seen.add((r,c))
                        que.append((r,c))
        
        coords(p_queue, p_seen)
        coords(a_queue, a_seen)

        return list(p_seen.intersection(a_seen))

# we have make pacific queue and set and add the top right and bottom point to the que and set, 
# similalry bottem up and left in to the que and set,
# we make a help set by finding offsets to find which grid positions can flow in the points added to the set
# intersection of pacific and atlantic is our answer
#tc: O(m*n)
#sc: O(m*n)











