class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        n = len(bloomDay)
        if m * k>n:
            return -1

        l,r= min(bloomDay),max(bloomDay)
        ans =-1
        while l<=r:
            mid = (l+r)//2
            if self.canMake(bloomDay,m,k,mid):
                ans = mid
                r = mid-1
            else:
                l = mid+1
        return ans
    def canMake(self,bloomDay,m,k,day):
        count = 0
        boquets = 0
        for bloom in bloomDay:
            if bloom<=day:
                count+=1
                if count==k:
                    boquets+=1
                    count=0
            else:
                count=0
        return boquets>=m
        