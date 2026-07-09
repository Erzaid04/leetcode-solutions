class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = nums[0]
        l,r=0,len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[l]<=nums[r]:
                return min(ans,nums[l])
            if nums[l]<=nums[mid]:
                ans = min(ans,nums[l])
                l= mid+1
            else:
                ans = min(ans,nums[mid])
                r=mid-1
        return ans