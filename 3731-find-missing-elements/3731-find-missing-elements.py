class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        idx = min(nums)
        ans = []
        nums.sort()
        for num in nums:
            while num != idx:
                ans.append(idx)
                idx+=1
            idx+=1
        return ans
        