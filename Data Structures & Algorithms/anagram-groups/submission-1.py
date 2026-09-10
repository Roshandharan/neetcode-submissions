from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        group_anagrams = defaultdict(list)

        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-ord('a')] += 1

            key = tuple(count)
            group_anagrams[key].append(s)

        return list(group_anagrams.values())

        #Time Complexity = O(n*m)
        #Space Complexity = O(n*m)

        #where n - number of words, m - length of the biggest word