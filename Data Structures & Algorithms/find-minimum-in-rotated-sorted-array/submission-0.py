class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n-1

        while l<r:
            m = (l+r)//2

            if nums[m]>nums[r]:
                l = m+1
            else:
                r = m
        
        return nums[l]
# the main logic lies in the comparison of the value at m and r, so if 
# the value m is greater than R the pivot point is towards right of m, else m could the pivot
# tc: O(log n), sc:O(1)
        