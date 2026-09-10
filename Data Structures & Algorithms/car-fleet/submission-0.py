class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p,s) for p,s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []

        for p, s in pair:
            stack.append((target-p)/s)
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        
        return len(stack)

#TC = O(nlogn) (sorting and loop of n)
#SC = O(n) (stack, list of n)

# Combine into pairs(list comprehension) and then compute time to reach destination, and if the cars
# merge into each other, estimated by time, pop the car behind the most leading car. 