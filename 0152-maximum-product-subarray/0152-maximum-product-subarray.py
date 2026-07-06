class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c_max = 1
        c_min = 1
        ans = float("-inf")
        for num in nums:
            temp_max= max(num,c_max*num,c_min*num)
            temp_min = min(num,c_max*num,c_min*num)
            c_max= temp_max
            c_min = temp_min
            ans = max(ans,c_max)
        return ans

        