class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
      res =[]
      nums = sorted(candidates)
      n = len(nums)

      def dfs(i,cur,total):
        if total == target:
            res.append(cur[:])
            return
        if i==n or total> target:
            return 
        
        cur.append(nums[i])
        dfs(i+1, cur, total+nums[i])
        cur.pop()

        while i+1<n and nums[i]==nums[i+1]:
            i += 1
        dfs(i+1, cur, total)
      dfs(0,[],0)
      return res

    