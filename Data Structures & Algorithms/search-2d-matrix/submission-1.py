class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        t = rows*cols
        l,r = 0, t-1

        while l<=r:
            m = (l+r) // 2
            i = m//cols
            j = m%cols
            mid_num = matrix[i][j]
            if mid_num > target:
                r =m-1
            elif mid_num<target:
                l = m+1
            else:
                return True
        
        return False
