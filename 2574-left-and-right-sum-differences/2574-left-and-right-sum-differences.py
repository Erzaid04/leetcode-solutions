class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        l = 0
        ans = []
        total = sum(nums)
        for i in range(len(nums)):
            r = total -  l -  nums[i]
            ans.append(abs(l-r))
            l+=nums[i]
        return ans
    