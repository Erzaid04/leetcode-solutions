class Solution(object):
    def minSpeedOnTime(self, dist, hour):
        """
        :type dist: List[int]
        :type hour: float
        :rtype: int
        """
        if hour <= len(dist) - 1:
                return -1
        def canReach(speed,dist,hour):
            time = 0
            for d in range(len(dist)-1):
               time += (dist[d]+speed-1)//speed
            time+= dist[-1]/float(speed)
            return time<=hour
        l =1
        r = 10**7
        ans = 0
        while l<=r:
            mid = (l+r)//2
            if canReach(mid,dist,hour):
                ans = mid
                r = mid-1
            else:
                l = mid+1
        return ans
    
