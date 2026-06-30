class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_length = 0
        seen = {0:-1}
        prefix = 0
        for i,num in enumerate(nums):
            if num == 0:
                prefix+=-1
            else:
                prefix+=1
            
            if prefix in seen:
                length = i - seen[prefix]
                max_length = max(length,max_length)
            else:
                seen[prefix] = i
        return max_length
        