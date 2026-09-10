# Create a Set of the enitre array(Provides O(1) lookup time)
# Only proceed in the loop when num -1 is not in the set 
# loop and fond longest


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in s:
                next_num = num + 1
                length = 1
                while next_num in s:
                    length += 1
                    next_num += 1
                longest = max(length, longest)
            
        return longest

# TC & SC = O(n)