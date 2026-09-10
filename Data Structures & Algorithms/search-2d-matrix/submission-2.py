class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        t = rows*cols
        l = 0
        r = t-1

        while l<=r:
            m = (l+r)//2
            i = m//cols
            j = m%cols
            mid_num = matrix[i][j]

            if target == mid_num:
                return True
            elif target < mid_num:
                r = m-1
            else:
                l = m+1
        
        return False
    #tc = O(log(m*n))
    #sc = O(1)