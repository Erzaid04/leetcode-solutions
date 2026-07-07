class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        c_sum = 0
        max_sum = 0
        freq = {}
        l = 0
        for r in range(n):
            c_sum+=nums[r]
            if nums[r] in freq:
                freq[nums[r]]+=1
            else:
                freq[nums[r]] = 1
           
            while freq[nums[r]]>1:
                freq[nums[l]]-=1
                c_sum-=nums[l]
                l+=1
            max_sum = max(c_sum,max_sum)
        return max_sum
