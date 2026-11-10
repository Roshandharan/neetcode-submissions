class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, sol = [],[]
        n = len(s)

        def ispal(s, l ,r):
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True


        def dfs(i):
            if i>=n:
                res.append(sol[:])
                return 
            for j in range(i, n):
                if ispal(s,i,j):
                    sol.append(s[i:j+1])
                    dfs(j+1)
                    sol.pop()
        dfs(0)
        return res