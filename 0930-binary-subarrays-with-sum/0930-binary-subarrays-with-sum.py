class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        seen = {0:1}
        total = 0
        prefix = 0
        for num in nums:
            prefix+=num
            current = prefix - goal
            if current in seen:
                total+=seen[current]
            if prefix in seen:
                seen[prefix]+=1
            else:
                seen[prefix] = 1
        return total
        