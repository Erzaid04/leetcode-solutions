class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        ans = 0
        for num in freq:
            if num+1 in freq:
                ans = max(ans,freq[num]+freq[num+1])
        return ans   
        