class Solution(object):
    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """
        position.sort()
        l = 1
        r = position[-1] - position[0]

        def canPlace(dist):
            count = 1
            last = position[0]
            n = len(position)
            for i in range(1,n):
                if position[i]-last>=dist:
                    count+=1
                    last = position[i]
                if count==m:
                    return True
            return False


        while l<=r:
            mid = (l+r)//2
            if canPlace(mid):
                l = mid+1
            else:
                r = mid-1
        return r


        