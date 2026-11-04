class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
            sol, res =[],[]
            nums.sort()
            n = len(nums)

            def backtrack(i):

                if i == n:
                    res.append(sol[:])
                    return
                
                #pick
                sol.append(nums[i])
                backtrack(i+1)
                sol.pop()

                #don't pick
                while i+1<n and nums[i]==nums[i+1]:
                    i += 1
                backtrack(i+1)
            
            backtrack(0)
            return res