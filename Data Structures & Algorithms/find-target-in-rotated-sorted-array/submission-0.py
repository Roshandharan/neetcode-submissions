class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n-1

        while l<r:
            mid = (l+r)//2

            if nums[mid]>nums[r]:
                l = mid+1
            else:
                r = mid
        
        min_i = l

        if min_i == 0:
            l,r = 0,n-1
        elif target>=nums[0] and target<=nums[min_i -1]:
            l,r = 0, min_i-1
        else:
            l,r = min_i, n-1
        
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                l = mid+1
            else:
                r = mid-1
        
        return -1
# first run the logic for minimum in roatated sorted array
# the we compute l,r for different cases
# if its standarad binary search then l, r =0,n-1
# if tagret is towards right or left of min_index 
# normal binary search

#tc: O(n)
#sc: O(1)
