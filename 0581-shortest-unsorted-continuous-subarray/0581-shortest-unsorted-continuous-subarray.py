class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left_idx = -1
        right_idx = 0
        n = len(nums)
        for i in range(n-1):
            if nums[i]>nums[i+1]:
                left_idx = i
                break
        if left_idx == -1:
            return 0
        right_idx = -1
        for i in range(n-1,0,-1):
            if nums[i]<nums[i-1]:
                right_idx = i
                break
        minimum = nums[left_idx]
        maximum = nums[right_idx]
        for i in range(left_idx,right_idx+1):
            maximum = max(nums[i],maximum)
            minimum = min(nums[i],minimum)
        for i in range(left_idx):
            if nums[i] > minimum:
                left_idx = i
                break
        for i in range(n-1,right_idx-1,-1):
            if nums[i]<maximum:
                right_idx = i
                break
        return right_idx - left_idx + 1
