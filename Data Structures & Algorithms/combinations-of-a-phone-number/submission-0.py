class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        
        sol, res =[], []
        n = len(digits)

        mapp = {'2':'abc', '3':'def', '4':'ghi','5':'jkl',
        '6':'mno','7':'pqrs','8':'tuv', '9':'wxyz'}

        def backtrack(i):
            if i == n:
                res.append(''.join(sol))
                return
            
            for letter in mapp[digits[i]]:
                sol.append(letter)
                backtrack(i+1)
                sol.pop()
            
        backtrack(0)
        return res