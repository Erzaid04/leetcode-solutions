class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        prefix = 0
        seen = {0:-1}
        length = 0
        for i,num in enumerate(nums):
            prefix+=num
            current = prefix%k
            if current in seen:
                length = i - seen[current]
                if length>=2:
                    return True
            else:
                seen[current] = i
        return False

        