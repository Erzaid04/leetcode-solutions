class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l,r=0,len(nums)-1
        while l<r:
            mid = (l+r)//2
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] == nums[mid+1]:
                l = mid+2
            else:
                r = mid
        return nums[l]




