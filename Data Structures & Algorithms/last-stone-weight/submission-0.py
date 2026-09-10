import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        for i in range(len(stones)):
            stones[i] = -stones[i]
        
        heapq.heapify(stones)

        while len(stones)>1:
            l = heapq.heappop(stones)
            nl = heapq.heappop(stones)

            if l != nl:
                heapq.heappush(stones, l-nl)
        
        if len(stones)==1:
            return -(heapq.heappop(stones))
        else:
            return 0
