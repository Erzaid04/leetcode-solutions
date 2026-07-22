class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        ls=0
        
        for r in range(len(nums)):
            rs=total-ls-nums[r]
            if ls == rs:
                return r
            ls+=nums[r]
        return -1

