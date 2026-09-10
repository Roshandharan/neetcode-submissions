class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1>n2:
            return False
        
        counts1 = [0]*26
        counts2 = [0]*26

        for i in range(n1):
            counts1[ord(s1[i])-97]+=1
            counts2[ord(s2[i])-97]+=1
        
        if counts1 == counts2:
            return True
        
        for i in range(n1, n2):
            counts2[ord(s2[i])-97]+=1
            counts2[ord(s2[i-n1])-97]-=1

            if counts1==counts2:
                return True
        
        return False
    
# compute n1 and n2
# create counts and update the array based on the window compare and if equal true if not fasle
# tc = O(n1)+O(n2) = O(n)
# sc = O(1)

        