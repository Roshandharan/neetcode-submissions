class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Hash Table Using Array, Create array or length 26, increment and decrement count of each character and return accordingly

        if len(s) != len(t):
            return False
        count = [0]*26

        for i in range(len(s)):
            count[ord(s[i])-ord('a')] += 1
            count[ord(t[i])-ord('a')] -= 1
        
        for val in count:
            if val != 0:
                return False
        
        return True

        #Time Complexity = O(n+m) , n: length of string s and m : lenght of string t
        #space Complexity = O(1) , count:  constant character space of length 26