#Input = list -> Output = list (both integers)
#Values can be negative as mentioned as integers
#Edge cases: Empty list, more than one element with same frequency

#- Brute Force: build a frequency map and then sort it by descending, then retrieve first k 
#- Complexity: Time: takes n for frequency map, (nlogn to sort)

# Optimal Approach: Build a frequuency map using Counter, then use a heap of size k, 
# to this we perform two operations, we push if len(heap) <k else we push pop and finally return the val from heap

import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums) #frequency map
        heap = []

        for num, freq in counter.items():
            if len(heap)<k:
                heapq.heappush(heap,(freq, num))
            else:
                heapq.heappushpop(heap,(freq,num))
        
        return [h[1] for h in heap]

#complexity: 
# time: O(nlogk)
# Space: O(n)-> frequency map, heap->O(k), overall: O(n+k) -> o(n)
    