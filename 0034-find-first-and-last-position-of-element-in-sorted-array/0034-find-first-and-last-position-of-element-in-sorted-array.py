class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        r = len(nums)-1
        first = -1
        while l <=r:
            mid = (l+r)//2
            if nums[mid] == target:
                first = mid
                r = mid - 1
            elif nums[mid]< target:
                l= mid+1
            else:
                r = mid - 1
        l = 0
        r = len(nums)-1
        last =-1
        while(l<=r):
            mid = (l+r)//2
            if nums[mid]==target:
                last = mid
                l=mid+1
            elif nums[mid] <target:
                l = mid+1
            else:
                r = mid - 1
        return [first,last]
        