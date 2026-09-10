class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       l = 0
       n = len(s)
       longest = 0
       sett = set()

       for r in range(n):
        while s[r] in sett:
            sett.remove(s[l])
            l+=1
        w = (r-l)+1
        longest = max(longest, w)
        sett.add(s[r])

       return longest

#TC : O(n)
#SC : O(n)
# if the character ar right is already in the set , the we remove character at left and increment left else we add chacter at right set and compute longest
