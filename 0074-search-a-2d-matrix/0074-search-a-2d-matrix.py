class Solution(object):
    def searchMatrix(self, mat, x):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(mat)
        n = len(mat[0])
        l = 0
        r = m*n-1
        while l<=r:
            mid = l+(r-l)//2
            row = mid//n
            col = mid%n
            if mat[row][col]==x:
                return True
            elif mat[row][col]<x:
                l = mid+1
            else:
                r = mid-1
        return False