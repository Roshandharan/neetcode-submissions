class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n= len(nums)
        answer = []

        for i in range(n):
            if nums[i]>0:
                break
            elif i>0 and nums[i]==nums[i-1]:
                continue
            lo, hi =i+1, n-1
            while lo<hi:
                summ = nums[i]+ nums[lo] + nums[hi]
                if summ == 0:
                    answer.append([nums[i], nums[lo], nums[hi]])
                    lo , hi = lo+1, hi-1
                    while lo<hi and nums[lo]==nums[lo-1]:
                        lo+=1
                    while lo<hi and nums[hi]==nums[hi+1]:
                        hi-=1
                elif summ<0:
                    lo+=1
                else:
                    hi-=1
        return answer
     

#'Sort the array, then for each index i fix nums[i] and use two pointers (lo, hi) 
#scanning inward from both ends of the remaining sorted subarray to find pairs summing to 
#-nums[i]. Move lo right when the triplet sum is too small, hi left when too big, and 
#record matches when the sum hits zero — advancing both pointers past duplicates to avoid 
#repeat triplets. Skip duplicate i values up front (comparing to nums[i-1]) to avoid redundant
# outer iterations. O(n²) time, O(1) extra space.'