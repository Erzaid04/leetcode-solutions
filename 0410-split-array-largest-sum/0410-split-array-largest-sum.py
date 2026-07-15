class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def split(nums,k,diff):
            c_sum = 0
            count=1
            for num in nums:
                c_sum+=num
                if c_sum>diff:
                    c_sum = num
                    count+=1

                if count>k:
                    return False
            return True
        l = max(nums)
        r = sum(nums)
        while l<=r:
            mid = l + (r- l)//2
            if split(nums,k,mid):
                r = mid-1
            else:
                l = mid+1
        return l

