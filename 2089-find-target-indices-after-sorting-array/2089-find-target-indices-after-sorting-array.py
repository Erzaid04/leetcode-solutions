class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans= []
        less = 0
        equal = 0
        for i in range(len(nums)):
            if nums[i]<target:
                 less +=1
            elif nums[i] == target:
                equal+=1
        for i in range(less,less+ equal):
            ans.append(i)
        return ans

        