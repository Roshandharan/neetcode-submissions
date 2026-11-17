class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n ==1:
            return nums[0]

        def rob_line(house):
            m = len(house)
            if m ==1:
                return house[0]
            
            prev, cur = house[0], max(house[0], house[1])

            for i in range(2,m):
                prev, cur = cur, max(house[i]+prev, cur)
            
            return cur
        
        return max(rob_line(nums[1:]), rob_line(nums[:-1]))