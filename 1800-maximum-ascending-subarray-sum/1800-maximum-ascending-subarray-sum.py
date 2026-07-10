class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        c_sum = nums[0]
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                c_sum+=nums[i]
            else:
                c_sum =nums[i]
            max_sum = max(c_sum,max_sum)
        return max_sum

