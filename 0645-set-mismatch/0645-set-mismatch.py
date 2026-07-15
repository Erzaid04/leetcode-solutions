class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        map = set()
        ans = []
        for num in nums:
            if num in map:
                ans.append(num)
            else:
                map.add(num)
        for i in range(1,len(nums)+1):
            if i not in map:
                ans.append(i)
        return ans
        

        