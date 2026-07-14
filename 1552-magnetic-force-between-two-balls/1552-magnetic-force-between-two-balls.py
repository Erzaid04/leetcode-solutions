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

        def canPlace(pos,m,dist):
            count = 1
            last = pos[0]
            for i in range(1,len(pos)):
                if pos[i]-last>=dist:
                    count+=1
                    last = pos[i]
                if count>=m:
                    return True
            return False


        while l<=r:
            mid = (l+r)//2
            if canPlace(position,m,mid):
                l = mid+1
            else:
                r = mid-1
        return r


        