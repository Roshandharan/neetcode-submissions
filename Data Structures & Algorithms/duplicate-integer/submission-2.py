class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set() #Hash Set
        for num in nums:
            if num in s:
                return True
            s.add(num)
        
        return False

        # Time Complexity = O(n)
        # Space complexity = O(n)


