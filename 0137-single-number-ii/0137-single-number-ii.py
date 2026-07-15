class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0)+1
        for num in freq:

            if freq[num] == 1:
                return num
