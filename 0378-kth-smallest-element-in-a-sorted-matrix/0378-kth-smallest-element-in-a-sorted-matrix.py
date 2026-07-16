class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        l = matrix[0][0]
        r = matrix[n-1][n-1]

        def helper(matrix,k,target):
            cnt = 0
            row = n-1
            col = 0
            while row>=0 and col<n:
                if matrix[row][col]<=target:
                    cnt+=(row+1)
                    col+=1
                else:
                    row-=1
            return cnt
        while l<=r:
            mid = l+(r-l)//2
            if helper(matrix,k,mid)<k:
                l=mid+1
            else:
                r = mid-1
        return l

        