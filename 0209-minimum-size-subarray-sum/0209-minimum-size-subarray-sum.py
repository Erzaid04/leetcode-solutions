class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        min_length = float("inf")
        total = 0
        l = 0
        for r in range(len(nums)):
            total+=nums[r]
            while total>=target:
                length=r-l+1
                min_length = min(min_length,length)
                total-=nums[l]
                l+=1
        if min_length == float("inf"):
            return 0
        return min_length
        