class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        total = 1
        max_total = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                total = ((nums[i]-1)* (nums[j]-1))
                max_total = max(total,max_total)
        return max_total