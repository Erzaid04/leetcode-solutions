class Solution(object):
    def searchMatrix(self, mat, x):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = 0
        col = len(mat[0])-1
        while row<len(mat) and col>=0:
            if mat[row][col]==x:
                return True
            elif mat[row][col]<x:
                 row+=1
            else:
               col-=1
        return False
        