'''
-Compute prefix and Suffix arrays 
1. Prefix - contians products of elements from right to left of previous index.
2. Suffix - contians products of elements from left to right of previous index(reversed).
3. Result array is the multiplication of both arrays.
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [0]*n
        suff = [0]*n
        res = [0]*n

        pref[0] = suff[n-1] = 1

        for i in range(1,n):
            pref[i] = nums[i-1]*pref[i-1]
         
        for i in range(n-2,-1,-1):
            suff[i] = nums[i+1] * suff[i+1]

        for i in range(n):
            res[i] = pref[i]*suff[i]

        return res

# Time Complexity = O(3.N) => O(n)
# Space Complexity = O(3.N) => O(n)  
     