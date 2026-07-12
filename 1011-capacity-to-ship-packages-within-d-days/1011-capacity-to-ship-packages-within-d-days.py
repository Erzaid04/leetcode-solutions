class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        l = max(weights)
        r = sum(weights)
        ans = 0
        while l<=r:
            mid = (l+r)//2
            c_weight = 0
            d = 1
            for w in weights:
                if c_weight+w <=mid:
                    c_weight+=w
                else:
                    d+=1
                    c_weight = w
            if d<=days:
                ans = mid
                r = mid-1
            else:
                l = mid+1
        return ans
        