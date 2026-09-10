class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]

        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if slow is fast: break
        
        fast = nums[0]

        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]
        
        return slow
# it's all dependent on the type of input they are giving us, we use slow and fast pointer technique to find and confirm the cycle and then find the number associated in that cycle
# tc: O(n), sc:O(1)