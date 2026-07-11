class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        l,r=1,max(piles)
        while l<=r:
            mid = (l+r)//2
            hours = 0
            for num in piles:
                hours+=(num+mid-1)//mid
            if hours<=h:
                r = mid-1
            else:
                l=mid+1
        return l
        