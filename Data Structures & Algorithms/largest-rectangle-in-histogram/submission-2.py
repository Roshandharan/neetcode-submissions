class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1]>h:
                index, height = stack.pop()
                maxArea = max(maxArea, height*abs(i-index))
                start = index
            stack.append((start,h))
        
        for i, h in stack:
            maxArea = max(maxArea, (len(heights)-i)*h)
        
        return maxArea

#TC = O(n)
#SC = O(n)
# add to stack, pop if the heights boundary does not extend and then compute max area, then append the index as
# lower boundary can extend backward. After this if the stack is not empty, then it extends till ends
# pop and compute area against maxarea