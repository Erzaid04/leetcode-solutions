class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c_max = b_max = c_min = b_min = nums[0]
        total_sum = nums[0]
        for num in nums[1:]:
            total_sum+=num
            c_max = max(num,c_max+num)
            b_max = max(c_max,b_max)
            c_min = min(num,c_min+num)
            b_min = min(b_min,c_min)
        if b_max<0:
            return b_max
        return max(b_max,total_sum - b_min)        