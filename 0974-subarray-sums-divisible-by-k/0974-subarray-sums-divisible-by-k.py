class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix = 0
        seen = {0:1}
        total = 0
        for num in nums:
            prefix+=num
            current = prefix%k
            if current in seen:
                total+= seen[current]
                seen[current]+=1
            else:
                seen[current] = 1
        return total
        