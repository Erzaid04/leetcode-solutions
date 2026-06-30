class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq = {0:1}
        total=0
        prefix = 0
        for num in nums:
            prefix+=num
            current = prefix - k
            if current in freq:
                total+=freq[current]
            if prefix in freq:
                freq[prefix]+=1
            else:
                freq[prefix]=1
        return total


        