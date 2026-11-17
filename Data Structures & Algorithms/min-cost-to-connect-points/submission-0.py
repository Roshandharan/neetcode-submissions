import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        seen = set()
        total = 0
        min_heap = [(0,0)]

        while len(seen)<n:
            dist, i = heapq.heappop(min_heap)

            if i in seen:
                continue
            
            total += dist
            seen.add(i)
            xi,xj = points[i]

            for j in range(n):
                if j not in seen:
                    yi,yj = points[j]
                    nei_dist = abs(xi-yi)+abs(xj-yj)
                    heapq.heappush(min_heap,(nei_dist, j))
        
        return total